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
 *  File   : Camera.h
 *  Project: MakeHuman <info@makehuman.org>, http://www.makehuman.org/
 *  Library: MHGUI
 *
 *  For individual developers look into the AUTHORS file.
 *
 */

#ifndef CAMERA_H
#define CAMERA_H 1

#ifdef HAVE_CONFIG_H
  #include <config.h>
#endif

#include <cmath>
#include <map>
#include <libgen3d/Matrix.h>
#include <libgen3d/Vector2.h>
#include <libgen3d/Vector3.h>
#include <animorph/FileWriter.h>
#include <animorph/util.h>
#include <animorph/VertexVector.h>
#include "GLUTWrapper.h"

using Gen3D::Matrix;
using Gen3D::Vector2f;
using Gen3D::Vector3f;
using Animorph::VertexVector;

namespace mhgui {

typedef std::vector <int> Reference_Verts;

struct AutozoomData
{
	Vector3f pos_camera;
	Vector2f xyRot_camera;
	Reference_Verts vertsIndexes;
	Vector3f vertsCenteroid;
};

// TODO: moving world vs. moving camera problem
/*! \brief Stores camera data.
 */
class Camera
{
private:
  Vector2f last_mouse_pos;
  Vector3f last_pos_camera;
  int width;
  int height;
  float angle;
  Vector3f axis ;

  Matrix cam_pos;
  Matrix cam_center;

  bool mode;

  // Ugly Test code following - just for test purposes!
  Vector3f  mCameraPos;
  float     mAngleX;
  float     mAngleY;
  float     mAngleZ;
  Vector3f startVector;
  Vector3f endVector;
  float startAngleX;
  float endAngleX;
  float startAngleY;
  float endAngleY;
  float timeForMorph;
  int   step;

public:
  /// construct a Camera that manages the world Matrix
  Camera ();
  Camera (const Camera& inRHS);
  Camera& operator=(const Camera& inRHS);

  void reshape (int width, int height);
  void rotate (float theta, Gen3D::Matrix::RotateAxis axis);
  void mouseRotateStart (int x, int y);
  void rotateMouse (int x, int y);
  void moveMouse (int x, int y);
  void move (float x, float y, float z);
  void resetRotation();
  void resetPosition();

  void applyMatrix ();

  const Vector3f& getPosition() const {return mCameraPos;}
  float           getAngleX()    const {return mAngleX;}
  float           getAngleY()    const {return mAngleY;}
  float           getAngleZ()    const {return mAngleZ;}
  bool 		  isPerspective() const {return mode;}
  void setPerspective (bool m);

  int   	steps();
  float 	getYForX(float x);
  void 		calcForStepAnimate(float inX);
  bool 	timerTrigger();

  void 		moveCameraAnimated(const std::string& filename, AutozoomData data,const VertexVector &vertexvector);
};

class Autozoom : public std::map <std::string, AutozoomData>
{
private:
	void fromStream (std::ifstream &in_stream,const std::string& filename);
	void createStream (std::ostringstream &out_stream,const std::string& filename,const Camera &camera);
public:
	bool lazyLoadData (const std::string& filename);
	bool save (const std::string& filename,const Camera &camera);
	AutozoomData getAutozoomData (const std::string& filename);

};

} // namespace mhgui
#endif // CAMERA_H
