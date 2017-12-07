package Boot::Lilo;

#   $Header: /cvsroot/systemconfig/systemconfig/lib/Boot/Lilo.pm,v 1.7 2002/07/31 18:07:54 sdague Exp $

#   Copyright (c) 2001-2002 International Business Machines

#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 2 of the License, or
#   (at your option) any later version.
 
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
 
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the Free Software
#   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

#   Donghwa John Kim <johkim@us.ibm.com>
#   Sean Dague <sean@dague.net>

=head1 NAME

Boot::Lilo - Lilo bootloader configuration module.

=head1 SYNOPSIS

  my $bootloader = new Boot::Lilo(%bootvars);

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
use vars qw($VERSION);
use Boot;
use Util::Cmd qw(:all);
use Util::Log qw(:print);

$VERSION = sprintf("%d.%02d", q$Revision: 1.7 $ =~ /(\d+)\.(\d+)/);

push @Boot::boottypes, qw(Boot::Lilo);

sub new {
    my $class = shift;
    my %this = (
                root => "",
		boot_bootdev => "",
                boot_timeout => 50,
                boot_rootdev => "",
                boot_extras => "",
		boot_vga => 'normal',
                @_,                  ### Overwrite default value.
                filesmod => [],
               );

    $this{config_file} = $this{root} . "/etc/lilo.conf";
    $this{bootloader_exe} = which("lilo");
    
    if(!$this{boot_bootdev} and $this{boot_rootdev}) {
        $this{boot_bootdev} = $this{boot_rootdev};
        $this{boot_bootdev} =~ s/\d+$//;
    }
            
    verbose("Lilo executable set to: $this{bootloader_exe}.");
    bless \%this, $class;
}

=head1 METHODS

The following methods exist in this module:

=over 4

=item files()

The files() method is merely an accessor method for the all files
touched by the instance during its run.

=cut

sub files {
    my $this = shift;
    return @{$this->{filesmod}};
}

=item footprint_config()

This method returns "TRUE" if the Lilo configuration file (i.e. "/etc/lilo.conf") exists. 

=cut

sub footprint_config {
    my $this = shift;
    return -e $this->{config_file};
}

=item footprint_loader()

This method returns "TRUE" if the Lilo executable exists. 

=cut

sub footprint_loader {
    my $this = shift;
    return $this->{bootloader_exe};
}

=item install_config()

This method reads the System Configurator config file and creates lilo.conf file.   

=cut

sub install_config {
    my $this = shift;

    if(!$this->{boot_bootdev})
    {
	croak("Error: BOOTDEV must be specified.\n");
    }
    if(!$this->{boot_defaultboot}) 
    {
	croak("Error: DEFAULTBOOT must be specified.\n");;
    }

    open(OUT,">$this->{config_file}") or croak("Couldn\'t open $this->{config_file} for writing");
    
    print OUT <<LILOCONF;
##################################################
# This file is generated by System Configurator. #
##################################################

# Do all the normal things lilo does
lba32
map=/boot/map
install=/boot/boot.b
vga=$this->{boot_vga}

$this->{boot_extras}
# The number of deciseconds (0.1 seconds) to wait before booting
prompt
timeout=$this->{boot_timeout}

# The boot device where lilo installs the boot block
boot=$this->{boot_bootdev}	

# the default label to boot
default=$this->{boot_defaultboot}

LILOCONF
  
  # Now we append the items that may have not been there previously
  
    if ($this->{boot_rootdev}) {
        print OUT "# Device to be mounted as the root ('/') \n";
        print OUT "root=" . $this->{boot_rootdev} . "\n";
    }
    if ($this->{boot_append}) {
        print OUT "# Kernel command line options. \n";
        print OUT "append=\"" . $this->{boot_append} . "\"\n";
    }
    
    foreach my $key (sort keys %$this) {
        if ($key =~ /^(kernel\d+)_path/ and $this->{$key}) {
            $this->setup_kernel($1,\*OUT);
        }
    }
    
    close(OUT);

    push @{$this->{filesmod}}, "$this->{config_file}";
    1;
}

=item setup_kernel()

An "internal" method.
This method sets up a kernel image as specified in the config file.

=cut

sub setup_kernel {
    my ($this, $kernel, $outfh) = @_;
    
    if ($this->{$kernel . "_label"} eq $this->{boot_defaultboot}) {
	unless ($this->{boot_rootdev} || $this->{$kernel . "_rootdev"}) {
	    croak("ROOTDEV must be specified either globally or locally.");
	    close($outfh);
	}
    }
          
    print $outfh <<LILOCONF;
#----- Options for \U$kernel\E -----#
image=$this->{root}$this->{$kernel . "_path"}
\tlabel=$this->{$kernel . "_label"}
\tread-only
LILOCONF

    ### Check for command line kernel options. 
    if ($this->{$kernel . "_append"}) {
	print $outfh "\tappend=" . "\"" . $this->{$kernel . "_append"} . "\"" . "\n";
    }

    ### Override global rootdev option?
    if ($this->{$kernel. "_rootdev"}) {
        print $outfh "\troot=" . $this->{$kernel . "_rootdev"} . "\n";
    }    

    ### Initrd image
    if ($this->{$kernel. "_initrd"}) {
        print $outfh "\tinitrd=" . $this->{root} . $this->{$kernel . "_initrd"} . "\n";
    }        
}

=item install_loader()

This method invokes the Lilo executable.
Lilo writes the boot image onto the device specified as the boot partition.  

=cut

sub install_loader {
    my $this = shift;

    my $chroot = ($this->{root}) ? "-r $this->{root}" : "";

    my $output = qx/$this->{bootloader_exe} $chroot 2>&1/;
    
    my $exitval = $? >> 8;
    
    if ($exitval) {
        croak("Error: Cannot execute $this->{bootloader_exe}.\n$output\n");
    }
    1;
}

=back

=head1 AUTHOR

Donghwa John Kim <donghwajohnkim@yahoo.com>

=head1 SEE ALSO

L<Boot>, L<perl>

=cut

1;



















