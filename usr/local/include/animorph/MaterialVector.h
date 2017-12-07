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
 *  Library: ANIMORPH
 *
 *  For individual developers look into the AUTHORS file.
 *
 */

#ifndef MATERIALVECTOR_H
#define MATERIALVECTOR_H 1

#ifdef HAVE_CONFIG_H
  #include <config.h>
#endif

#include <vector>
#include <string>
#include <iostream>
#include <libgen3d/Color.h>
#include <libgen3d/Material.h>
#include "FileReader.h"

using std::string;
namespace Animorph {

/*! \brief A loadable vector of materials

The format of Material file:
\verbatim
<string>,<float>,<float>,<float>
...
\endverbatim
*/
class MaterialVector : public std::vector <Gen3D::Material>
{
private:
  void fromStream (std::ifstream &in_stream);

public:
  /// load a Material file
  /*!
   * \param filename the file with Material data to load
   * \return true if file is found
   * \return false if file isn't found
   */
  bool loadMaterials (const std::string& filename);

};

}

#endif // MATERIALVECTOR_H
