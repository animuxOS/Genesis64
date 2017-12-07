#!/usr/bin/perl

# $Id: Farmerjoe.pl,v 0.1.3 Alpha 2006/08/29 10:27:10$
#
# --------------------------------------------------------------------------
# Farmerjoe by Mitch Hughes (AKA lobo_nz)
# --------------------------------------------------------------------------
# ***** BEGIN GPL LICENSE BLOCK *****
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
# ***** END GPL LICENCE BLOCK *****
# --------------------------------------------------------------------------

package Farmerjoe;
use strict;
use File::Basename;
use Config;

#Farmerjoe a Blender Render Farmer
#
#farmerjoe.conf - Config file
#farmerjoe.state - State file
#farmerjoe_bucket.py - Python BPY script for bucket rendering
#farmerjoe_render.py - Python BPY script to submit renders
#Files with .lck on the end are Semaphore files used for file locking

#read config here
my $util = FarmerTools->new();
my $dir = '.';
$dir  = dirname($0);
my $conf = $util->load_conf("$dir/Farmerjoe.conf");

my $osconf = {master=>$conf->{master},port=>$conf->{port}};
$osconf->{os} = $Config{osname};
$osconf->{appserver_port} = $conf->{appserver_port};

if ($Config{osname} eq 'linux'){
    $osconf->{sep} = '/';
    $osconf->{root} = $conf->{linux_root};
    $osconf->{jobs} = $osconf->{root}.$osconf->{sep}.$conf->{jobs};
    $osconf->{logs} = $osconf->{root}.$osconf->{sep}.$conf->{logs};
    $osconf->{blender} = $conf->{linux_blender};
    $osconf->{composite} = $conf->{linux_composite};
    $osconf->{nbtscan} = $osconf->{root}.$osconf->{sep}."bin".$osconf->{sep}."nbtscan";
}elsif($Config{osname} eq 'MSWin32'){
    $osconf->{sep} = "\\";
    $osconf->{root} = $conf->{windows_root};
    $osconf->{jobs} = $osconf->{root}.$osconf->{sep}.$conf->{jobs};
    $osconf->{logs} = $osconf->{root}.$osconf->{sep}.$conf->{logs};
    $osconf->{blender} = $conf->{windows_blender};
    $osconf->{composite} = $conf->{windows_composite};
    #osx probably wont work at the moment :/ I cant test it
}elsif($Config{osname} eq 'darwin'){#TODO find out wat the osname should be
    $osconf->{sep} = '/';
    $osconf->{root} = $conf->{osx_root};
    $osconf->{jobs} = $osconf->{root}.$osconf->{sep}.$conf->{jobs};
    $osconf->{logs} = $osconf->{root}.$osconf->{sep}.$conf->{logs};
    $osconf->{blender} = $conf->{osx_blender};
    $osconf->{composite} = $conf->{osx_composite};
    #$osconf->{nbtscan} = $osconf->{root}.$osconf->{sep}."bin".$osconf->{sep}."nbtscan";
    #smbutil status 192.168.1.10 <--use to get hostname on osx
}
$osconf->{bucket_render} = $osconf->{root}.$osconf->{sep}.'bin'.$osconf->{sep}.'farmerjoe_bucket.py';
$osconf->{statefile} = $osconf->{root}.$osconf->{sep}."farmerjoe.state";
my %args = ();
foreach my $arg (@ARGV){
    if ($arg =~ /^-?-/){#get commands out ignore paths
        $arg =~ s/^-?-//;
        $args{$arg} = 1; 
    }
}
$osconf->{debug} = 0;
$osconf->{debug} = 1 if $args{'debug'};
my ($cmd, $jobdir, $jobfile) = @ARGV;
if ($args{'submit'}){#job is being submitted
    my $farmer_job = FarmerSubmitJob->new($osconf);
    $farmer_job->run($jobdir, $jobfile);
}elsif($args{'master'}){#run as master server
   my $farmer = FarmerMaster->new($osconf);
   $farmer->run();
}elsif($args{'appserver'} || $args{'webgui'}){#run as web application server
    my $appserver = FarmerAppServer->new($osconf);
    $appserver->run();
}elsif($args{'help'}){#output help
    print "Farmerjoe - The Render Farmer
Usage: Farmerjoe [OPTIONS]
       Farmerjoe --master                   Run as the master server
       Farmerjoe                            Run as a slave
       Farmerjoe --appserver --webgui       Run as the appserver (Web gui)
       Farmerjoe --help                     Output this help text
       
       Farmerjoe --submit JOBDIR JOBFILE    Used by Blender gui to submit jobs
       
       --debug option can be added to make Farmerjoe output extra info
       
       NOTE: The Farmerjoe command may be Farmerjoe.pl, Farmerjoe.exe or Farmerjoe.bin
             depending on your platform and whether you use the perl script or binaries
       
";
}else{#run as slave
    my $farmer_slave = FarmerSlave->new($osconf);
    $farmer_slave->run();
}
1;
#{{{FarmerSlave###############################################################################
package FarmerSlave;

use IO::Socket;
my $server = '';

sub new
{
    my $class = shift;
    my $self = {};
	bless ($self, $class);
    
    $self->{c} = shift;
    
    return $self;
}

sub run_multiplexing{
    my $self = shift;
    my $connect_err = "";
    my $running = 1;
    my $connected_to_master = 0;
    
    use IO::Select;
    my $read_set = new IO::Select(); # create handle set for reading
    
    while ($running){
        $server = IO::Socket::INET->new(
            Proto => "tcp",
            PeerAddr => $self->{c}->{master},
            PeerPort => $self->{c}->{port},
            ) or $connect_err = "Can't Connect to $self->{c}->{master} at Port $self->{c}->{port}\n";
        
        if (!$connect_err){
            print $server "SU SLAVE\n";
            $read_set->add($server);# add the master server socket to the set
            $connected_to_master = 1;
        }else{
            print $connect_err;
            print "Will try to reconnect in 30 seconds\n";
            sleep(30);
            $connect_err = "";
            next;
        }
        
        while ($connected_to_master){
          # get a set of readable handles (blocks until at least one handle is ready)
          #my $rh_set = IO::Select->select($read_set, undef, undef, 0);
          # take all readable handles in turn
          my @ready = $read_set->can_read;
          
          foreach my $rh (@ready) {
            my $msg = <$rh>;
            print $msg;
            if($msg) { # we got input
                if ($rh == $server){
                    if ($msg =~ /CMD\s(\d+)\sRENDER\s-S\s(\d+)\s-E\s(\d+)\s-(.)\s"(.+)"/){
                        $self->{current_cmd} = {id=>$1,start=>$2,end=>$3,type=>$4,blend=>$5};
                        my $sep = $self->{c}{sep};
                        $self->{current_cmd}->{blend} =~ s/\|/$sep/ge;
                        $self->{rendertype} = "step";
                        $self->beginStep();
                    }
                    if ($msg =~ /CMD\s(\d+)\sRENDER\s-F\s(\d+)\s"(.+)"\s(\d+)\s(\d+\.?\d*)\s(\d+\.?\d*)\s(\d+\.?\d*)\s(\d+\.?\d*)/){
                        $self->{current_cmd} = {id=>$1,frame=>$2,blend=>$3,part=>$4,x1=>$5,y1=>$6,x2=>$7,y2=>$8};
                        my $sep = $self->{c}{sep};
                        $self->{current_cmd}->{blend} =~ s/\|/$sep/ge;
                        $self->{rendertype} = "part";
                        $self->renderPart();
                        #x1=0 x2=0.5 y1=0 y2=0.5 part=2 blender -b /render/bucket/bucket.blend -P /render/bucket_render.py
                    
                    }
                    if ($msg =~ /VAR\s(.+)\s=\s"(.+)"/){
                        $self->{$1} = $2;
                    }
                    #else do nothing
                    #print "yup\n";
                }else{
                    if ($self->{rendertype} eq "step"){
                        my $result = $self->handleStep($msg);
                        if ($result eq "complete"){
                            print $server "COMPLETED JOB ".$self->{current_cmd}->{id}." FRAME ".$2." TIME ".$4."\n";
                            print $server "STATUS IDLE\n";
                        }
                    }elsif($self->{rendertype} eq "part"){
                        
                    }
                }
            }
            else { # the connection has closed the socket
                print "FH Closed";
                # remove the socket from the $read_set and close it
                $connected_to_master = 0 if $rh == $server;
                $read_set->remove($rh);
                
                #close($rh) if $rh == $server;
            }
          }
        }
    }
}

sub beginStep{
    my $self = shift;
    my $c = $self->{current_cmd};
    my $anim = '';
    
    print "rendering... $c->{type}\n";
    $anim = " -a" if $c->{type} eq 'A';
    my $args = " -b ".'"'.$self->{c}{jobs}.$self->{c}{sep}.$c->{blend}.'"'." -s ".$c->{start}." -e ".$c->{end}.$anim;
    
    my $render_cmd = '"'.$self->{c}{blender}.'"'.$args;
    if ($self->{c}{os} eq 'MSWin32') {
        $render_cmd = "call $render_cmd";
    }
    print $render_cmd. "\n";

    $self->{subprocess_pid} = open my $blender, "-|", $render_cmd or die "couldn't fork: $!\n";

    return $blender;
}

sub handleStep{
    my $self = shift;
    my $msg = shift;
    my $status = "rendering";
    print "handleStep";
    #Saved: /render/jobs/farmerjoe_test.blend.2006-6-1_18-41/frames/0005.jpg Time: 00:05.53
    #Saved: r:\render\jobs\farmerjoe_test.blend.2006-6-1_18-41\frames\0005.jpg Time: 00:05.53
    if ($msg =~ /Saved\:\s(.+[\/\\](\d+)\.(.{3}))\sTime\:\s(.+)/){
        # $1 = fullpath, $2 = frame #, $3 = file extension, $4 = time
        $status = "complete";
        print "completed";
    }
    return { status=>$status };
}

sub run{
    my $self = shift;
    my $connect_err = "";
    my $running = 1;
    
    while ($running){
        $server = IO::Socket::INET->new(
         Proto => "tcp",
         PeerAddr => $self->{c}->{master},
         PeerPort => $self->{c}->{port},
         ) or $connect_err = "Can't Connect to $self->{c}->{master} at Port $self->{c}->{port}\n";
         if (!$connect_err){
            print $server "SU SLAVE\n";
            my $msg = '';
            while (defined ($msg = <$server>)) {
                #switch
                print $msg;
                
                if ($msg =~ /CMD\s(\d+)\sRENDER\s-S\s(\d+)\s-E\s(\d+)\s-(.)\s"(.+)"/){
                    my $cmd = {id=>$1,start=>$2,end=>$3,type=>$4,blend=>$5};
                    my $sep = $self->{c}{sep};
                    $cmd->{blend} =~ s/\|/$sep/ge;
                    $self->renderStep($cmd);
                }
                if ($msg =~ /CMD\s(\d+)\sRENDER\s-F\s(\d+)\s"(.+)"\s(\d+)\s(\d+\.?\d*)\s(\d+\.?\d*)\s(\d+\.?\d*)\s(\d+\.?\d*)/){
                    my $cmd = {id=>$1,frame=>$2,blend=>$3,part=>$4,x1=>$5,y1=>$6,x2=>$7,y2=>$8};
                    my $sep = $self->{c}{sep};
                    $cmd->{blend} =~ s/\|/$sep/ge;
                    $self->renderPart($cmd);
                    #x1=0 x2=0.5 y1=0 y2=0.5 part=2 blender -b /render/bucket/bucket.blend -P /render/bucket_render.py
                
                }
                if ($msg =~ /VAR\s(.+)\s=\s"(.+)"/){
                    $self->{$1} = $2;
                }
                #else do nothing
                #print "yup\n";
            }
         }else{
             print $connect_err;
             print "Will try to reconnect in 30 seconds\n";
             sleep(30);
         }
         $connect_err = "";
    }
}

sub renderPart{
    my $self = shift;
    my $c = shift;
    my $anim = '';
    print "rendering... part \n";
    my $args = " -b ".'"'.$self->{c}{jobs}.$self->{c}{sep}.$c->{blend}.'"'." -s ".$c->{frame}." -e ".$c->{frame}." -P ".$self->{c}{bucket_render};
    my $env_vars = "";
    if ($self->{c}{os} eq 'linux'){
        $env_vars = "part=$c->{part} x1=$c->{x1} y1=$c->{y1} x2=$c->{x2} y2=$c->{y2} ";
    }elsif ($self->{c}{os} eq 'MSWin32') {
        $env_vars = "SET part=$c->{part}&SET x1=$c->{x1}&SET y1=$c->{y1}&SET x2=$c->{x2}&SET y2=$c->{y2}&";
    }elsif ($self->{c}{os} eq 'darwin'){
        $env_vars = "part=$c->{part} x1=$c->{x1} y1=$c->{y1} x2=$c->{x2} y2=$c->{y2} ";
    }
    
    my $render_cmd = "";
    
    $render_cmd = $env_vars.'"'.$self->{c}{blender}.'"'.$args;
    if ($self->{c}{os} eq 'MSWin32') {
        $render_cmd = "call $render_cmd";
    }
    print $render_cmd. "\n";
    
    my $pid = open BLENDER, "-|", $render_cmd or die "couldn't fork: $!\n";
    select((select(BLENDER), $|=1)[0]);
    while(<BLENDER>){
        print $_;
        #Saved: /render/jobs/farmerjoe_test.blend.2006-6-1_18-41/frames/0005.jpg Time: 00:05.53
        #Saved: r:\render\jobs\farmerjoe_test.blend.2006-6-1_18-41\frames\part_4_0005.jpg Time: 00:05.53
        if ($_ =~ /Saved\:\s(.+[\/\\]part_(\d+)_(\d+)\.(.{3}))\sTime\:\s(.+)/){
            # $1 = fullpath, $2 = frame, $3 = part, $4 = file extension, $5 = time
            #COMPLETED JOB 1155428934 PART 0075 FRAME 4 TIME tga
            print $server "COMPLETED JOB ".$c->{id}." PART ".$2." FRAME ".$3." TIME ".$5."\n";
            print "COMPLETED JOB ".$c->{id}." PART ".$2." FRAME ".$3." TIME ".$5."\n";
        }
    }
    print $server "STATUS IDLE\n";
}

sub renderStep{
    my $self = shift;
    my $c = shift;
    my $anim = '';
    print "rendering... $c->{type}\n";
    $anim = " -a" if $c->{type} eq 'A';
    my $args = " -b ".'"'.$self->{c}{jobs}.$self->{c}{sep}.$c->{blend}.'"'." -s ".$c->{start}." -e ".$c->{end}.$anim;
    
    my $render_cmd = '"'.$self->{c}{blender}.'"'.$args;
    if ($self->{c}{os} eq 'MSWin32') {
        $render_cmd = "call $render_cmd";
    }
    print $render_cmd. "\n";

    my $pid = open BLENDER, "-|", $render_cmd or die "couldn't fork: $!\n";
    #$|=1;#set to flush buffer to get the %
    select((select(BLENDER), $|=1)[0]);
    while(<BLENDER>){
        print $_;
        #Saved: /render/jobs/farmerjoe_test.blend.2006-6-1_18-41/frames/0005.jpg Time: 00:05.53
        #Saved: r:\render\jobs\farmerjoe_test.blend.2006-6-1_18-41\frames\0005.jpg Time: 00:05.53
        if ($_ =~ /Saved\:\s(.+[\/\\](\d+)\.(.{3}))\sTime\:\s(.+)/){
            # $1 = fullpath, $2 = frame #, $3 = file extension, $4 = time
            print $server "COMPLETED JOB ".$c->{id}." FRAME ".$2." TIME ".$4."\n";
        }
    }
    print $server "STATUS IDLE\n";
}

#}}}
1;
#{{{FarmerSubmitJob###############################################################################
package FarmerSubmitJob;

use IO::Socket;
sub new
{
    my $class = shift;
    my $self = {};
	bless ($self, $class);
    
    $self->{c} = shift;

    return $self;
}

sub run{
    my $self = shift;
    my $job_dir = shift;
    my $job_file = shift;
    
    my $server = IO::Socket::INET->new(
     Proto => "tcp",
     PeerAddr => $self->{c}->{master},
     PeerPort => $self->{c}->{port},
     ) or die "cannot connect to $self->{c}->{master}";
     print $server "NEWJOB $job_dir|$job_file\n";
     my $msg = '';
     while (defined ($msg = <$server>)) {
    #switch
        print $msg;
        if ($msg =~ /^RECV\sNEWJOB\s.+$/){
            return;
        }
        #else do nothing
    }
}#}}}
1;

################################################################################
package FarmerJobs;
use File::Copy;
#$self->{jobs}->[jobnumber]->{blendfile}
#                          ->{startframe}
#                          ->{endframe}
#                          ->{step}
#                          ->{jobdir}
#
#                          ->{jobfile}
#                          ->{status} [pending,stopped,running]
sub new
{
    my $class = shift;
    my $self = {};
	bless ($self, $class);
    $self->{c} = shift;
    $self->{debug} = $self->{c}->{debug};
    $self->{jobs} = [];
    $self->{util} = FarmerTools->new();
    return $self;
}

sub new_job {
    my $self = shift;
    my $job_file = shift;
    my $new_job = '';
    if ($job_file ne ''){
        $new_job = $self->load_job($job_file);
        push (@{$self->{jobs}},$new_job);
    }
    
    return 'RECV NEWJOB '.$new_job->{id};
}


sub load_job {
    my $self = shift;
    my $job_file = shift;
    my $sep = $self->{c}{sep};
    $job_file =~ s/\|/$sep/ge;
    my $job_data = {jobfile => $job_file};
    my $job_data_file = [];
    
    #filename     # vr.blend
    #startframe   # 1
    #endframe     # 360
    #step         # 5
    #timeout      # 180
    #jobdir       # jobdir
    #jobname      # name
    #image_x      # 800
    #image_y      # 600
    #xparts       # 4
    #yparts       # 4
    
    $self->{util}->read_file($job_data_file,$self->{c}->{jobs}.$self->{c}{sep}.$job_file);
    

    map { $_ =~ s/\r?\n//g } @{$job_data_file};
    $job_data->{blendfile} = $job_data_file->[0];
    $job_data->{startframe} = $job_data_file->[1];
    $job_data->{endframe} = $job_data_file->[2];
    $job_data->{step} = $job_data_file->[3];
    $job_data->{timeout} = $job_data_file->[4];
    $job_data->{jobdir} = $job_data_file->[5];
    $job_data->{jobname} = $job_data_file->[6];
    $job_data->{image_x} = $job_data_file->[7];
    $job_data->{image_y} = $job_data_file->[8];
    $job_data->{xparts} = $job_data_file->[9];
    $job_data->{yparts} = $job_data_file->[10];
    
    #make writeable for slaves
    my $mode = 0777;
    chmod $mode, $self->{c}->{jobs}.$self->{c}{sep}.$job_data->{jobdir}.$self->{c}{sep}.'frames';
    
    $job_data->{status} = 'PENDING';#pending,rendering,completed,error
    
    $job_data->{tasks} = [];
    
    
    if ($job_data->{startframe} == $job_data->{endframe} && ($job_data->{xparts} > 1 || $job_data->{yparts} > 1)){
        #if we are doing a single frame bucket render
        #we treat each bucket (rect) as a task
        my $task = 0;
        my $xlen = 1.0 / $job_data->{xparts};
        my $ylen = 1.0 / $job_data->{yparts};
        my $xPoint = 0.0; # This stores the current X value, and incriments xlen each iteration until its equel to 1.0
        my $yPoint = 0.0; 
        
        while ($xPoint < 0.999)
        {
            while ($yPoint < 0.999)
            {
                $job_data->{type} = 'Parts';
                $job_data->{tasks}->[$task]->{number} = $task;
                $job_data->{tasks}->[$task]->{part} = $task+1;
                $job_data->{tasks}->[$task]->{status} = 'PENDING';#pending,rendering,completed,error
                $job_data->{tasks}->[$task]->{allocated} = 0;#not allocated = 0, allocated = client number
                $job_data->{tasks}->[$task]->{rect_x1} = min(1.0, $xPoint);
                $job_data->{tasks}->[$task]->{rect_y1} = min(1.0, $yPoint);
                $job_data->{tasks}->[$task]->{rect_x2} = min(1.0, $xPoint+$xlen);
                $job_data->{tasks}->[$task]->{rect_y2} = min(1.0, $yPoint+$ylen);
                
                $task++;
                $yPoint = $yPoint + $ylen;
            }
            $yPoint = 0.0;# Reset yPoint for the next column
            $xPoint = $xPoint + $xlen;
        }
    }else{
        #if we are doing a single frame or many frames
        #we treat each frame as a task
        my $frame = $job_data->{startframe};
        for (my $i=0; $i<=$job_data->{endframe}-$job_data->{startframe}; $i++)
        {
            $job_data->{type} = 'Frames';
            $job_data->{tasks}->[$i]->{number} = $i;
            $job_data->{tasks}->[$i]->{frame} = $frame;
            $job_data->{tasks}->[$i]->{status} = 'PENDING';#pending,rendering,completed,error
            $job_data->{tasks}->[$i]->{allocated} = 0;#not allocated = 0, allocated = client number
            $frame++;
        }
    }
    $job_data->{id} = time;
    return $job_data;
}
sub min{
    my $x = shift;
    my $y = shift;
    return $x if $x < $y;
    return $y;
}
sub getActiveJob{
     my $self = shift;
     my $active_job = '';
     $self->checkFinishedJobs;
     print STDERR "GET ACTIVE JOB\n";
     foreach my $job (@{$self->{jobs}}){
         print STDERR "JOB ".$job->{id}."\n" if $self->{debug};
         print STDERR "STATUS = ".$job->{status}."\n" if $self->{debug};
         
         if ($job->{status} eq 'ACTIVE'){
             #CHECK TO SEE IF WE HAVE PENDING OR ERROR'ED tasks
             for (my $i=0; $i<=$#{$job->{tasks}}; $i++)
             {
                 if ($job->{tasks}->[$i]->{status} eq 'PENDING'||
                     $job->{tasks}->[$i]->{status} eq 'ERROR'){
                     $active_job = $job;
                 }
                 last if $active_job;
             }
             
         }
         last if $active_job;
     }
     return $active_job if $active_job;
     #else we get the first PENDING job and make it active
     foreach my $job (@{$self->{jobs}}){
         if ($job->{status} eq 'PENDING'){
             $active_job = $job;
             $job->{status} = 'ACTIVE';
         }
         last if $active_job;
     }
     return $active_job;
}

sub checkFinishedJobs{
    my $self = shift;
    print STDERR "CHECKING STATUS OF ALL JOBS\n";
    foreach my $job (@{$self->{jobs}}){
        if ($job->{status} eq 'ACTIVE'){
            my $running = 0;
            for (my $i=0; $i<=$#{$job->{tasks}}; $i++){
                $running = 1 unless $job->{tasks}->[$i]->{status} eq 'COMPLETED';
            }
            if (!$running){
                $job->{status} = 'COMPLETED';
                if ($job->{type} =~ /parts/i){
                    #make the finished frame
                    my $parts_dir = $self->{c}->{jobs}.$self->{c}{sep}.$job->{jobdir}.$self->{c}{sep}.'render_parts'.$self->{c}{sep};
                    my $frames_dir = $self->{c}->{jobs}.$self->{c}{sep}.$job->{jobdir}.$self->{c}{sep}.'frames'.$self->{c}{sep};
                    for (my $i=0; $i<=$#{$job->{tasks}}; $i++){
                        my $part = $job->{tasks}->[$i]->{part};
                        my $partfile = $parts_dir."part_".$part."_".$self->{util}->pad($job->{startframe}).".tga";
                        my $final = $frames_dir.$self->{util}->pad($job->{startframe}).".tga";
                        if ($part == 1){
                            print STDERR "copy $partfile $final\n" if $self->{debug};
                            copy($partfile,$final);
                        }else{
                            print STDERR  "$self->{c}->{composite} $partfile $final -compose src-over $final\n";
                            `$self->{c}->{composite} "$partfile" "$final" -compose src-over "$final"`;
                        }
                    }
                }
            }
            print STDERR "JOB $job->{id} STATUS = $job->{status}\n";
        }
    }
    #copy 1st part to final frame name
    #composite 2st part over final name
    #composite 3rd part over final name
    #...
}
sub getJobs{
    my $self = shift;
    my @jobs = ();
    foreach my $job (@{$self->{jobs}}){
            push(@jobs, $job);
    }
    return @jobs;
}

sub deleteJob{
    my $self = shift;
    my $client = shift;
    my $jobID = shift;
    my $web = shift;
    my $offset = 0;
    my $msg = '';
    
    foreach my $job (@{$self->{jobs}}){
        if ($job->{id} eq $jobID){
            #remove job from our jobs array
            splice (@{$self->{jobs}},$offset,1);
            my $job_dir = $self->{c}->{jobs}.$self->{c}->{sep}.$job->{jobdir};
            if ($self->{c}->{os} eq 'MSWin32'){
                `rmdir /s /q "$job_dir"`;
            }else{ #must be unix like this should do it
                `rm -R "$job_dir"`;
            }
            $msg = "Deleted ".$job->{id};
        }
        $offset++;
    }
    $msg .= "\n--done--" if $web;
    return $msg;
}

sub getTasks{
    my $self = shift;
    my $jobID = shift;
    my @tasks = ();
    foreach my $job (@{$self->{jobs}}){
    if ($job->{id} eq $jobID){
        for (my $i=0; $i<=$#{$job->{tasks}}; $i++){
            push(@tasks, $job->{tasks}->[$i]);
            }
        }
    }
    return @tasks;
}

sub checkTimedOutTasks{
    my $self = shift;
    print STDERR "CHECKING FOR TIMED OUT TASKS\n";
    foreach my $job (@{$self->{jobs}}){
        if ($job->{status} eq 'ACTIVE'){
            for (my $i=0; $i<=$#{$job->{tasks}}; $i++){
                if ($job->{tasks}->[$i]->{status} eq 'RENDERING' && 
                    $job->{tasks}->[$i]->{start_time} < (time - $job->{timeout})){
                    $job->{tasks}->[$i]->{status} = 'PENDING';
                    print STDERR "JOB $job->{id} FRAME $i HAS TIMED OUT AND BEEN RE-QUEUED\n";
                }
            }
        }
    }
}

sub getNextStepFor{
    my $self = shift;
    my $job = shift;
    my $assigned_to = shift;
    #    [1],[2],[3],{4},{5},{6},<7>,(8),<9>,<10>,11,12,13,14
    my $start = '';
    my $end = '';
    my $part = '';
    my $x1 = '';
    my $y1 = '';
    my $x2 = '';
    my $y2 = '';
    my $step = 0;
    print STDERR "GET NEXT STEP\n";
    #  $#{$job->{tasks}}
    for (my $task=0; $task<=$#{$job->{tasks}}; $task++)
    {
        my $task_status = $job->{tasks}->[$task]->{status};
        if ($task_status eq 'PENDING'||$task_status eq 'ERROR'){
            #update status as we are sending the task out to render
            $job->{tasks}->[$task]->{status} = 'RENDERING';
            $job->{tasks}->[$task]->{assigned_to} = $assigned_to;
            $job->{tasks}->[$task]->{start_time} = time;#used to check for timeout
            if ($job->{tasks}->[$task]->{rect_x1} ne ''){
                $x1 = $job->{tasks}->[$task]->{rect_x1};
                $y1 = $job->{tasks}->[$task]->{rect_y1};
                $x2 = $job->{tasks}->[$task]->{rect_x2};
                $y2 = $job->{tasks}->[$task]->{rect_y2};
                $start = $job->{startframe};#set start frame is not allready set
                $end = $job->{endframe};#always set end frame
                $part = $job->{tasks}->[$task]->{part};
            }else{
                 $start = $job->{tasks}->[$task]->{frame} unless $start;#set start frame if not allready set
                 $end = $job->{tasks}->[$task]->{frame};#always set end frame

            }
            $step++;
            last if $step == $job->{step};
        }elsif($task_status eq 'COMPLETED'||$task_status eq 'RENDERING'){
            next;
        }
    }
    return {start=>$start,end=>$end, part=>$part, x1=>$x1, y1=>$y1, x2=>$x2, y2=>$y2};
}

#
# Sets any tasks which are not COMPLETED or PENDING (ie. RENDERING, ERROR) to be PENDING
# For a specific job, if no job_id is specified resets ALL jobs tasks
#
sub resetTasks{
    my $self = shift;
    my $attr = shift||{};
    
    my $msg = "Tasks Reset for $attr->{job_id}";
    
    foreach my $job (@{$self->{jobs}}){
        if (($job->{id} eq $attr->{job_id} || $attr->{job_id} eq '')
                && $job->{status} ne 'COMPLETE' 
                && $job->{status} ne 'PAUSED'){#dont process completed or pausedjobs
             my $not_all_complete = 0;
             for (my $task=0; $task<=$#{$job->{tasks}}; $task++)
             {
                if ($job->{tasks}->[$task]->{assigned_to} eq $attr->{slave}){#only reset tasks for this slave if supplied
                     if ($job->{tasks}->[$task]->{status} ne 'COMPLETED' &&
                         $job->{tasks}->[$task]->{status} ne 'PENDING' ){
                         $job->{tasks}->[$task]->{status} = 'PENDING';
                         $job->{tasks}->[$task]->{assigned_to} = '';
                     }
                     if ($job->{tasks}->[$task]->{status} ne 'COMPLETED'){
                         $not_all_complete = 1;
                     }
                 }
             }
             print STDERR "SETTING STATUS TO PENDING\n" if $self->{debug} && $not_all_complete;
             $job->{status} = "PENDING" if $not_all_complete;
             last if $attr->{job_id};
         }
     }
     $msg .= "\n--done--" if $attr->{web} ne '';
     return $msg;
}

sub setJobStatus{
    my $self = shift;
    my $attr = shift||{};
    
    my $msg = "Job $attr->{job_id} Status set to ".$attr->{status};
    foreach my $job (@{$self->{jobs}}){
        if ($job->{id} eq $attr->{job_id}){
            $job->{status} = $attr->{status};
             last;
         }
     }
     $msg .= "\n--done--" if $attr->{web} ne '';
     return $msg;
}

sub setTaskStatus{
    my $self = shift;
    my $job_id = shift;
    my $frame = shift;
    my $status = shift;
    my $time = shift;#time to complete frame
    my $part = shift;
    print STDERR "Setting task status for $job_id frame $frame status $status\n";
    foreach my $job (@{$self->{jobs}}){
         if ($job->{id} eq $job_id){
             for (my $task=0; $task<=$#{$job->{tasks}}; $task++)
             {
                 if ($job->{tasks}->[$task]->{frame} == $frame && !$part){
                     $job->{tasks}->[$task]->{status} = $status;
                     $job->{tasks}->[$task]->{rendertime} = $time if $time;
                     last;
                 }elsif($job->{tasks}->[$task]->{part} == $part && $part){
                     $job->{tasks}->[$task]->{status} = $status;
                     $job->{tasks}->[$task]->{rendertime} = $time if $time;
                     last;
                 }
             }
             last;
         }
     }
}
1;

################################################################################
package FarmerMaster;

use strict;
use Socket;
use IO::Socket;
#use Benchmark::Stopwatch;
#my $stopwatch = Benchmark::Stopwatch->new->start;
#$stopwatch->lap('got state');
#print $stopwatch->stop->summary;

sub new
{
    my $class = shift;
    my $self = {};
	bless ($self, $class);
    
    $self->{c} = shift;
    $self->{debug} = $self->{c}->{debug};
    
    $self->{easter} = 0;
    
    $self->{filebits} = '';
    $self->{server} ='';
    $self->{connections} = ();
    $self->{server_fileno} = '';
    $self->{clients} = {};
    $self->{util} = FarmerTools->new();
    
    $self->{jobobj} = FarmerJobs->new($self->{c});#blank arrayref incase there as there is no jobs to start with.
    
    $self->{state}->{id} = "farmerjoe";
    $self->{state}->{jobs} = $self->{jobobj}->{jobs};#copy ref into state
    $self->{state}->{clients} = $self->{clients};
    if (-e $self->{c}{statefile}){
        my $state = $self->{util}->load_state($self->{c}{statefile});#returns arrayref
        $self->{state}->{id} = $state->{id};
        if (defined($state->{jobs})){
            @{$self->{jobobj}->{jobs}} = @{$state->{jobs}};#ref magic
        }
    }
    
    $self->{jobobj}->resetTasks;# as we just loaded a state file we should reset any tasks
    return $self;
}

sub run{
    my $self = shift;
    print STDERR "Attempting to bind to port $self->{c}{port}\n" if $self->{debug};
    $self->OpenServer();
    print STDERR "Now Accepting Connections\n";
    my $rout;
    while( 1 ) {
        print STDERR "Waiting for Connections ...\n" if $self->{debug};
        
#The usual idiom is:
#($nfound,$timeleft) = select($rout=$rin, $wout=$win, $eout=$ein, $timeout);
#or to block until something becomes ready:
#$nfound = select($rout=$rin, $wout=$win, $eout=$ein, undef); 

        select( undef, undef, undef, 1 );
        select( $rout = $self->{filebits}, undef, undef, 60 );
        my $routs = unpack("b*", $rout);
        if (int($routs)){
            print STDERR "Select $routs\n" if $self->{debug};
            my $pos = index( $routs,'1');
            while ( $pos >= 0 ) {
                $self->HandleFile( $pos );
                $pos = index( $routs,'1', $pos+1);
            }
        }else{#we only check for timed out tasks if nothing else is happening
            $self->{jobobj}->checkTimedOutTasks;
            $self->{easter}++;
            if ($self->{easter} > 15){
                my @farmerjoes_passtimes = (
                "took a dump","had breakfast","had morning tea","took a nap",
                "had dinner","drank a few beers","showed mrs joe a good time",
                "changed the oil in the tractor","harvested the north field",
                "sharpened the axe","chopped firewood","lit the fire","farted",
                "had a coffee","watched simpsons","whips the slaves","plants the north field with corn"
                );
                srand(time);
                print STDERR $farmerjoes_passtimes[int(rand($#farmerjoes_passtimes))]."\n";
                $self->{easter} = 0;
            }
        }
    }
}
sub checkIdleSlaves{
    my $self = shift;
    #see if we have any slaves waiting
        my @idle_slaves = $self->getIdleSlaves;
        if (@idle_slaves){
            #get active job
            print STDERR "THERE ARE IDLE SLAVES\n";

            ##allocate commands to all free clients
            foreach my $idle_slave (@idle_slaves){
                my $active_job = $self->{jobobj}->getActiveJob;
                if ($active_job){
                    my $cmd = $self->{jobobj}->getNextStepFor($active_job,$idle_slave);
                    $self->{clients}->{$idle_slave}->{status} = 'BUSY';
                    if ($active_job->{type} =~ /frames/i){
#CMD 1155387601 RENDER -S 1 -E 1 -A "farmerjoe_test.blend.2006-8-13_1-0|farmerjoe_test.blend"
                        $self->SendMessage(
                        "CMD ".$active_job->{id}." RENDER -S ".$cmd->{start}." -E ".$cmd->{end}." -A ".
                        '"'.$active_job->{jobdir}."|".$active_job->{blendfile}.'"', $idle_slave );
                    }elsif($active_job->{type} =~ /parts/i){
#CMD 1155387601 RENDER -F 1 "farmerjoe_test.blend.2006-8-13_1-0|farmerjoe_test.blend" 0.0 0.0 0.5 0.5
                        $self->SendMessage(
                        "CMD ".$active_job->{id}." RENDER -F ".$cmd->{start}.
                        ' "'.$active_job->{jobdir}."|".$active_job->{blendfile}.'" '
                        .$cmd->{part}.' '.$cmd->{x1}.' '.$cmd->{y1}.' '.$cmd->{x2}.' '.$cmd->{y2}, $idle_slave );
                    }
                }
            }
        }
        
        #save the current state to disk incase we die
        $self->{util}->save_state($self->{state},$self->{c}{statefile});
}

sub ProcessCommands{
    my $self = shift;
    my $client = shift;
    my $msg = shift;
    my $output = "";
    ########################################################################
    #
    #  ACTIONS THAT ERQUIRE CHECKING FOR FINSHED JOBS OR IDLE CLIENTS
    #
    ########################################################################
    if ($msg =~ /^su\s(.+)$/i){
         $output = $self->setClientType($client,$1);
         $self->checkIdleSlaves;# might be a slave thats joined they would be idle so assign them some work
    }
    if ($msg =~ /^reset\stasks\s(\d+)$/||$msg =~ /^reset\stasks\s(\d+)\s(web)$/||$msg =~ /^rt\s(\d+)$/){
        $output = $self->{jobobj}->resetTasks({job_id=>$1,web=>$2});
        $self->checkIdleSlaves;
    }
    if ($msg =~ /^start\sslave\s(\d+)$/||$msg =~ /^start\sslave\s(\d+)\s(web)$/||$msg =~ /^ss\s(\d+)$/){
        if ($self->{clients}->{$1}->{status} eq 'PAUSED'){
            $self->{clients}->{$1}->{status} = 'IDLE';
        }
        $self->SendMessage("--done--",$client) if $2 eq "web";
        $self->checkIdleSlaves;
    }
    if ($msg =~ /^pause\sslave\s(\d+)$/||$msg =~ /^pause\sslave\s(\d+)\s(web)$/||$msg =~ /^ps\s(\d+)$/){
        $self->{clients}->{$1}->{status} = 'PAUSED';
        $self->SendMessage("--done--",$client) if $2 eq "web";
    }
    if ($msg =~ /^start\sjob\s(\d+)$/||$msg =~ /^start\sjob\s(\d+)\s(web)$/||$msg =~ /^sj\s(\d+)$/){
        $output = $self->{jobobj}->setJobStatus({job_id=>$1,web=>$2, status=>"PENDING"});
        $self->checkIdleSlaves;
    }
    if ($msg =~ /^pause\sjob\s(\d+)$/||$msg =~ /^pause\sjob\s(\d+)\s(web)$/||$msg =~ /^pj\s(\d+)$/){
        $output = $self->{jobobj}->setJobStatus({job_id=>$1,web=>$2, status=>"PAUSED"});
    }
    if ($msg =~ /^NEWJOB\s(.+)$/){
         $output = $self->{jobobj}->new_job($1);
         $self->checkIdleSlaves;
    }
    if ($msg =~ /^COMPLETED\sJOB\s(\d+)\sFRAME\s(\d\d\d\d)\sTIME\s(.+)$/){
         #COMPLETED JOB 123 FRAME 1 TIME 12345679
         $output = $self->{jobobj}->setTaskStatus($1,$2,'COMPLETED',$3);
         $self->{jobobj}->checkFinishedJobs;
    }
    if ($msg =~ /^COMPLETED\sJOB\s(.+)\sPART\s(.+)\sFRAME\s(.+)\sTIME\s(.+)$/){
         #COMPLETED JOB 123 PART 1 FRAME 1 TIME 12345679
         $output = $self->{jobobj}->setTaskStatus($1,$3,'COMPLETED',$4,$2);
         $self->{jobobj}->checkFinishedJobs;
    }
    if ($msg =~ /^STATUS\sIDLE$/){
        if ($self->{clients}->{$client}->{status} ne 'PAUSED'){
            $self->{clients}->{$client}->{status} = 'IDLE';
        }
        $self->checkIdleSlaves;#obviously we need to :)
    }
    if ($msg =~ /^delete\sjob\s(\d+)$/||$msg =~ /^delete\sjob\s(\d+)\s(web)$/){
        $output = $self->{jobobj}->deleteJob($client,$1,$2);
        #TODO: Tell slaves working on tasks that belong to a deleted job to stop
        $self->checkIdleSlaves;
    }
    ########################################################################
    #
    #  GENERAL ACTIONS
    #
    ########################################################################
    if ($msg =~ /^HELLO$/){ 
         $output = "Hi"; 
    }
    if ($msg =~ /^whoami$/){
         $output = $client;
    }
    if ($msg =~ /^help$/){
        $output = "".
"su <client type [SLAVE]>: change user
show jobs (sj): Show list of current jobs
show tasks <job number> (st <>): Show list of tasks in Job
reset tasks <job number> (rt <>): Show list of tasks in Job
delete job <job number> : Delete the Job (No Confirmation so beware!)
show slaves (ss): SHow Rendering clients
";
    }
    if ($msg =~ /^show\sslaves$/ || $msg =~ /^ss$/||$msg =~ /^show\sslaves\s(web)$/ ){
        $output = $self->showSlaves($client,$1);
    }
    if ($msg =~ /^show\sjobs$/ || $msg =~ /^sj$/){
        $output = $self->showJobs($client);
    }
    if ($msg =~ /^show\stasks\s(.+)$/ || $msg =~ /^st\s(.+)$/ ){
        $output = $self->showTasks($client,$1);
    }
    if ($msg =~ /^send\sstate$/){
        $output = $self->sendState($client);
    }
    if ($msg =~ /^PING$/){
        $output = "MASTER PONG";
    }

    
    # default case:
    #do nothing
    return $output;
}

sub sendState{
    my $self = shift;
    my $client = shift;
    my $yaml = YAML::Tiny->new;
    $yaml->[0] = $self->{state};
    my $state_as_gzipped_yaml = $self->{util}->gzip($yaml->write_string);
    $self->SendMessage($state_as_gzipped_yaml,$client,"gz");
    $self->SendMessage("--done--",$client);
}

sub showSlaves{
    my $self = shift;
    my $client = shift;
    my $web = shift;
    foreach my $slave (keys(%{$self->{clients}})){
        if ($self->{clients}->{$slave}->{type} eq "SLAVE"){
            $self->SendMessage($self->{clients}->{$slave}->{type}." ".
                               $self->{clients}->{$slave}->{status}." ".
                               $self->{clients}->{$slave}->{hostname}." ".
                               $self->{clients}->{$slave}->{ip}
                               ,$client);
        }
     }
     $self->SendMessage("--done--",$client) if $web;
}

sub showJobs{
    my $self = shift;
    my $client = shift;
    my @jobs = $self->{jobobj}->getJobs;
    foreach my $job (@jobs){
        $self->SendMessage($job->{id}." ".$job->{status}." ".$job->{jobdir},$client);
    }
}
sub showTasks{
    my $self = shift;
    my $client = shift;
    my $job = shift;
    my @tasks = $self->{jobobj}->getTasks($job);
    foreach my $frame (@tasks){
        $self->SendMessage($frame->{number}." - status: ". $frame->{status}." rendertime: ".$frame->{rendertime},$client);
    }
}

sub getIdleSlaves{
     my $self = shift;
     my @idle_slaves = ();
     foreach my $client (keys(%{$self->{clients}})){
         if ($self->{clients}->{$client}->{type} eq 'SLAVE' &&
             $self->{clients}->{$client}->{status} eq 'IDLE'){
             push(@idle_slaves, $client);
         }
     }
     return @idle_slaves;
}

sub setClientType {
  my $self = shift;
  my $client = shift;
  my $client_type = shift;
  #We dont allow changing the type of client once set
  return "NOT HAPPY WITH WHAT YOU ARE? TOUGH!" if (defined ($self->{clients}->{$client}->{type}));
  if ($client_type eq 'SLAVE'){
      $self->{clients}->{$client}->{type} = $client_type;
      $self->{clients}->{$client}->{status} = 'IDLE';#[IDLE,BUSY,?]
      #foreach my $key (keys($self->{c})){
      #    $self->SendMessage('VAR '.$key.' = "'.$self->{c}->{$key}.'"',$client);
      #}
      $self->SendMessage('YOU ARE NOW A SLAVE',$client);
  }
  return;
}

sub SendMessage {
  my $self = shift;
  local( $Farmer::message ) = shift;
  my $from_client = shift;#we check this to only send a message to this client
  my $gz = shift;
  
  print STDERR "SendMessage $Farmer::message\n" if $self->{debug} && !$gz;
  $Farmer::message .= "\r\n";
  
  foreach my $fileno (keys %{$self->{connections}}) {
      next if !$fileno;
      if ( $self->{connections}->{$fileno} && $fileno eq $from_client){
          my $to_client = $self->{connections}->{$fileno}{client};
      print $to_client $Farmer::message;
    }
  }
}

#file refers to filehandles to read/write to clients
sub HandleFile {
  my $self = shift;
  local( $Farmer::fileno ) = @_;
  
  print STDERR "HandleFile $Farmer::fileno\n" if $self->{debug};
  if ( $Farmer::fileno == $self->{server_fileno} ) {
    $self->HandleServer();
  } elsif ( $self->{connections}->{$Farmer::fileno} ) {
    $self->HandleClient( $Farmer::fileno );
  } else {
    print STDERR "Weird fileno $Farmer::fileno\n" if $self->{debug};
  }
}

 sub HandleServer {
  my $self = shift;
  my $client = $self->{server}->accept();

  print STDERR "HandleServer\n" if $self->{debug};

  if ( $client ) {
    my $fileno = fileno($client);
    $client->blocking(0);
    $self->{connections}->{$fileno}{client} = $client;
    
    vec($self->{filebits},$fileno,1) = 1;
    $self->SendMessage( "# Welcome $fileno",$fileno);
    
    #get info about the client
    my $to_slave = $self->{connections}->{$fileno}->{client};
    my $sockaddr    = $to_slave->peername();
    my ($port, $iaddr) = sockaddr_in($sockaddr);
    $self->{clients}->{$fileno}->{id}       = $fileno;
    $self->{clients}->{$fileno}->{ip}       = inet_ntoa($iaddr);
    $self->{clients}->{$fileno}->{hostname} = gethostbyaddr($iaddr, AF_INET);
    #if hostname is blank and we are on linux the client may be
    #a windows machine so try nbtstat to get hostname
    if (-e $self->{c}->{nbtscan} && 
            $self->{clients}->{$fileno}->{hostname} eq "" &&
            $self->{c}->{os} eq 'linux'){
        my $hostdata = eval `$self->{c}->{nbtscan} -P $self->{clients}->{$fileno}->{ip}`;
        $self->{clients}->{$fileno}->{hostname} = $hostdata->{NBTSCAN}->{$self->{clients}->{$fileno}->{ip}}->{ComputerName};
    }
  } else {
    print STDERR "No accept for server, reopen\n" if $self->{debug};
    $self->CloseServer();
    $self->OpenServer();
  }
}

sub HandleClient {
  my $self = shift;
  local( $Farmer::fileno ) = @_;
  my $receive = '';
  recv( $self->{connections}->{$Farmer::fileno}{client}, $receive, 200, 0 );
  if ( $receive ) {
    my $line = $self->{connections}->{$Farmer::fileno}{receive};
    $line .= $receive;

    while ( $line =~ s/(.*)\n// ) {
      my $temp = $1;
      $temp =~ tr/\r\n//d;
      print STDERR "HandleClient $Farmer::fileno\n";
      #$self->SendMessage( "RECV ".$temp, $Farmer::fileno );
      my $result = $self->ProcessCommands($Farmer::fileno,$temp);
      $self->SendMessage( $result, $Farmer::fileno ) if $result;
    }
    $self->{connections}->{$Farmer::fileno}{receive} = $line;
  } else {
    $self->{jobobj}->resetTasks({slave=>$Farmer::fileno});
    $self->closeClient($Farmer::fileno);
    print STDERR "Close client $Farmer::fileno\n";
    vec($self->{filebits},$Farmer::fileno,1) = 0;
    #remove clients connection info from connections
    delete $self->{connections}->{$Farmer::fileno};
    #remove client from clients
    delete $self->{clients}->{$Farmer::fileno};
  }  
}

sub closeClient{
    my $self = shift;
    local( $Farmer::fileno ) = @_;
    print STDERR "Close client $Farmer::fileno\n";
    vec($self->{filebits},$Farmer::fileno,1) = 0;
    $self->{connections}->{$Farmer::fileno}{client}->close();
    undef $self->{connections}->{$Farmer::fileno};
    #remove client from clients
    undef $self->{clients}->{$Farmer::fileno};
    $self->SendMessage( "Close Client ".$Farmer::fileno, $Farmer::fileno );
}

sub CloseServer {
  my $self = shift;
  vec($self->{filebits},$self->{server_fileno},1) = 0;
  $self->{server}->close();
  undef $self->{server};
}

sub OpenServer {
  my $self = shift;
  $self->{server} = IO::Socket::INET->new(Listen    => 10,
                            LocalPort => $self->{c}->{port},
							Reuse => 1,
							ReuseAddr => 1,
							Timeout   => 0,
							Proto     => 'tcp');
  if (!$self->{server}){
      print STDERR "Could not create socket $!\nFarmerjoe now Exiting\n";
      exit;
  }

  $self->{server}->blocking(0);
  $self->{server_fileno} = fileno($self->{server});
  vec($self->{filebits},$self->{server_fileno},1) = 1;

  print STDERR "Starting Farmerjoe Master on port $self->{c}{port}\n";
  print STDERR "Server Fileno: $self->{server_fileno}\n" if $self->{debug};
}
1;

package FarmerTools;
use POSIX qw(strftime);
use YAML::Tiny;
use Compress::Zlib;

sub new
{
    my $class = shift;
    my $self = {};
	bless ($self, $class);
    return $self;
}

sub pad{
    my $self = shift;
    my $frame = shift;
    while (length($frame) < 4) {
        $frame = "0".$frame;
    }
    return $frame;
}

sub file_to_string{
    my $self = shift;
    my $in = '';
    my $file = shift;
    open (IN,$file) or die "$! ".$file;
    while ( <IN> )
    {
      $in = $in . $_;
    }
    close(IN);
    return $in;
}

sub read_file{
    my $self = shift;
    my $in = shift;
    my $file = shift;
    open (IN,$file) or die "$! ".$file;
    @{$in} = <IN>;
    close(IN);
}

sub write_log 
{
    my($self) = shift;
    my($logfile) = shift;
    my $datetime = strftime "%d/%m/%Y %H:%M:%S", localtime;
    
    open(LOG,">>$logfile");
    print LOG "$datetime @_\n";
    close(LOG);
}

sub load_conf{
    my $self = shift;
    my $conf_file = shift;
    my $conf = {};
    my @conf_data = ();
    $self->read_file(\@conf_data,$conf_file);
    map { $_ =~ s/\r?\n//g } @conf_data;
    foreach my $line(@conf_data){
        next if $line =~/^#.+/;
        my ($key,$value) = split(/\s?=\s?/,$line);
        $conf->{$key} = $value;
    }
    return $conf;
}
sub save_state{
    my $self = shift;
    my $state = shift;
    my $state_file = shift;
    my $yaml = YAML::Tiny->new;
    $yaml->[0] = $state;
    #print $yaml->write_string;
    $yaml->write( $state_file );
    return;
}
sub load_state{
    my $self = shift;
    my $state_file = shift;
    my $state = YAML::Tiny->read($state_file);
    return $state->[0];
}
sub loadYAML{
    my $self = shift;
    my $yaml_string = shift;
    my $state = YAML::Tiny->read_string($yaml_string);
    return $state->[0];
}
sub gzip{
    my $self = shift;
    my $data = shift;
    return Compress::Zlib::memGzip($data) ;
}
sub gunzip{
    my $self = shift;
    my $data = shift;
    return Compress::Zlib::memGunzip($data) ;
}
1;
################################################################################
package FarmerAppServer;

use strict;
use Socket;
use IO::Socket;
use Sys::Hostname;

$|=1;

sub new
{
    my $class = shift;
    my $self = {};
	bless ($self, $class);
    #read template
    while(<FarmerAppServer::DATA>)
    {
        $self->{template} .= $_;
    }
    $self->{c} = shift;
    $self->{codes} = {200=>'OK',
                      404=>'Not Found',
                      500=>'Internal Server Error',
                      302=>'Found',
                      400=>'Bad request',
                      501=>'Not implemented'};
    $self->{util} = FarmerTools->new();
    return $self;
}

sub logmsg {
    my $self = shift;
    print STDERR scalar localtime, ": $$: @_\n";
}

sub logerr ($$) {
    my $self = shift; 
    my ($code, $detail) = @_;
    my $msg = "$code " . $self->{codes}{$code};
    $self->logmsg("$detail : $msg");
    print  "HTTP/1.0 $msg\nContent-type: text/html\n\n";
    print  "<I>Farmerjoe Server</I> : $detail : $msg\n";
}

sub run{
    my $self = shift;
    my $tcp = getprotobyname('tcp');
    socket(Server, PF_INET, SOCK_STREAM, $tcp)      || die "socket: $!";
    setsockopt(Server, SOL_SOCKET, SO_REUSEADDR,
    pack("l", 1))   || die "setsockopt: $!";
    bind(Server, sockaddr_in($self->{c}{appserver_port}, INADDR_ANY))    || die "bind: $!";
    listen(Server,SOMAXCONN)                        || die "listen: $!";
    
    $self->logmsg("Farmerjoe Application Server accepting connections on port ".$self->{c}{appserver_port});
    $self->logmsg("Point your web browser to http://".hostname().":".$self->{c}{appserver_port});
    
    my $addr;
    my @inetaddr;
    
    for ( ; $addr = accept(Client,Server); close Client) {
        my($undef, $undef, $inetaddr) = unpack('S n a4 x8', $addr);
        @inetaddr = unpack('C4', $inetaddr);
    
        $self->logmsg("Incoming connection from: " , join(".", @inetaddr));
    
        *STDIN = *Client;
        *STDOUT = *Client;
    
        $_ = <STDIN>;
        my ($method, $url, $proto, $garbage) = split;
    
        if ($garbage ne '') { 
        logerr 400, $_;
        } else {
                $self->logmsg("Req: mthd=$method, url=$url, prot=$proto");
                $url =~ s/%([\dA-Fa-f]{2})/chr(hex($1))/eg; # unescape.
                $self->logmsg("Unescaped url: $url");
    
            if ( $method ne 'GET') {
            if ( $method ne 'POST' ) {		
                $self->logerr(501, $method);
            } else {
                while ( <STDIN> ) {
                    print STDERR $_;
                }
            }
            } else {
                if ( $url !~ m|.*/([^/]*)$| ) {
                    $self->logerr(400, $url);
                } else {
                    my $file = $1;
                    $self->{code} = 200;
                    my $res = $self->process_request($url);
                    $self->logmsg("Sending results...");
                    print "HTTP/1.0 ".$self->{code}." ".$self->{codes}{$self->{code}}."\n";
                    print $res;
                }
            }
        }
        close STDIN;
        close STDOUT;
    }
}


sub process_request{
    my $self = shift;
    my $url = shift;
    my $output ="Content-type: text/html\n\n";
    # action /showtasks/<job id>
    # action /showtasks/1155676995
    
    $url =~ s/^\///;#remove leading /
    my @action = split(/\//,$url);
    
    if($action[0] eq 'logo.jpg'){
        return $self->logo;
    }
    if($action[0] eq 'pause.jpg'){
        return $self->pause_jpg;
    }
    if($action[0] eq 'play.jpg'){
        return $self->play_jpg;
    }
    if($action[0] eq 'reset.jpg'){
        return $self->reset_jpg;
    }
    if($action[0] eq 'delete.jpg'){
        return $self->delete_jpg;
    }
    
    #start/stop jobs
    if($action[0] eq 'startjob'){
        $self->farmerjoe_request('start job '.$action[1].' web');
    }
    if($action[0] eq 'pausejob'){
        $self->farmerjoe_request('pause job '.$action[1].' web');
    }
    #start/stop slaves
    if($action[0] eq 'startslave'){
        $self->farmerjoe_request('start slave '.$action[1].' web');
    }
    if($action[0] eq 'pauseslave'){
        $self->farmerjoe_request('pause slave '.$action[1].' web');
    }
    #reset tasks
    if($action[0] eq 'reset' && $action[1] eq 'tasks'){
        $self->farmerjoe_request('reset tasks '.$action[2].' web');
    }
    #delete job
    if($action[0] eq 'delete' && $action[1] eq 'job'){
        $self->farmerjoe_request('delete job '.$action[2].' web');
        $self->{code} = 302;
        sleep(1);#give the master time to do its thing
        return "Location: /\n\n";
    }
    
    
    #load state
    $self->loadState;
    
    $self->{jobobj} = FarmerJobs->new($self->{c});
    $self->{jobobj}->{jobs} = $self->{state}->{jobs};
    
    #get slaves
    my $slaves = $self->getSlaves();
    #show jobs
    my $jobs = $self->getJobs();
    #show tasks
    my $tasks = {output=>'<br/>Select a Job'};
    $self->logmsg("1->".$action[0]);
    $self->logmsg("2->".$action[1]);
    $self->logmsg("3->".$action[2]);
    if ($action[0] eq 'showtasks'){
        $tasks = $self->getTasks($action[1]);
    }
    $output .= $self->{template};
    if ($self->{connected}){
        $output =~ s/\[%\smessage\s%\]//g;
        $output =~ s/\[%\sslaves\s%\]/$slaves->{output}/ge;
        $output =~ s/\[%\sjobs\s%\]/$jobs->{output}/ge;
        $output =~ s/\[%\stasks\s%\]/$tasks->{output}/ge;
    }else{
        my $msg = "<strong>Could not connect to master: ".$self->{c}->{master}."</strong>";
        $output =~ s/\[%\smessage\s%\]/$msg/ge;
        $output =~ s/\[%\sslaves\s%\]//g;
        $output =~ s/\[%\sjobs\s%\]//g;
        $output =~ s/\[%\stasks\s%\]//g;
    }
    return $output;
}

sub farmerjoe_request{
    my $self = shift;
    my $request = shift;
    my @output = ();
    $self->logmsg("here");
    my $server = $self->{master};
    my $msg = '';
    
    if ( ref($server) ne 'IO::Socket::INET' ||
       ( ref($server) eq 'IO::Socket::INET' && !$server->connected)){
        $self->logmsg("Attempting to connect to Master");
        my $err = $self->connectMaster;
        if ($err){
            $self->{connected} = 0;
            $self->logmsg("Could not connect to Master ".$err->{output});
        }else{
            $self->{connected} = 1;
            $server = $self->{master};
        }
    }
    
    if ( ref($server) eq 'IO::Socket::INET' && $server->connected){
        print $server "$request\n";
        while (defined ($msg = <$server>)) {
             #$self->logmsg($msg);
             if ($msg =~ /--done--/){
                 $self->logmsg("done");
                 last;
             }elsif($msg =~ /Welcome/){
                 next;
             }
             $self->logmsg($request);
             push(@output,$msg);
        }
        return @output;
    }
}

sub connectMaster {
    my $self = shift;
    #TODO: Disconnect ?
    $self->{master} = IO::Socket::INET->new(
    Proto => "tcp",
    PeerAddr => $self->{c}->{master},
    PeerPort => $self->{c}->{port},
    ) or return {error=>1, output=>"Can't connect to $self->{c}->{master}"};
    return undef;
}
sub loadState{
    my $self = shift;
    my @state = $self->farmerjoe_request("send state");
    my $yaml = $self->{util}->gunzip(join("",@state));
    #$self->logmsg($yaml);
    $self->{state} = $self->{util}->loadYAML($yaml);
    return;
}

sub getTasks{
    my $self = shift;
    my $jobID = shift;
    my $type = "";
    my $output = "";
    
    
    foreach my $job (@{$self->{jobobj}->{jobs}}){
    if ($job->{id} eq $jobID){
        for (my $i=0; $i<=$#{$job->{tasks}}; $i++){
            my $task = $job->{tasks}->[$i];
            $type = $job->{type};
            $output .= Tr(td({width=>'10%'},$task->{number}).
                          td({width=>'10%'},$task->{frame}.$task->{part}).
                          td({width=>'26%'},$task->{rendertime}).
                          td({width=>'26%'},$self->{state}->{clients}->{$task->{assigned_to}}->{hostname}." / ".
                                            $self->{state}->{clients}->{$task->{assigned_to}}->{ip}).
                          td({width=>'26%',class=>lc($task->{status})},$task->{status}));
            }
        }
    }
    my $type_single = "";
    if ($type =~ /parts/i){
        $type_single = "Part";
    }elsif($type =~ /frames/i){
        $type_single = "Frame";
    }
    
    my $head = th(Tr({class=>"tasks"},td({width=>'10%'},"Number").
                                      td({width=>'10%'},$type_single).
                                      td({width=>'26%'},"Rendertime").
                                      td({width=>'26%'},"Assigned To").
                                      td({width=>'26%'},"Status")));
    
    $output = ScrollWidth(Table($head)).Scroll(Table($output));
    return {output=>$output};                 
}

sub getJobs{
    my $self = shift;
    my $output = th(Tr({class=>"jobs"},td({width=>'355'},"Job").td({width=>'20%'},"Type").td({width=>'20%'},"Status").td({style=>"text-align: right;"},"Actions")));
    my $gradient_css = "position:absolute; top:0px; left:0px; width:350px;	height:20px; background-color: #73BF60; background-repeat:no-repeat;";
    my $mask_css = "position:absolute; font-size:1px; height:20px; background-color:#EEEEEE; top:0px;";
    foreach my $job (@{$self->{jobobj}->{jobs}}){
        #calculate % done
        my $number_of_tasks = $#{$job->{tasks}}+1;#Tasks start at 0
        my $completed = 0;
        foreach my $task (@{$job->{tasks}}){$completed++ if $task->{status} eq 'COMPLETED'};
        my $percentage = $completed/$number_of_tasks;
        my $offset = int($percentage*350);
        my $width = 350 - $offset."px";
        $offset = $offset."px";
        $percentage = int($percentage*100).'%';
        my $jobname_progress = qq{<div id="mContainer">
        <div id="gradient_$job->{id}"  style="$gradient_css"></div>
        <div id="mask_$job->{id}" style="width: $width; left: $offset; $mask_css"></div>
        <div id="progressIndicator"><a title="$percentage Complete, $completed/$number_of_tasks Tasks" href="/showtasks/$job->{id}">$job->{jobdir}</a></div></div>};
        
        my $pause_play = "";
        if($job->{status} eq "PAUSED"){
            $pause_play = a({href=>'#', onclick=>"askfirst('/startjob/$job->{id}','Are you sure you want to start this job?')",title=>'Start Job'},'<img src="/play.jpg" alt="&gt;" width="16" height="16"/>');
        }elsif($job->{status} eq "ACTIVE"||$job->{status} eq "PENDING"){
            $pause_play = a({href=>'#', onclick=>"askfirst('/pausejob/$job->{id}','Are you sure you want to pause this job?')",title=>'Pause Job'},'<img src="/pause.jpg" alt="||" width="16" height="16"/>');
        }
        $output .= Tr(td($jobname_progress).td($job->{type}).td({class=>lc($job->{status})},$job->{status}).
        td({style=>"text-align: right;"},$pause_play.
        a({href=>'/reset/tasks/'.$job->{id},title=>'Reset Tasks - Sets all Tasks not COMPLETE to PENDING'},'<img src="/reset.jpg" alt="O" width="16" height="16"/>').
        a({href=>'#', onclick=>"askfirst('/delete/job/$job->{id}','Are you sure you want to Delete the job and job Directory?')",title=>'Deletes the job and job Directory'},'<img src="/delete.jpg" alt="X" width="16" height="16"/>')));
        
    }
    $output = Table($output);
    return {output=>$output};
}

sub getSlaves{
    my $self = shift;
    my $slaves = $self->{state}->{clients};
    my $header = th(Tr({class=>"slaves"},td({width=>'25%'},"IP").td({width=>'25%'},"Host Name").td({width=>'25%'},"Status").td({width=>'25%',style=>"text-align: right;"},"Actions")));
    my $output = "";
    foreach my $key (keys(%{$slaves})){
        my $slave = $slaves->{$key};
        if ($slave->{type} eq "SLAVE"){
            
            my $pause_play = "";
            if($slave->{status} eq "PAUSED"){
                $pause_play = a({href=>'#', onclick=>"askfirst('/startslave/$slave->{id}','Are you sure you want to start this slave?')",title=>'Start Job'},'<img src="/play.jpg" alt="&gt;" width="16" height="16"/>');
            }elsif($slave->{status} eq "BUSY"||$slave->{status} eq "IDLE"){
                $pause_play = a({href=>'#', onclick=>"askfirst('/pauseslave/$slave->{id}','Are you sure you want to pause this slave?')",title=>'Pause Job'},'<img src="/pause.jpg" alt="||" width="16" height="16"/>');
            }
            $output .= Tr(td($slave->{ip}).td($slave->{hostname}).td({class=>lc($slave->{status})},$slave->{status}).
            td({style=>"text-align: right;"},$pause_play));
            
        }
    }
    $output = tb($output) if $output;
    $output = Table($header.$output);
    return {output=>$output};
}
sub ScrollWidth{
    return '<div style="margin: 0px; width: 100%;">'.shift(@_).'</div>';
}
sub Scroll{
    return '<div style="border: 1px inset ; margin: 0px; padding: 6px; overflow: auto; width: 98%; height: 200px;">'.shift(@_).'</div>';
}
sub Table{return '<table width="100%" border="0" cellpadding="0" cellspacing="0">'."\n".shift(@_)."</table>\n"}

sub div{return element("div",@_);}
sub ul{return element("ul",@_);}
sub li{return element("li",@_);}
sub th{return element("thead",@_);}
sub tb{return element("tbody",@_);}
sub Tr{ return element("tr",@_);}
sub td{ return element("td",@_);}
sub a{ return element("a",@_);}

sub element{
    my $tag = shift;
    my $attrib = "";
    my $content = "";
    if ($#_ > 0){
        my $attrib_data = shift(@_);
        foreach my $key (keys(%{$attrib_data})){
            $attrib .= $key.'="'.$attrib_data->{$key}.'" ';
        }
        $content = shift(@_);
    }else{
        $content = shift(@_);
    }
    return "<$tag $attrib>\n$content</$tag>\n"
}
sub decode_base64 ($)
{
    local($^W) = 0; # unpack("u",...) gives bogus warning in 5.00[123]
    use integer;

    my $str = shift;
    $str =~ tr|A-Za-z0-9+=/||cd;            # remove non-base64 chars
    if (length($str) % 4) {
	require Carp;
	Carp::carp("Length of base64 data not a multiple of 4")
    }
    $str =~ s/=+$//;                        # remove padding
    $str =~ tr|A-Za-z0-9+/| -_|;            # convert to uuencoded format
    return "" unless length $str;

    ## I guess this could be written as
    #return unpack("u", join('', map( chr(32 + length($_)*3/4) . $_,
    #			$str =~ /(.{1,60})/gs) ) );
    ## but I do not like that...
    my $uustr = '';
    my ($i, $l);
    $l = length($str) - 60;
    for ($i = 0; $i <= $l; $i += 60) {
	$uustr .= "M" . substr($str, $i, 60);
    }
    $str = substr($str, $i);
    # and any leftover chars
    if ($str ne "") {
	$uustr .= chr(32 + length($str)*3/4) . $str;
    }
    return unpack ("u", $uustr);
}
sub decode_image_data{
    my $data = shift;
    my $content_type = shift;
    my $output ="Content-type: $content_type\n\n";
    foreach my $line (split(/\r?\n/,$data)) { 
        $output .= decode_base64($line); ### output decoded line
    }
    return $output;
}
sub logo{
    my $self = shift;
    my $logo_base64 = <<__END_LOGO__;
/9j/4AAQSkZJRgABAQAAAQABAAD/4QAMTmVvR2VvCAAAS//bAEMACAYGBwYFCAcHBwkJCAo=
DBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJ
CQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIy
MjIyMjL/wAARCAA8ASwDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQo=
C//EALUQAAIBAwMCBAMFBQQEAAABfQECAwAEEQUSITFBBhNRYQcicRQygZGhCCNCscEVUtHwJDNi
coIJCg==
FhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJ
ipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx
8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQo=
C//EALURAAIBAgQEAwQHBQQEAAECdwABAgMRBAUhMQYSQVEHYXETIjKBCBRCkaGxwQkjM1LwFWJy
0Qo=
FiQ04SXxFxgZGiYnKCkqNTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqCg4SF
hoeIiYqSk5SVlpeYmZqio6Slpqeoqaqys7S1tre4ubrCw8TFxsfIycrS09TV1tfY2dri4+Tl5ufo
6ery8/T19vf4+fr/2gAMAwEAAhEDEQA/ANUsB1IFRvcRR43yKuTgZNeJ3Os38l+T9pmDKSud5xiq
z3s8p3SzyHnqXJNe3LOIrRR/E87kPbF1nT2uGgF1GZF6jNUZ/F2jW8/kvdAtnGVGQK8bEsm07Gbc
epzigFQnIzjv71hLOKltIofIetz+ONIgdkLyNtbaSq5HWrtv4p0e5BKXiAAAndx1rxffIw2ggDrn
NL5mHIU8DioWb1k9Ug5D3SPVLGZd0d1Ew55DenWp1uIXVWWVCg==
tyCGHNeCx3cseDFIylewNSJfXAdUM0nyfdG4/LW6znvD8Q5D3nI9aXNeNHxLqcnKXboWO4AHgYr6
F0/UbSw8C2urX0O9YrNJpTHEGYnAzXJj+J6WEUF7NycnZJW/U2w+Fda+trHP5ozU9r8UPCd44RfM
VnOFDQKCf1qG+1aw1K9lurN4xA5+UAgdOK78szWpjZNTouml1bTv9zJrUY01eM7iZozTM0Zr2bHN
cfmjNMzRmiwXH5ozTM0ZosFx+aM0zNGaLBcfmjNMzRmiwXH5ozTM0ZosFx+aM1e0azt768MVxL5Y
CEqM43H0zUOpQw2188UD70GOc5wfSub61T+sfVrPmtfZ2te2+1/I09m/Z+06bFfNGaZmjNdNjO4/
NGaZmjNFguPzRmmZozRYLj80mabmjNFguOzRmqt3fQ2cIkkdQGOFyeprA1TxTHbyr9nbcEAZsHgg
1hWxFOkrzYXOo3DOMjNQG+gWR0Z9rIcEGvOX1+dbu2uRI2Y8owJyGHP9DVK81q8uLlmaViV+XKgY
IHSvMlnFP7KC5zM7OZ5uMAMcfnTAFI9c0ty5Ny577z/OmKRgAjg/pXgy3OuwKxBK9WHp0qQr8uCc
EdqjOwLxkN3PtTlzIrNjIHP1pA+4qZTccng9PQUFiWUgHcaMM0u5T1HQ/SgMBHkjn1BpCHAEkDsT
zikDtnIwC3B+lNVgqkg8gYJpy7iijPy55PoK
YrC7ihAXPB619Mw6UNc+GcOmJKIzdaciLIQSFO0YJA618x5JA5yFr3S78Tx2/wAJ7VfMeC5nsgkB
jydpUcHI6Zx+teDndKrUqYf2Wj5t+2h6OBsozv2Mq3+C+p2tzHPDrlusqDhvIPpjpmn+G/hzbRaj
qq6tqrPb6bKFzExjDfKGJJzxjPSvNR4j17DBNW1D/v8At9fWtvw3out+L1nRtQlisvMUzSyuSrOe
APc1pKli6VKTxGIstNUrNa/m9kTCVCckqdO77f0z2DS7LwzrCNFouq73hG0hJS+M9yD1rnLbWrYe
JZNEvsxXEdysBC87snqKv+CdM8L6B4iu7LS7ya71FYR9pmLAoBn7vpnNcDq7LJ8ZWZGJD38fOeP4
a0yrOMZh6lajzylFRuuffb7/AELxGGhJQlZJtpO2x7RcaDp8MkcrymO3AO/c/U9hmq+p6XYJDDcW
smFklVAFbcGz1xXGfF/Vruxm0qGC4MUbq7HacAngfyrkNC8bX7apBFdgGOR0CccISwFelk2Nr1qN
HE4nESulqtOVrXfrfz+RhifZwqOlGC6HtNzoml2oWSaZ44wcHJ+8aY+i2F7amTT5QG3YHJI+nrVL
xnqNrZR2puZgmd7ZPTAxmk8G6taXtpeNaziVYXG7b9P51yxx2Lhk0Mz+tN1E9nbla5rWatd6dbm/
s6bxLw/Ird+uxfi03Ro5PsrzebcdD85HPt2rF1u1i0m4AMo8l13qWPQelebS+Oru61u3tbOFYg90
ELMckjcBXWfFp3TUPD+XZU8/DnsBlc/Wu2WaVMBmFOEasqsaildSta61TjZaehgqUa9GT5VFxfT9
Tp1tNO07SjqWsXKxQYzy20AHpz601U0jW9ImuPDt3FcTxDgK
+RuxnDDqKr/EC50GLT7V9ftbqe1Z/lMOcA44zgiuT0Lxt4D8NXM82m2d9C0yBG+UnODwME188s9z
XFKWJpympXdkkuRW6Pv6nc8Lh6dqcuW3m9SXwLqN14n8S3thqCmBLWFmKIcHduA5roxpumaVq0i6
5raxidyLO2eYJ8vuepNcr8Ob+11D4na9eW6yJFNE7Rqy4blh1HbvXFfEa5luPH2pZkZxG4jUH+FQ
o4/MmuupjMfisb7L2soJwTdns79Oxgo=
nRo0eblUtbfmemx6TZzfEn+yV1W6mszYvOY45fuPlccjkjBNct4rudW0vx0NC0W5ml37FiikwxJY
etU/g9IzeOHJYkmzlznPPK11bNB/wv6Lzh8wtv3X+9s4/rUrG4vDYxU5VZSUabe+7T3D2NOrS5lF
K8joINKtfDmlC58T60jSEAtyEUEdQvc1fgt9G16xa50O9hlx/cl3AH0I6ivKvjPNdt4phhlc/ZUt
wYFzgZJO4/XpUHwgnuovHEUUXmNbyQOJggyAAOCfx/nTw+KzKrhvrixMlJq6WnKvKz/EclQjV9j7
NW/E7Gz1UXXiX/hH2t5Y9Q3bdpGV+ufTHOa7Oex0LTNkF/doJ26b5Npb6AdqwStovxoRljDXDaa2
ST0OeMfhWf421HwjbeIkHiCyvZbsRgxshO0r7YI96dbiXG4n2EPeSlHmfJbmfo3shwwNKnzy00el
9jqdT0WCO0F3ZPuixu+9kMPUGsHNZsHxM8N2ujPpenpeRx7XWPeu7aW6ck9K5zS/FV9ds8dxas6Q
JvuHhXonQtz6ZBr6PI85n7KcMZzaP3XJateduqZ5+OpU4yi6bWu9jsZbiKBGeWRVVRkknoKx4vEU
V1eTWluA8qcgf3gM5x69K5W71+WA/Z7mNbi3eJ1HJAOcjqOvIBrFtrq40+O01G3YF42O04+6ehU/
ga7sTnDuvYo41HubmsX73ttIIZUnaGUnCg==
p+VdvXP51zl3c/aUWQACXy9jkdGxUFzeyGWWSMtF5mSQD1B7UyLPODnIzXizqTm+aTG1pcRJC3ll
iRk4P5U6J9qkN1yajQkDITdg7ee9QSROZWxnGfWs9x8qbsyOaQo=
3Mpxkbzxj3prc4cdSAcDrUsg/wBJcnorng/WowvqOMkZFav4mdF0MCgOuTkjtUiblLkYAwQRViGz
89Qu4CXll3dxQ0aoyjKk9Dg1N7kOaIQCqj5Plx1zTfLJymTuByD6itn7Da/2RDfLOQdzRyKV79v6
002QhFoWuItsxMispzt7EH9KXMgu0Zn2VliWQ42uTkDrxSlANgQdSc1YaVo2ZQflzkZ7g1NJdWf2
wyfZDs8kKqK+MSYxu/OjUV2ysbIGMOqMUKdfcckVdV767ggjaZxbW6CLG84wx7j0quJJzatAspA6
7e31pUuJF+TORwo=
ffHSk0nv0EqkkmkxZ4hHcyIWB2HblTwa19N8S3mn6O2mW0nlwiUXGQvLkEcH24rDYlpHAySB+tS2
1yLacs0aspVl/MVM4RmlzK9tQpzlB+67Gtputy6Hc3MiFort8OW28MMhguPr3qRLqzvLiC5aeWG8
S48xpmGRt4/XNYNw0tzdiWSTc7AK
fy4p0ReM7kIyOuaz9lC7l1ZbxD5Yx6I3/GXiAeIbmzVFJitY2QOerEnk/oKxdL322o2ss2SscqPh
eTgEHj8qiLHBBwMjcMVNFcJGG/dbpNqlXz07mqp0oU6SpR2JnXnUqc73O8+J3iOw1+PTbTTnaSWF
neX5CCuQOPrR8N/Eml+H9H1K31G58m4kk3qrAkEbfauDink837SOEld1DMMnNQZeG4+TaWwGJPOa
4nllJ4RYS75V9+9zq+uzVf21lcntto1q2unO1TciU+wDg5xXc/FTxDpevxaaum3izNGzlyoIxnFc
PaNvG4gYzgN39KryqkabMjdk4+nrXRUwsKlanVb1he3z0MYYuUYSp2+I9T8OePNG1fw//Y/isR5R
QnmSDKSAdPoani/4Vl4emW+g8m4nQ7owGaY59geBXkRgR277OMep4piB9oZslWO3jtXE8npqcnTq
SipatJ2R1xzGVlzRTa6s77wT4p0u18e6tqt9ILa3ulfYZB0JYEDj2rlfF97Dqfi3Ub20cPDM+UYD
GRgDNY0q8Ao=
9z0pd7bVzyQO9d8MJCFf26bvy8vyMZ4mU6fJbrc7n4QLIvjpuqr9jk3ADt8tO+Il5daX8Sjqlr9+
18p1b1wOn9K1PhGNLt5r3UJ9RWO+CGMwOwUCM85yevSuQ8aat/bfie+urZy1s7BEYDhgABn864Uu
fNHJLSMLP5s6nJwwcbvVs9En8W+CfG+nRDXU+yTR44kyCD32uO1S23inwN4I0yYaGVnmfKlYiztI
e2WPavHo4mSAFgMhigUjv71ctbMSiCEsMSksAMdRRLKKavGM5KD+ynoQsxl/KnLuX08T64/jFfEY
TNyr52AfLs/ufTFdr4g8X+GfEJt4dV013KOBIQ2HjBGSVI6jnpXB3nmW5hdZASYwQV68cciqNzL5
tzvZgWYfe6V1TwVGpyaW5draWOWGOqx5ktb731OhNrZ6b4gurB0VrSdD5Lv12kZU59azX1SSO7ke
H92fLMLD+8vQ59ayXlKujMx3D36Y6U2SRpHkd2JZjncB3rqUO5zNX1RY5eHY7lghIGT90UJK/kGH
dmNjuIHY4pE27gTzkdKgXKDAxhsgc+9G5C1uOQLwrDPytwfSkRgjr8x4wKXG1UYg9cfhQY9swHbI
+b0ovoUEgRpyv3QG5xS7WBOMde5qOVvmZDyxfP5VPubJwyjnoTSQndJFadC9wSB0Yhj+PWl4ViCA
drZ5rqW0K2MrHzZhkngEf4VCfDloWP7649fvL/hXY6Em2Xe5koxXaFQMxOVb0PpVO8x9pYqCpbB2
+ldMNBthEo864yvQ7hn+VEnh+1kbc0s+49TuH+FT9XkmKLtocy7O0YjIGFbK5HWrFwsMr+ZECE2g
7fQ9xXQf8I/a7UHmTED1K/4UDQbYR7RLNx3yv+FJ0J9BOTOa8sSSOOwHBz0z0pjRqqkK
eQwzmupi0C1STiSY5XByR/hTJPD1od372cZPOGH+FJUJ3tcSk72OfKmMb85U45/CmgggEHkg9RXR
jQLVoQo=
ZZyAwP3h/hTo9AtfMD+ZPnGPvD/Cl9Xmt2I5yKNzIgC4xy3NK6GWRkPAVcg/Tiuji0C1R2Ikn5A4
3D/CnJoVsrPiSbkeo/wpPDzvuS27nLrtW4QAEkDOTSgK
sjnPCg==
M/U10o0C1Gf3k3PuP8KH8P2hjI3zYY8/MP8ACg==
Pq87jvqc2gyQzHAZDg0gXbEC5Jz8orpW0C02qN835j/Clk0G1eSPMk2F6DI/wo9hMLnND5FWIn7v
zYA601FRnLFmOMj24rpG0C1aUkyT9fUf4VEPD1qvCyzgZJ6r/hVLDztuUjBQ7IWZGYegqJsM5J5J
AH0rp/8AhH7Xao8ybj3H+FM/4R20Rgyyz5+q/wCFUqEhoxVuFLyscCTACEHAXHXio5wY41RD2yxr
cTw7aZY+bOc/7S/4U5vD1q24mWfP+8P8KPq8kx2sznVVZNrF1A5Az3xTkVVmZmVHAGcZ4roRoFqq
IokmwM45H+FNHh602v8AvZ/m4PK/4U/q8u40zBkiKW8UpAHm5AKnsODTkAjtH/eYYSAADp61uv4f
tWVQZrjAPA3D/Cmnw7aE5Ms/J5+Yf4UfV5dwRgy3DypkHc/GT71Kl49vFDPbzOJIzknH3WraHh20
HmASTfN7j/Ch/Dlmxb95OAewYY/lR9XkNWRzheSYvK0hJIJJz61XSRmIz2rqf+EaswgAluOn94f4
UL4cs1QjzZ/++l/wo+ryHdI5yYh87Dkhf0oTDJtyce1dGPDdmC2JbgZH94f4U9PDtopOJZ+eeq/4
UfV5Ceisc3CXPljHANKMGdk78kV03/CP2oCYlnGP9oev0pknh20Nxv8ANnBJ5AYf4VH1ebZF7s5y
RwIMOcgOADU23fFgHJxkGt1vDtmybTJNjbjqv+FSx6Daxjask2CPUf4UnhpWFLbQ5UpmSRifXFSr
GZFDZHTmujTw9aYIMk54x94f4U6Pw/aKpAknxn+8P8KTw87aMJSP/9k=
__END_LOGO__
return decode_image_data($logo_base64,'image/jpeg');
}
sub play_jpg{
    my $image_base64 = <<__END_IMG__;
/9j/4AAQSkZJRgABAQEASABIAAD/4QAWRXhpZgAATU0AKgAAAAgAAAAAAAD/2wBDAAUDBAQEAwUE
BAQFBQUGBwwIBwcHBw8LCwkMEQ8SEhEPERETFhwXExQaFRERGCEYGh0dHx8fExciJCIeJBweHx7/
2wBDAQUFBQcGBw4ICA4eFBEUHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4e
Hh4eHh4eHh4eHh7/wAARCAAQABADASIAAhEBAxEB/8QAFgABAQEAAAAAAAAAAAAAAAAABAYH/8QA
IRAAAQQCAQUBAAAAAAAAAAAAAQIDBBEABTEGEhMWIVH/xAAVAQEBAAAAAAAAAAAAAAAAAAAFBv/E
ACIRAAEBBgcAAAAAAAAAAAAAABEAAQMEFEHwBRUyM1Nxwf/aAAwDAQACEQMRAD8AtJbDaNnJaU46
pAIIpZ+Xd42Jr4LhBS+/f55T8zPvZthGm7MyoMqQ+Xe1hCWiAUi+TXGBib7qRUwPraeQSqglLRpI
vjJiDZiuaPTsGvTNNhOREjIu+UU9sr//2Q==
__END_IMG__
return decode_image_data($image_base64,'image/jpeg');
}
sub pause_jpg{
    my $image_base64 = <<__END_IMG__;
/9j/4AAQSkZJRgABAQEASABIAAD/4QAWRXhpZgAATU0AKgAAAAgAAAAAAAD/2wBDAAUDBAQEAwUE
BAQFBQUGBwwIBwcHBw8LCwkMEQ8SEhEPERETFhwXExQaFRERGCEYGh0dHx8fExciJCIeJBweHx7/
2wBDAQUFBQcGBw4ICA4eFBEUHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4e
Hh4eHh4eHh4eHh7/wAARCAAQABADASIAAhEBAxEB/8QAFgABAQEAAAAAAAAAAAAAAAAAAwEG/8QA
IxAAAQQBAwQDAAAAAAAAAAAABAECAwUGAAcREiExQRMi0f/EABUBAQEAAAAAAAAAAAAAAAAAAAMG
/8QAHhEAAgEDBQAAAAAAAAAAAAAAERIBACGBBBMVUbH/2gAMAwEAAhEDEQA/AAzexsQt4aWkGsJm
AFsc6WJF8r9vfn0mpg1hYWG7F/SmHkPBDYnwx9XHT3b71jMxIyQjdAS0QMp6CK5sciRLw1OXfuix
AjJRM/s7VQy41K4R0iwrw7umryJ0PH3Vtieiz+jIornNf//Z
__END_IMG__
return decode_image_data($image_base64,'image/jpeg');
}
sub delete_jpg{
    my $image_base64 = <<__END_IMG__;
/9j/4AAQSkZJRgABAQEASABIAAD/4QAWRXhpZgAATU0AKgAAAAgAAAAAAAD/2wBDAAUDBAQEAwUE
BAQFBQUGBwwIBwcHBw8LCwkMEQ8SEhEPERETFhwXExQaFRERGCEYGh0dHx8fExciJCIeJBweHx7/
2wBDAQUFBQcGBw4ICA4eFBEUHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4e
Hh4eHh4eHh4eHh7/wAARCAAQABADASIAAhEBAxEB/8QAFwAAAwEAAAAAAAAAAAAAAAAAAgMFBv/E
ACMQAAEDAwQCAwAAAAAAAAAAAAECAwQABQYREjFhEyEiUaH/xAAVAQEBAAAAAAAAAAAAAAAAAAAF
Bv/EACIRAAAFAQkAAAAAAAAAAAAAAAAREhQVYQEkMUFCUZGhsf/aAAwDAQACEQMRAD8Ap5xfVY9k
TLT8KQba6TvkJcJ+XQ6/aPDbqrIL1J8EV9FqbG1p9ThClKB+qw2bS8mu9xehvsvmGh1RQEoPs6nm
k4dLyizOmM23JEcrB08Z0556o28uM0HTbwWlkND6XKaljwvoh//Z
__END_IMG__
return decode_image_data($image_base64,'image/jpeg');
}
sub reset_jpg{
    my $image_base64 = <<__END_IMG__;
/9j/4AAQSkZJRgABAQEASABIAAD/4QAWRXhpZgAATU0AKgAAAAgAAAAAAAD/2wBDAAUDBAQEAwUE
BAQFBQUGBwwIBwcHBw8LCwkMEQ8SEhEPERETFhwXExQaFRERGCEYGh0dHx8fExciJCIeJBweHx7/
2wBDAQUFBQcGBw4ICA4eFBEUHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4e
Hh4eHh4eHh4eHh7/wAARCAAQABADASIAAhEBAxEB/8QAFgABAQEAAAAAAAAAAAAAAAAAAQYH/8QA
JhAAAQQBAwIHAQAAAAAAAAAAAgEDBAURAAYhMUETFBVRcZHR8P/EABUBAQEAAAAAAAAAAAAAAAAA
AAQG/8QAIBEAAQIFBQAAAAAAAAAAAAAAEQASAQIFMYEDE0FDUf/aAAwDAQACEQMRAD8A1Jurp4rP
qVkUpxp2T4QADhYTnkix2Tn60O1lJOSVIrCktpFcQHBV1VEkXoYqq9PzURU7zIWZ1DuKPYtR/NE7
FmRmFNW1yvBDjKp8e+i33iMarGn201YyleeE5M2RHUFVE6CI4Rcf3fUFGSpRqbnaj3gde2b+FuSl
mRnFslf/2Q==
__END_IMG__
return decode_image_data($image_base64,'image/jpeg');
}
1;
__DATA__
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta content="text/html; charset=ISO-8859-1" http-equiv="content-type">
<title>Farmerjoe - The Blender Render Farmer</title>
<style type="text/css">
body {
    margin: 0;
    font-family: verdana,sans-serif;
    font-size: .8em;
}
a{
    text-decoration: none;
    color: #660000;
}
img{
    border: 0;
}
.header {
	border: 1px solid #000000;
	font-weight: bold;
}
.slaves {
    background: #BFB1A9;
}
.jobs{
    background: #BF8A69;
    }
.tasks{
    background: #7f6759;
}

.delete{
    color: #ff0000;
}

.pending, .reset{
    color: #0000ff;
}

.rendering, .active, .busy{
    color: #ffcc00;
}

.completed, .idle{
    color: #00ff00;
}

.error{
    color: #ffcccc;
}
/* Progress Bar */
#mContainer {
	position:relative;
	width:350px;
	height:20px;
	padding:0px;
	border:1px solid #330000;
}

#gradient {
	position:absolute;
	top:0px;
	left:0px;
	width:350px;
	height:20px;
    background-color: #73BF60;
	background-repeat:no-repeat;
}

#mask {
    display: block;
	position:absolute;
	font-size:1px;
	width:350px;
	height:20px;
	background-color:#FFFFFF;
	left:0px;
	top:0px;
}

#progressIndicator {
	position:absolute;
    padding: 2px 0 0 3px;
	top:0px;
	left:0px;
	width:350px;
	height:20px;
	color:#eeeeee;
}
</style>
             
        
<script language="javascript" type="text/javascript">
var timeOut;
var selectList = { 0:"0",5:"1",10:"2", 30:"3", 60:"4", 120:"5", 300:"6"};
function getexpirydate( nodays){
    var UTCstring;
    Today = new Date();
    nomilli=Date.parse(Today);
    Today.setTime(nomilli+nodays*24*60*60*1000);
    UTCstring = Today.toUTCString();
    return UTCstring;
}

function setcookie(name,value,duration){
    cookiestring=name+"="+escape(value)+";EXPIRES="+getexpirydate(duration);
    document.cookie=cookiestring;
}

function getcookie(cookiename) {
    var cookiestring=""+document.cookie;
    var index1=cookiestring.indexOf(cookiename);
    if (index1==-1 || cookiename=="") return ""; 
    var index2=cookiestring.indexOf(';',index1);
    if (index2==-1) index2=cookiestring.length; 
    return unescape(cookiestring.substring(index1+cookiename.length+1,index2));
}
function warn(msg) {
  setTimeout('"' + msg, 0);
}
function askfirst(url,msg) {
    if(confirm(msg)){
        location.href = url;
    }
}

function fnSetTimeout( obj )
{
    if (obj.value == 0){
        window.clearTimeout(timeOut);
    }else{
        timeOut = setInterval("reload()", obj.value * 1000);
    }
    setcookie('timeOut',obj.value,1)
}
function reload()
{
    window.location.reload();
}
function init()
{
    cookie_timeout = getcookie('timeOut');
    if (cookie_timeout > 0)
    {
        timeOut = setInterval("reload()", cookie_timeout * 1000);
        timeout_menu = document.getElementById('timeoutmenu');
        timeout_menu.selectedIndex = selectList[cookie_timeout];
    }
}
</script>

</head>
<body onLoad="init()">
<table width="100%" style="height: 100%" border="0" cellpadding="0" cellspacing="0">
  <tr bgcolor="#E8E8E8">
    <td height="85" style="text-align: left; padding: 10px 0 0 30px;"><a href="http://blender.formworks.co.nz"><img alt="Farmerjoe" style="border: none;" src="/logo.jpg"></a>
    </td><td>
    Refresh  
    <select id="timeoutmenu" name="Refresh" size="1" onChange="fnSetTimeout(this);">
                 <option value="0"  >never</option>
                 <option value="5"  >every 5 secs</option>
                 <option value="10" >every 10 secs</option>
                 <option value="30" >every 30 secs</option>
                 <option value="60" >every minute</option>
                 <option value="120">every 2 mins</option>
                 <option value="300">every 5 mins</option>
    </select>
    <br/>
    <a href="/">RELOAD NOW</a>
</td>
  </tr>
  <tr> 
    <td height="2" bgcolor="#999999" colspan="2"> </td>
  </tr>
  <tr><td align="center" valign="top" colspan="2">[% message %]
  </td>
  </tr>
  <tr><td align="center" valign="top" colspan="2">
  
<form enctype="application/x-www-form-urlencoded" method="get" name="form1" action="/">

<table width="95%" border="0" cellpadding="0" cellspacing="0">
<tr>
    <td>
        <strong>Slaves</strong>
        [% slaves %]
    </td>
</tr>
<tr >
    <td>&nbsp;
    </td>
</tr>
<tr >
    <td>
        <strong>Jobs</strong>
        [% jobs %]
    </td>
</tr>
<tr >
    <td>&nbsp;
    </td>
</tr>
<tr >
    <td>
        <strong>Tasks</strong>
        [% tasks %]
    </td>
</tr>
</table>

</form>

</td></tr>
</table>

</body>
</html>
