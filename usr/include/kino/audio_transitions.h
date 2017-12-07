/*
 * audio_transitions.h -- audio transitions
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

#ifndef _AUDIO_TRANSITIONS_H_
#define _AUDIO_TRANSITIONS_H_

// C++ Includes

#include <vector>
using std::vector;

// C Includes

#include <stdint.h>
#include <gtk/gtk.h>

/** Public interface for all audio transition classes.

	This contains 2 methods:

	- GetDescription simply returns a GUI usable identifier for the implementing class
	- GetFrame receives two arrays of audio samples of the same frequency, number of channels 
	  and samples (the sender is responsible for resampling to ensure this), and a positional
	  indicator

	The aframes and bframes are those samples determined from the left and right part of a
	transition respectively. Confusingly, the bframes may be a duplicate of the aframes (in
	all cases other than when 'Image Transitions to frames' is selected...), and in many of the 
	implemented cases, the bframes aren't even used... (the Dub option for example uses neither... 
	the reason for this is that the Dub is incomplete... it should allow more than just overwrite 
	from a wav, and should mix and introduce at start and end... in which case, the bframes are 
	important). 

	It should also be noted that any audio obtained from alternative sources (such as wavs) should
	resample to the input sample provided... no functionality is exposed from kino to do this in
	the plugin mechanism in this release.

	In effect, the audio transitions and filters are poorly implemented, but the interface shouldn't 
	restrict the creation of comprehensive plugins.
*/

class AudioTransition 
{
	public:
		virtual ~AudioTransition() {}
		virtual char *GetDescription( ) const = 0;
		virtual void GetFrame( int16_t **aframe, int16_t **bframe, int frequency, int channels, int& samples, double position, double frame_delta ) = 0;
		virtual bool IsUsable( ) { return true; }
		virtual bool IsBFrameConsumer( ) const { return true; }
};

/** Public abstract class for audio transitions with additional GUI inputs and feedback.
 
	This allows a transition to attach and interpret any additional widgets in the container 
	provided. 

	The activation of the AttachWidget and DetachWidgets is handled automatically by the 
	repository on the detection of a selection change.

	InterpretWidgets must be called (by the repository owner) before the first call to 
	GetFrame.

	If an implementation doesn't attach any widgets, the default implementation is enough
	(though the adapter will give you that anyway).
*/

class GDKAudioTransition : public AudioTransition
{
	public:
		virtual ~GDKAudioTransition() {}
		virtual void AttachWidgets( GtkBin *bin ) { }
		virtual void InterpretWidgets( GtkBin *bin ) { }
		virtual void DetachWidgets( GtkBin *bin ) { }
};

/** Public AudioTransition to GDKAudioTransition adapter.
 
	Since not all transitions will require additional GUI functionality, this class is provided
	as a convenience to wrap the non-GDK transitions into basic GDK transitions.
*/

class GDKAudioTransitionAdapter : public GDKAudioTransition
{
	private:
		AudioTransition *transition;

	public:
		GDKAudioTransitionAdapter( AudioTransition *transition ) { this->transition = transition; }
		virtual ~GDKAudioTransitionAdapter( ) { delete transition; }
		char *GetDescription( ) const { return this->transition->GetDescription( ); }
		void GetFrame( int16_t **aframe, int16_t **bframe, int frequency,
					   int channels, int& samples, double position, double frame_delta ) {
			return this->transition->GetFrame( aframe, bframe, frequency, channels, samples, position, frame_delta );
		}
};

/** Public class for exposing each of the registered transitions through a selectable GUI
 	component (in this case, only an OptionMenu is provided).

	Transitions are currently registered in the repositories constructor and added to the
	OptionMenu provided via the Initialise function. 

	Additional transitions can be registered before an Initialise call (using the Register
	method), and Initialise can be called many times if necessary.

	The Initialise method is called with the menu to contain the selectable entries
	and a container for the transition specific widget handling. 
*/

class GDKAudioTransitionRepository
{
	private:
		vector <GDKAudioTransition *> transitions;
		GDKAudioTransition *selected_transition;
		GtkOptionMenu *menu;
		GtkBin *container;
	public:
		GDKAudioTransitionRepository();
		~GDKAudioTransitionRepository();
		void Register( GDKAudioTransition *transition );
		void Initialise( GtkOptionMenu *menu, GtkBin *container );
		GDKAudioTransition *Get( ) const;
		void SelectionChange( );
};

#endif
