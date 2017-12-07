package Boot::Grub;

#   $Header: /cvsroot/systemconfig/systemconfig/lib/Boot/Grub.pm,v 1.29 2003/11/17 20:56:58 pramath Exp $


#   Copyright (c) 2001 International Business Machines

#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 2 of the License, or
#   (at your option) any later version.
 
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  

#   See the
#   GNU General Public License for more details.
 
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the Free Software
#   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

#   Donghwa John Kim <johkim@us.ibm.com>

=head1 NAME

Boot::Grub - Grub bootloader configuration module.

=head1 SYNOPSIS

  my $bootloader = new Boot::Grub(%bootvars);

  if($bootloader->footprint_loader()) {
      $bootloader->install_config();
  }
  
  if($bootloader->footprint_config() && $bootloader->footprint_loader()) {
    $boot->install_loader();
  }

  my @fileschanged = $bootloader->files();

=cut

use strict;
use Carp;
use vars qw($VERSION $DEVICE_MAP $FSTAB);
use File::Basename;
use Boot;
use Boot::Label;
use Boot::Devfs;
use Data::Dumper;
use Util::Cmd qw(:all);
use Util::Log qw(:print);

$VERSION = sprintf("%d.%02d", q$Revision: 1.29 $ =~ /(\d+)\.(\d+)/);

push @Boot::boottypes, qw(Boot::Grub);

# The constructor for grub is a bit more complex than most
# which is directly the result of the fact that grub is more complex
# than most boot loaders to setup.

# Grub has its own device convention, (hdX,Y) where X is disk, Y is partition.
# X and Y are zero indexed, and X doesn't matter if the device is IDE or SCSI.
# Though good in theory, the fact that we are running under devfs means there
# is a whole lot of device translation required here devfs -> oldlinux -> grub, and
# back again all over the place.  The code here is sort of a morass because of it.

# The other issue is that grub doesn't have an 'install' program.  grub-install, which
# one would think installs grub to be ready to go, doesn't.  It just ensures that /boot/grub
# is populated correctly.  Great...!

# Hence you have to run the following:
# grub> root (hdX,Y); setup (hdZ)

# Yes, you have to run these at the interactive grub command line.  Granted, you
# can slurp from STDIN (which is what we do), but the lack of command line
# flags to perform this installation annoys me.

# And to make matters a little worse, not all distros use 'menu.lst' as the config file.
# Red Hat has modified grub to use grub.conf instead, which means we have to 
# make the symbolic link right.

# And just think, the code to handle lilo was a simple as 'run /sbin/lilo'.

sub new {
    my $class = shift;
    my %this = (
                root => "",
                filesmod => [],
		boot_timeout => 50,   
		boot_defaultboot => "",      ### Label identifying default image to boot with.
                @_,                          ### Overwrite default values.
                grub => which('grub'), # location of grub
                bootloader_exe => which('grub-install'), # location of grub-install
                bootdev => "(hd0)",     ### Device to which to install boot image. (default, we'll mod this later)
               );

    verbose("Grub executable set to: $this{bootloader_exe}.");
    $this{config_file} = "$this{root}/boot/grub/menu.lst";

    bless \%this, $class;
}

# footpring_config returns "TRUE" if Grub's configuration file, i.e. "/boot/grub/menu.lst", exists. 

sub footprint_config {
    my $this = shift;
    return -e $this->{config_file};
}

# footprint_loader returns "TRUE" if executable Grub bootloader is installed. 

sub footprint_loader {
    my $this = shift;
    verbose("bootloader = $this->{bootloader_exe}");
    return $this->{bootloader_exe};
}

# This creates the grub counter for the default boot.  Grub requires the
# default to be a 0 indexed number which is the number of the boot entry.

# System Configurator uses symbolic labels, like lilo.  So we have to translate/

sub get_default_boot {
    my $this = shift;
    
    my $counter = 0;
    foreach my $key (sort keys %{$this}) {
        if ($key =~ /^(kernel\d+)_label/) {
            if ($$this{$key} eq $$this{boot_defaultboot}) {
                return $counter;
            }
            $counter++;
        }
    }
    return 0;
}

# dev2bios is used as an internal method.
# It takes a path to the device as the argument and returns device syntax ( 
# matching an entry in the device map file) used by Grub 

sub dev2bios {
    my ($devpath) = @_;
    my $biosdev = "";

    if(!(defined $DEVICE_MAP)) {
        $DEVICE_MAP = device_map(which("grub")); 
    }

    $devpath = devfs_lookup($devpath);

    if($devpath =~ m{^/dev/(.+?)p*(\d*)$}) {
        my ($dev, $part) = ($1,$2);
        verbose("Device: $dev; Part: $part");
        $biosdev = $DEVICE_MAP->{$dev};
        verbose("Biosdev: $biosdev");
        if($part) {
            # grub 0 orders things
            my $biospart = $part - 1;
            $biosdev =~ s/\)/,$biospart\)/;
        }
    }
    
    return $biosdev;
}

# loads the device map into a memory struct

sub device_map {
    my $grub = shift;
    my $device_map = {};
      
    my $file = "/tmp/grub.devices";
    if(-e $file) {
        unlink $file;
    }
    
    my $cmd = "$grub --batch --device-map=$file < /dev/null > /dev/null";
    !system($cmd) or croak("Couldn't run $cmd");
    
    verbose("generated device map file $file");

    open(IN,"<$file");
    
    while(<IN>) {
        my ($grub, $real) = split;
        $real = devfs_lookup($real);
        $real =~ s{/dev/}{};
        verbose("$real => $grub");
        $device_map->{$real} = $grub;
    }
    close(IN);
    unlink $file;
    return $device_map;
}

# finds what grub thinks is root:
# load the fstab struct
# look for /boot or /
# return bios mapping for /boot or /

sub find_grub_root {
    my $fstab = Boot::Label::fstab_struct("/etc/fstab");
    
    # invert the mapping... now it is mount => device name
    my %mounts = map {$fstab->{$_}->{mount} => $_} keys %{$fstab};

    foreach my $mount (qw(/boot /)) {
        if($mounts{$mount}) {
            return dev2bios($mounts{$mount});
        }
    }

    # If we get this far, something is very very wrong
    croak("Couldn't find grub root");
}

# install_loader()
# 
#
# This method invokes the Grub executable.
# Grub write the boot image onto the MBR of the bootable disk.  

sub install_loader {
    my $this = shift;
    my $bootdev = $this->{bootdev};
    system("$$this{bootloader_exe} --recheck '$$this{bootdev}'");
        
    my $grubroot = find_grub_root();

    verbose("Grub root set to '$grubroot'");

    my $install_cmd = <<END_GRUB;
$$this{grub} --no-curses <<EOF > /dev/null
root $grubroot
setup $bootdev
EOF
END_GRUB

    !system($install_cmd) or croak("Error: Couldn't setup grub with cmd '$install_cmd'!\n$!\n");
    
    return 1;
}

# dev_transform takes the path (in devfs format) and turns it into a grub device

sub dev_transform {
    my ($path) = @_;
    if(!$FSTAB) {
        $FSTAB = Boot::Label::fstab_struct("/etc/fstab");
    }
    
    my %mounts = map {$FSTAB->{$_}->{mount} => $_} keys %{$FSTAB};
    my @mounts = sort {length($b) <=> length($a)} keys %mounts;
    
    foreach my $mount (@mounts) {
        if($mount ne "/" and $path =~ s/^$mount//) {
            verbose("Mount = $mount; Path = $path");
            $path = dev2bios($mounts{$mount}) .  $path;
            last;
        } elsif ($mount eq "/") {
            $path = dev2bios($mounts{"/"}) .  $path;
        }
    }

    return $path;
}

=item install_config()

This method read the System Configurator's config file and creates Grub's 
menu file, i.e. "/boot/grub/menu.lst". 

=cut

sub install_config {
    my $this = shift;
    my @splashfiles = qw(/boot/grub/splash.xpm.gz);
    my $splashline = "";

    if(!$this->{boot_defaultboot}) {
	croak("Error: DEFAULTBOOT must be specified.\n");;
    }

    foreach my $img (@splashfiles) {
        if(-e $img) {
            $splashline = "splashimage=" . dev_transform($img);
            last;
        }
    }

    ### Open the native bootloader config file for write.
    open(OUT,">$this->{config_file}") or croak("Couldn't open $this->{config_file} for writing!");
    
    my $timeout = $this->{boot_timeout} / 10;
    my $defaultbootnum = get_default_boot($this);

print OUT <<EOF;
##################################################
# This file is generated by System Configurator. #
##################################################
# The number of seconds to wait before booting.
timeout $timeout 
# The default kernel image to boot.
default $defaultbootnum
# The splash image (this line will be empty if nothing was found)
$splashline

EOF


    ### Set up kernel image options
    foreach my $key (sort keys %$this) {
        if ($key =~ /^(kernel\d+)_path/) {
            $this->setup_kernel($1, \*OUT);
        }
    }
    
    close(OUT); ### "$this->{root}/boot/grub/menu.lst"

    my $linkname = "$this->{root}/boot/grub/grub.conf";
    # If it exists, we need to remove it and link it to our config file
    if(-e $linkname) {
        unlink($linkname);
    }
    symlink(basename($this->{config_file}),$linkname);
    
    ### To be part of the exclusion files
    push @{$this->{filesmod}}, ("$this->{config_file}", $linkname);
    
    return 1;
  } 

=item setup_kernel()

An internal method.
This method sets up a kernel image as specified in the config file.

=cut

sub setup_kernel {
    my ($this, $image, $outfh) = @_;

    my $label = $this->{$image . "_label"};
#    my $boot_device = $this->dev2bios($this->{boot_bootdev}) || $this->{bootdev};

    my $kernel = dev_transform($this->{$image . "_path"});
    my $rootdev = $this->{$image . "_rootdev"} || $this->{boot_rootdev};
    my $initrdline = ($this->{$image . "_initrd"}) ? ("\tinitrd " . dev_transform($this->{$image . "_initrd"})) : "";
    my $append = $this->{$image . "_append"} || $this->{boot_append};
    
    print $outfh <<EOF;
# $image
title $label
\tkernel $kernel ro root=$rootdev $append
$initrdline

EOF
}

# Utility method for files.  We should push this into a super class, just haven't yet

sub files {
    my $this = shift;
    return @{$this->{filesmod}};
}


=back

=head1 AUTHOR

  Sean Dague <sean@dague.net>
  Donghwa John Kim <donghwajohnkim@yahoo.com>

=head1 SEE ALSO

L<Boot>, L<perl>

=cut

1;




















