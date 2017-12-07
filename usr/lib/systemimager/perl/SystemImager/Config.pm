#
# "SystemImager"
#
#  Copyright (C) 2002 Bald Guy Software 
#                     Brian E. Finley <brian.finley@baldguysoftware.com>
#
#    $Id: Config.pm 1806 2002-09-12 04:26:46Z brianfinley $
#

package SystemImager::Config;

use strict;
use AppConfig;


my $config = AppConfig->new(
    'default_image_dir'         => { ARGCOUNT => 1 },
    'autoinstall_script_dir'    => { ARGCOUNT => 1 },
    'autoinstall_boot_dir'      => { ARGCOUNT => 1 },
    'custom_boot_dir'           => { ARGCOUNT => 1 },
    'rsyncd_conf'               => { ARGCOUNT => 1 },
    'rsync_stub_dir'            => { ARGCOUNT => 1 },
    'tftp_dir'                  => { ARGCOUNT => 1 },
    'net_boot_default'          => { ARGCOUNT => 1 },
);

$config->file('/etc/systemimager/systemimager.conf');

$::main::config = $config;

