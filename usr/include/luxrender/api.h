/***************************************************************************
 *   Copyright (C) 1998-2008 by authors (see AUTHORS.txt )                 *
 *                                                                         *
 *   This file is part of LuxRender.                                       *
 *                                                                         *
 *   Lux Renderer is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 3 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 *   Lux Renderer is distributed in the hope that it will be useful,       *
 *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
 *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
 *   GNU General Public License for more details.                          *
 *                                                                         *
 *   You should have received a copy of the GNU General Public License     *
 *   along with this program.  If not, see <http://www.gnu.org/licenses/>. *
 *                                                                         *
 *   This project is based on PBRT ; see http://www.pbrt.org               *
 *   Lux Renderer website : http://www.luxrender.net                       *
 ***************************************************************************/

#ifndef LUX_API_H
#define LUX_API_H 1

#ifdef __cplusplus
extern "C" {
#endif

typedef char *LuxToken;
typedef char *LuxPointer;
#define LUX_NULL NULL

/* Basic control flow, scoping, stacks */
void luxIdentity();
void luxTranslate(float dx, float dy, float dz);
void luxRotate(float angle, float ax, float ay, float az);
void luxScale(float sx, float sy, float sz);
void luxLookAt(float ex, float ey, float ez, float lx, float ly, float lz, float ux, float uy, float uz);
void luxConcatTransform(float transform[16]);
void luxTransform(float transform[16]);
void luxCoordinateSystem(const char *);
void luxCoordSysTransform(const char *);
void luxPixelFilter(const char *name, ...);
void luxPixelFilterV(const char *name, int n, LuxToken tokens[], LuxPointer params[]);
void luxFilm(const char *name, ...);
void luxFilmV(const char *name, int n, LuxToken tokens[], LuxPointer params[]);
void luxSampler(const char *name, ...); 
void luxSamplerV(const char *name, int n, LuxToken tokens[], LuxPointer params[]);
void luxAccelerator(const char *name, ...);
void luxAcceleratorV(const char *name, int n, LuxToken tokens[], LuxPointer params[]);
void luxSurfaceIntegrator(const char *name, ...);
void luxSurfaceIntegratorV(const char *name, int n, LuxToken tokens[], LuxPointer params[]);
void luxVolumeIntegrator(const char *name, ...);
void luxVolumeIntegratorV(const char *name, int n, LuxToken tokens[], LuxPointer params[]);
void luxCamera(const char *name, ...);
void luxCameraV(const char *name, int n, LuxToken tokens[], LuxPointer params[]);
void luxWorldBegin();
void luxAttributeBegin();
void luxAttributeEnd();
void luxTransformBegin();
void luxTransformEnd();
void luxTexture(const char *name, const char *type, const char *texname, ...);
void luxTextureV(const char *name, const char *type, const char *texname, int n, LuxToken tokens[], LuxPointer params[]);
void luxMaterial(const char *name, ...);
void luxMaterialV(const char *name, int n, LuxToken tokens[], LuxPointer params[]);
void luxMakeNamedMaterial(const char *name, ...);
void luxMakeNamedMaterialV(const char *name, int n, LuxToken tokens[], LuxPointer params[]);
void luxNamedMaterial(const char *name, ...);
void luxNamedMaterialV(const char *name, int n, LuxToken tokens[], LuxPointer params[]);
void luxLightSource(const char *name, ...);
void luxLightSourceV(const char *name, int n, LuxToken tokens[], LuxPointer params[]);
void luxAreaLightSource(const char *name, ...);
void luxAreaLightSourceV(const char *name, int n, LuxToken tokens[], LuxPointer params[]);
void luxPortalShape(const char *name, ...);
void luxPortalShapeV(const char *name, int n, LuxToken tokens[], LuxPointer params[]);
void luxShape(const char *name, ...);
void luxShapeV(const char *name, int n, LuxToken tokens[], LuxPointer params[]);
void luxReverseOrientation();
void luxVolume(const char *name, ...);
void luxVolumeV(const char *name, int n, LuxToken tokens[], LuxPointer params[]);
void luxObjectBegin(const char *name);
void luxObjectEnd();
void luxObjectInstance(const char *name);
void luxWorldEnd();

/* User interactive thread functions */
void luxStart();
void luxPause();
void luxExit();

/* Controlling number of threads */
int luxAddThread();
void luxRemoveThread();

/* Framebuffer access */
void luxUpdateFramebuffer();
unsigned char* luxFramebuffer();

/* Networking */
void luxAddServer(const char * name);
void luxUpdateFilmFromNetwork();

/* Informations and statistics */
double luxStatistics(const char *statName);

/* Error Handlers */
extern int luxLastError; /*  Keeps track of the last error code */
typedef void (*LuxErrorHandler)(int code, int severity, const char *msg);
extern void luxErrorHandler(LuxErrorHandler handler);
extern void luxErrorAbort(int code, int severity, const char *message);
extern void luxErrorIgnore(int code, int severity, const char *message);
extern void luxErrorPrint(int code, int severity, const char *message);

/*
 Error codes

 1 - 10     System and File errors
 11 - 20     Program Limitations
 21 - 40     State Errors
 41 - 60     Parameter and Protocol Errors
 61 - 80     Execution Errors
 */

#define LUX_NOERROR         0

#define LUX_NOMEM           1       /* Out of memory */
#define LUX_SYSTEM          2       /* Miscellaneous system error */
#define LUX_NOFILE          3       /* File nonexistant */
#define LUX_BADFILE         4       /* Bad file format */
#define LUX_BADVERSION      5       /* File version mismatch */
#define LUX_DISKFULL        6       /* Target disk is full */

#define LUX_UNIMPLEMENT    12       /* Unimplemented feature */
#define LUX_LIMIT          13       /* Arbitrary program limit */
#define LUX_BUG            14       /* Probably a bug in renderer */

#define LUX_NOTSTARTED     23       /* luxInit() not called */
#define LUX_NESTING        24       /* Bad begin-end nesting - jromang will be used in API v2 */
#define LUX_NOTOPTIONS     25       /* Invalid state for options - jromang will be used in API v2 */
#define LUX_NOTATTRIBS     26       /* Invalid state for attributes - jromang will be used in API v2 */
#define LUX_NOTPRIMS       27       /* Invalid state for primitives - jromang will be used in API v2 */
#define LUX_ILLSTATE       28       /* Other invalid state - jromang will be used in API v2 */
#define LUX_BADMOTION      29       /* Badly formed motion block - jromang will be used in API v2 */
#define LUX_BADSOLID       30       /* Badly formed solid block - jromang will be used in API v2 */

#define LUX_BADTOKEN       41       /* Invalid token for request */
#define LUX_RANGE          42       /* Parameter out of range */
#define LUX_CONSISTENCY    43       /* Parameters inconsistent */
#define LUX_BADHANDLE      44       /* Bad object/light handle */
#define LUX_NOPLUGIN       45       /* Can't load requested plugin */
#define LUX_MISSINGDATA    46       /* Required parameters not provided */
#define LUX_SYNTAX         47       /* Declare type syntax error */

#define LUX_MATH           61       /* Zerodivide, noninvert matrix, etc. */

/* Error severity levels */

#define LUX_INFO            0       /* Rendering stats & other info */
#define LUX_WARNING         1       /* Something seems wrong, maybe okay */
#define LUX_ERROR           2       /* Problem.  Results may be wrong */
#define LUX_SEVERE          3       /* So bad you should probably abort */

#ifdef __cplusplus
}
#endif

#endif /* LUX_API_H */