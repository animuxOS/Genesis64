/*
 * time_map.h -- Time Mapping Interfaces and Templates
 * Copyright (C) 2002 Charles Yates <charles.yates@pandora.be>
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

#ifndef _TIME_MAP_H
#define _TIME_MAP_H

#include <iostream>
#include <stdint.h>
#include <math.h>

/** A time entry is defined by its location in the time line (a double
	from 0 to 1) and its editable status (keys are editable).

	An implementation of a time entry extends this template:

	class SomeEntry : public TimeEntry< SomeEntry >
	{
		public:
			int value;

			SomeEntry *Get( double position, SomeEntry *ante )
			{
				... generate a new entry which is between this and ante ...
			}
	}
*/

template < typename Entry > class TimeEntry
{
	private:
		double position;
		bool is_editable;

	public:
		virtual ~TimeEntry() { }
		// Get the position of this entry
		double GetPosition( ) { return position; }
		// Is it a key field?
		bool IsEditable( ) { return is_editable; }
		// Set the position of this entry
		void SetPosition( double m_position ) { position = m_position; }
		// Set its key status
		void SetEditable( bool m_is_editable ) { is_editable = m_is_editable; }
		// This method is used to generate the virtual/computed entries
		virtual Entry *Get( double position, Entry *ante ) = 0;
};

// Seems silly to extend the single, pair and triple entities - so 3 specific classes are provided

class TimeMapValue : public TimeEntry< TimeMapValue >
{
	protected:
		double value;

	public:
		virtual ~TimeMapValue() { }
		TimeMapValue( ) : value(0) { SetPosition( 0 ); SetEditable( false ); }
		TimeMapValue( double position ) : value(0) { SetPosition( position ); SetEditable( false ); }
		TimeMapValue( double position, TimeMapValue *entry ) { SetPosition( position ); SetEditable( false ); this->value = entry->value; }
		void SetValue( double value ) { this->value = value; }
		double GetValue( ) { return value; }
		TimeMapValue *Get( double position, TimeMapValue *ante ) 
		{
			TimeMapValue *entry = new TimeMapValue();
			double r = ( position - GetPosition( ) ) / ( ante->GetPosition() - GetPosition( ) );
			entry->SetValue( value + ( ante->GetValue() - value ) * r );
			return entry;
		}
};

class TimeMapPair : public TimeEntry< TimeMapPair >
{
	protected:
		double first;
		double second;

	public:
		virtual ~TimeMapPair() { }
		TimeMapPair( ) : first(0), second(0) { SetPosition( 0 ); SetEditable( false ); }
		TimeMapPair( double position ) : first(0), second(0) { SetPosition( position ); SetEditable( false ); }
		TimeMapPair( double position, TimeMapPair *entry ) 
		{ 
			SetPosition( position ); 
			SetEditable( false ); 
			this->first = entry->first; 
			this->second = entry->second;
		}
		void SetFirst( double first ) { this->first = first; }
		void SetSecond( double second ) { this->second = second; }
		double GetFirst( ) { return first; }
		double GetSecond( ) { return second; }
		TimeMapPair *Get( double position, TimeMapPair *ante ) 
		{
			TimeMapPair *entry = new TimeMapPair();
			double r = ( position - GetPosition( ) ) / ( ante->GetPosition() - GetPosition( ) );
			entry->SetFirst( first + ( ante->GetFirst() - first ) * r );
			entry->SetSecond( second + ( ante->GetSecond() - second ) * r );
			return entry;
		}
};

class TimeMapTriple : public TimeEntry< TimeMapTriple >
{
	protected:
		double first;
		double second;
		double third;

	public:
		virtual ~TimeMapTriple() { }
		TimeMapTriple( ) : first(0), second(0), third(0) { SetPosition( 0 ); SetEditable( false ); }
		TimeMapTriple( double position ) : first(0), second(0), third(0) { SetPosition( position ); SetEditable( false ); }
		TimeMapTriple( double position, TimeMapTriple *entry ) 
		{ 
			SetPosition( position ); 
			SetEditable( false ); 
			this->first = entry->first; 
			this->second = entry->second;
			this->third = entry->third;
		}
		void SetFirst( double first ) { this->first = first; }
		void SetSecond( double second ) { this->second = second; }
		void SetThird( double third ) { this->third = third; }
		double GetFirst( ) { return first; }
		double GetSecond( ) { return second; }
		double GetThird( ) { return third; }
		TimeMapTriple *Get( double position, TimeMapTriple *ante ) 
		{
			TimeMapTriple *entry = new TimeMapTriple();
			double r = ( position - GetPosition( ) ) / ( ante->GetPosition() - GetPosition( ) );
			entry->SetFirst( first + ( ante->GetFirst() - first ) * r );
			entry->SetSecond( second + ( ante->GetSecond() - second ) * r );
			entry->SetThird( third + ( ante->GetThird() - third ) * r );
			return entry;
		}
};


/** A filter time entry provides an additional two methods to render the preview and
	final images.
*/

template < typename Entry > class FilterTimeEntry : public TimeEntry< Entry >
{
	public:
		virtual ~FilterTimeEntry() { }
		// Called when the final image is being rendered
		virtual void RenderFinal( uint8_t *image, int width, int height ) = 0;
};

/** A transition time entry provides an additional two methods to render the preview and
	final images.
*/

template < typename Entry > class TransitionTimeEntry : public TimeEntry< Entry >
{
	public:
		virtual ~TransitionTimeEntry() { }
		// Called when the final image is being rendered
		virtual void RenderFinal( uint8_t *out, uint8_t *in, int width, int height ) = 0;
};

/** A time map provides a means of addressing time entries consistently over the 0 to 1
	time range for which its defined.
*/

template < typename Entry > class TimeMap 
{
	private:
		map < double, Entry * > key_frames;

	public:
		virtual ~TimeMap() { }

		void Clear( )
		{
			key_frames.erase( key_frames.begin( ), key_frames.end( ) );
		}

		void FinishedWith( Entry *entry )
		{
			if ( !entry->IsEditable( ) )
				delete entry;
		}

		bool RoughlyEquals( double x, double y )
		{
			return x == y;
		}

		Entry *Get( double position )
		{
			Entry *current = NULL;
			position = (double)( rint( position * 1000000 ) / 1000000 );

			if ( key_frames.size() == 0 )
			{
				current = new Entry();
				current->SetPosition( position );
				current->SetEditable( false );
			}
			else if ( key_frames.size() == 1 )
			{
				double first_key = GetFirst( );
				Entry *ante = key_frames[ first_key ];

				if ( position != first_key )
					current = new Entry( position, *ante );
				else
					current = ante;
			}
			else 
			{
				double post_key = GetNext( position );
				double ante_key = GetPrevious( position );
				bool frame_key = IsKeyFrame( position );

				if ( frame_key )
				{
					current = key_frames[ position ];
				}
				else
				{
					Entry *ante = key_frames[ ante_key ];

					// We may now be at the end of the map
					if ( post_key == ante_key )
					{
						current = new Entry( position, *ante );
					}
					else
					{
						Entry *post = key_frames[ post_key ];
						current = ante->Get( position, post );
					}
				}
			}

			return current;
		}

		Entry *SetEditable( double position, bool editable )
		{
			Entry *entry = Get( position );
			position = (double)( rint( position * 1000000 ) / 1000000 );

			if ( entry->IsEditable() != editable )
			{
				if ( entry->IsEditable() )
					key_frames.erase( position );
				else
					key_frames[ position ] = entry;
				entry->SetEditable( editable );
			}

			FinishedWith( entry );

			return Get( position );
		}

		Entry *GotoNextKey( double position )
		{
			return Get( GetNext( position + 0.000001 ) );
		}

		Entry *GotoPreviousKey( double position )
		{
			return Get( GetPrevious( position - 0.000001 ) );
		}

		double GetFirst( )
		{
			typename map< double, Entry * >::iterator it = key_frames.begin();
			if ( it == key_frames.end() )
				return 0;
			else
				return it->first;
		}

		double GetLast( )
		{
			typename map< double, Entry * >::iterator it = key_frames.end();
			if ( key_frames.size() == 0 )
				return 0;
			else
				return ( -- it )->first;
		}

		double GetNext( double position )
		{
			double ret_val = 0;
			if ( key_frames.size() >= 1 )
			{
				typename map< double, Entry * >::iterator it = key_frames.begin();
				for ( ; ret_val <= position && it != key_frames.end(); it ++ )
					ret_val = it->first;
/*				if ( it != key_frames.end() )
				{
					++it;
					ret_val = it->first;
				}*/
			}
			return ret_val;
		}

		double GetPrevious( double position )
		{
			double ret_val = 0;
			if ( key_frames.size() >= 1 )
			{
				typename map< double, Entry * >::iterator it = key_frames.begin();
				for ( ; it != key_frames.end() && it->first < position; it ++ )
					ret_val = it->first;
/*				if ( it != key_frames.begin() )
				{
					--it;
					ret_val = it->first;
				}*/
			}
			return ret_val;
		}

		bool IsKeyFrame( double position )
		{
			if ( key_frames.size() >= 1 )
			{
				typename map< double, Entry * >::iterator it = key_frames.begin();
				for ( ; it != key_frames.end() && it->first <= position; it ++ )
				{
					if ( position == it->first )
						return true;
				}
			}
			return false;
		}

		void Invert( ) 
		{
			map < double, Entry * > temp_frames;
			if ( key_frames.size() >= 1 )
			{
				typename map< double, Entry * >::iterator it = key_frames.begin();
				for ( ; it != key_frames.end(); it ++ )
				{
					it->second->SetPosition( 0.999999 - it->first );
					temp_frames[ 0.999999 - it->first ] = it->second;
				}
			}

			key_frames = temp_frames;
		}
};

#endif
