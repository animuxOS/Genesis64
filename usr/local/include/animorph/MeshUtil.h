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
 *  File: MeshUtil.h
 *  Project: MakeHuman <info@makehuman.org>, http://www.makehuman.org/
 *  Library: ANIMORPH
 *
 *  For individual developers look into the AUTHORS file.
 *
 */

#ifndef MESHUTIL_H
#define MESHUTIL_H 1

#ifdef HAVE_CONFIG_H
  #include <config.h>
#endif

#include <cstdlib>
#include <string>
#include <sstream>
#include <iomanip>
#include <vector>
#include <iostream>
#include "VertexVector.h"

namespace Animorph {

/*! \brief Returns the location of the center of gravity
 * \param vertexNumbers a vector of indices into vertexvector
 * \param vertexvector a vector of vertices, from which only the ones indicated by vertexNumbers are used
 * \return location of the center of gravity
 */
Gen3D::Vector3f calcCenteroid(const std::vector<int>& vertexNumbers, const VertexVector& vertexvector);

Gen3D::Vector3f calcAverageNormalLength(const std::vector<int> vertexNumbers, const VertexVector& vertexvector);

} // end namespace


#endif	// MESHUTIL_H
