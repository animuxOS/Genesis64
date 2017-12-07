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
 *  File: Material.h
 *  Project: MakeHuman <info@makehuman.org>, http://www.makehuman.org/
 *  Library: libgen3d
 *
 *  For individual developers look into the AUTHORS file.
 *
 */

#ifndef MATERIAL_H
#define MATERIAL_H 1

#ifdef HAVE_CONFIG_H
  #include <config.h>
#endif

#include <vector>
#include <string>
#include <iostream>
#include "Color.h"

using std::string;
namespace Gen3D {

/*! \brief Represents a material by its name, surface colour and edge colour
*/
class Material
{
private:
  Color  rgbCol;
  Color  edgeCol;
  string name;

public:

   Material() : rgbCol(), edgeCol(), name() {}
  ~Material() {}
  /*!
   * \return rgbCol the RGB Color values from this Material
   */
  const Color &getRGBCol () const {return rgbCol;}

  /*!
   * \return edgeCol the RGB edge color values from this Material
   */
  const Color &getEdgeCol () const {return edgeCol;}

  /*!
   * \param rgbCol set the RGB Color values for this Material
   */
  void setRGBCol (const Color &rgbCol) {this->rgbCol = rgbCol;}

  /*!
   * \param edgeCol set the RGB edge color values for this Material
   */
  void setEdgeCol (const Color &edgeCol) {this->edgeCol = edgeCol;}

  /*!
   * \return name the name of this Material
   */
  const string &getName () const {return name;}

  /*!
   * \param name set the name the name for this Material
   */
  void setName (const std::string &name) {this->name = name;}

};

}

#endif // MATERIAL_H
