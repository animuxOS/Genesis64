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
 *  File: VertexVector.h
 *  Project: MakeHuman <info@makehuman.org>, http://www.makehuman.org/
 *  Library: ANIMORPH
 *
 *  For individual developers look into the AUTHORS file.
 *
 */

#ifndef VERTEXVECTOR_H
#define VERTEXVECTOR_H 1

#ifdef HAVE_CONFIG_H
  #include <config.h>
#endif

#include <iostream>
#include <fstream>
#include <libgen3d/Vertex.h>
#include <libgen3d/Face.h>
#include "FaceVector.h"
#include "FileReader.h"

namespace Animorph {

/*! \brief Loadable vector of Vertices.

The format of Vertices file:
\verbatim
<float>,<float>,<float>
...
\endverbatim
*/
class VertexVector : public std::vector <Gen3D::Vertex>
{
private:
  void fromStream (std::ifstream &in_stream);


public:
  bool load (const std::string& filename);

  int setCoordinates (std::vector <Gen3D::Vector3f> &vertexvector);
};

/*Subdivision surfaces */

class subdVertexVector : public std::vector <Gen3D::subdVertex>
{
private:
  void fromStream (std::ifstream &in_stream);


public:
  bool load (const std::string& filename);
  void loadFromFaceVector (FaceVector &facevector);
  void updateFacePoints (VertexVector &vertexvector);
  void updateEdgePoints (VertexVector &vertexvector, subdVertexVector &facePoints);
};


class origVertexVector : public std::vector <Gen3D::origVertex>
{
private:
  void fromStream (std::ifstream &in_stream);


public:
  bool load (const std::string& filename);
  void updateOrigVertexPoints (VertexVector &vertexvector, subdVertexVector &facePoints,  subdVertexVector &edgePoints);
};

}

#endif	// VERTEXVECTOR_H
