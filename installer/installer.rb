#!/usr/bin/env ruby
#
# dli.rb - Dreamlinux Installer
# This app help installing Deamlinux on your hard disk
# Copyright (c) 2007 Nelson Gomes da Silveira (nelsongs) <ngsilveira@gmail.com>
# This program is licenced under the LGPL licence.
# 
# :title:dli.rb
# :version: 2.0.1 
# :date: 2007/07/22 12:30
# :last update: 2007/11/30, 14:20 (Beta 10)

$KCODE = "u" # UTF-8
require "jcode"
require "gtk2" 
require "fileutils" 
require "yaml"
require "support"
include Support

COL_DEV = 0
COL_SIZE = 1
COL_TYPE = 2

P_COMBO_TEXT_COLUMN = 3
P_COMBO_MODEL = 4
P_COMBO_HAS_ENTRY = 5
P_COMBO_EDITABLE = 6
P_COMBO_TEXT = 7

T_COMBO_TEXT_COLUMN = 8
T_COMBO_MODEL = 9
T_COMBO_HAS_ENTRY = 10
T_COMBO_EDITABLE = 11
T_COMBO_TEXT = 12

COL_FORMAT = 13

class Global
# partition = partition to install in
	def Global.partition=(partition)
		@@partition = partition
	end
	def Global.partition
		@@partition
	end
# partition type
	def Global.partitiontype=(partitiontype)
		@@partitiontype = partitiontype
	end
	def Global.partitiontype
		@@partitiontype
	end
# partition size # added on 11/07/2007, 12:00
	def Global.partitionsize=(partitionsize)
		@@partitionsize = partitionsize
	end
	def Global.partitionsize
		@@partitionsize
	end
# partitions = array of partitions
	def Global.partitions=(partitions)
		@@partitions = partitions
	end
	def Global.partitions
		@@partitions
	end
#swap = swap partition	
	def Global.swap=(swap)
		@@swap = swap
	end
	def Global.swap
		@@swap
	end
	def Global.chosenpart=(partitions)
		@@chosenpart = partitions
	end
	def Global.chosenpart
		@@chosenpart
	end
# parts2install
	def Global.part2inst=(partitions)
		@@part2inst = partitions
	end
	def Global.part2inst
		@@part2inst
	end
# rootpart
	def Global.rootpart=(partition)
		@@rootpart = partition
	end
	def Global.rootpart
		@@rootpart
	end
# source
	def Global.source=(src)
		@@source = src
	end
	def Global.source
		@@source
	end
# target
	def Global.target=(mountpoint)
		@@target = mountpoint
	end
	def Global.target
		@@target
	end
# outofroot
	def Global.outofroot=(partitions)
		@@outofroot = partitions
	end
	def Global.outofroot
		@@outofroot
	end	
#ptomnt = mounting point of the partition	
	def Global.mntpt=(mntpt)
		@@mntpt = mntpt
	end
	def Global.mntpt
		@@mntpt
	end
#fspartition = fs to format partition with	
	def Global.fspartition=(fs)
		@@fspartition = fs
	end
	def Global.fspartition
		@@fspartition
	end
#format = format partition?	
	def Global.format=(format)
		@@format = format
	end
	def Global.format
		@@format
	end
# user = user
	def Global.user=(value)
		@@user = value
	end
	def Global.user
		@@user
	end
# userpass = user password
	def Global.userpass=(value)
		@@userpass = value
	end
	def Global.userpass
		@@userpass
	end
# rootpass = root password
	def Global.rootpass=(value)
		@@rootpass = value
	end
	def Global.rootpass
		@@rootpass
	end
# ruserpass = repeated user password
	def Global.ruserpass=(value)
		@@ruserpass = value
	end
	def Global.ruserpass
		@@ruserpass
	end
# rrootpass = repeated root password
	def Global.rrootpass=(value)
		@@rrootpass = value
	end
	def Global.rrootpass
		@@rrootpass
	end
# boxname = name of the boxr
	def Global.boxname=(value)
		@@boxname = value
	end
	def Global.boxname
		@@boxname
	end
# users = keep record of the assigned users
	def Global.users=(value)
		@@users = value
	end
	def Global.users
		@@users
	end
# Grub install
	def Global.grub=(value)
		@@grub = value
	end
	def Global.grub
		@@grub
	end
	def Global.can_install=(value)
		@@can_install = value
	end
	def Global.can_install
		@@can_install
	end
#Distro Title
	def Global.distro_title=(value)
		@@distro_title = value
	end
	def Global.distro_title
		@@distro_title
	end
private
	@@source = "/LIVE"
	@@partition = "none"
	@@partitiontype = "none"
	@@partitionsize = 0
	@@swap = ""
	@@mntpt = "none"
	@@fspartition = "none"
	@@format = false
	@@partitions = Array.new
	@@chosenpart = Array.new
	@@part2inst = Array.new
	@@rootpart = nil
	@@target = nil
	@@outofroot = Array.new
	@@user = "animux"
	@@userpass = nil
	@@ruserpass = nil
	@@rootpass = nil
	@@rrootpass = nil
	@@boxname = "Animux"
	@@users = Array.new
	@@grub = "mbr"
	@@can_install = false
	@@distro_title = nil
end # class Global

def read_dliconf
	# read dliconfig.yaml
	dliconf = YAML::load(File.open("/usr/local/etc/dli_config.yaml"))
	@leftpanel = dliconf['leftpanel']
	@gparttool = dliconf['gparted']
	@tparttool = dliconf['tparted']
	@framebuffer = dliconf['fbvalue']
end

def about
# Credits to:
# Andre Felipe J. Souja - Arts and testings
# Joao Baptista Esteves - Testings
# Gaspar Domingos de Araujo - Testings
#========================
	if str = Gtk.check_version(2, 6, 0)
		puts "This dialog requires GTK+ 2.6.0 or later"
		puts str
		exit
	end
	image = Gtk::Image.new("./dream-start.png")
	button = StockButton.new("Ok", Gtk::Stock::OK)
	table = Gtk::Table.new(1, 3, true)
	table.attach_defaults(button, 1, 2, 0, 1)
	appname = Gtk::Label.new.set_markup("<b>Anumix Installer</b>")
	appversion = Gtk::Label.new("Release 2.0.0")
	appwebsite = Gtk::Label.new.set_markup("<span foreground=\"blue\">http://www.ngsys.eti.br/dli</span>")
	appproject = Gtk::Label.new("Project website at: ")
	appauthor = Gtk::Label.new("Copyright(c) 2007 Nelson Gomes da Silveira")
	appauthornick = Gtk::Label.new("<nelsongs>")
	appcredits = Gtk::Label.new("Credits to: drjesteves, GDA and andrefelipe")
	dummyrow1 = Gtk::Label.new("")
	dummyrow2 = Gtk::Label.new("")
	dummyrow3 = Gtk::Label.new("")
	aboutwin = BasicWindow.new("Animux Installer")
	aboutwin.set_border_width(10)
	box = Gtk::VBox.new
	aboutwin.add(box)
	box.pack_start(image, false, false)
	box.pack_start(appname, false, false)
	box.pack_start(appversion, false, false)
	box.pack_start(appauthor, false, false)
	box.pack_start(appauthornick, false, false)
	box.pack_start(dummyrow1, false, false)
	box.pack_start(appcredits, false, false)
	box.pack_start(dummyrow2, false, false)
	box.pack_start(appproject, false, false)
	box.pack_start(appwebsite, false, false)
	box.pack_start(dummyrow3, false, false)
	box.pack_start(table, false, false, 10)
	button.signal_connect('clicked') { aboutwin.destroy }
	aboutwin.show_all
end

def good_boxname
	if Global.boxname != nil and Global.boxname != ""
		return true
	else
		title = "Box name needed"
		msg = "You need to name your box. Any name can be of use\nlike box, mwBox, myComputer, Alf, whatever!"
		msgwin(Gdk::Pixbuf.new("./dream-start.png"), title, msg)
		@entry_box.text = ""
		@entry_box.has_focus = true
	end
end

def good_username
	if Global.user != nil and Global.user != ""
		return true
	else
		title = "User name needed"
		msg = "You need to provide at least a user name."
		msgwin(Gdk::Pixbuf.new("./dream-start.png"), title, msg)
		@entry_user.text = ""
		@entry_user.has_focus = true
	end
end

def good_passwd(passwd1, passwd2)
	if (passwd1 == passwd2) 
		return true
	else
		title = "Verify password"
		if passwd1 == Global.userpass
			msg = "User password doesn't match.\nPlease, enter it again."
		else
			msg = "Root password doesn't match.\nPlease, enter it again."
		end
		msgwin(Gdk::Pixbuf.new("./dream-start.png"), title, msg)
		if passwd1 == Global.userpass
			@entry_userpass.text = ""
			@entry_ruserpass.text = ""
			@entry_userpass.has_focus = true
			@model_users.clear
		else
			@entry_rootpass.text = ""
			@entry_rrootpass.text = ""
			@entry_rootpass.has_focus = true
		end
	end
end

def read_partitions
	# read *nix type partitions
	Global.partitions = `fdisk -l | grep /dev | grep -v Disk | awk '{if ($2=="*" && ($6=="83" || $6=="82")) print $1":"$5":"$6;else {if ($5=="83" || $5=="82") print $1":"$4":"$5}}' | sed s/+//g`.split
	check_no_parts if Global.partitions.empty? # verify if there are partitions
	if Global.partitions.size > 0
		Global.partitions.each do |partition|
			device, size, type = partition.strip.split(/\s*:\s*/)
			sizeGB = (size.to_i/1048576).to_s
			typename = "swap" if type == "82"
			typename = `file -s "#{device}" | awk '{print $2}'`.chomp if (type == "83" || type == "7")
			case typename 
			when "ReiserFS"
				typename = "reiserfs"
			when "Reiser4"
				typename = "reiser4"
			when "SGI"
				typename = "xfs"
			when "data"
				typename = "jfs"
			when "Macintosh"
				typename = "hfsplus"
			when "x86"
				typename = "ntfs" if system("fdisk -l | grep #{partition} | grep 7")
			end
			iter = @store.append
			iter[COL_DEV] = "#{device}"
			iter[COL_SIZE] = "#{sizeGB} GB"
			iter[COL_TYPE] = "#{typename}"
			iter[P_COMBO_MODEL] = @partition_model
			iter[P_COMBO_HAS_ENTRY] = false
			iter[P_COMBO_EDITABLE] = true
			iter[P_COMBO_TEXT] = @partition_model.get_iter("0")[0]
			iter[T_COMBO_MODEL] = @fs_model
			iter[T_COMBO_HAS_ENTRY] = false
			iter[T_COMBO_EDITABLE] = true
			iter[T_COMBO_TEXT] = @fs_model.get_iter("0")[0]
			iter[COL_FORMAT] = Global.format
		end
	end
end

def create_models
	# The Filesystems Model
	@fs_model = Gtk::ListStore.new(String)
	fstype = ["none", "swap", "ext2", "ext3", "reiserfs", "reiser4", "xfs", "jfs", "ntfs", "vfat" ]
	fstype.each do |v|
		iter = @fs_model.append
		iter[0] =  v
	end
	# The partitions Model
	@partition_model = Gtk::ListStore.new(String)
	partitions = ["none", "swap", "/", "/boot", "/home", "/opt", "/srv", "/tmp", "/usr", "/var", "/usr/local" ]
	partitions.each do |v|
		iter = @partition_model.append
		iter[0] =  v
	end
	# The Main Model
	@store = Gtk::ListStore.new(String, #COL_DEV
				String, #COL_SIZE
				String, #COL_TYPE
				Integer, #P_COMBO_TEXT_COLUMN
				Gtk::ListStore, # P_COMBO_MODEL
				TrueClass, # P_COMBO_HAS_ENTRY
				TrueClass, # P_COMBO_EDITABLE
				String, # P_COMBO_TEXT
				Integer, #T_COMBO_TEXT_COLUMN
				Gtk::ListStore, # T_COMBO_MODEL
				TrueClass, # T_COMBO_HAS_ENTRY
				TrueClass, # T_COMBO_EDITABLE
				String, # T_COMBO_TEXT
				TrueClass) #COL_FORMAT
	read_partitions
	return @store
end

def changed
	iter = @treeview.selection.selected
	if iter
		Global.partition = iter[COL_DEV]
		Global.partitionsize = iter[COL_SIZE] #added on 11/07/2007, 12:00
		Global.partitiontype = iter[COL_TYPE]
		Global.mntpt = iter[P_COMBO_TEXT]
		Global.fspartition = iter[T_COMBO_TEXT]
		Global.format = iter[COL_FORMAT]
	end
end

def fixed_toggled(model, path_str)
	path = Gtk::TreePath.new(path_str)
	iter = model.get_iter(path)# get toggled iter
	fixed = iter[COL_FORMAT]
	fixed = ! fixed# do something with the value
	iter[COL_FORMAT] = fixed# set new value
end
	
def check_no_parts
	dialog = Gtk::MessageDialog.new(@win, 
                      Gtk::Dialog::DESTROY_WITH_PARENT,
                      Gtk::MessageDialog::ERROR,
                      Gtk::MessageDialog::BUTTONS_CLOSE, "ERROR: No availaible partitions found.\n
If you want to install Animux in your computer\nfirst you have to create a partition.\n
Click either Graphical Partition Tool or \nText Partition Tool menu item and try again.\n")
	dialog.run
	dialog.destroy
end

def reread_partitions
	@store.clear
	@model_partitions.clear
	Global.partitions = []
	Global.chosenpart = []
	Global.part2inst = []
	Global.partitionsize = 0
	Global.format = true
	read_partitions
end

def can_install
	if ((Global.boxname != "") and (Global.rootpass != nil) and (Global.user != "") and (Global.userpass != nil) and (not Global.chosenpart.empty?) ) 
		Global.can_install = true
	end
	Global.can_install ? @execbutton.sensitive = true : @execbutton.sensitive = false
end

def grubmenu_create(device, framebuffer, distroname, devmap)
	oses = `os-prober` # Detects other OS'es 
	osesbyline = [] #Break string by lines. Each line will reference an OS.
	oses.each do |line| #Populate osesbyline
		osesbyline.push(line.chomp)
	end
	#Tokenize string into arrays. Each array will contain an OS, with its parts separated.
	osessplit = []
	osesbyline.each do |line|
		osessplit.push(line.split(":"))
	end
	#now disks correctly mapped according to Grub conventions, nelsongs 2007/08/24, 13:55 h
	diskletters = Array.new
	devmap.each do |dev|
		diskletters << dev.slice(7..7)
	end
	#process
	target = "#{device}".sub(/dev/, "mnt")  #e.g.: /mnt/hda7
	system("mount #{device} #{target} 2>/dev/null") # mount target, doesn't hurt if its already mounted
	targetdiskletter = target.slice(7..7) # eg, a, b, c, ...
	targetdisknum = diskletters.index(targetdiskletter) # 0 for a; 1 for b, etc....
	targetpartnum = target.slice(8..9).to_i - 1
	targetosroot = target.slice(6..6) #ex: d
	targetkernel = `ls "#{target}"/boot | grep vmlinuz-2.6.24`.chomp.split[0]
	targetinitrd = `ls "#{target}"/boot | grep initrd.img-2.6.24`.chomp.split[0]
	#generates a basic menu.lst
	system("mv #{target}/boot/grub/menu.lst #{target}/boot/grub/menu.lst.bak") if File.exists?("#{target}/boot/grub/menu.lst")
	grubmenu = File.new("#{target}/boot/grub/menu.lst", "w")
	grubmenu.puts "# See www.gnu.org/software/grub for details"
	grubmenu.puts "# By default, boot the first entry"
	grubmenu.puts "#This menu automatically generated by dli.rb"
	grubmenu.puts "default 0"
	grubmenu.puts "# Boot automatically after 5 seconds"
	grubmenu.puts "timeout 5"
	#loads gfxmenu
	grubmenu.puts "gfxmenu (h#{targetosroot}#{targetdisknum},#{targetpartnum})/boot/grub/message"
	grubmenu.puts
	grubmenu.puts "title\t#{distroname}"
	grubmenu.puts "root\t(h#{targetosroot}#{targetdisknum},#{targetpartnum})"
	grubmenu.puts "kernel\t/boot/#{targetkernel} root=#{device} ro quiet vga=#{framebuffer} splash resume=#{Global.swap}"
	grubmenu.puts "initrd\t/boot/#{targetinitrd}" if "#{targetinitrd}" != ""
	grubmenu.puts
        grubmenu.puts "title\t#{distroname} Xen"
        grubmenu.puts "kernel\t/boot/xen-3.2-1-amd64.gz"
        grubmenu.puts "module\t/boot/vmlinuz-2.6.18-6-xen-amd64 root=#{device} ro console=tty0"
        grubmenu.puts "module\t/boot/initrd.img-2.6.18-6-xen-amd64"
        grubmenu.puts
	grubmenu.puts "title\t#{distroname} (recovery mode)"
	grubmenu.puts "root\t(h#{targetosroot}#{targetdisknum},#{targetpartnum})"
	grubmenu.puts "kernel\t/boot/#{targetkernel} root=#{device} ro quiet vga=#{@framebuffer} single"
	grubmenu.puts "initrd\t/boot/#{targetinitrd}" if "#{targetinitrd}" != ""
	grubmenu.puts
	if File.exists?("#{target}/boot/memtest86+.bin")
		grubmenu.puts "title\t#{distroname} memtest86+"
		grubmenu.puts "root\t(h#{targetosroot}#{targetdisknum},#{targetpartnum})"
		grubmenu.puts "kernel\t/boot/memtest86+.bin"
		grubmenu.puts "quiet"
		grubmenu.puts
	end
	grubmenu.puts "# This is a divider, added to separate the menu items below from the Animux ones"
	grubmenu.puts "title\t	Other operating systems:"
	grubmenu.puts "root"
	grubmenu.puts
	osessplit.each do |os|
		if "#{os[0]}" != "#{device}" #not to include again the target device
			diskletter = os[0].slice(7..7) # eg, a, b, c, ...
			disknum = diskletters.index(diskletter) # 0 for a; 1 for b, etc....
			partnum = os[0].slice(8..9).to_i - 1
			grubmenu.puts "title\t#{os[1]}"
			osroot = "#{os[0]}".slice(6..6) #ex: d
			grubmenu.puts "root\t(h#{osroot}#{disknum},#{partnum})" # (hd0,1), etc...
			if os[3] == "chain"
				grubmenu.puts "savedefault"
				grubmenu.puts "chainloader\t+1"
				grubmenu.puts
			else
				partition = os[0].sub(/dev/, "mnt")
				Dir.mkdir("#{partition}") if ! File.exists?("#{partition}")
				%x(mount "#{os[0]}" "#{partition}" 2>/dev/null)
				kernel = `ls "#{partition}"/boot | grep vmlinuz-`.chomp.split[0]
				initrd = `ls "#{partition}"/boot | grep initrd`.chomp.split[0]
				%x(umount -l "#{partition}")
				grubmenu.puts "kernel\t/boot/#{kernel} root=#{os[0]} ro quiet vga=#{framebuffer} splash resume=#{Global.swap}"
				grubmenu.puts "initrd\t/boot/#{initrd}" if "#{initrd}" != ""
				grubmenu.puts
			end 
		end 
	end 
	grubmenu.close
end 

def grub_install(disk, partition, mountpt, distrotitle, framebuffer)
	kernelv = `uname -r`
	title = "Animux"
	Dir.mkdir("#{mountpt}/boot/grub") if ! File.exists?("#{mountpt}/boot/grub")
	#verify gfxboot
	if File.exists?("#{mountpt}/bin/mbchk") && File.exists?("#{mountpt}/usr/local/include/message") 
		system("mv -f #{mountpt}/usr/local/include/message #{mountpt}/boot/grub/") 
	end	
	system("mv #{mountpt}/boot/grub/menu.lst #{mountpt}/boot/grub/menu.lst.bak") if File.exists?("#{mountpt}/boot/grub/menu.lst")
	title = "#{distrotitle}" if (("#{distrotitle}" != nil) and ("#{distrotitle}" != ""))
	# verify the disk devices for grub mapping correctness
	devmap = `fdisk -l | grep Disk | grep -v "Disk identifier:" | awk '{print $2}' | sed 's/://'`.chomp.split
	grubmenu_create(partition, framebuffer, title, devmap)
	%x(mount "#{partition}" "#{mountpt}" 2>/dev/null) # grubmenu_create closes all mountpoints
	# backup current mbr on target/boot
	system("dd if=#{disk} of=#{mountpt}/boot/mbr.orig bs=512 count=1") if disk.size == 8 # e.g., /dev/sda
	#zero fill mbr, if grub install on mbr
	system("dd if=/dev/zero of=#{disk} bs=446 count=1") if disk.size == 8 # e.g., /dev/sda. Only zeroes grub/lilo area
	#install grub on mbr or partition
	system("grub-install --recheck --no-floppy --root-directory=#{mountpt} #{disk}")
	insert_on_grub(partition, framebuffer, title, devmap, true) if disk.size >= 9 # if grub installed in a partition, e.g. /dev/sda7 (equals 9)
end

def insert_on_grub(device, framebuffer, distrotitle, devmap, chain = false)
	("#{distrotitle}" != nil || "#{distrotitle}" != "") ? title = "#{distrotitle}" : title = "Animux"
	target = device.sub(/dev/, "mnt")
	#now disks correctly mapped according to Grub conventions, nelsongs 2007/08/24, 13:55 h
	diskletters = Array.new
	devmap.each do |dev|
		diskletters << dev.slice(7..7)
	end
	diskletter ="#{device}".slice(7..7) # eg, a, b, c, ...
	disknum = diskletters.index(diskletter) # for a, 0; for b, 1; etc....
	partnum = "#{device}".slice(8..9).to_i - 1 # takes the partition number and decreases it by 1 to meet grub requirements
	osroot = "#{device}".slice(6..6)#eg.: d
	kernel = `ls "#{target}"/boot | grep vmlinuz-`.chomp.split[0]
	initrd = `ls "#{target}"/boot | grep initrd`.chomp.split[0]
	nix_installed = `os-prober | grep linux | awk -F":" '{print $1}'`.chomp.split
	nix_installed.each do |nix|
		partition = nix.sub(/dev/, "mnt")
		Dir.mkdir("#{partition}") if ! File.exists?("#{partition}")
		%x(mount "#{nix}" "#{partition}")
		if File.exists?("#{partition}/boot/grub/menu.lst")
			# Delete previous menu entries equal to the one being entered. Menu is an array 
			menu = IO.readlines("#{partition}/boot/grub/menu.lst")
			# Create an empty string
			block = ""
			# Create an empty array
			blocks = []
			# Process each line forming blocks and verify for identical entries
			menu.each do |line|
				if "#{line}" != "\n"
					block += line
				else
					block += "\n"
					blocks << block unless block.include?("#{device}")
					block = ""
				end
			end
			# in the case block still holds any content
			if block != ""
				oldblock = "\n"
				oldblock += block
				blocks << block
				block = ""
			end
			# Now, add the new entry to the blocks array
			newblock = ""
			newblock += "# This was added to the current menu by DLI\n"
			newblock += "title\t#{title}\n"
			if chain
				newblock += "root\t(h#{osroot}#{disknum},#{partnum})\n"
				newblock += "chainloader\t+1\n"
			else
				newblock += "kernel\t(h#{osroot}#{disknum},#{partnum})/boot/#{kernel} root=#{device} ro quiet vga=#{framebuffer} splash\n"
				newblock += "initrd\t(h#{osroot}#{disknum},#{partnum})/boot/#{initrd}\n" if "#{initrd}" != ""
				newblock += "\n"
			end
			blocks << newblock
			# Make a backup of the current menu.lst
			system("mv #{partition}/boot/grub/menu.lst #{partition}/boot/grub/menu.lst.previous")
			# Now overwrite menu.lst with blocks contents 
			newmenu = File.open("#{partition}/boot/grub/menu.lst", "w")
			blocks.each do |line|
				newmenu.puts line
			end
			newmenu.close
		end
		%x(umount -l "#{partition}")
	end
end

def create_fstab
	FileUtils.rm_r("#{Global.target}/etc/fstab") if File.exists?("#{Global.target}/etc/fstab")
	fstabfile = File.new("#{Global.target}/etc/fstab", "w")
	fstabfile.puts "#{@rootpartition[1]}\t#{@rootpartition[0]}\t#{@rootpartition[2]}\tdefaults\t0\t1"
	#verify other partitions, except the ones installed, and insert them at the end of fstab
	@other_partitions = @resultingpart - Global.rootpart.split # Extracts, e.g, /dev/sda5 from other_partitions
	if Global.outofroot.size >= 1
		Global.outofroot.each do |part|
			fstabfile.puts "#{part[1]}\t#{part[0]}\t#{part[2]}\tdefaults\t0\t2" 
			@other_partitions = @other_partitions - part[1].split # Extracts, e.g, /dev/sda6 (/home) from other_partitions
		end	
	end
	#setup swap, partition or file
	if Global.swap.size > 0 
		fstabfile.puts "#{Global.swap}\tnone\tswap\tsw\t0\t0" 
	else	
		fstabfile.puts "/.swapfile\tnone\tswap\tsw\t0\t0"
	end
	fstabfile.puts "proc\t/proc\tproc\tdefaults\t0\t0"

	@other_partitions.each do |device| # /dev/sda7
		mntpt = device.sub(/dev/, "mnt") #/mnt/sda7
		Dir.mkdir("#{mntpt}") if ! File.exists?("#{mntpt}") 
		fstype = `file -s "#{device}" | awk '{print $2}'`.chomp
		case fstype 
		when "ReiserFS"
			fstype = "reiserfs"
		when "Reiser4"
			fstype = "reiser4"
		when "SGI"
			fstype = "xfs"
		when "data"
			fstype = "jfs"
		when "Macintosh"
			fstype = "hfsplus"
		when "x86"
			filesystem = `/sbin/fdisk -l |grep "#{device}" | grep -v Disk | awk '{if ($2 == "*") print $6; else print $5}'`.chomp
			filesystem ==  "7" ? fstype = "ntfs" : fstype = "vfat"
		end
		fstabfile.puts "#{device}\t#{mntpt}\t#{fstype}\tnoauto,users,exec,umask=000\t0\t0" if fstype == "vfat"
		# if fs = ntfs, mount it using ntfs-3g for read/write access
		fstabfile.puts "#{device}\t#{mntpt}\tntfs-3g\tsilent,umask=0 0 0\t0\t0" if fstype == "ntfs"
		fstabfile.puts "#{device}\t#{mntpt}\t#{fstype}\tnoauto,users,exec\t0\t0" if ((fstype != "vfat") and (fstype != "ntfs"))
	end
	fstabfile.close
end

def update_network
    system("cp /etc/network/interfaces #{Global.target}/etc/network/interfaces");
end

def setup_directories
	Global.chosenpart.each do |v|
		Global.swap = v[1]  if v[4] == "swap"
	end
	Global.swap = list_swap_partitions if "#{Global.swap}" == "none"
	# Copiar o Global.chosenpart, sem a particao swap. para Global.part2inst
	Global.chosenpart.each do |v|
		Global.part2inst << v  if v[4] != "swap" #initialize Global.part2inst
	end
	if Global.part2inst.size == 1 # so ha a particao /
		@rootpartition = Global.part2inst[0] 
		Global.rootpart = Global.part2inst[0][1] # device partition, eg. /dev/hda6
		Global.target = Global.part2inst[0][1].sub(/dev/, "mnt") # mounting point, e.g: /mnt/hda6
	else # Global.part2inst > 1, i.e., there are more than the / partition, e.g., /home
		@rootpartition = Global.part2inst.detect {|e| e if e.index("/") != nil} #verify which partition holds the / and store the whole info in @rootpartition. Eg: /    /dev/sda5    reiserfs    linux 
		Global.rootpart = @rootpartition[1] # store the root partition in Global.rootpart. Eg: /dev/sda5
		Global.target = @rootpartition[1].sub(/dev/, "mnt") # mounting point, e.g: /mnt/hda6
		temparray = []
		Global.part2inst.each {|m| temparray << m}
		temparray.delete(@rootpartition)
		Global.outofroot = temparray # outofroot contains all other partitions, except / and swap. Ex: /home, /boot, /var
	end
	# verify linux partitions, creating mounting points and mounting them.
	Global.part2inst.each do |part|
		mntpt = part[0]
		@dev = part[1]
		@devmap = part[1].sub(/dev/, "mnt")
		@fstype = part[2]
		format = part[3]
		Dir.mkdir("#{@devmap}") if not File.exists?("#{@devmap}")
		if "#{format}" == "yes"
			case @fstype
			when "reiserfs" 
				%x(umount -l "#{@devmap}" 2>/dev/null)
				system("mkfs.#{@fstype} -f -q -l Animux #{@dev}")
			when "reiser4"
				%x(umount -l "#{@devmap}" 2>/dev/null)
				system("mkfs.#{@fstype} -y -L Animux #{@dev}")
			when "xfs" 
				%x(umount -l "#{@devmap}" 2>/dev/null)
				system("mkfs.#{@fstype} -f -q -L Animux #{@dev}")
			when "jfs"
				system("modprobe jfs") if `lsmod | grep jfs | awk '{print $1}'`.chomp != "jfs"
				%x(umount -l "#{@devmap}" 2>/dev/null)
				system("mkfs.#{@fstype} -q -L Animux #{@dev}")
			else
				%x(umount -l "#{@devmap}" 2>/dev/null)
				system("mkfs.#{@fstype} #{@dev}")
			end
			system("mount #{@dev} #{@devmap}")
		end
	end
	#sets up the distro directories to work on
	rootdirarr = `find  #{Global.source} -mindepth 1 -maxdepth 1 -type d | sed -r 's\/.*\\/\/\\/\/'`.split
	#rootdirarr = %w[/bin /boot /dev /etc /home /initrd /lib /media /mnt /opt /proc /root /sbin /srv /sys /tmp /var /usr]
	emptydirs = %w[/initrd /media /mnt /proc /srv /sys /tmp]
	root = rootdirarr - emptydirs 
	return root
end

def setup_rootlinks
	#sets up the distro directories to work on
	rootlinksarr = `find  #{Global.source} -mindepth 1 -maxdepth 1 -type l | sed -r 's\/.*\\/\/\\/\/'`.split
	return rootlinksarr
end

def fix_groups

	users = `ls "#{Global.target}"/home`.split
	usersnoroot = users - ["root"]
	usersnoroot.each do |user|
	    %x(chroot "#{Global.target}" usermod -a -G adm	"#{user}")
	    %x(chroot "#{Global.target}" usermod -a -G disk	"#{user}")
	    %x(chroot "#{Global.target}" usermod -a -G dialout	"#{user}")
	    %x(chroot "#{Global.target}" usermod -a -G dip	"#{user}")
	    %x(chroot "#{Global.target}" usermod -a -G users	"#{user}")
	    %x(chroot "#{Global.target}" usermod -a -G voice	"#{user}")
	    %x(chroot "#{Global.target}" usermod -a -G fuse	"#{user}")
	    %x(chroot "#{Global.target}" usermod -a -G plugdev	"#{user}")
	    %x(chroot "#{Global.target}" usermod -a -G cdrom	"#{user}")
	    %x(chroot "#{Global.target}" usermod -a -G floppy	"#{user}")
	    %x(chroot "#{Global.target}" usermod -a -G audio	"#{user}")
	    %x(chroot "#{Global.target}" usermod -a -G games	"#{user}")
	    %x(chroot "#{Global.target}" usermod -a -G lp	"#{user}")
	    %x(chroot "#{Global.target}" usermod -a -G video	"#{user}")
	    %x(chroot "#{Global.target}" usermod -a -G powerdev	"#{user}")
	end
	%x(chroot "#{Global.target}" usermod -a -G disk		root)
	%x(chroot "#{Global.target}" usermod -a -G lp		root)
	%x(chroot "#{Global.target}" usermod -a -G dialout	root)
	%x(chroot "#{Global.target}" usermod -a -G voice	root)
	%x(chroot "#{Global.target}" usermod -a -G cdrom	root)
	%x(chroot "#{Global.target}" usermod -a -G floppy	root)
	%x(chroot "#{Global.target}" usermod -a -G audio	root)
	%x(chroot "#{Global.target}" usermod -a -G video	root)
	%x(chroot "#{Global.target}" usermod -a -G plugdev	root)
	%x(chroot "#{Global.target}" usermod -a -G games	root)
	%x(chroot "#{Global.target}" usermod -a -G users	root)
	%x(chroot "#{Global.target}" usermod -a -G fuse		root)
	%x(chroot "#{Global.target}" usermod -a -G powerdev	root)
end

def do_install(distrotitle, root, rootlinks)
	@pb_msglabel.text = @install_msg + "Commencing..."
	# clean up local repo
#	system("apt-get clean 2>/dev/null")
#	system("rm -rf /var/cache/apt/*.bin 2>/dev/null")
	# setup swap, if it exists as a partition, or create it as a file and set it up.
	if Global.swap.size > 0
		system("swapoff -a")
		system ("mkswap #{Global.swap}")  
		system("swapon #{Global.swap}")  
	elsif Global.swap.size == 0
	# creating swap file of 200 MB, if swap partition doesn't exists
		system("dd if=/dev/zero of=#{Global.target}/.swapfile bs=4k count=51200")
		system("mkswap #{Global.target}/.swapfile")
		system("swapon #{Global.target}/.swapfile")
	end
	# Copying directories to HDD
	root.each do |d| 
#		@pb_msglabel.text = @install_msg + @percentcopied_msg
		puts "rsync -aq #{Global.source}/#{d} #{Global.target} 2>/dev/null"
		system("rsync -aq #{Global.source}/#{d} #{Global.target} 2>/dev/null")
	end
	sleep 3 # to give time of the copy routine to really flush its buffers
	rootlinks.each do |l| 
		puts "cp -d #{Global.source}/#{l} #{Global.target} 2>/dev/null"
		system("cp -d #{Global.source}/#{l} #{Global.target} 2>/dev/null")
	end
	#Here we finished copy. Set percentage to 100% and start configuring the system...
	@percentage = 100
	# creating empty dirs
	emptydirs = %w[/initrd /media /mnt /proc /srv /sys /tmp]
	emptydirs.each do |e|
		Dir.mkdir("#{Global.target}/#{e}")
	end
	@pb_msglabel.text = @config_msg + "Setting up files and directories......"
	# create /boot/grub
	Dir.mkdir("#{Global.target}/boot/grub") if ! File.exists?("#{Global.target}/boot/grub")
	# now copying/creating other necessary dirs...
	Dir.mkdir("#{Global.target}/opt") if ! File.exists?("#{Global.target}/opt")
	#take out mkdistro live remaster from menu
	system("rm -f #{Global.target}/usr/share/applications/mkdistroeasy.desktop") if File.exists?("#{Global.target}/usr/share/applications/mkdistroeasy.desktop")
	# rebuild /var/tmp
	@pb_msglabel.text = @config_msg + "Adjusting /var directory..."
	system("rm -fr #{Global.target}/var/tmp")
	system("mkdir -p #{Global.target}/var/tmp")
	%x(chroot "#{Global.target}" chmod 1777 /tmp)
	%x(chroot "#{Global.target}" chmod 1777 /var/tmp)
	#some cleaning routines
	%x(chroot "#{Global.target}" rm -f /var/cache/apt/list/* 2>/dev/null)
	%x(chroot "#{Global.target}" touch /var/cache/apt/list/lock 2>/dev/null)
	%x(chroot "#{Global.target}" rm -f * /var/cache/apt/* 2>/dev/null)
	%x(chroot "#{Global.target}" rm -f /var/log/* 2>/dev/null)
	%x(chroot "#{Global.target}" rm -f /var/run/* 2>/dev/null)
	%x(chroot "#{Global.target}" touch /var/run/utmp)
	%x(chroot "#{Global.target}" chmod 664 /var/run/utmp)
	%x(chroot "#{Global.target}" chown root.utmp /var/run/utmp)
	%x(chroot "#{Global.target}" touch /var/log/wtmp)
	%x(chroot "#{Global.target}" chmod 664 /var/log/wtmp)
	%x(chroot "#{Global.target}" chown root.utmp /var/log/wtmp)
	%x(chroot "#{Global.target}" updatedb)
	#creating partitions map
	@pb_msglabel.text = @config_msg + "Creating partitions map..."
	partitions = `fdisk -l | grep /dev | grep -v Disk | awk '{print $1}'`.chomp.split
	swap = `fdisk -l | grep /dev | grep -v Disk | awk '{if ($2=="*" && $6=="82") print $1;else {if ($5=="82") print $1}}'`.chomp.split
	extended = `fdisk -l | grep /dev | grep -v Disk | awk '{if ($5=="5" || $5=="f") print $1}' | head -1`.chomp.split
	@resultingpart = partitions - swap - extended
	mountpoints = []
	@resultingpart.each do |part|
		mountpoints << part.sub(/dev/, "mnt")
	end
	# create all mount points in target
	mountpoints.each do |point|
		%x(chroot "#{Global.target}" mkdir "#{point}") 
	end
	# set up hostname
	@pb_msglabel.text = @config_msg + "Setup hostname and users..."
	FileUtils.rm_r("#{Global.target}/etc/hostname") if File.exists?("#{Global.target}/etc/hostname")
	hostnamefile = File.open("#{Global.target}/etc/hostname", "w")
	hostnamefile.puts "#{Global.boxname}"
	hostnamefile.close
	# set up mailname
	FileUtils.rm_r("#{Global.target}/etc/mailname") if File.exists?("#{Global.target}/etc/mailname")
	mailnamefile = File.open("#{Global.target}/etc/mailname", "w")
	mailnamefile.puts "#{Global.boxname}"
	mailnamefile.close
	%x(echo "127.0.0.1\tlocalhost\t #{Global.boxname}" > tempfile)
	%x(cat "#{Global.target}"/etc/hosts | grep -v ^127.0.0.1 >> tempfile)
	%x(mv "#{Global.target}"/etc/hosts "#{Global.target}"/etc/hosts.orig)
	%x(mv tempfile "#{Global.target}"/etc/hosts)
	# create user(s)
	# first, move /etc/skel to /etc/skel.bak, and then copy /home/dreamer to /etc/skel
#	%x(mv "#{Global.target}"/etc/skel "#{Global.target}"/etc/skel.bak) if File.exists?("#{Global.target}/etc/skel")
#	system("rsync -aq --exclude #{Global.target}/home/dreamer/.ecore #{Global.target}/home/dreamer/ #{Global.target}/etc/skel")
#	system("rm -rf #{Global.target}/etc/skel/.ecore") if File.exists?("#{Global.target}/etc/skel/.ecore")
	# now, remove dreamer user
#	system("chroot #{Global.target} userdel -r dreamer") if File.exists?("#{Global.target}/home/dreamer")
	#setup root password
	rootpass = Global.rootpass.chomp
	%x(chroot "#{Global.target}" echo "root:#{rootpass}" > /tmp/passwd)
	%x(chroot "#{Global.target}" chpasswd < /tmp/passwd)
	# and now, create user(s)
	if (Global.users.size == 0) #or (Global.users.size ==1) 
		user = Global.user.chomp
		%x(chroot "#{Global.target}" groupadd -g 1000 "#{user}")
		%x(chroot "#{Global.target}" grpconv)
		userpass = Global.userpass.chomp
		%x(chroot "#{Global.target}" echo "#{user}:#{userpass}" > /tmp/passwd)
		%x(chroot "#{Global.target}" useradd -m -g "#{user}" -c "Animux User" -s /bin/bash "#{user}")
		%x(chroot "#{Global.target}" chpasswd < /tmp/passwd)
		FileUtils.rm_r("#{Global.target}/tmp/passwd") if File.exists?("#{Global.target}/tmp/passwd")
		%x(chroot "#{Global.target}" pwconv)
		%x(chroot "#{Global.target}" chown -R "#{user}.#{user}" /home/"#{user}")
		if ! File.exists?("#{Global.target}/home/#{user[0]}/.Xauthority")
			%x(chroot "#{Global.target}" touch /home/"#{user}"/.Xauthority)
			%x(chroot "#{Global.target}" chmod 600 /home/"#{user}"/.Xauthority)
			%x(chroot "#{Global.target}" chown "#{user}.#{user}" /home/"#{user}"/.Xauthority)
		end		
		if ! File.exists?("#{Global.target}/home/#{user}/.ICEauthority")
			%x(chroot "#{Global.target}" touch /home/"#{user}"/.ICEauthority)
			%x(chroot "#{Global.target}" chmod 600 /home/"#{user}"/.ICEauthority)
			%x(chroot "#{Global.target}" chown "#{user}.#{user}" /home/"#{user}"/.ICEauthority)
		end
		userin = `cat "#{Global.target}"/etc/shadow | grep ^"#{user}" | awk -F":" '{print $1}'`.chomp
	else # you have 1 or more users on Global.users
		groupnumber = 999
		Global.users.each do |user|
			groupnumber += 1
			%x(chroot "#{Global.target}" echo "#{user[0]}:#{user[1]}" >> /tmp/passwd)
			%x(chroot "#{Global.target}" groupadd -g "#{groupnumber}" "#{user[0]}")
			%x(chroot "#{Global.target}" useradd -m -g "#{user[0]}" -c "Animux User" -s /bin/bash "#{user[0]}")
			%x(chroot "#{Global.target}" chown -R "#{user[0]}.#{user[0]}" /home/"#{user[0]}")
			if ! File.exists?("#{Global.target}/home/#{user[0]}/.Xauthority")
				%x(chroot "#{Global.target}" touch /home/"#{user[0]}"/.Xauthority)
				%x(chroot "#{Global.target}" chmod 600 /home/"#{user[0]}"/.Xauthority)
				%x(chroot "#{Global.target}" chown "#{user[0]}.#{user[0]}" /home/"#{user[0]}"/.Xauthority)
			end		
			if ! File.exists?("#{Global.target}/home/#{user}/.ICEauthority")
				%x(chroot "#{Global.target}" touch /home/"#{user[0]}"/.ICEauthority)
				%x(chroot "#{Global.target}" chmod 600 /home/"#{user[0]}"/.ICEauthority)
				%x(chroot "#{Global.target}" chown "#{user[0]}.#{user[0]}" /home/"#{user[0]}"/.ICEauthority)
			end
		end
		%x(chroot "#{Global.target}" chpasswd < /tmp/passwd)
		%x(chroot "#{Global.target}" grpconv)
		%x(chroot "#{Global.target}" pwconv)
		%x(chroot "#{Global.target}" rm -f /tmp/passwd)
	end
	@pb_msglabel.text = @config_msg + "Setup sudoers, menu, groups..."
	# set up /etc/sudoers
	%x(cat "#{Global.target}"/etc/sudoers | grep -v animux > "#{Global.target}"/etc/tempsudoers)
	%x(mv "#{Global.target}"/etc/tempsudoers "#{Global.target}"/etc/sudoers)
	if (Global.users.size == 0) #or (Global.users.size ==1) 
		%x(echo "#{Global.user} ALL=NOPASSWD: ALL" >> "#{Global.target}"/etc/sudoers)
	else
		Global.users.each do |user|
			%x(echo "#{user[0]}    ALL=NOPASSWD: ALL" >> "#{Global.target}"/etc/sudoers)
		end
	end
	%x(chmod 0440 "#{Global.target}"/etc/sudoers)
	### Copia icones para o menu:
	### postinst routines
#	if (Global.users.size == 0) 
#		system("mv #{Global.target}/home/#{Global.user}/Desktop/dli2.desktop #{Global.target}/usr/local/share/applications")
#	else
#		Global.users.each do |user|
#			system("mv #{Global.target}/home/#{Global.user}/Desktop/dli2.desktop #{Global.target}/usr/local/share/applications")
#		end
#	end
#	system("mv #{Global.target}/etc/rcS.d/S27fstab_create #{Global.target}/usr/local/etc/")
#	system("mv #{Global.target}/etc/rcS.d/S57hwdetected #{Global.target}/usr/local/etc/")
#	system("mv #{Global.target}/etc/rcS.d/S72xorgconf #{Global.target}/usr/local/etc/")
#	system("mv #{Global.target}/etc/rc2.d/S27copyskel #{Global.target}/usr/local/etc/")
	fix_groups
	
	# Check 
	@pb_msglabel.text = @config_msg + "Setting up fstab..."
	# create fstab
	create_fstab
	@pb_msglabel.text = @config_msg + "Update interfaces..."
	# eth devs
	update_network
	@pb_msglabel.text = @config_msg + "Setting up Grub..."
	# create grub
	disks = `fdisk -l | grep Disk | grep -v "Disk identifier:" | awk '{print $2}' | sed 's/://'`.chomp.split # ["/dev/sda", "/dev/sdb"]
	masterdisk = disks[0] # "/dev/sda" 
	diskinstalled = Global.rootpart.slice(0, 8) # Ex: /dev/sda
	if Global.grub == "mbr"
		grub_install(masterdisk, Global.rootpart, Global.target, distrotitle, @framebuffer)
	elsif Global.grub == "root"
		grub_install(Global.rootpart, Global.rootpart, Global.target, distrotitle, @framebuffer)
	elsif Global.grub == "existing"
		insert_on_grub(Global.rootpart, @framebuffer, distrotitle, disks)
	end
	@pb_msglabel.text = @config_msg + "Finalizing config..."
	# now, move outofroot partitions...
	# If there's more than one partition where the system will be installed, like /home
	if Global.part2inst.size > 1 
		Global.outofroot.each do |part|
			# move each directory in outofroot to its specific partition.
			# Global.outofroot can be, e.g., [["/home", "/dev/sda7", "ReiserFS", "yes", "linux"]]
			device = "#{part[1]}"
			mountpoint = device.sub(/dev/, "mnt")
			folder = "#{part[0]}"
			system("mount #{device} #{mountpoint}") # this should be already mounted
			system("mount #{Global.rootpart} #{Global.target}")
			system("rsync -aq #{Global.target}#{folder}/* #{mountpoint}") if Global.format #copy outoftheroot dir to its partition, if Global.format = true
			system("rm -fr #{Global.target}#{folder}/*") # delete content of outoftheroot dir
		end
	end
	#write flag Dreamlinux installed
#	system("mount #{Global.rootpart} #{Global.target} 2>/dev/null")
#	%x(echo "yes" > "#{Global.target}"/etc/dreamlinux/dreaminstalled)
end

def create_progress_box
	# progress bar 
	pb_frame = Gtk::Frame.new
	pb_box = Gtk::HBox.new(true)
	pb_frame.add(pb_box)
	pb_msgbox = Gtk::VBox.new
	pb_box.pack_start(pb_msgbox)
	@pb_msglabel = Gtk::Label.new # Ex: Installing, Configuring, Installed 
	@pb_msglabel.set_alignment(0, 0.5)
	pb_msgbox.pack_start(@pb_msglabel)

	pb_progress = Gtk::VBox.new
	pb_box.pack_start(pb_progress)
	@progress_bar = Gtk::ProgressBar.new
	@progress_bar.set_fraction(0)
	pb_progress.pack_start(@progress_bar)	
	return pb_frame
end

def install(distrotitle)
	root = setup_directories # mount partitions, setup directories and return the root dir 
	rootlinks = setup_rootlinks
	#calculating approx. space to install
	size_install = 0
	puts "calculating size"
	puts root
	root.each do |d|
		size_install += `du -s "#{Global.source}/#{d}"`.chomp.to_i
	end
	size_install += (size_install * 1/100)
	@total_size = (size_install / 1024).to_i
	@percentage = 0
	@pb_msglabel.text = @install_msg
	t1 = Thread.new do
		@execbutton.sensitive = false
		do_install(distrotitle, root, rootlinks) # copy the directories to assigned partition(s)
		Gtk::timeout_remove(@timer2)
		@progress_bar.set_fraction(1)
		@pb_msglabel.text = @installed_msg + "Reboot and have fun!"
	end
	t2 = Thread.new do
		timer = Gtk::timeout_add(1000) do
			if @percentage == 100
				@percentage = 0
				Gtk::timeout_remove(timer)
				@progress_bar.set_fraction(1)
				sleep 1
				@progress_bar.pulse_step = 0.10
				@timer2 = Gtk::timeout_add(100) do
					@progress_bar.pulse
				end
				@pb_msglabel.text = @config_msg
			else
				@sizecopied = `df -m "#{Global.target}" | grep -v Used | awk '{print $3}'`.chomp.to_i
				@percentcopied_msg = @sizecopied.to_s + " MB of approx. " + @total_size.to_s + " MB"
				@pb_msglabel.text = @install_msg + @percentcopied_msg
				@percentage = ((@sizecopied / @total_size.to_f) * 100).to_i
				@progress_bar.set_text("#{@percentage}" + "%")
				@progress_bar.set_fraction("#{@percentage}".to_f/100)
			end
		end
	end
end

##main 
Gtk.init
@lang = ENV["LANG"]
ENV["LANG"] = "C"
#setup flushing
$stdout.sync = true
$stderr.sync = true
# Get DLI config
read_dliconf
# setup fixed variables
@install_msg = " Installing | "
@config_msg = " Configuring | "
@installed_msg = " Installed | "


Dir.mkdir("#{Global.source}") if ! File.exists?("#{Global.source}")
puts "grep -q \"#{Global.source}\" /proc/mounts || mount -o loop /live_media/casper64/filesystem.squashfs \"#{Global.source}\""
system("grep -q \"#{Global.source}\" /proc/mounts || mount -o loop /live_media/casper64/filesystem.squashfs \"#{Global.source}\"")

# main window
@win = Gtk::Window.new("Animux Installer - Installs Animux to HDD")
@win.set_border_width(10)
@win.set_default_size(700, -1) 
@win.set_window_position(Gtk::Window::POS_CENTER_ALWAYS)
@win.set_icon("./dream-start.png")
@win.signal_connect('destroy') do
	ENV["LANG"] = @lang
	Gtk.main_quit
end

# we need to set up @execbutton here
@execbutton = Gtk::Button.new(Gtk::Stock::APPLY)

# The main container
box = Gtk::VBox.new
@win.add(box)

# menu bar
menubar = Gtk::MenuBar.new
box.pack_start(menubar, false, false, 0)
#menu items
menu_about = Gtk::MenuItem.new("_About")
menu_about.signal_connect("activate") {about}
menu_parted = Gtk::MenuItem.new("_Partition Tools")
menu_tutorial = Gtk::MenuItem.new("_Help")
if File.exist?("/usr/bin/acroread") 
	pdfhelper = "acroread"
elsif File.exist?("/usr/bin/evince")
	pdfhelper = "evince"
else
	pdfhelper = "xpdf"
end
menu_tutorial.signal_connect("activate") {system("#{pdfhelper} /usr/local/share/dli_tutorial.pdf")}
menu_exit = Gtk::MenuItem.new("_Exit")
menu_exit.signal_connect("activate") {Gtk.main_quit}
# add menu items to menubar
menubar.append(menu_about)
menubar.append(menu_parted)
menubar.append(menu_tutorial)
menubar.append(menu_exit)
#tooltips
tooltips = Gtk::Tooltips.new
tooltips.set_tip(menu_about, "About the Application", "")
tooltips.set_tip(menu_parted, "Lauch Partition Tools", "")
tooltips.set_tip(menu_tutorial, "Launch a DLI pdf Tutorial", "")
tooltips.set_tip(menu_exit, "Exit the app", "")

partitions_submenu = Gtk::Menu.new
menu_parted.set_submenu(partitions_submenu)
menu_gparted = Gtk::MenuItem.new("_Graphical Partition Tool")
menu_gparted.signal_connect("activate") {%x("#{@gparttool}")}
menu_tparted = Gtk::MenuItem.new("_Text Partition Tool")
menu_tparted.signal_connect("activate") {`xterm -e "#{@tparttool}" &`}

partitions_submenu.append(menu_gparted)
partitions_submenu.append(menu_tparted)

#The main panels container
mainbox = Gtk::HBox.new(false, 5)
box.pack_start(mainbox)

# Check leftpanel
if @leftpanel
	# The left "panel"			
	leftbox = Gtk::VBox.new(false)
	mainbox.pack_start(leftbox, false, false, 0)
	# The image on left "panel"
	frame = Gtk::Frame.new
	frame.shadow_type = Gtk::SHADOW_IN
	leftbox.pack_start(frame, false, false, 0)
	@image = Gtk::Image.new("./hdd-install2.png")
	frame.add(@image)
end

# The right "panel"			
rightbox = Gtk::VBox.new(false)
mainbox.pack_start(rightbox, true, true, 0)

# Box name, Root passwd, User name and passwd
infoframe = Gtk::Frame.new("Box, Root & User Info")
rightbox.pack_start(infoframe, false, false, 0)

infobox = Gtk::HBox.new(false, 0)
infoframe.add(infobox)
infobox.set_spacing(5)

# rootbox
rootbox = Gtk::VBox.new(false, 0)
infobox.pack_start(rootbox, false, false)
roottable = Gtk::Table.new(3, 2)
rootbox.pack_start(roottable)
roottable.set_border_width(5)

boxnamelb = Gtk::Label.new("Box name:")
boxnamelb.set_size_request(95, -1)
boxnamelb.set_alignment(1, 0.5)
@entry_box = Gtk::Entry.new
@entry_box.editable = true
@entry_box.signal_connect('changed') do
	Global.boxname = @entry_box.text
	can_install
end
@entry_box.text = Global.boxname if Global.boxname

rootpasslb = Gtk::Label.new("Root passwd:")
rootpasslb.set_size_request(95, -1)
rootpasslb.set_alignment(1, 0.5)
@entry_rootpass = Gtk::Entry.new
@entry_rootpass.editable = true
@entry_rootpass.visibility = false
@entry_rootpass.signal_connect('changed') do
	Global.rootpass = @entry_rootpass.text
	good_boxname
end
@entry_rootpass.text = Global.rootpass if Global.rootpass

rrootpasslb = Gtk::Label.new("Again:")
rrootpasslb.set_size_request(95, -1)
rrootpasslb.set_alignment(1, 0.5)
@entry_rrootpass = Gtk::Entry.new
@entry_rrootpass.editable = true
@entry_rrootpass.visibility = false
@entry_rrootpass.signal_connect('changed') do
	Global.rrootpass = @entry_rrootpass.text
	can_install
end
@entry_rrootpass.text = Global.rrootpass if Global.rrootpass

roottable.attach_defaults(boxnamelb, 0, 1, 0, 1)
roottable.attach_defaults(@entry_box, 1, 2, 0, 1)
roottable.attach_defaults(rootpasslb, 0, 1, 1, 2)
roottable.attach_defaults(@entry_rootpass, 1, 2, 1, 2)
roottable.attach_defaults(rrootpasslb, 0, 1, 2, 3)
roottable.attach_defaults(@entry_rrootpass, 1, 2, 2, 3)

## user name
userbox = Gtk::VBox.new(false, 0)
infobox.pack_start(userbox, false, false)
usertable = Gtk::Table.new(3, 2)
usertable.set_border_width(5)
userbox.pack_start(usertable)

usernamelb = Gtk::Label.new("User name:")
usernamelb.set_size_request(95, -1)
usernamelb.set_alignment(1, 0.5)
@entry_user = Gtk::Entry.new
@entry_user.editable = true
@entry_user.signal_connect('changed') do
	Global.user = @entry_user.text
	good_passwd(Global.rootpass, Global.rrootpass)
	can_install
end
@entry_user.text = Global.user if Global.user

userpasslb = Gtk::Label.new("User passwd:")
userpasslb.set_size_request(95, -1)
userpasslb.set_alignment(1, 0.5)
@entry_userpass = Gtk::Entry.new
@entry_userpass.editable = true
@entry_userpass.visibility = false
@entry_userpass.signal_connect('changed') do
	good_passwd(Global.rootpass, Global.rrootpass)
	Global.userpass = @entry_userpass.text
end
@entry_userpass.text = Global.userpass if Global.userpass

ruserpasslb = Gtk::Label.new("Again:")
ruserpasslb.set_size_request(95, -1)
ruserpasslb.set_alignment(1, 0.5)
@entry_ruserpass = Gtk::Entry.new
@entry_ruserpass.editable = true
@entry_ruserpass.visibility = false
@entry_ruserpass.signal_connect('changed') do
	Global.ruserpass = @entry_ruserpass.text
	can_install
end
@entry_ruserpass.text = Global.ruserpass if Global.ruserpass

usertable.attach_defaults(usernamelb, 0, 1, 0, 1)
usertable.attach_defaults(@entry_user, 1, 2, 0, 1)
usertable.attach_defaults(userpasslb, 0, 1, 1, 2)
usertable.attach_defaults(@entry_userpass, 1, 2, 1, 2)
usertable.attach_defaults(ruserpasslb, 0, 1, 2, 3)
usertable.attach_defaults(@entry_ruserpass, 1, 2, 2, 3)

userbtbox = Gtk::VBox.new(false, 0) ##
infobox.pack_start(userbtbox, false, false) ##
userbuttonstable = Gtk::Table.new(2,1, true)
userbtbox.pack_start(userbuttonstable, false, false)

incuserbt = StockButton.new("Add", Gtk::Stock::ADD, :vert)
userbuttonstable.attach_defaults(incuserbt, 0, 1, 0, 1)
incuserbt.signal_connect("clicked") do
	if good_passwd(Global.userpass, Global.ruserpass) == true
		Global.users << ["#{Global.user}", "#{Global.userpass}", "#{Global.ruserpass}"]
		@model_users.clear
		Global.users.each do |v|
			iter = @model_users.append
			iter[0] =  v[0]
		end
	else
		good_passwd(Global.userpass, Global.ruserpass)
	end
end

newuserbt = StockButton.new("New", Gtk::Stock::NEW, :vert)
userbuttonstable.attach_defaults(newuserbt, 0, 1, 1, 2)
newuserbt.signal_connect("clicked") do
	@entry_user.text = ""
	@entry_userpass.text = ""
	@entry_ruserpass.text = ""
	@entry_user.has_focus = true
end

## Show users names
usersbox = Gtk::VBox.new(false, 0)
infobox.pack_start(usersbox)

scrolled_win = Gtk::ScrolledWindow.new
scrolled_win.set_policy(Gtk::POLICY_AUTOMATIC,Gtk::POLICY_AUTOMATIC)
usersbox.pack_start(scrolled_win, true, true, 0)

@model_users = Gtk::ListStore.new(String)
treeview = Gtk::TreeView.new(@model_users)
column = Gtk::TreeViewColumn.new("Users",
                                 Gtk::CellRendererText.new, {:text => 0})
treeview.append_column(column)
scrolled_win.add_with_viewport(treeview)

# The select partitions "panel"
partframe = Gtk::Frame.new("Partitions")
rightbox.pack_start(partframe, true, true, 0)
partbox = Gtk::HBox.new
partframe.add(partbox)
partselbox = Gtk::VBox.new(false) # contains detected partitions
partbox.pack_start(partselbox)
partbuttonsbox = Gtk::VBox.new(false) # contains select and re-read button
partbox.pack_start(partbuttonsbox, false, false, 2)
partinfobox = Gtk::VBox.new(false) # contain selected partitions
partbox.pack_start(partinfobox)

# info on *nix partitions column
label = Gtk::Label.new.set_markup("<b>Detected *nix partitions</b>")
partselbox.pack_start(label, false, false, 0)

@model = create_models
			
framescroll = Gtk::ScrolledWindow.new
framescroll.shadow_type = Gtk::SHADOW_IN
framescroll.set_policy(Gtk::POLICY_AUTOMATIC, Gtk::POLICY_AUTOMATIC)
partselbox.pack_start(framescroll, true, true, 0)
			
@treeview = Gtk::TreeView.new(@model)
@treeview.selection.set_mode(Gtk::SELECTION_BROWSE)
@treeview.headers_visible = true
@treeview.selection.signal_connect('changed') {changed} 
framescroll.add(@treeview)

# 1st column(Text) => /dev/(h)(s)d??
trenderer = Gtk::CellRendererText.new
tcol = Gtk::TreeViewColumn.new("Partition", trenderer, :text => COL_DEV)
@treeview.append_column(tcol)

# 2nd column(Text) sizeMB
trenderer = Gtk::CellRendererText.new
tcol = Gtk::TreeViewColumn.new('Size', trenderer, :text => COL_SIZE)
@treeview.append_column(tcol)

# 3rd column(Text) type
trenderer = Gtk::CellRendererText.new
tcol = Gtk::TreeViewColumn.new('Type', trenderer, :text => COL_TYPE)
@treeview.append_column(tcol)

# 4th column(Combo) mntpt
crenderer = Gtk::CellRendererCombo.new
crenderer.signal_connect("edited") do |renderer, path, text|
	@model.get_iter(path)[P_COMBO_TEXT] = text
end

ccol = Gtk::TreeViewColumn.new("Mntpt", crenderer,
							:text_column => P_COMBO_TEXT_COLUMN, 
							:model => P_COMBO_MODEL, 
							:has_entry => P_COMBO_HAS_ENTRY,
							:editable => P_COMBO_EDITABLE,
							:text => P_COMBO_TEXT)
@treeview.append_column(ccol)

# 5th column(Combo) fstype
crenderer = Gtk::CellRendererCombo.new
crenderer.signal_connect("edited") do |renderer, path, text|
	@model.get_iter(path)[T_COMBO_TEXT] = text
end

ccol = Gtk::TreeViewColumn.new("Filesys", crenderer,
							:text_column => T_COMBO_TEXT_COLUMN, 
							:model => T_COMBO_MODEL, 
							:has_entry => T_COMBO_HAS_ENTRY,
							:editable => T_COMBO_EDITABLE,
							:text => T_COMBO_TEXT)
@treeview.append_column(ccol)

# 6th column(TrueClass) Format
renderer = Gtk::CellRendererToggle.new
renderer.signal_connect('toggled') do |cell, path|
	fixed_toggled(@treeview.model, path)
end
column = Gtk::TreeViewColumn.new('Format', renderer, :active => COL_FORMAT)
@treeview.append_column(column)

## buttons select and re-read column
#buttonstable = Gtk::Table.new(4,1, true)
buttonstable = Gtk::Table.new(3,1, true)
dummybt = Gtk::Label.new(" ")
buttonstable.attach_defaults(dummybt, 0, 1, 0, 1)
partbuttonsbox.pack_start(buttonstable, false, false)
selpartinfobt = StockButton.new("Add", Gtk::Stock::ADD, :vert)
#buttonstable.attach_defaults(selpartinfobt, 0, 1, 1, 2)
buttonstable.attach_defaults(selpartinfobt, 0, 1, 1, 2)
rereadpartbt = StockButton.new("Redo", Gtk::Stock::REFRESH, :vert)
#buttonstable.attach_defaults(rereadpartbt, 0, 1, 2, 3)
buttonstable.attach_defaults(rereadpartbt, 0, 1, 2, 3)
selpartinfobt.signal_connect("clicked") do
	#verify if any partition was chosen
	Global.format ? format = "yes" : format = "no"
	if ("#{Global.mntpt}" == "none") || ("#{Global.fspartition}" == "none")
		title = "Partition Info!"
msg = <<END
You need to choose a mounting point and a filesystem to your partition, as well as marking
or unmarking the Format option check box!
Please, on the line related to the chosen partition, left click and hold under the column 
labeled Mntpt, then navigate downwards to select a mounting point.
Do the same on the next column, Filesys, to select a Filesystem in which the selected 
partition will be formatted.
Next, mark the Format check box to confirm that the selected partition will be formatted. 
If you don't want it to be formatted, leave the check box blank.

Note that you need to select the whole line (turning it to blue) prior to clicking on the Add 
button. You can do this by clicking on any part of the line, except the "editable fields" 
(Mntpt, Filesys and Format). 
Another option is to mark/unmark the Format field, which will also select the entire row, 
turning it to blue (selected) instead of grey (edited).

And a third option is you to exercise all your choices on each of the desired partitions first 
and then select them back one by one and then clicking on the Add button.

If you would like to re-start selecting the partitions, click on the Redo button and everything 
will be restored to the original state. 
END
		msgwin(Gdk::Pixbuf.new("./dream-start.png"), title, msg)
	else
		Global.chosenpart << ["#{Global.mntpt}", "#{Global.partition}",  "#{Global.fspartition}", "#{format}", "#{Global.partitiontype}"]
		@model_partitions.clear
		Global.chosenpart.each do |v|  
			iter = @model_partitions.append
			iter[0] = v[0]
			iter[1] = v[1]
			iter[2] = v[2]
			iter[3] = v[3]
		end
		can_install
	end
end

rereadpartbt.signal_connect("clicked") {reread_partitions}

## Chosen partitions column
labelpart2inst = Gtk::Label.new.set_markup("<b>Selected partitions</b>")
chosenpartbox = Gtk::VBox.new
chosenpartbox.pack_start(labelpart2inst, false, false, 0)
partinfobox.pack_start(chosenpartbox, true, true, 0)
scrolled_win = Gtk::ScrolledWindow.new
scrolled_win.set_policy(Gtk::POLICY_AUTOMATIC,Gtk::POLICY_AUTOMATIC)
chosenpartbox.pack_start(scrolled_win, true, true, 0)

@model_partitions = Gtk::ListStore.new(String, String, String, String)
treeview = Gtk::TreeView.new(@model_partitions)
column = Gtk::TreeViewColumn.new("Mount",
                                 Gtk::CellRendererText.new, {:text => 0})
treeview.append_column(column)

column = Gtk::TreeViewColumn.new("Device",
                                 Gtk::CellRendererText.new, {:text => 1})
treeview.append_column(column)

column = Gtk::TreeViewColumn.new("Filesys",
                                 Gtk::CellRendererText.new, {:text => 2})
treeview.append_column(column)

column = Gtk::TreeViewColumn.new("Format",
                                 Gtk::CellRendererText.new, {:text => 3})
treeview.append_column(column)

scrolled_win.add_with_viewport(treeview)

# Grub install radiobuttons and entry text
grubbox = Gtk::VBox.new
grubbox.set_border_width(5)
grubbuttonsbox = Gtk::HBox.new
grubbox.pack_start(grubbuttonsbox)
grubframe = Gtk::Frame.new("Install Grub on")
grubframe.add(grubbox)
rightbox.pack_start(grubframe, false, false)

button1 = Gtk::RadioButton.new("MBR")
button2 = Gtk::RadioButton.new(button1, "Root partition")
button3 = Gtk::RadioButton.new(button1, "Existing Grub")
button4 = Gtk::RadioButton.new(button1, "Don't Install")

button1.signal_connect("clicked") {Global.grub = "mbr" }
button2.signal_connect("clicked") {Global.grub = "root" }
button3.signal_connect("clicked") {Global.grub = "existing" }
button4.signal_connect("clicked") {Global.grub = "none" }

grubbuttonsbox.pack_start(button1)
grubbuttonsbox.pack_start(button2)
grubbuttonsbox.pack_start(button3)
grubbuttonsbox.pack_start(button4)

separator = Gtk::HSeparator.new
grubbox.pack_start(separator)

grubtitlelabel = Gtk::Label.new("Input the title of the Distro as to appear on Grub Menu (optional)")
grubtitlelabel.set_alignment(0, 1)
grubbox.pack_start(grubtitlelabel)
grubtitle_entry = Gtk::Entry.new
grubbox.pack_start(grubtitle_entry)

# command buttons 
buttons = Gtk::HBox.new
rightbox.pack_start(buttons, false, false, 0)

cancelbuttonbox = Gtk::HBox.new(false, 2)
buttons.pack_start(cancelbuttonbox, false)
cancelbutton = Gtk::Button.new(Gtk::Stock::QUIT)
cancelbutton.signal_connect("clicked") do 
	ENV["LANG"] = @lang
	Gtk.main_quit
end
cancelbuttonbox.pack_start(cancelbutton)

@progressbox_hold = Gtk::HBox.new
buttons.pack_start(@progressbox_hold)

@execbuttonbox = Gtk::HBox.new(false, 2)
buttons.pack_start(@execbuttonbox, false)
@execbuttonbox.pack_start(@execbutton)
@execbutton.signal_connect("clicked") do 
	Global.distro_title = grubtitle_entry.text if grubtitle_entry.text != ""
	progressbox = create_progress_box
	@progressbox_hold.pack_start(progressbox)
	@win.show_all
	install(Global.distro_title)
end

@win.show_all

Gtk.main
