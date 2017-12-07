/*
 *  Copyright (C) 2005  Andreas Volz
 *  Copyright (C) 2006-2007  MakeHuman Project
 *
 *  This program is free software; you  can  redistribute  it  and/or
 *  modify  it  under  the terms of the GNU General Public License as
 *  published by the Free Software Foundation; either  version  3  of
 *  the License, or (at your option) any later version.
 *
 *  This  program  is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the  implied  warranty  of
 *  MERCHANTABILITY  or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
 *  General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program; if not, write to the Free Software Foun-
 *  dation, Inc., 59 Temple Place, Suite 330, Boston,  MA  02111-1307
 *  USA
 *
 *  File: Euler.h
 *  Project: MakeHuman <info@makehuman.org>, http://www.makehuman.org/
 *  Library: libgen3d
 *
 *  For individual developers look into the AUTHORS file.
 *
 */

#ifndef EULER_H
#define EULER_H 1

#ifdef HAVE_CONFIG_H
  #include <config.h>
#endif

#include "Vector3.h"

namespace Gen3D {

/*! \brief Represents an Euler notation (3D rotation angles).
 */
class Euler : public Vector3f
{
public:
  enum Notation
  {
    XYZ
  };

private:
  Notation n;

public:
  /// constructor for Euler with all components 0.
  Euler (Notation n) : Vector3f (0,0,0), n(XYZ) {}

  /// constructor for Euler with tree components and Notation (in PI)
  /*!
   * \param x The rotation about the X-Axis (in PI).
   * \param y The rotation about the Y-Axis (in PI).
   * \param z The rotation about the Z-Axis (in PI).
   * \param n A Notation for this three rotations.
   */
  Euler (float x, float y, float z, Notation n) : Vector3f (x, y, z), n (n) {}

  /*!
   * \return The Notation of this Euler angle.
   */
  Notation getNotation () {return n;}
};

}

#endif  // EULER_H
