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
 *  File   : Image.h
 *  Project: MakeHuman <info@makehuman.org>, http://www.makehuman.org/
 *  Library: MHGUI
 *
 *  For individual developers look into the AUTHORS file.
 *
 */

#ifndef IMAGE_H
#define IMAGE_H 1

#ifdef HAVE_CONFIG_H
  #include <config.h>
#endif

#include <string>
#include <libgen3d/Color.h>
#include "Widget.h"
#include "Panel.h"
#include "Texture.h"

using Gen3D::Color;

using std::string;

namespace mhgui {

class Tooltip;
class ImageSysListener;

/** \brief Image widget
 *
 * The images that will be displayed are kept in the member variables of
 * the class Texture.
 */
/* ========================================================================== */
class Image : public Widget
{
  //Textures
private:
  string            imageFilename;

  string            imageFilenameOver;

  string            imageFilenameDisabled;
  Texture           textureDisabled;
  Texture           texture;
  Texture           textureOver;

  bool              textureIsInited; // used by lazyLoadTexture
  bool              textureOverIsInited;
  bool              textureDisabledIsInited;

  ImageSysListener *imageSysListener;
  float             alpha;
  Color overlay;
  bool overlayEffect;

  bool enabled;
  bool kill_mouse_drag;
  // intentionally not implemented
  Image           (const Image&);
  Image& operator=(const Image&);

public:
  Image (uint32_t inId, const string& inFilename, const Rect& inGeometry);
  virtual ~Image();

  void  setAlpha (float);
  float getAlpha() const {return alpha;}

  void setEnabled(bool inEnabled) {enabled = inEnabled;}
  bool isEnabled() {return enabled;}

  void setKillMouseDrag(bool kill){kill_mouse_drag = kill;}
  /*!
   * Set the Color for the overlay rectangle. The overlay is enabled at this time.
   * @param c The color for the overlay. Transparency is set by the alpha component.
   */
  void setOverlayRectangle (const Color& c);
  void setOverlayRectangle (bool overlayEffect);

  void setOverlayTexture(const string& inFilename);
  void setDisabledTexture(const string& inFilename);

  const Texture& getTextures (); //return the textureID
  const Texture& getTexturesOver (); //return the textureID

  virtual void show ();
  virtual void hide ();
  virtual void draw ();
  virtual void drawOverlay ();

  bool isMouseDragged (const Point& inMousePos);
  bool isMouseClick (const Point& inMousePos, int button, int state);

protected:
  bool lazyLoadTexture (bool over = false);
};

} // namespace mhgui

#endif //IMAGE_H
