
############################################################################
#    Copyright (C) 2005 by Fabio Marzocca                             #
#    thesaltydog@gmail.com                                                 #
#                            
#                                                  #
#    This program is free software; you can redistribute it and or modify  #
#    it under the terms of the GNU General Public License as published by  #
#    the Free Software Foundation; either version 2 of the License, or     #
#    (at your option) any later version.                                   #
#                                                                          #
#    This program is distributed in the hope that it will be useful,       #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of        #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         #
#    GNU General Public License for more details.                          #
#                                                                          #
#    You should have received a copy of the GNU General Public License     #
#    along with this program; if not, write to the                         #
#    Free Software Foundation, Inc.,                                       #
#    59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.             #
#
# 
# 
############################################################################



#==============================================================================
#=== The class Application
#==============================================================================

package bum_app;

use Glib qw(TRUE FALSE);
use bum_Config;
use Carp;
use File::Spec;
use strict ;
use Locale::gettext;
use POSIX qw(setlocale);
use POSIX qw(getuid);
use Encode qw(decode);
use Gtk2 -init ;
use Gtk2::GladeXML;
use constant NULL => 0;
use bum_ops;
use bum_cbk;
use bumlib;
use bum_init;


our ($gladexml,$AUTOLOAD);



	setlocale(LC_MESSAGES, "");
	textdomain(bum_Config->PACKAGE);    
	bind_textdomain_codeset(bum_Config->PACKAGE,"UTF-8");
	bindtextdomain(bum_Config->PACKAGE,
							bum_Config->DATADIR . '/locale');
							
#####################################################
sub _ {return decode("utf-8",dgettext( bum_Config->PACKAGE,$_[0]));}
######################################################

my %go_fields=(
	version => bum_Config->VERSION,
	# the main window
	window=>undef,
	# the about dialog window
	about=>undef,
	#icon path
	icon_path=>undef,
	#progress bar
	pbar => undef,
	#the notebook
	notebook => undef,
	#the treeviews lists
	summary =>undef,
	standardRL => undef,
	rcSd => undef,
	#textviews
	text_standard	=> undef,
	text_rcS		=> undef,
	#info buffers
	info_b_standard => undef,
	info_b_rcS		=> undef,
	#pages
	SUM_PAGE => 0,
    STA_PAGE => 1,
    RCS_PAGE => 2,
);


sub new{
	my $that =shift;
	my $classe=ref($that) ||$that;
	my $self={
		_permitted=>\%go_fields,%go_fields,};
	bless($self,$classe);

	bum_cbk::init($self);
	bum_ops::init($self);

		
	#is user root?
	if (getuid() != 0) {
		bum_ops::message(_("You must run this program as the root user."),
							'GTK_MESSAGE_ERROR');
		exit 1;		
	}
	
	exit 1 if (bum_ops::check_if_lock());
	
	####################################################
	####### User Interface
	####################################################
	my $gladepath=File::Spec->catfile(bum_Config->PKGDATADIR,
	                                   'bum.glade');
	croak("Unable to find '$gladepath': $!") unless -f $gladepath;
		
	$gladexml = Gtk2::GladeXML->new($gladepath );
	$gladexml->signal_autoconnect_from_package('bum_cbk' );

	#### Initialization of the Application attributes
	$self->icon_path (File::Spec->catfile(
		(bum_Config->DATADIR, 'pixmaps'),
		"bum.png"));
	$self->about($gladexml->get_widget('about1' ));
	$self->window($gladexml->get_widget('window1' ));
	$self->notebook($gladexml->get_widget('notebook1' ));
	$self->window->set_icon(Gtk2::Gdk::Pixbuf->new_from_file($self->icon_path));

	#start progress bar
	$self->pbar(bum_ops::start_progress());
	
	#standard treeview SimpleList 
	$self->standardRL(bum_ops::create_standardRL_treeview(
					$gladexml->get_widget('treeview2' )));
	$self->text_standard($gladexml->get_widget('textview2' ));
	$self->info_b_standard($self->text_standard->get_buffer());
	$self->info_b_standard->create_tag ("title", weight => 700);

	#summary treeview Gtk2::TreeView
	croak("Unable to create standard treeview!") unless defined($self->standardRL);
	$self->summary(bum_ops::create_summary_treeview(
					$gladexml->get_widget('treeview1' )));

	#rcSd treeview SimpleList
	$self->rcSd(bum_ops::create_rcSd_treeview(
					$gladexml->get_widget('treeview3' )));
	$self->text_rcS($gladexml->get_widget('textview3') );
	$self->info_b_rcS($self->text_rcS->get_buffer());
	$self->info_b_rcS->create_tag ("title", weight => 700);


	bum_init::init_human_text();
	bumlib::get_packages();
	bum_ops::populate_standardRL();
	bum_ops::populate_rcSd();
	bum_ops::change_page(0);
	bum_ops::check_menu_sens();
	bum_ops::destroy_progress($self->pbar);
	$gladexml->get_widget('quit_btn')->set_sensitive(TRUE);

	return $self;

}

sub AUTOLOAD {
	my $self=shift;
	my $type=ref($self) or croak "$self is not an object";
	my $name=$AUTOLOAD;
	$name=~  s/.*:://;
	unless (exists $self->{_permitted}->{$name}) {
	croak "Cannot load  $name fields in class $type" ;}
	if (@_) {
		return $self->{$name}=shift;
	}else {
		return $self->{$name};
		}
}

sub DESTROY {}

	
sub find_program_in_path{
	my $file=shift;
    my $found_prog_and_path=NULL;
	my ($dir,$path);
     
       
       for $dir (split(/:/,$ENV{'PATH'})) {
          if(-x ($path="$dir/$file") ){
             $path=~s/\/\//\//g;  ## removing /bin//gzip like entry
             $found_prog_and_path = $path ;
			 last; 
          }
       }
    
     return($found_prog_and_path);
}



1 ;
