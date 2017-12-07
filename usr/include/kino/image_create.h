/*
 * image_create.h -- RGB24 image create
 * Copyright (C) 2002 Charles Yates <charles.yates@pandora.be>
 * Copyright (C) 2002-2007 Dan Dennedy <dan@dennedy.org>
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software Foundation,
 * Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
 */

#ifndef _IMAGE_CREATE_H_
#define _IMAGE_CREATE_H_

// C++ Includes

#include <vector>
using std::vector;

// C Includes

#include <stdint.h>
#include <gtk/gtk.h>

/** Public interface for all image create classes.

	This contains 3 methods:

	- GetDescription simply returns a GUI usable identifier for the implementing class
	- CreateFrame create an RGB24 image of the given width and height relative to the
	  positional indicator (which will always be 0 on the first call)
	- GetNumberOfFrames returns the number of frames that will be created in this iteration
*/
 
class ImageCreate 
{
	public:
		virtual ~ImageCreate() {}
		virtual char *GetDescription( ) const = 0;
		virtual void CreatePAL( bool is_pal ) { }
		virtual void CreateFrame( uint8_t *pixels, int width, int height, double position, double frame_delta ) = 0;
		virtual int GetNumberOfFrames( ) = 0;
		virtual bool IsUsable( ) { return true; }
};

/** Public abstract class for image creators with additional GUI inputs and feedback.
 
	This allows a creator to attach and interpret any additional widgets in the container 
	provided. It is highly experimental at the moment and use via the adapter provided
	is recommended (ie: it's currently just a placeholder).

	The activation of the AttachWidget and DetachWidgets is handled automatically by the 
	repository on the detection of a selection change.

	InterpretWidgets must be called (by the repository owner) before the first call to 
	CreateFrame.

	If an implementation doesn't attach any widgets, the default implementation is enough
	(though the adapter will give you that anyway).
*/

class GDKImageCreate : public ImageCreate
{
	public:
		virtual ~GDKImageCreate() {}
		virtual void AttachWidgets( GtkBin *bin ) { }
		virtual void DetachWidgets( GtkBin *bin ) { }
		virtual void InterpretWidgets( GtkBin *bin ) { }
};

/** Public interface for the audio import classes.

	This interface provides an additional method to allow the creator to provide audio
	information as well. 
	
	Note that CreateFrame is called before CreateAudio and the channels and frequency returned 
	from here must be specified consistently over all calls and must be 1 or 2 channels and 32000, 
	44100 or 48000 khz. The number of samples per frame must match the frequency and the PAL/NTSC 
	usage (you can detect this from the height requested in the previous CreateFrame - 576 for PAL, 
	480 for NTSC). Number of Samples should subsequently be frequency / 25 for PAL or 
	frequency / 30 for NTSC.
*/

class GDKAudioImport : public GDKImageCreate
{
	public:
		virtual ~GDKAudioImport() {}
		virtual void CreateAudio( int16_t **buffer, short int *channels, int *frequency, int *samples ) = 0;
};

/** Public ImageCreate to GDKImageCreate adapter.
 
	Since not all filters will require additional GUI functionality, this class is provided
	as a convenience to wrap the non-GDK filters into basic GDK filters.
*/

class GDKImageCreateAdapter : public GDKImageCreate
{
	private:
		ImageCreate *creator;

	public:
		GDKImageCreateAdapter( ImageCreate *creator ) { this->creator = creator; }
		virtual ~GDKImageCreateAdapter( ) { delete creator; }
		void AttachWidgets( GtkBin *bin ) { }
		void DetachWidgets( GtkBin *bin ) { }
		void InterpretWidgets( GtkBin *bin ) { }
		char *GetDescription( ) const { return this->creator->GetDescription( ); }
		void CreateFrame( uint8_t *pixels, int width, int height, double position, double frame_delta ) 
		{ 
			return this->creator->CreateFrame( pixels, width, height, position, frame_delta ); 
		}
};

/** Public class for exposing each of the registered creators through a selectable GUI
 	component (in this case, only an OptionMenu is provided).

	Creators are currently registered in the repositories constructor and added to the
	OptionMenu provided via the Initialise function. 

	Additional creators can be registered before an Initialise call (using the Register
	method), and Initialise can be called many times if necessary.
*/

class GDKImageCreateRepository
{
	private:
		vector <GDKImageCreate *> creators;
		GDKImageCreate *selected_creator;
		GtkOptionMenu *menu;
		GtkBin *container;
	public:
		GDKImageCreateRepository();
		~GDKImageCreateRepository();
		void Register( GDKImageCreate *creator );
		void Initialise( GtkOptionMenu *menu, GtkBin *container );
		GDKImageCreate *Get( ) const;
		void SelectionChange( );
};

#endif
