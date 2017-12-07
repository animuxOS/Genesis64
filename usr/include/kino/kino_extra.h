/*
 * kino_extra.h -- FX Header File for Additional Plug-in functionality
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

#ifndef _KINO_EXTRA_H_
#define _KINO_EXTRA_H_

#include <stdint.h>
#include <gtk/gtk.h>

// This is mandatory for plug-ins to be able to access the functionality here
// and is mandatory throughout (in fact, the define should be dropped)
#ifndef WITH_LIBDV
#define WITH_LIBDV
#endif

// Forward declaration to playlist
class PlayList;

// Provide a means to obtain the current playlist
extern PlayList &GetCurrentPlayList( );

// Provide access to a selection of frames
class SelectedFrames
{
	public:
		virtual ~SelectedFrames( ) { }
		virtual int GetNumInputFrames( ) = 0;
		virtual int GetNumOutputFrames( ) = 0;
		virtual double GetPosition( int index ) = 0;
		virtual double GetFrameDelta( ) = 0;
		virtual bool IsEffectReversed( ) = 0;
		virtual double GetRealStart( ) = 0;
		virtual double GetRealEnd( ) = 0;
		virtual void GetImageA( double position, uint8_t *image, int width = 0, int height = 0 ) = 0;
		virtual void GetImageB( double position, uint8_t *image, int width = 0, int height = 0 ) = 0;
		virtual void GetAudioA( double position, int16_t **audio, short int &channels, int &frequency, int &samples ) = 0;
		virtual void GetAudioB( double position, int16_t **audio, short int &channels, int &frequency, int &samples ) = 0;
		virtual void Repaint( ) = 0;
		virtual bool IsRepainting() = 0;
		virtual int GetIndex( double position ) = 0;
		virtual bool IsPreviewing() = 0;
};

// Get the selected frames for FX
extern SelectedFrames &GetSelectedFramesForFX( );
extern GtkWindow* GetKinoWidgetWindow( );
extern void Repaint( );

class SelectionNotification
{
	public:
		virtual ~SelectionNotification( ) { }
		virtual void OnSelectionChange( ) = 0;
};

/** Interface for receiving callbacks from the KeyFrame Controller.
*/

class KeyFrameControllerClient
{
	public:
		virtual ~KeyFrameControllerClient() { }
		// Called when the key button is changed to define/undefine a key frame
		virtual void OnControllerKeyChanged( double position, bool editable ) { } 
		// Called when the previous button is pressed
		virtual void OnControllerPrevKey( double position ) { }
		// Called when the next button is pressed
		virtual void OnControllerNextKey( double position ) { }
};

/** Enumerated type for classifying the current frame, being either a computed frame, a key or
	a locked/non-removable key.
*/

enum frame_type { FRAME = 0, KEY = 1, LOCKED_KEY = 2 };

/** Key frame controller is a GUI widget which provides a simple key frame definition/editing tool.
 
	This is currently represented by 4 components - a slide bar to select the position, a toggle 
	button which allows you to specify whether a key exists at the current position, and two buttons
	to allow navigation between the key frames. 

	Intended use is for a container to implement the controller client.
*/

class KeyFrameController
{
	public:
		virtual ~KeyFrameController() { }
		// Set the current feedback 
		virtual void ShowCurrentStatus( double position, frame_type type, bool hasPrev, bool hasNext ) = 0;
		// Get the current position
		virtual double GetCurrentPosition( ) = 0;
};

/** Factory method for the key frame controller.
*/

extern KeyFrameController *GetKeyFrameController( KeyFrameControllerClient *client );


#endif
