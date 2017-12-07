/*
 * image_transitions.h -- RGB24 image transitions
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

#ifndef _IMAGE_TRANSITIONS_H_
#define _IMAGE_TRANSITIONS_H_

// C++ Includes

#include <vector>
using std::vector;

// C Includes

#include <stdint.h>
#include <gtk/gtk.h>

/** Public interface for all image transition classes.

	This contains 2 methods:

	- GetDescription simply returns a GUI usable identifier for the implementing class
	- GetFrame receives 2 RGB24 images, the width, height and a positional indicator. It
	  then carries out some operations on the two and returns the output in the first.
*/

class ImageTransition 
{
	public:
		virtual ~ImageTransition() {}
		virtual char *GetDescription( ) const = 0;
		virtual void GetFrame( uint8_t *io, uint8_t *mesh, int width, int height, double position, double frame_delta, bool reverse ) = 0;
		virtual bool IsUsable( ) { return true; }
};

/** Public abstract class for image transitions with additional GUI inputs and feedback.
 
	This allows a transition to attach and interpret any additional widgets in the container 
	provided. 

	The activation of the AttachWidget and DetachWidgets is handled automatically by the 
	repository on the detection of a selection change.

	InterpretWidgets must be called (by the repository owner) before the first call to 
	GetFrame.

	If an implementation doesn't attach any widgets, the default implementation is enough
	(though the adapter will give you that anyway).
*/

class GDKImageTransition : public ImageTransition
{
	public:
		virtual ~GDKImageTransition() {}
		virtual void AttachWidgets( GtkBin *bin ) { }
		virtual void DetachWidgets( GtkBin *bin ) { }
		virtual void InterpretWidgets( GtkBin *bin ) { }
};

/** Public ImageTransition to GDKImageTransition adapter.
 
	Since not all transitions will require additional GUI functionality, this class is provided
	as a convenience to wrap the non-GDK transitions into basic GDK transitions.
*/

class GDKImageTransitionAdapter : public GDKImageTransition
{
	private:
		ImageTransition *transition;

	public:
		GDKImageTransitionAdapter( ImageTransition *transition ) { this->transition = transition; }
		virtual ~GDKImageTransitionAdapter( ) { delete transition; }
		char *GetDescription( ) const { return this->transition->GetDescription( ); }
		void GetFrame( uint8_t *io, uint8_t *mesh, int width, int height, double position, double frame_delta, bool reverse ) 
		{ 
			return this->transition->GetFrame( io, mesh, width, height, position, frame_delta, reverse ); 
		}
};

/** Public class for exposing each of the registered transitions through a selectable GUI
 	component (in this case, only an OptionMenu is provided).

	Transitions are currently registered in the repositories constructor and added to the
	OptionMenu provided via the Initialise function. 

	Additional transitions can be registered before an Initialise call (using the Register
	method), and Initialise can be called many times if necessary.
*/

class GDKImageTransitionRepository
{
	private:
		vector <GDKImageTransition *> transitions;
		GDKImageTransition *selected_transition;
		GtkOptionMenu *menu;
		GtkBin *container;

	public:
		GDKImageTransitionRepository();
		~GDKImageTransitionRepository();
		void Register( GDKImageTransition *transition );
		void Initialise( GtkOptionMenu *menu, GtkBin *container );
		GDKImageTransition *Get( ) const;
		void SelectionChange( );
};

#endif
