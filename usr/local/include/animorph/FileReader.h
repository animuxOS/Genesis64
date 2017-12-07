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
 *  File: FileReader.h
 *  Project: MakeHuman <info@makehuman.org>, http://www.makehuman.org/
 *  Library: ANIMORPH
 *
 *  For individual developers look into the AUTHORS file.
 *
 */

#ifndef FILEREADER_H
#define FILEREADER_H 1

#ifdef HAVE_CONFIG_H
  #include <config.h>
#endif

#include <sstream>
#include <iostream>
#include <fstream>

/// define the maximum length of an input line
#define MAX_LINE_BUFFER 1024

namespace Animorph {

/*! \brief Wrapper for ifstream using C locale
 */
class FileReader : public std::ifstream
{
private:
  char *locale;

// Intentionally declared as private because not implemented yet
private:
   FileReader           (const FileReader&);
   FileReader& operator=(const FileReader&);

public:
  FileReader () : locale (NULL) {}

  /// destructor closes the file
  virtual ~FileReader () {close ();}

  /*!
  * \param filename the file to open for reading
  * \return 0 if the file could be opened.
  */
  virtual int open (const std::string& filename);

  /// closes the currently opened file
  virtual void close ();

};

}

#endif // FILEREADER_H
