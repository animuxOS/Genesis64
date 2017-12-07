/*
 * image_filters.h -- RGB24 image filters
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

#ifndef _IMAGE_FILTERS_H_
#define _IMAGE_FILTERS_H_

// C++ Includes

#include <vector>
using std::vector;

// C Includes

#include <stdint.h>
#include <gtk/gtk.h>

/** Dummy interface for non-image encoding filters (only ImageFilterKeep should implement
	this. When this is implemented on a class, the image is not re-encoded.
*/

class NullImageFilter
{
};

/** Public interface for all image filter classes.

	This contains 2 methods:

	- GetDescription simply returns a GUI usable identifier for the implementing class
	- FilterFrame receives and overwrites an RGB24 image of the given width and height and
	  a positional indicator
*/
 
class ImageFilter 
{
	public:
		virtual ~ImageFilter() {}
		virtual char *GetDescription( ) const = 0;
		virtual void FilterFrame( uint8_t *pixels, int width, int height, double position, double frame_delta ) = 0;
		virtual bool IsUsable( ) { return true; }
};

/** Public abstract class for image filters with additional GUI inputs and feedback.
 
	This allows a filter to attach and interpret any additional widgets in the container 
	provided. 

	The activation of the AttachWidget and DetachWidgets is handled automatically by the 
	repository on the detection of a selection change.

	InterpretWidgets must be called (by the repository owner) before the first call to 
	FilterFrame.

	If an implementation doesn't attach any widgets, the default implementation is enough
	(though the adapter will give you that anyway).

	As an example (unimplemented): the image repository could expose a single filter called
	Mirror, and the AttachWidgets could provide a GUI component to obtain a Left or Right
	user preference. The FilterFrame would then be sensitive to the users selection. Note 
	that the current implementation exposes two filters in the repository for this.
*/

class GDKImageFilter : public ImageFilter
{
	public:
		virtual ~GDKImageFilter() {}
		virtual void AttachWidgets( GtkBin *bin ) { }
		virtual void DetachWidgets( GtkBin *bin ) { }
		virtual void InterpretWidgets( GtkBin *bin ) { }
};

/** Public ImageFilter to GDKImageFilter adapter.
 
	Since not all filters will require additional GUI functionality, this class is provided
	as a convenience to wrap the non-GDK filters into basic GDK filters.
*/

class GDKImageFilterAdapter : public GDKImageFilter
{
	private:
		ImageFilter *filter;

	public:
		GDKImageFilterAdapter( ImageFilter *filter ) { this->filter = filter; }
		virtual ~GDKImageFilterAdapter( ) { delete filter; }
		char *GetDescription( ) const { return this->filter->GetDescription( ); }
		void FilterFrame( uint8_t *pixels, int width, int height, double position, double frame_delta ) 
		{ 
			return this->filter->FilterFrame( pixels, width, height, position, frame_delta ); 
		}
};

/** Public class for exposing each of the registered filters through a selectable GUI
 	component (in this case, only an OptionMenu is provided).

	Filters are currently registered in the repositories constructor and added to the
	OptionMenu provided via the Initialise function. 

	Additional filters can be registered before an Initialise call (using the Register
	method), and Initialise can be called many times if necessary.
*/

class GDKImageFilterRepository
{
	private:
		vector <GDKImageFilter *> filters;
		GDKImageFilter *selected_filter;
		GtkOptionMenu *menu;
		GtkBin *container;
	public:
		GDKImageFilterRepository();
		~GDKImageFilterRepository();
		void Register( GDKImageFilter *filter );
		void Initialise( GtkOptionMenu *menu, GtkBin *container );
		GDKImageFilter *Get( ) const;
		void SelectionChange( );
};

#endif
