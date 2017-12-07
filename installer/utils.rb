#!/usr/bin/env ruby

module Utils
=begin
  utils.rb - Ruby/GTK Dreamlinux mkdistro utilities routines.

  Copyright (c) 2007 Nelson Gomes da Silveira (nelsongs) <ngsilveira@gmail.com>
  This program is licenced under the lgpl licence.

  $Id: utils.rb, v 1.0 2007/01/06 22:30 nelsongs Exp $
  Last update: 2007/04/26, 23:00
  Changes:
  2007/02/18, 19:05 => added method kmod_loaded?
  2007/03/13, 09:15 => added list_extendedpart
  2007/04/09, 19:15 => added verify mounted
  2007/04/21, 13:50 => added list_ntfs_partitions
  2007/04/26, 23:00 => several modifications to partitons grab info routines
  2007/05/29, 09:00 => several new routines, like graphic card detection, etc.
=end

def get_kernel_version
	%x{uname -r}
end

def cloop_exists?
	kernel_version = get_kernel_version.chomp
	File.exists?("/lib/modules/#{kernel_version}/extra/cloop.ko")
end

def cloop_dev?
	File.exists?("/dev/cloop") and File.blockdev?("/dev/cloop")
end

def cloop_utils_exists?
	File.exists?("/usr/bin/create_compressed_fs")
end

def squashfs_exists?
	File.exists?("/lib/modules/#{kernel_version.chomp}/kernel/fs/squashfs/squashfs.ko")
end

def squashfs_tools_exists?
	File.exists?("/usr/sbin/mksquashfs")
end

def kmod_loaded?(kmod)
	%x{lsmod | grep kmod}
end

def mkisofs_exists?
	File.exists?("/usr/bin/mkisofs")
end

def list_disks
	return `fdisk -l | grep Disk | awk '{print $2}' | sed 's/://'`.chomp.split
end

# list all found partitions, doesn't matter the type
def list_partitions #by nelsongs
	return `fdisk -l | grep /dev | grep -v Disk | awk '{print $1}'`.chomp.split
end

# same as above, bur adding size and type
def list_partitions_with_size_and_type # by nelsongs. => list: partition size type
	return `fdisk -l | grep /dev | grep -v Disk | awk '{if ($2=="*") print $1":"$5":"$6;else print $1":"$4":"$5}' | sed s/+//g`.split
end

# List only Linux partitions (type 83)
def list_nix_partitions # nelsongs
	return `fdisk -l | grep /dev | grep -v Disk | awk '{if ($2=="*" && $6=="83") print $1;else {if ($5=="83") print $1}}'`.chomp.split
end

# list only Linux partitions (type 83)
def list_nix_partitions_with_size # nelsongs 
	return `fdisk -l | grep /dev | grep -v Disk | awk '{if ($2=="*" && $6=="83") print $1":"$5;else {if ($5=="83") print $1":"$4}}' | sed s/+//g`.chomp.split
end

def list_nix_partitions_with_type
	`fdisk -l | grep /dev | grep -v Disk | awk '{if ($2=="*" && ($6=="83" || $6=="82")) print $1":"$6;else {if ($5=="83" || $5=="82") print $1":"$5}}' | sed s/+//g`.split
end

# List only Linux partitions, including swap partitions
def list_nix_partitions_with_size_and_type # nelsongs
	`fdisk -l | grep /dev | grep -v Disk | awk '{if ($2=="*" && ($6=="83" || $6=="82")) print $1":"$5":"$6;else {if ($5=="83" || $5=="82") print $1":"$4":"$5}}' | sed s/+//g`.split
end

# list only the size of nix partitions
def list_size_nix_partitions # nelsongs
	return `fdisk -l | grep /dev | grep -v Disk | awk '{if ($2=="*" && $6=="83") print $5;else {if ($5=="83") print $4}}' | sed s/+//g`.chomp.split
end

# List swap partitions
def list_swap_partitions # nelsongs
	return `fdisk -l | grep /dev | grep -v Disk | awk '{if ($2=="*" && $6=="82") print $1;else {if ($5=="82") print $1}}'`.chomp.split
end

# List swap partitions with type and size
def list_swap_partitions_with_type_and_size # nelsongs
	return `fdisk -l | grep /dev | grep -v Disk | awk '{if ($2=="*" && $6=="82") print $1":"$5":"$6;else {if ($5=="82") print $1":"$4":"$5}}' | sed s/+//g`.chomp.split
end

# List swap partitions with size
def list_swap_partitions_with_size # nelsongs
	return `fdisk -l | grep /dev | grep -v Disk | awk '{if ($2=="*" && $6=="82") print $1":"$5;else {if ($5=="82") print $1":"$4}}' | sed s/+//g`.chomp.split
end

# List only the size os the swap partitions
def list_size_swap_partitions # nelsongs
	return `fdisk -l | grep /dev | grep -v Disk | awk '{if ($2=="*" && $6=="82") print $5;else {if ($5=="82") print $4}}' | sed s/+//g`.chomp
end

def list_extended_partition # nelsongs
	return `fdisk -l | grep /dev | grep -v Disk | awk '{if ($5=="5" || $5=="f") print $1":"$4":"$5}' | head -1 | sed s/+//g`.chomp.split
end

def list_ntfs_partitions # nelsongs
	return `fdisk -l | grep /dev | grep -v Disk | awk '{if (($2=="*" && $6=="7") || $5=="7") print $1}' `.chomp.split
end

def list_vfat_partitions # nelsongs
	return `fdisk -l | grep /dev | grep -v Disk | awk '{if (($2=="*" && $6=="b") || ($2=="*" && $6=="c") || ($2=="*" && $6=="e")) print $1;else {if ($5=="b" || $5=="c" || $5=="e") print $1}}'`.chomp.split
end

def list_special_partitions
	`fdisk -l | grep /dev | grep -v Disk | awk '{if ($2=="*" && ($6=="de" || $6=="db")) print $1":"$5":"$6;else {if ($5=="de" || $5=="db") print $1":"$4":"$5}}' | sed s/+//g`.chomp.split 
end

def get_partitions
	return `echo $(ls /dev/[sh]d[a-z]?*)`.chomp.split
end

def get_filesystem(partition) # nelsongs
	return `/sbin/fdisk -l |grep "#{partition}" | grep -v Disk | awk '{if ($2 == "*") print $6; else print $5}'`.chomp
end

# returns the filetype. e.g: reiserFS, ext3, etc...
def get_filetype(partition) # by nelsongs
	return `file -s "#{partition}" | awk '{print $2}'`.chomp
end

def get_cdroms
	return `head -3 /proc/sys/dev/cdrom/info | tail -1 | cut -f 3-`.chomp
end

# returns 0 if true, 1 if false.
def verify_mounted(partition)
	return `grep partition /proc/mounts | wc -l`.chomp
end

def get_graphic_card_model
	`hwinfo --framebuffer | grep Model: | awk -F":" '{print $2}'`.chomp
end

def get_graphic_card_vendor
	`hwinfo --framebuffer | grep Vendor: | awk -F":" '{print $2}'`.chomp
end

def get_graphic_card_device
	`hwinfo --framebuffer | grep Device: | awk -F":" '{print $2}'`.chomp
end

def get_graphic_card_subvendor
	`hwinfo --framebuffer | grep SubVendor: | awk -F":" '{print $2}'`.chomp
end

def get_graphic_card_revision
	`hwinfo --framebuffer | grep Revision: | awk -F":" '{print $2}'`.chomp
end

def get_graphic_card_modes
	`hwinfo --framebuffer | grep -v Model | grep Mode | awk '{print $3";"$5";"$2";"$4}' | sed 's/,//'`.chomp.split
end

def get_monitor_max_resolution
	 `xdpyinfo | grep dimensions | head -1 | awk '{print $2}'`.chomp
#	`hwinfo --monitor | grep "Max. Resolution" | awk 'print{$3}'`.chomp # Alternative, but longer
end

def get_maxhres
	`hwinfo --monitor | grep Horizontal | awk '{print $2}'`.chomp
end

def get_maxvres
	`hwinfo --monitor | grep Vertical | awk '{print $2}'`.chomp
end

def get_gfx_memorysize
	`hwinfo --framebuffer | grep "Memory Size:" | awk '{print $3}'`.chomp.to_i
end

def get_res_number(hres, vres, maxcolors)
	`hwinfo --framebuffer | grep -v Model | grep Mode | grep "#{hres}x#{vres}" | grep "#{maxcolors}" | awk '{print $2}'`.chomp
end

def get_monitor_max_colors
	numcolors = `xdpyinfo | grep "maximum request size:" | awk '{print $4}'`.chomp.to_i
	if numcolors >= 16777212 
		return 24
	elsif numcolors == 65536
		return  16
	elsif numcolors == 32768
		return 15
	elsif numcolors == 256
		return 8
	end
end

# by nelsongs. Module mod_type is used to identify the image type, whether cloop or squashfs
# Use: mod_type file, where file comprises the image (complete path) to be verified.
# Example: 
# file = /usr/local/bin/linux.mod
# if mod_type(file) == "squashfs" ....bla bla bla

def mod_type file
	compression = %x{dd if="#{file}" bs=4 count=1} 
	if  compression == "#!/b" 
		return "cloop"
	elsif compression == "hsqs"
		return "squashfs"
	else
		return "none"
	end
end

def run(command, input='')
		IO.popen(command, 'r+') do |io|
		io.puts input
		io.close_write
		return io.read
	end
end


end #module