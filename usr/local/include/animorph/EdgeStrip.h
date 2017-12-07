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
 *  File: EdgeStrip.h
 *  Project: MakeHuman <info@makehuman.org>, http://www.makehuman.org/
 *  Library: ANIMORPH
 *
 *  For individual developers look into the AUTHORS file.
 *
 */

#ifndef EDGESTRIP_H
#define EDGESTRIP_H 1

#ifdef HAVE_CONFIG_H
  #include <config.h>
#endif

#include <vector>
#include <iostream>
#include <fstream>
#include "FileReader.h"

#define MAX_LINE 350000

namespace Animorph {

typedef std::vector <int> StripData;

/*! \brief A vector of ints, loadable from a file

The format of EdgeStrips files:

\verbatim
<int>,<int>,<int>,...
...
\endverbatim

*/
class EdgeStrip : public std::vector <StripData>
{
private:
  void fromStream (std::ifstream &in_stream);

public:
  /// Load the Strip data from a file
  /*!
   * \param filename the file to load
   * \return true if file is found
   * \return false if file isn't found
   */
  bool load (const std::string& filename);
};

}

#endif	// EDGESTRIP_H
