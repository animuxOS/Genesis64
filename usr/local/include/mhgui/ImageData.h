/*
 *  Copyright (C) 2005-2007  MakeHuman Project
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
 *  File   : ImageData.h
 *  Project: MakeHuman <info@makehuman.org>, http://www.makehuman.org/
 *  Library: MHGUI
 *
 *  For individual developers look into the AUTHORS file.
 *
 */

#ifndef IMAGEDATA_H
#define IMAGEDATA_H 1

#ifdef HAVE_CONFIG_H
  #include <config.h>
#endif

#include <string>
#include <stdlib.h>
#include <stdint.h>

#include "Texture.h"

#ifndef __APPLE__
    #define USE_PNGLIB
#else
    /* On OS X: Decide: Use pnglib or coregraphics
     * The following define uses the pnglib but you must make sure that this lib
     * is installed on your Mac! It is not when you are using OS-X "out of the box!"
     * So, better leave this commented out! ;-) */

//    #define USE_PNGLIB
#endif


#if defined(USE_PNGLIB)
  #include <png.h>
#endif

using std::string;

namespace mhgui {

struct buffer_color_rgba_t {uint8_t r,g,b,a;};
struct buffer_color_rgb_t  {uint8_t r,g,b;};

/// Represents a PNG image loaded into memory
class ImageData
{
  friend class Texture;
private:
  char         *image_data; /* raw png image data */
  char         *end_bufferPtr;
  unsigned long width, height;
  unsigned int  bytesPerRow;
  bool          alpha;

// Intionally declared as private because not implemented (yet)
private:
   ImageData(const ImageData&);
   ImageData& operator=(const ImageData&);

private:
   ImageData ();
  ~ImageData ();

  bool pngLoad             (const string& filename);

  unsigned long getWidth  () const;
  unsigned long getHeight () const;
  unsigned int  getBytesPerRow() const {return bytesPerRow;}
  bool          hasAlpha  () const;
  const void*   getData   () const;

private:
    #if defined(USE_PNGLIB)
        bool pngLoadPNGLib(const string& filename);
    #elif defined(__APPLE__) && defined(__MACH__)
        bool pngLoadOSX(const string& filename);
    #endif
};

} // namespace mhgui

#endif //IMAGEDATA_H
