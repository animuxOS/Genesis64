/*
 * audio_filters.h -- audio filters
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

#ifndef _AUDIO_FILTERS_H_
#define _AUDIO_FILTERS_H_

// C++ Includes

#include <vector>
using std::vector;

// C Includes

#include <stdint.h>
#include <gtk/gtk.h>

/** Public interface for all audio filter classes.

	This contains 2 methods:

	- GetDescription simply returns a GUI usable identifier for the implementing class
	- GetFrame receives and overwrites an array of audio samples of a given size,
	  relative to the position in the frame sequence
*/

class AudioFilter 
{
	public:
		virtual ~AudioFilter() {}
		virtual char *GetDescription( ) const = 0;
		virtual void GetFrame( int16_t **buffer, int frequency, int channels, int& samples, double position, double frame_delta ) = 0;
		virtual bool IsUsable( ) { return true; }
		virtual bool IsAFrameConsumer( ) const { return true; }
};

/** Public abstract class for audio filters with additional GUI inputs and feedback.
 
	This allows a filter to attach and interpret any additional widgets in the container 
	provided. It is highly experimental at the moment and use via the adapter provided
	is recommended (ie: it's currently just a placeholder).

	The activation of the AttachWidget and DetachWidgets is handled automatically by the 
	repository on the detection of a selection change.

	InterpretWidgets must be called (by the repository owner) before the first call to 
	GetFrame.

	If an implementation doesn't attach any widgets, the default implementation is enough
	(though the adapter will give you that anyway).
*/

class GDKAudioFilter : public AudioFilter
{
	public:
		virtual ~GDKAudioFilter() {}
		virtual void AttachWidgets( GtkBin *bin ) { }
		virtual void InterpretWidgets( GtkBin *bin ) { }
		virtual void DetachWidgets( GtkBin *bin ) { }
};

/** Public AudioFilter to GDKAudioFilter adapter.
 
	Since not all filters will require additional GUI functionality, this class is provided
	as a convenience to wrap the non-GDK filters into basic GDK filters.
*/

class GDKAudioFilterAdapter : public GDKAudioFilter
{
	private:
		AudioFilter *filter;

	public:
		GDKAudioFilterAdapter( AudioFilter *filter ) { this->filter = filter; }
		virtual ~GDKAudioFilterAdapter( ) { delete filter; }
		char *GetDescription( ) const { return this->filter->GetDescription( ); }
		void GetFrame( int16_t **buffer, int frequency, int channels, int& samples, double position, double frame_delta ) {
			return this->filter->GetFrame( buffer, frequency, channels, samples, position, frame_delta );
		}
};

/** Public class for exposing each of the registered filters through a selectable GUI
 	component (in this case, only an OptionMenu is provided).

	Filters are currently registered in the repositories constructor and added to the
	OptionMenu provided via the Initialise function. 

	Additional filters can be registered before an Initialise call (using the Register
	method), and Initialise can be called many times if necessary.

	The Initialise method is called with the menu to contain the selectable entries
	and a container for the filter specific widget handling. 
*/

class GDKAudioFilterRepository
{
	private:
		vector <GDKAudioFilter *> filters;
		GDKAudioFilter *selected_filter;
		GtkOptionMenu *menu;
		GtkBin *container;
	public:
		GDKAudioFilterRepository();
		~GDKAudioFilterRepository();
		void Register( GDKAudioFilter *filter );
		void Initialise( GtkOptionMenu *menu, GtkBin *container );
		GDKAudioFilter *Get( ) const;
		void SelectionChange( );
};

#endif
