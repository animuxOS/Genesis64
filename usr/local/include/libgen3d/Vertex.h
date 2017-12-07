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
 *  File: Vertex.h
 *  Project: MakeHuman <info@makehuman.org>, http://www.makehuman.org/
 *  Library: libgen3d
 *
 *  For individual developers look into the AUTHORS file.
 *
 */

#ifndef VERTEX_H
#define VERTEX_H 1

#ifdef HAVE_CONFIG_H
  #include <config.h>
#endif

#include <vector>
#include <cmath>
#include <string>
#include "Vector3.h"
#include "Color.h"

namespace Gen3D {

/*! \brief Represents a vertex by its coordinates and a normal vector.
 */
class Vertex
{
protected:
  std::vector <int> shared_faces_vector;

public:
  /// vertex coordinate
  Vector3f co;

  /// vertex normal
  Vector3f no;

  // vertex color
  //Color color;

  Vertex () : co(), no() {co.zero (); no.zero ();}

  /// construct Vertex with coordinates
  /*!
   * \param x the x component to the vertex coordinate
   * \param y the y component to the vertex coordinate
   * \param z the z component to the vertex coordinate
   */
  Vertex (float x, float y, float z)
  : co(x,y,z), no()
  {
    no.zero ();
  }

  /*!
   * \param shared_face add the index number to which face this Vertex belongs
   */
  void addSharedFace (int shared_face);

  /*!
   * \return get a vector with all faces this Vertex belongs to
   */
  std::vector <int> &getSharedFaces ();
};

/*Subdivision surfaces */

class subdVertex : public Vertex
{
private:
  ///Vertices from which this one is generated
  int vertices[4];
  int size;

public:
  ///construct Vertex from a quad
  subdVertex (int v0, int v1, int v2, int v3);
  
  ///construct Vertex from a tri
  subdVertex (int v0, int v1, int v2);
  
    int getVertexAtIndex(int inIndex) const
    {   assert(inIndex<size);
        return vertices[inIndex];}
    
    int getSize() {return size;}
};


class origVertex : public Vertex
{
private:
  ///Vertices from which this one is generated
  int valence, fvalence;
  std::vector <int> faceVerts;
  std::vector <int> edgeVerts;


public:
  ///construct origVertex
  origVertex (std::vector <int> &i_faceVerts, std::vector <int> &i_edgeVerts);
  
  int getFaceVertexAtIndex (int inIndex) const
    {   return faceVerts[inIndex];}
  
  int getEdgeVertexAtIndex (int inIndex) const
    {   return edgeVerts[inIndex];}
  
  int getValence() {return valence;}
  int getFValence() {return fvalence;}

};

}

#endif	// VERTEX_H
