#!BPY
"""
Name: 'MOSAIC RenderMan(R) System'
Blender: 244
Group: 'Render'
Tooltip: 'RenderMan(R) developement tool for blender'
"""
####################################################################### AUTHOR BLOCK
# MOSAIC RenderMan(R) System
# by Eric Nathen Back, 02-02-2007
# This plugin is protected by the GPL: Gnu Public Licence
# GPL - http://www.gnu.org/copyleft/gpl.html
####################################################################### GPL LICENSE BLOCK
# Script Copyright (C) Eric Nathen Back
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
####################################################################### COPYRIGHT BLOCK
# The RenderMan(R) Interface Procedures and Protocol are:
# Copyright 1988, 1989, 2000, 2005 Pixar
# All Rights Reserved
# RenderMan(R) is a registered trademark of Pixar
####################################################################### END BLOCKS

__author__	= "Eric Nathen Back AKA >WHiTeRaBBiT<"
__url__		= ["Project page, http://www.sourceforge.net/projects/ribmosaic/",
		   "Wiki documentation, http://ribmosaic.wiki.sourceforge.net/",
		   "GPL Licence, http://www.gnu.org/copyleft/gpl.html"]
__version__	= "Beta"
__bpydoc__	= """\
Welcome to MOSAIC<br>

Follow the links above to find the latest versions, news, tutorials and reference materials.

MOSAIC is protected by the GPL: Gnu Public Licence<br>
The RenderMan(R) Interface Procedures and Protocol are:<br>
Copyright 1988, 1989, 2000, 2005 Pixar<br>
All Rights Reserved<br>
RenderMan(R) is a registered trademark of Pixar<br>
"""

import os
import time
import math
import Blender
from Blender		import *
from Blender.Draw	import *
from Blender.BGL	import *
from Blender.Window	import *
from math		import pi
from math		import atan
from time 		import localtime
from time		import strftime

print "Welcome to MOSAIC!"

####################################################################### SETUP REGISTRY HANDELING
#Registry Vars
RenderDir		= ""						#Directory to render to
ProjectDir		= ""						#Final export directory which is RenderDir+Users Project Folder
RenderBin		= ""						#Renderman renderer binary
CompilerBin		= ""						#Shader compiler
TexmakeBin		= ""						#Texture Optimizer
InfoBin			= ""						#Shader info binary
RibOutput		= ""						#Main rib file name

#Text file name filters: [code, shader source, surface, displacement, volume, imager, light, shader include]
Filters			= ["cf_", ".sl", "ss_", "ds_", "vs_", "is_", "ls_", ".h"]

#### Update settings to registry cache
def UpdateRegistry():
	data = {}
	data['RenderDir']		= RenderDir
	data['RenderBin']		= RenderBin
	data['CompilerBin']		= CompilerBin
	data['TexmakeBin']		= TexmakeBin
	data['InfoBin']			= InfoBin
	data['CodeFilter']		= Filters[0]
	data['SourceFilter']		= Filters[1]
	data['SurfaceFilter']		= Filters[2]
	data['DisplacementFilter']	= Filters[3]
	data['VolumeFilter']		= Filters[4]
	data['ImagerFilter']		= Filters[5]
	data['LightFilter']		= Filters[6]
	data['IncludeFilter']		= Filters[7]
	Blender.Registry.SetKey('Mosaic', data, True)			#Save data to registry


#### Check if registry cache is available and if so load it
registry = Registry.GetKey('Mosaic', True)
if registry:
	try:
		RenderDir		= registry['RenderDir']
		RenderBin		= registry['RenderBin']
		CompilerBin		= registry['CompilerBin']
		TexmakeBin		= registry['TexmakeBin']
		InfoBin			= registry['InfoBin']
		Filters[0]		= registry['CodeFilter']
		Filters[1]		= registry['SourceFilter']
		Filters[2]		= registry['SurfaceFilter']
		Filters[3]		= registry['DisplacementFilter']
		Filters[4]		= registry['VolumeFilter']
		Filters[5]		= registry['ImagerFilter']
		Filters[6]		= registry['LightFilter']
		Filters[7]		= registry['IncludeFilter']
	except: UpdateRegistry()					#If registry does not exist make one from defaults


####################################################################### SETUP USER GLOBAL VARIABLES
#These are a list of tokens used to plug blender control values into shader and/or custom code parameter values, there format is as follows:
#This array of tokens is separated according to object types and then parameter types so...
#first by objects: lamps(light shader), materials(surface, displace, area), cameras(imager), world/scene(atmosphere)
#and then by parameters: numbers integer, float, color, point, vector, normal, matrix, hpoint, string
#also tokens can have parameters, they are: _I=integer, _F=float, _C=color, _P=point, _V=vector, _N=normal, _M=matrix, _H=hpoint, _S=string, _X#=texture index, _A#=range adjust adder, _M#=range adjust multiplier
			    #Lamp tokens (light shaders/code)
Tokens			= [[["LampEnergy", "LampDist", "LampSpotSi", "LampSpotBl", "LampShadBufSize", "LampSamples", "LampHaloInt", "LampBias", "LampSoft", "LampClipStart", "LampClipEnd", "LampSizeX", "LampSizeY", "LampSamplesX", "LampSamplesY", "LampHaloStep", "LampQuad1", "LampQuad2"], #Integers
			    ["LampEnergy", "LampDist", "LampSpotSi", "LampSpotBl", "LampShadBufSize", "LampSamples", "LampHaloInt", "LampBias", "LampSoft", "LampClipStart", "LampClipEnd", "LampSizeX", "LampSizeY", "LampSamplesX", "LampSamplesY", "LampHaloStep", "LampQuad1", "LampQuad2"], #Floats
			    ["LampLightColor"], #Colors
			    ["TO", "FROM"], #Points
			    ["TO"], #Vectors
			    ["TO"], #Normals
			    ["FROM"], #Matrices
			    [], #Hpoints
			    []], #Strings
			    #Material tokens (surface/displace/area shaders/code)
			   [["MatHaloAdd", "MatAmb", "MatDiffuseDark", "MatDiffuseSize", "MatDiffuseSmooth", "MatEmit", "MatRayFilt", "MatFlareBoost", "MatFlareSeed", "MatFlareSize", "MatMirrorFresnel", "MatMirrorFac", "MatRayFresnel", "MatRayFac", "MatHaloSeed",
			     "MatHaloSize", "MatHard", "MatRayIOR", "MatFlares", "MatLines", "MatRings", "MatStar", "MatRayMir", "MatMirrorDepth", "MatRef", "MatRefr", "Matrms", "MatRough", "MatShadA", "MatSpec", "MatSpecSize", "MatSpecSmooth", "MatSpecTra", "MatSSSBack", "MatSSSColBlend",
			     "MatSSSError", "MatSSSIOR", "MatSSSRadiusB", "MatSSSRadiusR", "MatSSSRadiusG", "MatSSSTex", "MatHaloSubSize", "MatRayDepth", "MatTranslu", "MatZoffs", "MatMapCol_X", "MatMapDisp_X", "MatMapDVar_X", "MatMapNor_X", "MatMapOfsX_X", "MatMapOfsY_X", "MatMapOfsZ_X",
			     "MatMapSizeX_X", "MatMapSizeY_X", "MatMapSizeZ_X", "MatMapVar_X", "MatTexFrames_X", "MatTexOffs_X", "MatTexStartFr_X", "MatTexBright_X", "MatTexContr_X", "MatTexMinX_X", "MatTexMaxX_X", "MatTexMinY_X", "MatTexMaxY_X", "MatTexFieIma_X", "MatTexFilter_X",
			     "MatTexXrepeat_X", "MatTexYrepeat_X", "MatTexDistAmnt_X", "MatTexExp_X", "MatTexiScale_X", "MatTexH_X", "MatTexLacu_X", "MatTexNDepth_X", "MatTexNSize_X", "MatTexOcts_X", "MatTexTurb_X", "MatTexW1_X", "MatTexW2_X", "MatTexW3_X", "MatTexW4_X", "MatImageSizeX_X",
			     "MatImageSizeY_X", "MatImageStart_X", "MatImageEnd_X", "MatImageDepth_X", "MatImageSpeed_X", "MatImageXrep_X", "MatImageYrep_X"], #Integers
			    ["MatHaloAdd", "MatAmb", "MatDiffuseDark", "MatDiffuseSize", "MatDiffuseSmooth", "MatEmit", "MatRayFilt", "MatFlareBoost", "MatFlareSeed", "MatFlareSize", "MatMirrorFresnel", "MatMirrorFac", "MatRayFresnel", "MatRayFac", "MatHaloSeed",
			     "MatHaloSize", "MatHard", "MatRayIOR", "MatFlares", "MatLines", "MatRings", "MatStar", "MatRayMir", "MatMirrorDepth", "MatRef", "MatRefr", "Matrms", "MatRough", "MatShadA", "MatSpec", "MatSpecSize", "MatSpecSmooth", "MatSpecTra", "MatSSSBack", "MatSSSColBlend",
			     "MatSSSError", "MatSSSIOR", "MatSSSRadiusB", "MatSSSRadiusR", "MatSSSRadiusG", "MatSSSTex", "MatHaloSubSize", "MatRayDepth", "MatTranslu", "MatZoffs", "MatMapCol_X", "MatMapDisp_X", "MatMapDVar_X", "MatMapNor_X", "MatMapOfsX_X", "MatMapOfsY_X", "MatMapOfsZ_X",
			     "MatMapSizeX_X", "MatMapSizeY_X", "MatMapSizeZ_X", "MatMapVar_X", "MatTexFrames_X", "MatTexOffs_X", "MatTexStartFr_X", "MatTexBright_X", "MatTexContr_X", "MatTexMinX_X", "MatTexMaxX_X", "MatTexMinY_X", "MatTexMaxY_X", "MatTexFieIma_X", "MatTexFilter_X",
			     "MatTexXrepeat_X", "MatTexYrepeat_X", "MatTexDistAmnt_X", "MatTexExp_X", "MatTexiScale_X", "MatTexH_X", "MatTexLacu_X", "MatTexNDepth_X", "MatTexNSize_X", "MatTexOcts_X", "MatTexTurb_X", "MatTexW1_X", "MatTexW2_X", "MatTexW3_X", "MatTexW4_X", "MatImageSizeX_X",
			     "MatImageSizeY_X", "MatImageStart_X", "MatImageEnd_X", "MatImageDepth_X", "MatImageSpeed_X", "MatImageXrep_X", "MatImageYrep_X"], #floats
			    ["MatMirrorColor", "MatCol", "MatSpecCol", "MatSSSCol", "MatMapColor_X", "MatTexColor_X"], #Colors
			    [], #Points
			    [], #Vectors
			    [], #Normals
			    [], #Matrices
			    [], #Hpoints
			    ["MatImageName_X"]], #Strings
			    #Camera tokens (imager shaders/code)
			   [["CameraAlpha", "CameraAngle", "CameraEnd", "CameraStart", "CameraDofDist", "CameraSize", "CameraLens", "CameraScale", "CameraX", "CameraY"], #Integers
			    ["CameraAlpha", "CameraAngle", "CameraEnd", "CameraStart", "CameraDofDist", "CameraSize", "CameraLens", "CameraScale", "CameraX", "CameraY"], #Floats
			    [], #Colors
			    ["TO", "FROM"], #Points
			    ["TO"], #Vectors
			    ["TO"], #Normals
			    ["FROM"], #Matrices
			    [], #Hpoints
			    []], #Strings
			    #World/Scene Global tokens (for all shaders/code)
			   [["Add User Value", "LightID", "SceneAspX", "SceneAspY", "SceneEnd", "SceneFps", "SceneBf", "SceneFilterSize", "ScenePlanes", "SceneOSALevel", "SceneStart", "SceneSizeX", "SceneSizeY", "SceneXparts", "SceneYparts", "WorldMist", "WorldSta", "WorldDi", "WorldHi", "WorldSize", "WorldMinDist", "WorldStarDist", "WorldColnoise"], #Integers
			    ["Add User Value", "SceneAspX", "SceneAspY", "SceneEnd", "SceneFps", "SceneBf", "SceneFilterSize", "ScenePlanes", "SceneOSALevel", "SceneStart", "SceneSizeX", "SceneSizeY", "SceneXparts", "SceneYparts", "WorldMist", "WorldSta", "WorldDi", "WorldHi", "WorldSize", "WorldMinDist", "WorldStarDist", "WorldColnoise"], #Floats
			    ["Add User Value", "SceneEdgeColor", "WorldAmbCol", "WorldHorCol", "WorldZenCol"], #Colors
			    ["Add User Value"], #Points
			    ["Add User Value"], #Vectors
			    ["Add User Value"], #Normals
			    ["Add User Value"], #Matrices
			    ["Add User Value"], #Hpoints
			    ["Add User Value", "ObjectName", "ProjectDir", ]],#Strings
			    #None Group
			   [[],
			    [],
			    [],
			    [],
			    [],
			    [],
			    [],
			    [],
			    []]] #None

#This array is used to try and identity standard integer and float shader parameters and return standard upper and lower bounds adjustments for easy translation of blender controls to shader parameters
#The array uses the following fields: ["blender control token", (+/-float) blender control adder as string, (+/-float) blender control multiplier as string]
StandardRanges		= [["LampEnergy", "0.0", "30.0"],
			   ["LampSpotSi", "0.0", "0.5"],
			   ["LampSpotBl", "0.0", "0.2"],
			   ["MatSpec", "0.0", "1.0"],
			   ["MatHard", "1.0", "-0.001956947162426614481"]]

#These are the default shaders to approximate blender like renders without renderman setup
defaultPointlight	= "LightSource \"pointlight\" <LightID_I> \"float intensity\" <LampEnergy_F_A0_M30> \"point from\" <FROM_P> \"color lightcolor\" <LampLightColor_C>\n"
defaultSpotlight	= "LightSource \"spotlight\" <LightID_I> \"float intensity\" <LampEnergy_F_A0_M30> \"point to\" <TO_P> \"point from\" <FROM_P> \"color lightcolor\" <LampLightColor_C> \"float coneangle\" <LampSpotSi_F_A0_M0.5> \"float conedeltaangle\" <LampSpotBl_F_A0_M0.2>\n"
defaultDistantlight	= "LightSource \"distantlight\" <LightID_I> \"float intensity\" <LampEnergy_F_A0_M1.0> \"point to\" <TO_P> \"point from\" <FROM_P> \"color lightcolor\" <LampLightColor_C>\n"
defaultAmbientlight	= "LightSource \"ambientlight\" <LightID_I> \"float intensity\" <LampEnergy_F_A0_M0.75> \"color lightcolor\" <LampLightColor_C>\n"
defaultSurface		= ["Color [ 0.8 0.8 0.8 ]\n", "Surface \"plastic\" \"float Kd\" [ 0.8 ] \"float Ks\" [ 0.5 ] \"float roughness\" [ 0.25 ]\n"]


####################################################################### SETUP GUI GLOBAL VARIABLES
#Global GUI Vars
killExport		= False						#Used to kill render process on esc
instanceCount		= 0						#Used to keep track of object instances being used
lightList		= []						#Used to keep track of lights in current working scene
ScrollPos		= 0						#Mouse scroll offset for menu graphics
ScrollState		= 0						#Last know SubWindows total overlap to available window area
LastObject		= ""						#Used to trigger redraw when active selection has changed and mouse moves over area
LastScene		= ""
MousePos		= [0, 0]					#Track mouse position

#Events Constants
EVENT_WIDTH		= 100						#Sets the increments in event numbers between sub-windows, this basically means the number of buttons possible in each sub-window
EVENT_NONE		= 1
EVENT_ACTIONS_SET	= EVENT_WIDTH*1
EVENT_SETTINGS_SET	= EVENT_WIDTH*2
EVENT_UTILITY_SET	= EVENT_WIDTH*3
EVENT_PROJECT_SET	= EVENT_WIDTH*4
EVENT_SCENE_SET		= EVENT_WIDTH*5
EVENT_CAMERA_SET	= EVENT_WIDTH*6
EVENT_GROUP_SET		= EVENT_WIDTH*7
EVENT_GEOM_SET		= EVENT_WIDTH*8
EVENT_LIGHT_SET		= EVENT_WIDTH*9
EVENT_MAT_SET		= EVENT_WIDTH*10

#ButtonData index constants
#Sub-windows
ACTIONS			= 0
SETTINGS		= 1
UTILITIES		= 2
PROJECT			= 3
SCENES			= 4
CAMERAS			= 5
GROUPS			= 6
GEOMETRY		= 7
LIGHTS			= 8
MATERIALS		= 9
#Buttons
ACT_RENDER		= 0
ACT_ANIMATION		= 1
ACT_PREVIEW		= 2
ACT_DIVIDER		= 3
ACT_RENDER_RIB		= 4
ACT_CREATE_RIB		= 5
ACT_CREATE_SEL		= 6
ACT_COMPILE_SL		= 7
ACT_EXPORT_MAPS		= 8
ACT_HELP		= 9
ACT_QUIT		= 10
SET_OUTPUT_DIR		= 0
SET_TEXT_FILTER		= 1
SET_RENDER_BIN		= 2
SET_SHADER_BIN		= 3
SET_TEXMAKE_BIN		= 4
SET_INFO_BIN		= 5
UTIL_LIBRARY_FRAG	= 0
UTIL_SOURCE_FRAG	= 1
UTIL_CLEAN_DIR		= 2
UTIL_COPY_PROP		= 3
UTIL_CLEAR_PROP		= 4
PROJECT_FOLDER		= 0
PROJECT_PASSES		= 1
PROJECT_DIVIDER		= 2
PROJECT_ARCHIVES	= 3
PROJECT_SHADERS		= 4
PROJECT_TEXTURES	= 5
PROJECT_DISPLAYS	= 6
PROJECT_PROCEDURALS	= 7
PROJECT_RESOURCES	= 8
SCENE_SELECT		= 0
SCENE_FRAME_ARCH	= 1
SCENE_CUSTOM_RENDER	= 2
SCENE_DIVIDER1		= 3
SCENE_HEADER_CODE	= 4
SCENE_BEGINFRAME_CODE	= 5
SCENE_BEGINWORLD_CODE	= 6
SCENE_ENDWORLD_CODE	= 7
SCENE_ENDFRAME_CODE	= 8
SCENE_DIVIDER2		= 9
SCENE_ATMO		= 10
SCENE_DISPLAY_CODE	= 11
SCENE_FRAMEBUF_CODE	= 12
SCENE_USE_DISPLAY	= 13
SCENE_USE_FRAME		= 14
SCENE_XSAMPLES		= 15
SCENE_YSAMPLES		= 16
SCENE_FILTER		= 17
SCENE_XWIDTH		= 18
SCENE_YWIDTH		= 19
SCENE_SHADE_RATE	= 20
SCENE_BUCKET		= 21
SCENE_GRID		= 22
SCENE_EYES		= 23
SCENE_OTHRESHOLD	= 24
SCENE_DEFAULT		= 25
CAM_SELECT		= 0
CAM_ARCH		= 1
CAM_DIVIDER1		= 2
CAM_BEGIN_CODE		= 3
CAM_END_CODE		= 4
CAM_DIVIDER2		= 5
CAM_IMAGE		= 6
CAM_MBLUR		= 7
CAM_FRAMES		= 8
CAM_DOF			= 9
CAM_FSTOP		= 10
CAM_FOCAL		= 11
CAM_SHUT_MIN		= 12
CAM_SHUT_MAX		= 13
CAM_DEFAULT		= 14
GRP_SELECT		= 0
GRP_ARCH		= 1
GRP_DIVIDER1		= 2
GRP_BEGIN_CODE		= 3
GRP_END_CODE		= 4
GRP_DIVIDER2		= 5
GRP_ATMO		= 6
GRP_DEFAULT		= 7
GEO_SELECT		= 0
GEO_OBJ_ARCH		= 1
GEO_DATA_ARCH		= 2
GEO_DIVIDER1		= 3
GEO_BEGINOBJ_CODE	= 4
GEO_GEO_CODE		= 5
GEO_ENDOBJ_CODE		= 6
GEO_DIVIDER2		= 7
GEO_ATMO		= 8
GEO_OBJ_MBLUR		= 9
GEO_OBJ_FRAMES		= 10
GEO_GEO_MBLUR		= 11
GEO_GEO_FRAMES		= 12
GEO_ANIM_OBJECT		= 13
GEO_SHADE_RATE		= 14
GEO_DISP_BOUND		= 15
GEO_COOR_SYS		= 16
GEO_DEFAULT		= 17
LIGHT_SELECT		= 0
LIGHT_ARCH		= 1
LIGHT_DIVIDER1		= 2
LIGHT_BEGIN_CODE	= 3
LIGHT_END_CODE		= 4
LIGHT_DIVIDER2		= 5
LIGHT_SHADER		= 6
LIGHT_MBLUR		= 7
LIGHT_FRAMES		= 8
LIGHT_DEFAULT		= 9
MAT_SELECT		= 0
MAT_ARCH		= 1
MAT_DIVIDER1		= 2
MAT_BEGIN_CODE		= 3
MAT_END_CODE		= 4
MAT_DIVIDER2		= 5
MAT_SURF		= 6
MAT_DISP		= 7
MAT_INT_VOL		= 8
MAT_EXT_VOL		= 9
MAT_AREA		= 10
MAT_MBLUR		= 11
MAT_FRAMES		= 12
MAT_DEFAULT		= 13
#Window data indexes
WIN_EVENT		= 0
WIN_COLLAPSE		= 1
WIN_TITLE		= 2
WIN_COLOR		= 3
WIN_BUTS		= 4
#Button data indexes
BUTTON			= 0
BUT_MENU		= 1
BUT_SHOW		= 2
BUT_TYPE		= 3
BUT_WIDTH_DIV		= 4
BUT_DIV_POS		= 5
BUT_TITLE		= 6
BUT_TIP			= 7
BUT_PROP		= 8
BUT_DEFAULT		= 9
BUT_MIN			= 10
BUT_MAX			= 11

#Button Data - This is a 4 element array containing data for [sub-window arrays...][sub_data..., Buttons_arrays...][Buttons data fields...]
#Sub-window data is:	[event #, Collapse?, Title, color adjust, [buttons]]
#Button data is:	[Button Object, Last Selection, Show?, Button type(0-button, 1-list, 2-Int, 3-Tog, 4-Str, 5-Line), Width Divider, Divider Position, Title, Tool Tip, Prop (titles for menu and properties), default value, min value, max value]
#NOTE: If Title = "CodeF", "SourceF", "SurfaceF", "DisplacementF", "VolumeF", "ImageF", "LightF", "SceneF", "CameraF", "GroupF", "GeometryF", "LampF", "MaterialF" then a menu will be generated with those items
ButtonData		= [[EVENT_ACTIONS_SET, False, "MOSAIC Actions", [1.0,1.0,1.0,1.0],
			   [[Blender.Draw.Create(1), "", True, 0, 1, 0, "(R)ender Scene", "Press \"r\" to render current scene", "", 1, 0, 1],
			    [Blender.Draw.Create(1), "", True, 0, 1, 0, "Render (A)nimation/Passes", "Press \"a\" to render current scenes animation from Sta to End or use Render Passes if present", "", 1, 0, 1],
			    [Blender.Draw.Create(1), "", True, 0, 1, 0, "(P)review Scene", "Press \"p\" to preview current selection/s using the current 3D view", "", 1, 0, 1],
			    [0, "", True, 5, 1, 0, "", "", "", 1, 0, 1],
			    [Blender.Draw.Create(1), "", True, 3, 3, 0, "Render RIB", "Whether or not to Call renderer after RIB code generation", "", 1, 0, 1],
			    [Blender.Draw.Create(1), "", True, 3, 3, 1, "Create RIB", "Whether or not to create Rib files from current scene", "", 1, 0, 1],
			    [Blender.Draw.Create(0), "", True, 3, 3, 2, "Only Select", "Only update selected geometry (non archive code will have to regenerate)", "", 0, 0, 1],
			    [Blender.Draw.Create(1), "", True, 3, 2, 0, "Compile SL", "Whether or not to compile projects shaders", "", 1, 0, 1],
			    [Blender.Draw.Create(1), "", True, 3, 2, 1, "Export Maps", "Whether or not to export and optimize texture maps", "", 1, 0, 1],
			    [Blender.Draw.Create(1), "", True, 0, 2, 0, "(H)elp", "Press \"h\" to view Mosaic's help doc", "", 1, 0, 1],
			    [Blender.Draw.Create(1), "", True, 0, 2, 1, "(Q)uit", "Press \"q\" to quit Mosaic", "", 1, 0, 1]]],
			   [EVENT_SETTINGS_SET, True, "MOSAIC Settings", [1.0,1.0,1.0,1.0],
			   [[Blender.Draw.Create(1), "", True, 0, 2, 0, "Output Directory", "Ouput Directory: "+RenderDir, "", 1, 0, 1],
			    [Blender.Draw.Create(1), "", True, 0, 2, 1, "Text Filters", "Text name filters allow you to group text files into catagories for mosaic menus", "", 1, 0, 1],
			    [Blender.Draw.Create(1), "", True, 0, 2, 0, "Renderer Binary", "Renderer: "+RenderBin, "", 1, 0, 1],
			    [Blender.Draw.Create(1), "", True, 0, 2, 1, "Shader Compiler", "Compiler: "+CompilerBin, "", 1, 0, 1],
			    [Blender.Draw.Create(1), "", True, 0, 2, 0, "Texture Optimizer", "Leave blank to disable: "+TexmakeBin, "", 1, 0, 1],
			    [Blender.Draw.Create(1), "", True, 0, 2, 1, "Shader Info", "Shader Info: "+InfoBin, "", 1, 0, 1]]],
			   [EVENT_UTILITY_SET, True, "MOSAIC Utilities", [1.0,1.0,1.0,1.0],
			   [[Blender.Draw.Create(1), "", True, 0, 1, 0, "Setup Shader From Name", "Generate a shader fragment for an already compiled shader in system", "", 1, 0, 1],
			    [Blender.Draw.Create(1), "", True, 0, 1, 0, "Setup Shader From Source", "Generate a shader fragment for a shader source text file in Blender", "", 1, 0, 1],
			    [Blender.Draw.Create(1), "", True, 0, 1, 0, "Clean Project Directory", "Removes project folder and all content generated for project render", "", 1, 0, 1],
			    [Blender.Draw.Create(1), "", True, 0, 2, 0, "Copy Properties", "Copies Active objects RenderMan settings too all other objects in selection", "", 1, 0, 1],
			    [Blender.Draw.Create(1), "", True, 0, 2, 1, "Clear Properties", "Clears selected objects of all RenderMan settings (resets all to default)", "", 1, 0, 1]]],
			   [EVENT_PROJECT_SET, True, "Project Setup", [1.0,0.75,0.25,1.0],
			   [[Blender.Draw.Create("Mosaic"), "", True, 4, 1, 0, "Project Folder", "Project export folder to create in \"MOSAIC Settings\" Output Directory", "Project Folder", "Mosaic", 0, 255],
			    [Blender.Draw.Create(""), "", True, 4, 1, 0, "Render Passes: ", "Render select scenes through frame ranges using \"scene:frame,nextscene:sta-end\" for examples PhotonPass:1,CausticPass:1,BeautyPass1-20,ect...", "Render Passes", "", 0, 255],
			    [0, "", True, 5, 1, 0, "", "", "", 1, 0, 1],
			    [Blender.Draw.Create(""), "", True, 4, 1, 0, "Archive Searchpath", "Search paths for archive RIBs (blank to use default, NONE to turn off)", "Archive Searchpath", "@:.:Archives:Archives"+sys.sep+sys.sep+"Scenes:Archives"+sys.sep+sys.sep+"Groups:Archives"+sys.sep+sys.sep+"Materials:Archives"+sys.sep+sys.sep+"Lights:Archives"+sys.sep+sys.sep+"Cameras:Archives"+sys.sep+sys.sep+"Geometry:Archives"+sys.sep+sys.sep+"Objects", 0, 255],
			    [Blender.Draw.Create(""), "", True, 4, 1, 0, "Shader Searchpath", "Search paths for shaders (blank to use default, NONE to turn off)", "Shader Searchpath", "@:.:Shaders", 0, 255],
			    [Blender.Draw.Create(""), "", True, 4, 1, 0, "Texture Searchpath", "Search paths for textures maps (blank to use default, NONE to turn off)", "Texture Searchpath", "@:.:Maps", 0, 255],
			    [Blender.Draw.Create(""), "", True, 4, 1, 0, "Display Searchpath", "Search paths for displays (blank to use default, NONE to turn off)", "Display Searchpath", "NONE", 0, 255],
			    [Blender.Draw.Create(""), "", True, 4, 1, 0, "Procedural Searchpath", "Search paths for procedurals (blank to use default, NONE to turn off)", "Procedural Searchpath", "NONE", 0, 255],
			    [Blender.Draw.Create(""), "", True, 4, 1, 0, "Resource Searchpath", "Search paths for resources (blank to use default, NONE to turn off)", "Resource Searchpath", "NONE", 0, 255]]],
			   [EVENT_SCENE_SET, True, "Scenes Setup", [1.0,0.75,0.75,1.0],
			   [[Blender.Draw.Create(1), "", True, 1, 1, 0, "SceneF", "Select the scene to setup", "Select Scene", 1, 0, 1],
			    [Blender.Draw.Create(1), "", False, 1, 1, 0, ["Frame Archive:%t|Read Archive|Inline Code", "Read Archive", "Inline Code"], "Set the archive method for rib in frame blocks", "Frame Archive", 1, 0, 1],
			    [Blender.Draw.Create(""), "", False, 4, 1, 0, "Custom Render Call: ", "Use custom render command for this scene (uses \"MOSAIC Settings\" Renderer if blank)", "Custom Render Call", "", 0, 255],
			    [0, "", False, 5, 1, 0, "", "", "", 1, 0, 1],
			    [Blender.Draw.Create(1), "", False, 1, 1, 0, "CodeF", "Insert custom code at the beginning of main RIB", "Header Begin Code", 1, 0, 1],
			    [Blender.Draw.Create(1), "", False, 1, 1, 0, "CodeF", "Insert custom code fragment into beginning of frame block", "Frame Begin Code", 1, 0, 1],
			    [Blender.Draw.Create(1), "", False, 1, 1, 0, "CodeF", "Insert custom code fragment into beginning of world block", "World Begin Code", 1, 0, 1],
			    [Blender.Draw.Create(1), "", False, 1, 1, 0, "CodeF", "Insert custom code fragment into end of world block", "World End Code", 1, 0, 1],
			    [Blender.Draw.Create(1), "", False, 1, 1, 0, "CodeF", "Insert custom code fragment into end of frame block", "Frame End Code", 1, 0, 1],
			    [0, "", False, 5, 1, 0, "", "", "", 1, 0, 1],
			    [Blender.Draw.Create(1), "", False, 1, 1, 0, "VolumeF", "Set atmosphere shader for entire scene", "Atmosphere Shader", 1, 0, 1],
			    [Blender.Draw.Create(""), "", False, 4, 1, 0, "Display Code: ", "RiDisplay code for output file, blank to use default (use <#> to add frame numbers to file name)", "Display Code", "Display \"<####>.tif\" \"file\" \"rgb\"", 0, 255],
			    [Blender.Draw.Create(""), "", False, 4, 1, 0, "Framebuffer Code: ", "RiDisplay code for framebuffer, blank to use default (use <#> to add frame numbers to file name)", "Framebuffer Code", "Display \"+<####>.tif\" \"framebuffer\" \"rgb\"", 0, 255],
			    [Blender.Draw.Create(1), "", False, 3, 2, 0, "Use Display Code", "Create a display driver from the above display code", "Use Display Code", 1, 0, 1],
			    [Blender.Draw.Create(1), "", False, 3, 2, 1, "Use Framebuffer", "Create a framebuffer from the above framebuffer code", "Use Framebuffer", 1, 0, 1],
			    [Blender.Draw.Create(4), "", False, 2, 2, 0, "Xsamples: ", "RiPixelSamples xwidth parameter", "Xsamples", 4, 0, 200],
			    [Blender.Draw.Create(4), "", False, 2, 2, 1, "Ysamples: ", "RiPixelSamples ywidth parameter", "Ysamples", 4, 0, 200],
			    [Blender.Draw.Create(""), "", False, 4, 3, 0, "Filter: ", "If blank RiPixelFilter is not used (box, triangle, catmull-rom, sinc, gaussian", "Filter", "", 0, 255],
			    [Blender.Draw.Create(2), "", False, 2, 3, 1, "Xwidth: ", "RiPixelFilter xwidth parameter", "FilterX", 2, 0, 200],
			    [Blender.Draw.Create(2), "", False, 2, 3, 2, "Ywidth: ", "RiPixelFilter ywidth parameter", "FilterY", 2, 0, 200],
			    [Blender.Draw.Create(1.0), "", False, 2, 1, 0, "Shading Rate: ", "Sets RiShadingRate for current scene", "Shading Rate", 1.0, 0.0, 20.0],
			    [Blender.Draw.Create(16), "", False, 2, 2, 0, "bucketsize: ", "Dimensions of pixel blocks the screen gets divided into (0 is off)", "bucketsize", 16, 0, 1024],
			    [Blender.Draw.Create(256), "", False, 2, 2, 1, "gridsize: ", "Maximum number of micropolygons shaded at once (0 is off)", "gridsize", 256, 0, 1024],
			    [Blender.Draw.Create(6), "", False, 2, 2, 0, "eyesplits: ", "Eye-plane eyesplits failure detection threshold (0 is off)", "eyesplits", 6, 0, 1024],
			    [Blender.Draw.Create(0.996), "", False, 2, 2, 1, "othreshold: ", "Opacity at which a stack of transparent samples are to be fully opaque (0 is off)", "othreshold", 0.996, 0.0, 1.0],
			    [Blender.Draw.Create(1), "", False, 0, 1, 0, "Use these settings on new scenes", "Uses current settings as defaults for new items", "", 1, 0, 1]]],
			   [EVENT_CAMERA_SET, True, "Cameras Setup", [1.0,0.75,1.0,1.0],
			   [[Blender.Draw.Create(1), "", True, 1, 1, 0, "CameraF", "Select the camera to setup", "Select Camera", 1, 0, 1],
			    [Blender.Draw.Create(1), "", False, 1, 1, 0, ["Camera Archive:%t|Read Archive|Inline Code", "Read Archive", "Inline Code"], "Set the archive method for camera", "Camera Archive", 1, 0, 1],
			    [0, "", False, 5, 1, 0, "", "", "", 1, 0, 1],
			    [Blender.Draw.Create(1), "", False, 1, 1, 0, "CodeF", "Insert custom code fragment into beginning of camera block", "Camera Begin Code", 1, 0, 1],
			    [Blender.Draw.Create(1), "", False, 1, 1, 0, "CodeF", "Insert custom code fragment into end of camera block", "Camera End Code", 1, 0, 1],
			    [0, "", False, 5, 1, 0, "", "", "", 1, 0, 1],
			    [Blender.Draw.Create(1), "", False, 1, 1, 0, "ImageF", "Set image shader to current camera view", "Image Shader", 1, 0, 1],
			    [Blender.Draw.Create(0), "", False, 3, 2, 0, "Camera MBlur", "Enables motion blur (transform)", "CameraMBlur", 0, 0, 1],
			    [Blender.Draw.Create(5), "", False, 2, 2, 1, "frames: ", "Number of frames to blur across", "CameraFrames", 5, 2, 1000],
			    [Blender.Draw.Create(0), "", False, 3, 3, 0, "Use DOF", "Enable DOF (focaldistance is set by cameras DoFDist)", "Use DOF", 0, 0, 1],
			    [Blender.Draw.Create(22.0), "", False, 2, 3, 1, "fstop: ", "RiDepthOfField fstop setting", "fstop", 22.0, 0.0, 600.0],
			    [Blender.Draw.Create(45.0), "", False, 2, 3, 2, "focalL: ", "RiDepthOfField focal length setting", "focalL", 45.0, 0.0, 5000.0],
			    [Blender.Draw.Create(0.0), "", False, 2, 2, 0, "Shutter min: ", "Sets RiShutter min parameter", "shuttermin", 0.0, 0.0, 100.0],
			    [Blender.Draw.Create(1.0), "", False, 2, 2, 1, "Shutter max: ", "Sets RiShutter max paramter", "shuttermax", 1.0, 0.0, 100.0],
			    [Blender.Draw.Create(1), "", False, 0, 1, 0, "Use these settings on new cameras", "Uses current settings as defaults for new items", "", 1, 0, 1]]],
			   [EVENT_GROUP_SET, True, "Groups Setup", [0.75,0.75,1.0,1.0],
			   [[Blender.Draw.Create(1), "", True, 1, 1, 0, "GroupF", "Select the group to setup", "Select Group", 1, 0, 1],
			    [Blender.Draw.Create(2), "", False, 1, 1, 0, ["Group Block:%t|Attribute Block|Ignore Group", "Attribute Block", "Ignore Group"], "Wraps geometry in selected group into a attribute block for custom attributes", "Group Block", 2, 0, 1],
			    [0, "", False, 5, 1, 0, "", "", "", 1, 0, 1],
			    [Blender.Draw.Create(1), "", False, 1, 1, 0, "CodeF", "Insert custom code fragment into beginning of group block", "Group Begin Code", 1, 0, 1],
			    [Blender.Draw.Create(1), "", False, 1, 1, 0, "CodeF", "Insert custom code fragment into end of group block", "Group End Code", 1, 0, 1],
			    [0, "", False, 5, 1, 0, "", "", "", 1, 0, 1],
			    [Blender.Draw.Create(1), "", False, 1, 1, 0, "VolumeF", "Set atmosphere shader for objects in this group", "Atmosphere Shader", 1, 0, 1],
			    [Blender.Draw.Create(1), "", False, 0, 1, 0, "Use these settings on new groups", "Uses current settings as defaults for new items", "", 1, 0, 1]]],
			   [EVENT_GEOM_SET, True, "Geometry Setup", [0.75,1.0,1.0,1.0],
			   [[Blender.Draw.Create(1), "", True, 1, 1, 0, "GeometryF", "Select the geometry to setup", "Select Geometry", 1, 0, 1],
			    [Blender.Draw.Create(2), "", False, 1, 1, 0, ["Object Archive:%t|Delayed Archive|Read Archive|Inline Code", "Delayed Archive", "Read Archive", "Inline Code"], "Set the archive method for this object", "Object Archive", 2, 0, 1],
			    [Blender.Draw.Create(1), "", False, 1, 1, 0, ["Datablock Archive:%t|Read Archive|Instance Object|Inline Code", "Read Archive", "Instance Object", "Inline Code"], "Set the archive method for this objects geometry Datablock", "Datablock Archive", 1, 0, 1],
			    [0, "", False, 5, 1, 0, "", "", "", 1, 0, 1],
			    [Blender.Draw.Create(1), "", False, 1, 1, 0, "CodeF", "Insert custom code fragment into beginning of object block", "Object Begin Code", 1, 0, 1],
			    [Blender.Draw.Create(1), "", False, 1, 1, 0, "CodeF", "Insert hand written geometry using meshes materials and settings", "Geometry Code", 1, 0, 1],
			    [Blender.Draw.Create(1), "", False, 1, 1, 0, "CodeF", "Insert custom code fragment into end of object block", "Object End Code", 1, 0, 1],
			    [0, "", False, 5, 1, 0, "", "", "", 1, 0, 1],
			    [Blender.Draw.Create(1), "", False, 1, 1, 0, "VolumeF", "Set atmosphere shader for this object", "Atmosphere Shader", 1, 0, 1],
			    [Blender.Draw.Create(0), "", False, 3, 2, 0, "Transform MBlur", "Enables motion blur on object motion (translate, rotate, scale)", "ObjectMBlur", 0, 0, 1],
			    [Blender.Draw.Create(5), "", False, 2, 2, 1, "frames: ", "Number of frames to blur across", "ObjectFrames", 5, 2, 1000],
			    [Blender.Draw.Create(0), "", False, 3, 2, 0, "Mesh MBlur", "Enables motion blur on mesh data (any mesh animation)", "MeshMBlur", 0, 0, 1],
			    [Blender.Draw.Create(5), "", False, 2, 2, 1, "frames: ", "Number of frames to blur across", "MeshFrames", 5, 2, 1000],
			    [Blender.Draw.Create(1), "", False, 3, 2, 0, "Animate Object", "Used to manually control what objects get animated (speed hack)", "Animate Object", 1, 0, 1],
			    [Blender.Draw.Create(0.0), "", False, 2, 2, 1, "Shading Rate: ", "Sets RiShadingRate for this object (0.0 will use the scenes rate)", "Shading Rate", 0.0, 0.0, 20.0],
			    [Blender.Draw.Create(0.0), "", False, 2, 2, 0, "DisplaceBound: ", "Increase to compensate for displacements clipping on bounding box (0.0 is off)", "Bound", 0.0, 0.0, 10.0],
			    [Blender.Draw.Create("camera"), "", False, 4, 2, 1, "CoorSystem: ", "Set displacementbound coordinate system (object, world, camera, screen, raster)", "Coor", "camera", 0, 255],
			    [Blender.Draw.Create(1), "", True, 0, 1, 0, "Use these settings on new geometry", "Uses current settings as defaults for new items", "", 1, 0, 1]]],
			   [EVENT_LIGHT_SET, True, "Lights Setup", [0.75,1.0,0.75,1.0],
			   [[Blender.Draw.Create(1), "", True, 1, 1, 0, "LampF", "Select the light to setup", "Select Light", 1, 0, 1],
			    [Blender.Draw.Create(1), "", False, 1, 1, 0, ["Light Archive:%t|Read Archive|Inline Code", "Read Archive", "Inline Code"], "Set the archive method for this light", "Light Archive", 1, 0, 1],
			    [0, "", False, 5, 1, 0, "", "", "", 1, 0, 1],
			    [Blender.Draw.Create(1), "", False, 1, 1, 0, "CodeF", "Insert custom code fragment into beginning of light block", "Light Begin Code", 1, 0, 1],
			    [Blender.Draw.Create(1), "", False, 1, 1, 0, "CodeF", "Insert custom code fragment into end of light block", "Light End Code", 1, 0, 1],
			    [0, "", False, 5, 1, 0, "", "", "", 1, 0, 1],
			    [Blender.Draw.Create(1), "", False, 1, 1, 0, "LightF", "Set shader for this light", "Light Shader", 1, 0, 1],
			    [Blender.Draw.Create(0), "", False, 3, 2, 0, "Light MBlur", "Enables motion blur (transform, shader)", "LightMBlur", 0, 0, 1],
			    [Blender.Draw.Create(5), "", False, 2, 2, 1, "frames: ", "Number of frames to blur across", "LightFrames", 5, 2, 1000],
			    [Blender.Draw.Create(1), "", False, 0, 1, 0, "Use these settings on new lights", "Uses current settings as defaults for new items", "", 1, 0, 1]]],
			   [EVENT_MAT_SET, True, "Materials Setup", [1.0,1.0,0.75,1.0],
			   [[Blender.Draw.Create(1), "", True, 1, 1, 0, "MaterialF", "Select the material block to setup", "Select Material", 1, 0, 1],
			    [Blender.Draw.Create(1), "", False, 1, 1, 0, ["Material Archive:%t|Read Archive|Inline Code", "Read Archive", "Inline Code"], "Set the archive method for this material block", "Material Archive", 1, 0, 1],
			    [0, "", False, 5, 1, 0, "", "", "", 1, 0, 1],
			    [Blender.Draw.Create(1), "", False, 1, 1, 0, "CodeF", "Insert custom code fragment into beginning of material block", "Material Begin Code", 1, 0, 1],
			    [Blender.Draw.Create(1), "", False, 1, 1, 0, "CodeF", "Insert custom code fragment into end of material block", "Material End Code", 1, 0, 1],
			    [0, "", False, 5, 1, 0, "", "", "", 1, 0, 1],
			    [Blender.Draw.Create(1), "", False, 1, 1, 0, "SurfaceF", "Set surface shader for this material block", "Surface Shader", 1, 0, 1],
			    [Blender.Draw.Create(1), "", False, 1, 1, 0, "DisplacementF", "Set displacement shader for this material block", "Displacement Shader", 1, 0, 1],
			    [Blender.Draw.Create(1), "", False, 1, 1, 0, "VolumeF", "Set interior volume shader for this material block", "Int Volume Shader", 1, 0, 1],
			    [Blender.Draw.Create(1), "", False, 1, 1, 0, "VolumeF", "Set exterior volume shader for this material block", "Ext Volume Shader", 1, 0, 1],
			    [Blender.Draw.Create(1), "", False, 1, 1, 0, "LightF", "Set arealight shader for this material block", "Area Light Shader", 1, 0, 1],
			    [Blender.Draw.Create(0), "", False, 3, 2, 0, "Shader MBlur", "Enables motion blur (all animated shader parameters)", "ShaderMBlur", 0, 0, 1],
			    [Blender.Draw.Create(5), "", False, 2, 2, 1, "frames: ", "Number of frames to blur across", "ShaderFrames", 5, 2, 1000],
			    [Blender.Draw.Create(1), "", False, 0, 1, 0, "Use these settings on new materials", "Uses current settings as defaults for new items", "", 1, 0, 1]]]]

#Array of dialogs
DialogData		= [#File Filter Dialog
			   [("Code Fragment: ", Create(Filters[0]), 0, 100, "Text name filter for code fragments (blank will show all files)"),
			    ("Shader Source: ", Create(Filters[1]), 0, 100, "Text name filter for shader source GENERALLY LEAVE AS IS!!!!"),
			    ("Surface Shader: ", Create(Filters[2]), 0, 100, "Text name filter for surface shaders (blank will show all files)"),
			    ("Displace Shade: ", Create(Filters[3]), 0, 100, "Text name filter for displacement shaders (blank will show all files)"),
			    ("Volume Shader: ", Create(Filters[4]), 0, 100, "Text name filter for volume shaders (blank will show all files)"),
			    ("Imager Shader: ", Create(Filters[5]), 0, 100, "Text name filter for showing image shaders (blank will show all files)"),
			    ("Light Shader: ", Create(Filters[6]), 0, 100, "Text name filter for all light shaders (blank will show all files)"),
			    ("Shader Include: ", Create(Filters[7]), 0, 100, "Text name filter for shader include GENERALLY LEAVE AS IS!!!!")],
			   #Shader Fragment Name Dialog
			   [("", Create(""), 0, 100, "The text name to save shader fragment as")],
			   #Renderman Binary Dialog
			   [("", Create(RenderBin), 0, 100, "Use <RIB> in options to place input rib, appended if unused")],
			   #Shader Compiler Binary Dialog
			   [("", Create(CompilerBin), 0, 100, "Use <SHADER> in options to place input shader, appended if unused (requires BMRT like ouput)")],
			   #Texture Optimizer Dialog
			   [("", Create(TexmakeBin), 0, 100, "Use <TEX> in options to place input texture, appended if unused")],
			   #Shader Info Dialog
			   [("", Create(InfoBin), 0, 100, "Define the shader info binary (used by Shader Fragment utilities)")],
			   #Shader Name Dialog
			   [("", Create(""), 0, 100, "Type the name of a shader already compiled and available for this renderer")],
			   #Range Multiplier and Adder Dialog
			   [("Multiply Range", Create("1.0"), 0, 100, "This allows you to multiply the control value allowing you to change its range"),
			    ("Adder to Range", Create("0.0"), 0, 100, "After multiplication this allows you to shift the new control value range")],
			   #Manual Parameter Value Dialog
			   [("", Create(""), 0, 100, "Type the string you want to manually ad to this parameter")]]


####################################################################### START USER GLOBAL FUNCTIONS
#### Default shudown routine
def Shutdown():
	print "MOSAIC shutting down..."
	Exit()
	
	
#### Show a error
def ErrorPopup(errortext):
	print "ERROR: "+errortext
	PupMenu("ERROR: "+errortext)


#### Generate a project folder name from "Project Setup"->"Project Folder" entry or use default if not set
def GetProjectFolder():
	global RenderDir, ProjectDir, ButtonData
	ProjectDir = RenderDir+GetProperty(Blender.Scene.Get()[0], ButtonData[PROJECT][WIN_BUTS][PROJECT_FOLDER][BUT_PROP], "", ButtonData[PROJECT][WIN_BUTS][PROJECT_FOLDER][BUT_DEFAULT])+sys.sep
	return ProjectDir


#### Create passed "OutputDir" and all standard project folders
def SetupDirectories(OutputDir):
	if (OutputDir):
		try:
			if (sys.exists(OutputDir) != 2):				os.mkdir(OutputDir)
			if (sys.exists(OutputDir+"Cache") != 2):			os.mkdir(OutputDir+"Cache")
			if (sys.exists(OutputDir+"Shaders") != 2):			os.mkdir(OutputDir+"Shaders")
			if (sys.exists(OutputDir+"Maps") != 2):				os.mkdir(OutputDir+"Maps")
			if (sys.exists(OutputDir+"Archives") != 2):			os.mkdir(OutputDir+"Archives")
			if (sys.exists(OutputDir+"Archives"+sys.sep+"Scenes") != 2):	os.mkdir(OutputDir+"Archives"+sys.sep+"Scenes")
			if (sys.exists(OutputDir+"Archives"+sys.sep+"Materials") != 2):	os.mkdir(OutputDir+"Archives"+sys.sep+"Materials")
			if (sys.exists(OutputDir+"Archives"+sys.sep+"Lights") != 2):	os.mkdir(OutputDir+"Archives"+sys.sep+"Lights")
			if (sys.exists(OutputDir+"Archives"+sys.sep+"Cameras") != 2):	os.mkdir(OutputDir+"Archives"+sys.sep+"Cameras")
			if (sys.exists(OutputDir+"Archives"+sys.sep+"Geometry") != 2):	os.mkdir(OutputDir+"Archives"+sys.sep+"Geometry")
			if (sys.exists(OutputDir+"Archives"+sys.sep+"Objects") != 2 ):	os.mkdir(OutputDir+"Archives"+sys.sep+"Objects")
		except:
			ErrorPopup("Could not write output directories, check paths and permissions!")
			return 1
		return 0


#### Removes passed Directory and everything in them!
def DelTree(Directory, RemoveRoot = False):
	if (Directory and sys.exists(Directory)):
		for root, dirs, files in os.walk(Directory, topdown=False):
			for name in files:
				os.remove(os.path.join(root, name))
			for name in dirs:
				os.rmdir(os.path.join(root, name))
		if (RemoveRoot): os.rmdir(Directory)


#### Exports blender text as a text file in current directory
def ExportText(blenderText):
	try:
		textfile = open(blenderText.name, 'wb')
		for line in blenderText.asLines():
			textfile.write(line+"\n")
		textfile.close()
	except:
		ErrorPopup("Could not export text file, check paths and permissions!")
		return 1
	return 0

#### Creates and compiles shader in current directory from passed blender text object containing shader source
def CompileShader(shaderText):
	global CompilerBin
	if (not CompilerBin):
		ErrorPopup("Must set shader compiler binary under MOSAIC setting tab!")
		return 0
	print "\tWriting Shader "+shaderText.name+"..."
	if (ExportText(shaderText)): return 1
	print "\tCompiling Shader "+shaderText.name+"..."
	compileCall = CompilerBin
	if (compileCall.count("<SHADER>")): compileCall = compileCall.replace("<SHADER>", shaderText.name)
	else: compileCall = compileCall+" \""+shaderText.name+"\""
	os.system(compileCall)
	return 0


#### Creates a string with the number of tabs requested
def CreateTabs(tabLevel = 1):
	tabString = ""
	while tabLevel > 0:
		tabString	= tabString+"\t"
		tabLevel	= tabLevel-1
	return tabString


#### Adds tabs to beginning of each line of passed list
def AddTabs(List, TabLevel):
	if (List and TabLevel):
		for index, item in enumerate(List):
			List[index] = CreateTabs(TabLevel)+item
	return List


#### Looks for Object[Property][SubProperty] and return property value or OnError value
def GetProperty(Object, Property, SubProperty = "", OnError = False):
	try:
		if (SubProperty): return Object.properties[Property][SubProperty]
		else: return Object.properties[Property]
	except: return OnError


#### Parse tokens in source strings based on passed Object type
#### Object can be a single object or object list, if it is a list it will cycle through each object type parsing tokens for each type in the line
def ParseTokens(Scene, tokenObjects, Source):
	global lightList, ProjectDir
	if (Source and Source.count('<')):				#Only process if theres source code and it has tokens!
		if (type(tokenObjects) != list):	Objects = [tokenObjects] #If this is not a list then put object in list
		else:					Objects = tokenObjects
		for original in [block[0] for block in [end.split('>') for end in [start for start in Source.split('<')]] if len(block) > 1]: #Cycle through any tokens in this source line
			
			token		= ''
			tokenType	= ''
			texIndex	= -1
			rangeAdder	= 0.0
			rangeMulti	= 1.0
			controlValue	= 'NONE'
			controlString	= "\"Token Error\""
			world		= Scene.world			#Get this scenes world data for tokens
			
			for index, parameter in enumerate(original.split('_')): #Extract token parameters to be processed
				try:
					if (index == 0):					token		= parameter
					elif (parameter[0] == 'X'):				texIndex	= int(parameter.lstrip('X'))-1
					elif (parameter[0] == 'A'):				rangeAdder	= float(parameter.lstrip('A'))
					elif (parameter[0] == 'M' and len(parameter) > 1):	rangeMulti	= float(parameter.lstrip('M'))
					else:							tokenType	= parameter
				except:
					ErrorPopup("Invalid token parameter \""+parameter+"\" in <"+original+"> using defaults instead!")
					continue			#If theres an error skip token parameter and go to next one
			
			for Object in Objects:
				#Global parameters
				if (token.count('#') == len(token)):				controlValue = str(Scene.render.cFrame)
				elif (token == "ProjectDir"):					controlValue = ProjectDir
				elif (token == "ObjectName"):
					if (Object):						controlValue = Object.name #Pass objects name through token
					elif (Scene):						controlValue = Scene.name #If no object pass scenes name through token
				elif (token == "SceneAspX"):					controlValue = Scene.render.aspectX
				elif (token == "SceneAspY"):					controlValue = Scene.render.aspectY
				elif (token == "SceneEdgeColor"):				controlValue = list(Scene.render.edgeColor)
				elif (token == "SceneEnd"):					controlValue = Scene.render.eFrame
				elif (token == "SceneFps"):					controlValue = Scene.render.fps
				elif (token == "SceneBf"):					controlValue = Scene.render.mblurFactor
				elif (token == "SceneFilterSize"):				controlValue = Scene.render.gaussFilter
				elif (token == "ScenePlanes"):					controlValue = Scene.render.imagePlanes
				elif (token == "SceneOSALevel"):				controlValue = Scene.render.OSALevel
				elif (token == "SceneStart"):					controlValue = Scene.render.sFrame
				elif (token == "SceneSizeX"):					controlValue = Scene.render.sizeX
				elif (token == "SceneSizeY"):					controlValue = Scene.render.sizeY
				elif (token == "SceneXparts"):					controlValue = Scene.render.xParts
				elif (token == "SceneYparts"):					controlValue = Scene.render.yParts
				elif (world):				#Is there world data to check?
					if (token == "WorldAmbCol"):				controlValue = list(world.getAmb())
					elif (token == "WorldHorCol"):				controlValue = list(world.getHor())
					elif (token == "WorldZenCol"):				controlValue = list(world.getZen())
					elif (token == "WorldMist"):				controlValue = world.getMist()[0]
					elif (token == "WorldSta"):				controlValue = world.getMist()[1]
					elif (token == "WorldDi"):				controlValue = world.getMist()[2]
					elif (token == "WorldHi"):				controlValue = world.getMist()[3]
					elif (token == "WorldSize"):				controlValue = world.getStar()[3]
					elif (token == "WorldMinDist"):				controlValue = world.getStar()[4]
					elif (token == "WorldStarDist"):			controlValue = world.getStar()[5]
					elif (token == "WorldColnoise"):			controlValue = world.getStar()[6]
				if (controlValue != 'NONE'):	break	#If already found then break!
				
				#Object and type based parameters
				if (type(Object) == Blender.Types.ObjectType):	#Used for all object based parameters
					if (token == "TO" or token == "FROM"):	#To and from can be used for any object
						m = Object.mat			#Global matrix
						if (token == "TO" and tokenType == 'P'):
							controlValue	= [-m[2][0]+m[3][0], -m[2][1]+m[3][1], -m[2][2]+m[3][2]] #To point
						if (token == "TO" and (tokenType == 'V' or tokenType == 'N')):
							controlValue	= list(Blender.Mathutils.Vector([-m[2][0]+m[3][0], -m[2][1]+m[3][1], -m[2][2]+m[3][2]]).normalize()) #To vector/normal
						if (token == "FROM" and tokenType == 'P'):
							controlValue	= [m[3][0]/m[3][3], m[3][1]/m[3][3], m[3][2]/m[3][3]] #From point
						if (token == "FROM" and tokenType == 'M'):
							controlValue	= list(m) #From matrix
					elif (token == "LightID"):
						if (lightList.count([Object, True])):		controlValue = lightList.index([Object, True])+1 #Illuminate ID for lights and arealight objects
						else:						controlValue = 'SKIP'
					
					elif (Object.getType() == "Lamp"): #Used for light parameters
						if (token == "LampLightColor"):			controlValue = list(Object.getData().col)
						elif (token == "LampEnergy"):			controlValue = Object.getData().energy
						elif (token == "LampDist"):			controlValue = Object.getData().dist
						elif (token == "LampSpotSi"):			controlValue = Object.getData().spotSize*0.0174532925199
						elif (token == "LampSpotBl"):			controlValue = Object.getData().spotBlend
						elif (token == "LampShadBufSize"):		controlValue = Object.getData().bufferSize
						elif (token == "LampSamples"):			controlValue = Object.getData().samples
						elif (token == "LampHaloInt"):			controlValue = Object.getData().haloInt
						elif (token == "LampBias"):			controlValue = Object.getData().bias
						elif (token == "LampSoft"):			controlValue = Object.getData().softness
						elif (token == "LampClipSta"):			controlValue = Object.getData().clipStart
						elif (token == "LampClipEnd"):			controlValue = Object.getData().clipEnd
						elif (token == "LampSizeX"):			controlValue = Object.getData().areaSizeX
						elif (token == "LampSizeY"):			controlValue = Object.getData().areaSizeY
						elif (token == "LampSamplesX"):			controlValue = Object.getData().raySamplesX
						elif (token == "LampSamplesY"):			controlValue = Object.getData().raySamplesY
						elif (token == "LampHaloStep"):			controlValue = Object.getData().haloStep
						elif (token == "LampQuad1"):			controlValue = Object.getData().quad1
						elif (token == "LampQuad2"):			controlValue = Object.getData().quad2
					elif (Object.getType() == "Camera"): #Used for camera parameters
						if (token == "CameraAlpha"):			controlValue = Object.getData().alpha
						elif (token == "CameraAngle"):			controlValue = Object.getData().angle
						elif (token == "CameraEnd"):			controlValue = Object.getData().clipEnd
						elif (token == "CameraStart"):			controlValue = Object.getData().clipStart
						elif (token == "CameraDofDist"):		controlValue = Object.getData().dofDist
						elif (token == "CameraSize"):			controlValue = Object.getData().drawSize
						elif (token == "CameraLens"):			controlValue = Object.getData().lens
						elif (token == "CameraScale"):			controlValue = Object.getData().scale
						elif (token == "CameraX"):			controlValue = Object.getData().shiftX
						elif (token == "CameraY"):			controlValue = Object.getData().shiftY
				elif (type(Object) == Blender.Types.MaterialType): #Used for material parameters
					if (token == "MatHaloAdd"):				controlValue = Object.add
					elif (token == "MatAmb"):				controlValue = Object.amb
					elif (token == "MatDiffuseDark"):			controlValue = Object.diffuseDarkness
					elif (token == "MatDiffuseSize"):			controlValue = Object.diffuseSize
					elif (token == "MatDiffuseSmooth"):			controlValue = Object.diffuseSmooth
					elif (token == "MatEmit"):				controlValue = Object.emit
					elif (token == "MatRayFilt"):				controlValue = Object.filter
					elif (token == "MatFlareBoost"):			controlValue = Object.flareBoost
					elif (token == "MatFlareSeed"):				controlValue = Object.flareSeed
					elif (token == "MatFlareSize"):				controlValue = Object.flareSize
					elif (token == "MatMirrorFresnel"):			controlValue = Object.fresnelDepth
					elif (token == "MatMirrorFac"):				controlValue = Object.fresnelDepthFac
					elif (token == "MatRayFresnel"):			controlValue = Object.fresnelTrans
					elif (token == "MatRayFac"):				controlValue = Object.fresnelTransFac
					elif (token == "MatHaloSeed"):				controlValue = Object.haloSeed
					elif (token == "MatHaloSize"):				controlValue = Object.haloSize
					elif (token == "MatHard"):				controlValue = Object.hard
					elif (token == "MatRayIOR"):				controlValue = Object.IOR
					elif (token == "MatMirrorColor"):			controlValue = list(Object.mirCol)
					elif (token == "MatFlares"):				controlValue = Object.nFlares
					elif (token == "MatLines"):				controlValue = Object.nLines
					elif (token == "MatRings"):				controlValue = Object.nRings
					elif (token == "MatStar"):				controlValue = Object.nStars
					elif (token == "MatRayMir"):				controlValue = Object.rayMirr
					elif (token == "MatMirrorDepth"):			controlValue = Object.rayMirrDepth
					elif (token == "MatRef"):				controlValue = Object.ref
					elif (token == "MatRefr"):				controlValue = Object.refracIndex
					elif (token == "MatCol"):				controlValue = list(Object.rgbCol)
					elif (token == "Matrms"):				controlValue = Object.rms
					elif (token == "MatRough"):				controlValue = Object.roughness
					elif (token == "MatShadA"):				controlValue = Object.shadAlpha
					elif (token == "MatSpec"):				controlValue = Object.spec
					elif (token == "MatSpecCol"):				controlValue = list(Object.specCol)
					elif (token == "MatSpecSize"):				controlValue = Object.specSize
					elif (token == "MatSpecSmooth"):			controlValue = Object.specSmooth
					elif (token == "MatSpecTra"):				controlValue = Object.specTransp
					elif (token == "MatSSSBack"):				controlValue = Object.sssBack
					elif (token == "MatSSSCol"):				controlValue = list(Object.sssCol)
					elif (token == "MatSSSColBlend"):			controlValue = Object.sssColorBlend
					elif (token == "MatSSSError"):				controlValue = Object.sssError
					elif (token == "MatSSSIOR"):				controlValue = Object.sssIOR
					elif (token == "MatSSSRadiusB"):			controlValue = Object.sssRadiusBlue
					elif (token == "MatSSSRadiusR"):			controlValue = Object.sssRadiusRed
					elif (token == "MatSSSRadiusG"):			controlValue = Object.sssRadiusGreen
					elif (token == "MatSSSTex"):				controlValue = Object.sssTextureScatter
					elif (token == "MatHaloSubSize"):			controlValue = Object.subSize
					elif (token == "MatRayDepth"):				controlValue = Object.transDepth
					elif (token == "MatTranslu"):				controlValue = Object.translucency
					elif (token == "MatZoffs"):				controlValue = Object.zOffset
					elif (texIndex > -1 and texIndex < 10):	#Are we using a texture token
						maps = Object.getTextures()
						if (maps[texIndex]):		#Is there a mapping available at given index
							if (token == "MatMapColor"):		controlValue = list(maps[texIndex].col)
							elif (token == "MatMapCol"):		controlValue = maps[texIndex].colfac
							elif (token == "MatMapDisp"):		controlValue = maps[texIndex].dispfac
							elif (token == "MatMapDVar"):		controlValue = maps[texIndex].dvar
							elif (token == "MatMapNor"):		controlValue = maps[texIndex].norfac
							elif (token == "MatMapOfsX"):		controlValue = maps[texIndex].ofs[0]
							elif (token == "MatMapOfsY"):		controlValue = maps[texIndex].ofs[1]
							elif (token == "MatMapOfsZ"):		controlValue = maps[texIndex].ofs[2]
							elif (token == "MatMapSizeX"):		controlValue = maps[texIndex].size[0]
							elif (token == "MatMapSizeY"):		controlValue = maps[texIndex].size[1]
							elif (token == "MatMapSizeZ"):		controlValue = maps[texIndex].size[2]
							elif (token == "MatMapVar"):		controlValue = maps[texIndex].varfac
							elif (token == "MatMapWarp"):		controlValue = maps[texIndex].warpfac
							tex = maps[texIndex].tex
							if (tex):		#Is there a texture available for this mapping
								if (token == "MatTexFrames"):	controlValue = tex.animFrames
								elif (token == "MatTexOffs"):	controlValue = tex.animOffset
								elif (token == "MatTexStartFr"):controlValue = tex.animStart
								elif (token == "MatTexBright"):	controlValue = tex.brightness
								elif (token == "MatTexContr"):	controlValue = tex.contrast
								elif (token == "MatTexMinX"):	controlValue = tex.crop[0]
								elif (token == "MatTexMaxX"):	controlValue = tex.crop[2]
								elif (token == "MatTexMinY"):	controlValue = tex.crop[1]
								elif (token == "MatTexMaxY"):	controlValue = tex.crop[3]
								elif (token == "MatTexFieIma"):	controlValue = tex.fieldsPerImage
								elif (token == "MatTexFilter"):	controlValue = tex.filterSize
								elif (token == "MatTexXrepeat"):controlValue = tex.repeat[0]
								elif (token == "MatTexYrepeat"):controlValue = tex.repeat[1]
								elif (token == "MatTexColor"):	controlValue = list(tex.rgbCol)
								elif (token == "MatTexDistAmnt"):controlValue = tex.distAmnt
								elif (token == "MatTexExp"):	controlValue = tex.exp
								elif (token == "MatTexiScale"):	controlValue = tex.iScale
								elif (token == "MatTexH"):	controlValue = tex.hFracDim
								elif (token == "MatTexLacu"):	controlValue = tex.lacunarity
								elif (token == "MatTexNDepth"):	controlValue = tex.noiseDepth
								elif (token == "MatTexNSize"):	controlValue = tex.noiseSize
								elif (token == "MatTexOcts"):	controlValue = tex.octs
								elif (token == "MatTexTurb"):	controlValue = tex.turbulence
								elif (token == "MatTexW1"):	controlValue = tex.weight1
								elif (token == "MatTexW2"):	controlValue = tex.weight2
								elif (token == "MatTexW3"):	controlValue = tex.weight3
								elif (token == "MatTexW4"):	controlValue = tex.weight4
								image = tex.image
								if (image and image.has_data):
									if (token == "MatImageName"):	controlValue = sys.basename(image.filename)
									elif (token == "MatImageSizeX"):controlValue = image.size[0]
									elif (token == "MatImageSizeY"):controlValue = image.size[1]
									elif (token == "MatImageDepth"):controlValue = image.depth
									elif (token == "MatImageStart"):controlValue = image.start
									elif (token == "MatImageEnd"):	controlValue = image.end
									elif (token == "MatImageSpeed"):controlValue = image.speed
									elif (token == "MatImageXrep"):	controlValue = image.xrep
									elif (token == "MatImageYrep"):	controlValue = image.yrep
				if (controlValue != 'NONE'):	break	#If already found then break!
			
			if(controlValue != 'NONE' and controlValue != 'SKIP'): #If we have a valid value then process
				if (type(controlValue) == str):		#Lets process string types
					if (token.count('#') == len(token)): #Lets process frame number string
						controlString = token.replace('#', '0')[len(controlValue):len(token)]+controlValue
					if (tokenType == 'S'):
						controlString = "\""+controlValue+"\""
				elif (type(controlValue) == list):	#Lets process list types
					if (len(controlValue) == 3 and (tokenType == 'P' or tokenType == 'N' or tokenType == 'V' or tokenType == 'C')):
						controlString = "[ "+str(controlValue[0])+" "+str(controlValue[1])+" "+str(controlValue[2])+" ]"
					elif (len(controlValue) == 4 and tokenType == 'M'):
						controlString = "[ "+str(controlValue[0][0])+" "+str(controlValue[0][1])+" "+str(controlValue[0][2])+" "+str(controlValue[0][3])+" "+str(controlValue[1][0])+" "+str(controlValue[1][1])+" "+str(controlValue[1][2])+" "+str(controlValue[1][3])+" "+str(controlValue[2][0])+" "+str(controlValue[2][1])+" "+str(controlValue[2][2])+" "+str(controlValue[2][3])+" "+str(controlValue[3][0])+" "+str(controlValue[3][1])+" "+str(controlValue[3][2])+" "+str(controlValue[3][3])+" ]"
					elif (len(controlValue) == 4 and tokenType == 'H'):
						controlString = "[ "+str(controlValue[0])+" "+str(controlValue[1])+" "+str(controlValue[2])+" "+str(controlValue[3])+" ]"
				else:					#Lets processes whatever where left with
					controlValue = (float(controlValue)*rangeMulti)+rangeAdder #Lets adjust values range based on user token parameters
					if (tokenType == 'I'):
						if (token == "LightID"):	controlString = str(int(controlValue)) #For integer as command
						else:				controlString = "[ "+str(int(controlValue))+" ]" #For integer as parameter
					elif (tokenType == 'F'): controlString	= "[ "+str(float(controlValue))+" ]" #For float
			if(controlValue != 'SKIP'):			#If we are not skipping then write token (used to give multiple objects a chance to be valid!)
				if(controlString == "\"Token Error\""):  ErrorPopup("Check spelling or type for token <"+original+">") #Show token error if there was one
				Source = Source.replace('<'+original+'>', controlString) #Now at last, lets insert the control value over the token
	return Source


#### Interprete any tokens for custom code fragment
def ParseFragment(Scene, Object, FragmentName, TabLevel = 0):
	fragment = []
	if (FragmentName):						#Dont process if theres no name
		text = [Text for Text in Blender.Text.Get() if Text and Text.name == FragmentName] #Try and get FragmentName text
		if (text):						#If no text by that name then do nothing
			for index, line in enumerate(text[0].asLines()): #Process text line by line
				fragment.append(CreateTabs(TabLevel)+ParseTokens(Scene, Object, line)+"\n") #Processes any tokens in text
				errorCount = fragment[index].count("\"Token Error\"") #See if there were any errors
				if (errorCount): ErrorPopup(str(errorCount)+" error/s in fragment \""+FragmentName+"\" on line "+str(index+1)) #If there were any errors then report them
	return fragment


#### Passes parameters to function pointer to generate RIB code that is either passed straight through or wrapped in motion block through blurLength frames according to useBlur state
def MotionBlock(Scene, functionPointer, functionParam1 = "", functionParam2 = "", functionParam3 = "", useBlur = False, blurLength = 1, tabLevel = 0):
	motionCode					= []
	if (functionPointer):						#If we cant generate code then return blank
		beginCode				= "MotionBegin [ "
		startFrame				= Scene.render.currentFrame() #Get current frame so we can reset later
		if (useBlur):				blurFrame = blurLength
		else:					blurFrame = 1
		while blurFrame > 0:					#Cycle through the number of frames specified adjusting the render frame accordingly
			if (startFrame-blurFrame+1 > 0):Scene.render.currentFrame(startFrame-blurFrame+1) #Set frame back to blur length
			else:				Scene.render.currentFrame(1) #If blurLength is before first frame just make first frame
			functionReturn			= functionPointer(functionParam1, functionParam2, functionParam3) #Create code
			if (functionReturn != 'NORIB'):	motionCode.extend(functionReturn)
			else:				return functionReturn #If an error was returned then pass it straight through
			if (motionCode and useBlur):	print CreateTabs(tabLevel)+"- Motion blur pass "+str((blurLength-blurFrame)+1)+" of "+str(blurLength)
			blurFrame			= blurFrame-1	#Update frame
			beginCode			= beginCode+str(1.0-(float(blurFrame)/float(blurLength-1)))+" " #Add position for last change to header
		if (motionCode and useBlur):
			motionCode			= AddTabs(motionCode, 1) #Tab motion block body
			motionCode.insert(0, beginCode+"]\n")		#Add motion block begin
			motionCode.append("MotionEnd\n")		#Add motion block end
		Scene.render.currentFrame(startFrame)			#Reset frame to were we started
	return motionCode


#### Generate RIB code for material opacity
def RibifyOpacity(Material, Dummy1 = False, Dummy2 = False):
	opacity = []
	if (Material): opacity = ["Opacity [ "+str(Material.alpha)+" "+str(Material.alpha)+" "+str(Material.alpha)+" ]\n"]
	return opacity


#### Generate RIB code for material color
def RibifyColor(Material, Dummy1 = False, Dummy2 = False):
	color = []
	if (Material): color = ["Color [ "+str(Material.rgbCol[0])+" "+str(Material.rgbCol[1])+" "+str(Material.rgbCol[2])+" ]\n"]
	return color


#### Generate RIB code for light groups for passed material as a collection of RiIlluminate on and offs for all lights in LightList
def RibifyLightgroup(Material, TabLevel = 0):
	global lightList
	lightgroupCode = []
	if (Material and Material.lightGroup):
		lightgroupCode.append("##Light Group Illuminates\n")
		for index, light in enumerate(lightList):
			if (light[1]):					#Only process light if it is used in this scene
				if ([True for GrLight in Material.lightGroup.objects if GrLight == light[0]]): lightgroupCode.append(CreateTabs(TabLevel)+"Illuminate "+str(index+1)+" 1\n")
				else: lightgroupCode.append(CreateTabs(TabLevel)+"Illuminate "+str(index+1)+" 0\n")
	return lightgroupCode


#### Returns token interpreted RIB code for shader code in TextName
def RibifyShader(Scene, Material, TextName):
	Shader = []
	if (TextName): Shader = ParseFragment(Scene, Material, TextName)
	return Shader


#### Generate RIB code for poly, mesh, clouds and sds, separating elements by passed material index
def RibifyMesh(Object, materialIndex, Dummy1 = False):
	global killExport
	geoCode		= []
	sdsObject	= False						#Track if object is using sds mod
	for modifier in Object.modifiers:				#Cycle through object modifiers to determine if this is an sds object
		if (modifier.type == Modifier.Types.SUBSURF):
			sdsObject = True
	mesh = Blender.Mesh.New()					#Create new object for render
	mesh.getFromObject(Object, 0, 1)				#Extract display ready mesh for render
	npolyCode	= []
	nvertCode	= []
	vertsCode 	= []
	normalCode	= []
	uvCode		= []
	colorCode	= []
	sdsTagCode	= []
	sdsTagNint	= []
	sdsTagNfloat1	= []
	sdsTagNfloat2	= []
	allSmooth	= True
	allFlat		= True
	delFaces	= False
	
	if (mesh.faces):						#Only process mesh if it has faces
		if (mesh.materials and mesh.materials[materialIndex]):
			halo = mesh.materials[materialIndex].mode&Material.Modes.HALO
		else:	halo	= False
		
		mesh.sel	= False					#Make sure nothing is selected on mesh
		for face in mesh.faces:					#Isolate faces that are using same material as passed
			if (face.mat == materialIndex):
				face.sel		= True
				if (face.smooth):	allFlat	= False
				else:			allSmooth = False
			else: delFaces			= True
		if (delFaces):
			mesh.faces.delete(1, [face for face in mesh.faces if not face.sel]) #Remove any faces and edges that are not using passed material
			mesh.verts.delete([vert for vert in mesh.verts if not vert.sel]) #Remove any vertices that are not using passed material
		
		for vert in mesh.verts:					#Cycle through vertices and generate code
			vertsCode.extend([str(vert.co[0])+" ", str(vert.co[1])+" ", str(vert.co[2])+" "])
		
		if (vertsCode):						#Only process faces if there are verts
			if (not halo):					#Only process faces if this is not a halo
				for face in mesh.faces:			#Cycle through meshes faces
					while QTest():			#Cycle through events looking for an esc
						if (QRead()[0] == ESCKEY): #If user escaped
							killExport = True
							return []
					faceSides = len(face)
					npolyCode.append(str(faceSides)+" ")
					nvertCode.extend([str(face.v[0].index)+" ", str(face.v[1].index)+" ", str(face.v[2].index)+" "])
					if (faceSides == 4): nvertCode.append(str(face.v[3].index)+" ")
					if (mesh.faceUV):			#Process face UV if there are any
						uvCode.extend([str(face.uv[0][0])+" ", str(1.0-face.uv[0][1])+" ", str(face.uv[1][0])+" ", str(1.0-face.uv[1][1])+" ", str(face.uv[2][0])+" ", str(1.0-face.uv[2][1])+" "])
						if (faceSides == 4): uvCode.extend([str(face.uv[3][0])+" ", str(1.0-face.uv[3][1])+" "])
					if (mesh.vertexColors):			#Process faces vertex colors if there are any
						colorCode.extend([str(face.col[0][0]/256.0)+" ", str(face.col[0][1]/256.0)+" ", str(face.col[0][2]/256.0)+" ", str(face.col[1][0]/256.0)+" ", str(face.col[1][1]/256.0)+" ", str(face.col[1][2]/256.0)+" ", str(face.col[2][0]/256.0)+" ", str(face.col[2][1]/256.0)+" ", str(face.col[2][2]/256.0)+" "])
						if (faceSides == 4): colorCode.extend([str(face.col[3][0]/256.0)+" ", str(face.col[3][1]/256.0)+" ", str(face.col[3][2]/256.0)+" "])
					if ((sdsObject and not allSmooth) or (not sdsObject and not allFlat)): #Process face normals if renderman primitive defaults wont work
						if (face.smooth):
							normalCode.extend([str(face.v[0].no[0])+" ", str(face.v[0].no[1])+" ", str(face.v[0].no[2])+" ", str(face.v[1].no[0])+" ", str(face.v[1].no[1])+" ", str(face.v[1].no[2])+" ", str(face.v[2].no[0])+" ", str(face.v[2].no[1])+" ", str(face.v[2].no[2])+" "])
							if (faceSides == 4): normalCode.extend([str(face.v[3].no[0])+" ", str(face.v[3].no[1])+" ", str(face.v[3].no[2])+" "])
						else:
							normalCode.extend([str(face.no[0])+" ", str(face.no[1])+" ", str(face.no[2])+" ", str(face.no[0])+" ", str(face.no[1])+" ", str(face.no[2])+" ", str(face.no[0])+" ", str(face.no[1])+" ", str(face.no[2])+" "])
							if (faceSides == 4): normalCode.extend([str(face.no[0])+" ", str(face.no[1])+" ", str(face.no[2])+" "])
			
				if (sdsObject):				#If this is a sds process edge creases
					for edge in mesh.edges:
						if (edge.crease > 0):	#Only process edges that have crease data
							sdsTagCode.append(" \"crease\"")
							sdsTagNint.append(" 2 1")
							sdsTagNfloat1.extend([" "+str(edge.v1.index), " "+str(edge.v2.index)])
							crease = (edge.crease/255.0)*5.5 #Calculate crease up to 5.5 (looks the same as blenders up to that point)
							if (crease > 5.0): crease = crease+((crease-5.0)*6) #After 5.0 increase sharpening rate to match blenders rate
							sdsTagNfloat2.append(" "+str(crease)) #Not quite using fully square edge (10.0) but seems to match blenders creasing
					geoCode.append("SubdivisionMesh \"catmull-clark\"\n")
				else:	geoCode.append("PointsPolygons\n")
			else:						#If this is a halo then make a point cloud
				geoCode.append("Points\n")
				sdsObject = False
			
			if (npolyCode):		geoCode.append("\t[ "+"".join(npolyCode)+"]\n")
			if (nvertCode):		geoCode.append("\t[ "+"".join(nvertCode)+"]\n")
			if (sdsObject):		geoCode.append("\t[ \"interpolateboundary\""+"".join(sdsTagCode)+" ] [ 0 0"+"".join(sdsTagNint)+" ] ["+"".join(sdsTagNfloat1)+" ] ["+"".join(sdsTagNfloat2)+" ]\n")
			if (vertsCode):		geoCode.append("\t\"P\" [ "+"".join(vertsCode)+"]\n")
			if (normalCode):	geoCode.append("\t\"N\" [ "+"".join(normalCode)+"]\n")
			if (colorCode):		geoCode.append("\t\"Cs\" [ "+"".join(colorCode)+"]\n")
			if (uvCode):		geoCode.append("\t\"st\" [ "+"".join(uvCode)+"]\n")
			if (halo):		geoCode.append("\t\"constantwidth\" [ "+str(mesh.materials[materialIndex].haloSize/25.0)+" ]\n")
	
	mesh.verts = None						#Lets clean up	
	del(mesh)
	if (not geoCode): geoCode = 'NORIB'
	return geoCode


#### Generate RIB code for curves and point clouds from particles
def RibifyParticles(Object, materialIndex, Dummy1 = False):
	global killExport
	partCode	= []
	vectsCode	= []
	nvectCode	= []
	widthCode	= []
	materials	= Object.getData(False, True).materials
	if (materials and materials[0]):				#If theres materials get strand start and end thickness
		width	= materials[materialIndex].haloSize/25.0
		tip	= width*(materials[materialIndex].hard/100.0)
	else:								#If theres no materials then create strand thickness defaults
		width	= 0.005
		tip	= 0.005
	localMatrix	= Object.getMatrix("worldspace").copy().invert() #Get a copy of this objects world matrix and make it local
	particleData	= [effect for effect in Object.effects if effect.dispMat-1 == materialIndex] #Get all particles with current material
	
	if (particleData and width):					#Are there any particles to process and are they visible
		for effect in particleData:
			particleVects	= effect.getParticlesLoc()
			if (particleVects):
				maxVect		= len(max(particleVects)) #Whats the max static length
				numParticles	= len(particleVects)
				percent		= 0
				if (maxVect < 2):	print "\t\t\tProcessing "+str(numParticles)+" particle points:"
				elif (maxVect == 2): 	print "\t\t\tProcessing "+str(numParticles)+" particle vectors:"
				else:			print "\t\t\tProcessing "+str(numParticles)+" particle strands:"
				print "\t\t\t\t- 0%"
			for partCount, vects in enumerate(particleVects):
				percent		= ((partCount+1.0)/numParticles)*100
				if (not percent%10): print "\t\t\t\t- "+str(int(percent))+"%" #Show percent in 10 increments
				while QTest():				#Cycle through events looking for an esc
					if (QRead()[0] == ESCKEY):	#If user escaped
						killExport = True
						return []
				if (len(vects) > 1):
					if (type(vects) == Blender.Types.vectorType): #If particles are points only
						vects			= vects*localMatrix #Transform vectors into objects local space
						vectsCode.extend([str(vects[0])+" ", str(vects[1])+" ", str(vects[2])+" "])
					elif (maxVect == 2):		#If max static length is 2 points then use this optimization
						vect1			= vects[0]*localMatrix
						vect2			= vects[1]*localMatrix
						nvectCode.append("2 ")
						vectsCode.extend([str(vect1[0])+" ", str(vect1[1])+" ", str(vect1[2])+" ", str(vect2[0])+" ", str(vect2[1])+" ", str(vect2[2])+" "])
						if (width != tip):	widthCode.extend([str(width)+" ", str(tip)+" "])
					else:				#Otherwise particles are static curves
						lastPoint	= len(vects)-1
						for index, point in enumerate(vects): #Cycle through all the points in this strand
							remainder	= index%3 #The remainder of points not within beziers point requirements
							if (remainder and index == lastPoint): addCount = (3-remainder)+1 #How many times to subivide last segment for proper bezier
							else: addCount	= 1
							vectsCount	= lastPoint+addCount
							if (width != tip and (not remainder or index == lastPoint)): #Calculate varying widths on bezier segments breaks only when not using constant width
								widthCode.append(str(width-(((width-tip)/lastPoint)*index))+" ")
							point		= point*localMatrix #Transform vectors into objects local space
							for count in range(addCount): vectsCode.extend([str(point[0])+" ", str(point[1])+" ", str(point[2])+" "]) #Add point or add multiple points to complete a bezier curve
						nvectCode.append(str(vectsCount)+" ")
		if (vectsCode):						#Only draw code if there were particles
			if (not nvectCode):	partCode.append("Points\n")
			elif (maxVect == 2):	partCode.append("Curves \"linear\"\n")
			else:			partCode.append("Curves \"cubic\"\n")
			if (nvectCode): 	partCode.append("\t[ "+"".join(nvectCode)+"] \"nonperiodic\"\n")
			partCode.append("\t\"P\" [ "+"".join(vectsCode)+"]\n")
			if (widthCode):		partCode.append("\t\"width\" [ "+"".join(widthCode)+"]\n")
			else:			partCode.append("\t\"constantwidth\" [ "+str(width)+" ]\n")
	if (not partCode): partCode = 'NORIB'
	return partCode


#### Generate RIB code for curves
def RibifyCurve(Object, materialIndex, Dummy1 = False):
	global killExport
	curveCode		= []
	vectsCode		= []
	nvectCode		= []
	normalCode		= []
	widthCode		= []
	ribbonWidth		= 0.0
	curveData		= Object.getData(False, True)
	materials		= curveData.materials
	if (materials and materials[0]):				#If theres materials get curve start and end thickness
		width		= materials[materialIndex].haloSize/25.0
		tip		= width*(materials[materialIndex].hard/100.0)
	else:								#If theres no materials then set to not create curve
		width		= 0.0
		tip		= 0.0
	
	if (curveData):							#Are there any curves to process
		ribbonWidth	= curveData.getExt1()*2			#Get curve width (if zero then material strand width is used)
		if (ribbonWidth): width = ribbonWidth			#If curve has width set the ribbon width to curve width
		if ([True for curve in curveData if curve.isCyclic()]):	cyclic	= "periodic" #If any curves are cyclic then all curves in this object are cyclic
		else:	cyclic	= "nonperiodic"
		
		if (width):						#Are the curves visible
			for Curve in curveData:
				while QTest():				#Cycle through events looking for an esc
					if (QRead()[0] == ESCKEY):	#If user escaped
						killExport = True
						return []
				if (Curve.getType() == 1 and Curve.getMatIndex() == materialIndex): #Only process bezier curves and curves with passed material index
					for nodeIndex, node in enumerate(Curve): #Cycle through all bezier nodes
						for vectIndex, vect in enumerate(node.vec): #Cycle through all control points in bezier curve
							if (nodeIndex+vectIndex != 0): #Dont use first control point
								if (cyclic == "periodic" or nodeIndex+vectIndex != len(Curve)+1): vectsCode.extend([str(vect[0])+" ", str(vect[1])+" ", str(vect[2])+" "]) #Add points into code list (only use last control point if curves are cyclic)
						if (ribbonWidth):	#Apply custom widths and normals if using a ribbon
							if (node.radius):	widthCode.append(str(width*node.radius)+" ")  #If theres ribbon width then apply width for this point and adjust it by radius
							else:			widthCode.append(str(width)+" ")
							normal	= Mathutils.TriangleNormal(Mathutils.Vector(node.vec[0]), Mathutils.Vector(node.vec[1]), Mathutils.Vector(node.vec[1])+Mathutils.Vector([0.0, 0.0, 1.0])) #Find normal by adding a point with higher z and finding normal
							normal	= normal*Blender.Mathutils.RotationMatrix(180.0-node.tilt*51.42857, 3, "r", Mathutils.Vector(node.vec[0])-Mathutils.Vector(node.vec[1])) #Rotate normal by amount in nodes tilt value
							if (str(normal[0]).lower().find('nan')>=0): normal[0] = 0.0
							if (str(normal[1]).lower().find('nan')>=0): normal[1] = 0.0
							if (str(normal[2]).lower().find('nan')>=0): normal[2] = 0.0
							normalCode.extend([str(normal[0])+" ", str(normal[1])+" ", str(normal[2])+" "])
						elif (width != tip):	#Otherwise apply material base and tip widths if they are set
							widthCode.append(str(width-(((width-tip)/(len(Curve)-1))*nodeIndex))+" ")
					if (cyclic == "periodic"):	#If curves are cyclic
						nvectCode.append(str(len(Curve)*3)+" ")
						vectsCode.extend([str(Curve[0].vec[0][0])+" ", str(Curve[0].vec[0][1])+" ", str(Curve[0].vec[0][2])+" "]) #Add first control point to end of point list for cyclic curve
					else:				#If not...
						nvectCode.append(str((len(Curve)*3)-2)+" ")
				elif (Curve.getMatIndex() == materialIndex):
					print "Only bezier curves supported in RenderMan, skipping this curve!"
			if (vectsCode):					#Only draw code if there were control points
				curveCode.append("Curves \"cubic\"\n")
				curveCode.append("\t[ "+"".join(nvectCode)+"] \""+cyclic+"\"\n")
				curveCode.append("\t\"P\" [ "+"".join(vectsCode)+"]\n")
				if (widthCode):		curveCode.append("\t\"width\" [ "+"".join(widthCode)+"]\n")
				else:			curveCode.append("\t\"constantwidth\" [ "+str(width)+" ]\n")
				if (normalCode):	curveCode.append("\t\"N\" [ "+"".join(normalCode)+"]\n")
	if (not curveCode): curveCode = 'NORIB'
	return curveCode


#### Generate RIB code for NURBS surfaces
def RibifySurface(Object, materialIndex, surfData):
	global killExport
	surfCode		= []
	vectsCode		= []
	if (surfData and materialIndex == 0):				#Does this surface have data (can only use the first material since theres no way to tell what surface uses what material at the moment)
		try:							#Try to access NurvSurf data if cant then assume this is not a surface and return nothing
			if (surfData.cyclicU or surfData.cyclicV): print "Only non cyclic patches available under RiNuPatch, ignoring cyclic tag!"
			nu		= surfData.pointsU
			nv		= surfData.pointsV
			uorder		= surfData.orderU
			vorder		= surfData.orderV
			uknotCount	= nu+uorder
			vknotCount	= nv+vorder
		except:
			print "Only 1x1 or greater NURBS surfaces allowed, skipping this patch!"
			return []
		if (surfData.flagU):	uknots = ["0.0 " for knot in range(0, uorder)]+[str(float(knot)/(uknotCount-(uorder*2)+1))+" " for knot in range(1, uknotCount-(uorder*2)+1)]+["1.0 " for knot in range(uknotCount-uorder, uknotCount)]
		else:				uknots	= [str(float(knot)/uknotCount)+" " for knot in range(0, uknotCount)]
		if (surfData.flagV):	vknots = ["0.0 " for knot in range(0, vorder)]+[str(float(knot)/(vknotCount-(vorder*2)+1))+" " for knot in range(1, vknotCount-(vorder*2)+1)]+["1.0 " for knot in range(vknotCount-vorder, vknotCount)]
		else:				vknots	= [str(float(knot)/vknotCount)+" " for knot in range(0, vknotCount)]
		while QTest():						#Cycle through events looking for an esc
			if (QRead()[0] == ESCKEY):			#If user escaped
				killExport = True
				return []
		for vect in surfData:
			vectsCode.extend([str(vect[0]*vect[3])+" ", str(vect[1]*vect[3])+" ", str(vect[2]*vect[3])+" ", str(vect[3])+" "])
		if (vectsCode):						#Only draw code if there were control points
			surfCode.append("NuPatch\n")
			surfCode.append("\t"+str(nu)+" "+str(uorder)+" [ "+"".join(uknots)+"] 0.0 1.0\n")
			surfCode.append("\t"+str(nv)+" "+str(vorder)+" [ "+"".join(vknots)+"] 0.0 1.0\n")
			surfCode.append("\t\"Pw\" [ "+"".join(vectsCode)+"]\n")
	if (not surfCode): surfCode = 'NORIB'
	return surfCode


#### Generate RIB code for material blocks
def RibifyMaterial(Scene, Object, Material):
	global ButtonData, defaultSurface
	materialCode		= []
	if (Material):
		surfCode	= []
		isGroup		= Material.lightGroup
		Mblur		= GetProperty(Material, ButtonData[MATERIALS][WIN_BUTS][MAT_MBLUR][BUT_PROP], "", ButtonData[MATERIALS][WIN_BUTS][MAT_MBLUR][BUT_DEFAULT])
		Mframes		= GetProperty(Material, ButtonData[MATERIALS][WIN_BUTS][MAT_FRAMES][BUT_PROP], "", ButtonData[MATERIALS][WIN_BUTS][MAT_FRAMES][BUT_DEFAULT])
		isBeginCode	= GetProperty(Material, ButtonData[MATERIALS][WIN_BUTS][MAT_BEGIN_CODE][BUT_PROP])
		isEndCode	= GetProperty(Material, ButtonData[MATERIALS][WIN_BUTS][MAT_END_CODE][BUT_PROP])
		isSurf		= GetProperty(Material, ButtonData[MATERIALS][WIN_BUTS][MAT_SURF][BUT_PROP])
		isDisp		= GetProperty(Material, ButtonData[MATERIALS][WIN_BUTS][MAT_DISP][BUT_PROP])
		isINvol		= GetProperty(Material, ButtonData[MATERIALS][WIN_BUTS][MAT_INT_VOL][BUT_PROP])
		isEXvol		= GetProperty(Material, ButtonData[MATERIALS][WIN_BUTS][MAT_EXT_VOL][BUT_PROP])
		isArea		= GetProperty(Material, ButtonData[MATERIALS][WIN_BUTS][MAT_AREA][BUT_PROP])
		if (isBeginCode and isBeginCode != 'NONE'):
			materialCode.extend(ParseFragment(Scene, Material, isBeginCode)) #Parse custom code
		if (isGroup): materialCode.extend(RibifyLightgroup(Material)) #Create RiIlluminate based on any assigned lightgroups
		if (isSurf and isSurf != 'NONE'):
			surfCode = MotionBlock(Scene, RibifyShader, Scene, Material, isSurf, Mblur, Mframes, 3)
		if (surfCode):
			print "\t\t\t- Surface Shader ("+isSurf+")"
			materialCode.extend(surfCode)		#Surface Shader
		else:
			print "\t\t\t- Default Surface Shader"
			materialCode.extend([defaultSurface[1]])		#Default surface shader
		if (isDisp and isDisp != 'NONE'):
			print "\t\t\t- Displacement Shader ("+isDisp+")"
			materialCode.extend(MotionBlock(Scene, RibifyShader, Scene, Material, isDisp, Mblur, Mframes, 3)) #Displacement shader
		if (isINvol and isINvol != 'NONE'):
			print "\t\t\t- Interior Volume Shader ("+isINvol+")"
			materialCode.extend(MotionBlock(Scene, RibifyShader, Scene, Material, isINvol, Mblur, Mframes, 3)) #Interior volume shader
		if (isEXvol and isEXvol != 'NONE'):
			print "\t\t\t- Exterior Volume Shader ("+isEXvol+")"
			materialCode.extend(MotionBlock(Scene, RibifyShader, Scene, Material, isEXvol, Mblur, Mframes, 3)) #Exterior volume shader
		if (isArea and isArea != 'NONE'):
			print "\t\t\t- Area Light Shader ("+isArea+")"
			materialCode.extend(MotionBlock(Scene, RibifyShader, Scene, [Object, Material], isArea, Mblur, Mframes, 3)) #Arealight shader (uses object instead of material for token parse so proper ID will pass for <LightID_I>)
		if (isEndCode and isEndCode != 'NONE'):
			materialCode.extend(ParseFragment(Scene, Material, isEndCode)) #Parse custom code
	return materialCode


#### Returns a RiTransform matrix for object or a RiConcatTransform matrix if Object and Matrix are supplied (Object being parent and Matrix being world space child matrix).
#### If no Object or Matrix is provided then make a 3D view matrix from current active Blender window. If View is set convert whatever matrix combination is given into a view matrix
def RibifyTransform(Object, Matrix, View = False):
	if (Matrix and Object):						#If supplying both Object and Matrix then perform concate
		m = (Matrix.copy()*Object.getMatrix().copy().invert())*Blender.Mathutils.Matrix() #Get concate matrix with Object being parent and Matrix being world space child (handy for dupli matrix blur)
	elif (not Object and Matrix):					#If no Object and Matrix straight copy Matrix
		m = Matrix.copy()
	elif (not Object and not Matrix):				#If theres no Object and no Matrix then use the view matrix if theres no view matrix then create an identity matrix
		m = Blender.Window.GetViewMatrix().copy()
		if (not m): m = Blender.Mathutils.Matrix().copy()
	else:								#If just object then get its matrix
		m = Object.getMatrix().copy()
	if (View):							#Adjust up for camera view
		if (Object or Matrix): m = m.invert()			#Invert matrix if for camera or object view
		m[0][2] = -m[0][2]
		m[1][2] = -m[1][2]
		m[2][2] = -m[2][2]
		m[3][2] = -m[3][2]
	if (Matrix and Object):
		header	= "ConcatTransform"
		space	= "                  "
	else:
		header	= "Transform"
		space	= "            "
	return	[header+" [ "+str(m[0][0])+" "+str(m[0][1])+" "+str(m[0][2])+" "+str(m[0][3])+"\n",
		 space+str(m[1][0])+" "+str(m[1][1])+" "+str(m[1][2])+" "+str(m[1][3])+"\n",
		 space+str(m[2][0])+" "+str(m[2][1])+" "+str(m[2][2])+" "+str(m[2][3])+"\n",
		 space+str(m[3][0])+" "+str(m[3][1])+" "+str(m[3][2])+" "+str(m[3][3])+" ]\n"]


#### Generate a bounding box for given object, also calculate bounds to contain minimum and maximum geometry movement within MBlur frames range and also include particles or curves if using a Delayed Read archive.
def RibifyBounds(Scene, Object):
	xMin		= None
	xMax		= None
	yMin		= None
	yMax		= None
	zMin		= None
	zMax		= None
	archiveTYPE	= GetProperty(Object, ButtonData[GEOMETRY][WIN_BUTS][GEO_OBJ_ARCH][BUT_PROP])
	startFrame	= Scene.render.currentFrame()			#Get current frame so we can reset later
	localMatrix	= Object.getMatrix().copy().invert()
	if (GetProperty(Object, ButtonData[GEOMETRY][WIN_BUTS][GEO_GEO_MBLUR][BUT_PROP])|GetProperty(Object, ButtonData[GEOMETRY][WIN_BUTS][GEO_OBJ_MBLUR][BUT_PROP])):
		blurFrame = max([GetProperty(Object, ButtonData[GEOMETRY][WIN_BUTS][GEO_GEO_FRAMES][BUT_PROP], "", ButtonData[GEOMETRY][WIN_BUTS][GEO_GEO_FRAMES][BUT_DEFAULT]), GetProperty(Object, ButtonData[GEOMETRY][WIN_BUTS][GEO_OBJ_FRAMES][BUT_PROP], "", ButtonData[GEOMETRY][WIN_BUTS][GEO_OBJ_FRAMES][BUT_DEFAULT])])
	else: blurFrame = 1
	while blurFrame > 0:						#Cycle through the number of frames specified adjusting the render frame accordingly
		if (startFrame-blurFrame+1 > 0): Scene.render.currentFrame(startFrame-blurFrame+1) #Set frame back to blur length
		else:		Scene.render.currentFrame(1)		#If blurLength is before first frame just make first frame
		blurFrame	= blurFrame-1				#Update frame
		extents = [vector*localMatrix for vector in Object.boundingBox] #Get each bounds vector and transform into local space
		for effect in Object.effects:
			partLoc = effect.getParticlesLoc()
			if (partLoc):
				if (type(partLoc[0]) == Blender.Types.vectorType):
					extents.extend(partLoc)	#Get each vector in particle and transform into local space
				else:
					for curve in partLoc:
						for vect in curve:
							extents.append(vect*localMatrix) #Get each vector in curve and transform into local space
		if (xMin != None): extents.extend([[xMin, yMin, zMin], [xMax, yMax, zMax]]) #Also check last min and max values found if doing animation or blur		
		xMin		= min(map(lambda x: x[0], extents))
		xMax		= max(map(lambda x: x[0], extents))
		yMin		= min(map(lambda y: y[1], extents))
		yMax		= max(map(lambda y: y[1], extents))
		zMin		= min(map(lambda z: z[2], extents))
		zMax		= max(map(lambda z: z[2], extents))
		
	Scene.render.currentFrame(startFrame)				#Reset frame to were we started
	return [xMin, xMax, yMin, yMax, zMin, zMax] #Create min and max bounds


#### Returns a transparent blue box representing the passed bounding box as a text list
def ShowBounds(boundB = [-1, 1, -1, 1 , -1, 1]):
	Code = ["AttributeBegin\n"]
	Code.append("\tOpacity [ 0.5 0.5 0.5 ]\n")
	Code.append("\tColor [ 0.0 0.0 1.0 ]\n")
	Code.append("\tPointsPolygons [ 4 4 4 4 4 4 ] [ 0 3 2 1 1 2 6 5 5 6 7 4 4 7 3 0 2 3 7 6 0 4 5 1 ] \"P\" [ "+str(boundB[0])+" "+str(boundB[2])+" "+str(boundB[5])+" "+str(boundB[0])+" "+str(boundB[2])+" "+str(boundB[4])+" "+str(boundB[0])+" "+str(boundB[3])+" "+str(boundB[4])+" "+str(boundB[0])+" "+str(boundB[3])+" "+str(boundB[5])+" "+str(boundB[1])+" "+str(boundB[2])+" "+str(boundB[5])+" "+str(boundB[1])+" "+str(boundB[2])+" "+str(boundB[4])+" "+str(boundB[1])+" "+str(boundB[3])+" "+str(boundB[4])+" "+str(boundB[1])+" "+str(boundB[3])+" "+str(boundB[5])+" ]\n")
	Code.append("AttributeEnd\n")
	return Code



#### Generate rib code for the passed Object
def RibifyObject(Scene, Object, Frame, TabLevel = 0, isCamera = False):
	global ButtonData, defaultPointlight, defaultSpotlight, defaultDistantlight, defaultAmbientlight, defaultSurface
	objectCode = []
	if (Object):	objectType = Object.getType()
	else:		objectType = ""
	
	if (isCamera):							#Handle object as a camera
		#Figure for custom aspect ratios
		Xres	= Scene.render.sizeX
		Yres	= Scene.render.sizeY
		Xratio	= Xres*(float(Scene.render.aspectX)/200)	#Image width after x aspect adjustment
		Yratio	= Yres*(float(Scene.render.aspectY)/200)	#Image height after y aspect adjustment
		if (Xratio >= Yratio):					#Figure out which side is longer to get ratio from
			aspectRatio	= Xratio/float(Yratio)
			Xaspect		= aspectRatio
			Yaspect		= 1.0
		else:
			aspectRatio	= Yratio/float(Xratio)
			Yaspect		= aspectRatio
			Xaspect		= 1.0
		#Add global code
		if (objectType == "Camera"):
			isCameraCode	= GetProperty(Object, ButtonData[CAMERAS][WIN_BUTS][CAM_BEGIN_CODE][BUT_PROP])
			if (isCameraCode and isCameraCode != 'NONE'): objectCode.extend(ParseFragment(Scene, Object, isCameraCode)) #Parse custom begin code
		objectCode.append("Format "+str(Xres)+" "+str(Yres)+" 1\n")
		objectCode.append("ShadingRate "+str(GetProperty(Scene, ButtonData[SCENES][WIN_BUTS][SCENE_SHADE_RATE][BUT_PROP], "", ButtonData[SCENES][WIN_BUTS][SCENE_SHADE_RATE][BUT_DEFAULT]))+"\n")
		objectCode.append("PixelSamples "+str(GetProperty(Scene, ButtonData[SCENES][WIN_BUTS][SCENE_XSAMPLES][BUT_PROP], "", ButtonData[SCENES][WIN_BUTS][SCENE_XSAMPLES][BUT_DEFAULT]))+" "+str(GetProperty(Scene, ButtonData[SCENES][WIN_BUTS][SCENE_YSAMPLES][BUT_PROP], "", ButtonData[SCENES][WIN_BUTS][SCENE_YSAMPLES][BUT_DEFAULT]))+"\n")
		isFilter	= GetProperty(Scene, ButtonData[SCENES][WIN_BUTS][SCENE_FILTER][BUT_PROP])
		if (isFilter):	objectCode.append("PixelFilter \""+isFilter+"\" "+str(GetProperty(Scene, ButtonData[SCENES][WIN_BUTS][SCENE_XWIDTH][BUT_PROP]))+" "+str(GetProperty(Scene, ButtonData[SCENES][WIN_BUTS][SCENE_YWIDTH][BUT_PROP]))+"\n")
		#Add object specific code
		if (objectType):
			if (objectType == "Camera"):
				print "\tExporting Camera Perspective: "+Object.name
				objectCode.append("Clipping "+str(Object.getData().clipStart)+" "+str(Object.getData().clipEnd)+"\n")
				if (Object.getData().type == 'persp'):	objectCode.append("Projection \"perspective\" \"fov\" [ "+str(360.0*atan(16.0/Object.getData().lens/aspectRatio)/pi)+" ]\n")
				else:					objectCode.append("Projection \"orthographic\"\n")
				objectCode.append("ScreenWindow -"+str(Xaspect)+" "+str(Xaspect)+" -"+str(Yaspect)+" "+str(Yaspect)+"\n") #Set custom x y ratios
				if (Scene.render.borderRender):		#Set border cropping region if on
					border	= Scene.render.border
					objectCode.append("CropWindow "+str(border[0])+" "+str(border[2])+" "+str(1.0-border[3])+" "+str(1.0-border[1])+"\n")		
				objectCode.append("Shutter "+str(GetProperty(Object, ButtonData[CAMERAS][WIN_BUTS][CAM_SHUT_MIN][BUT_PROP], "", ButtonData[CAMERAS][WIN_BUTS][CAM_SHUT_MIN][BUT_DEFAULT]))+" "+str(GetProperty(Object, ButtonData[CAMERAS][WIN_BUTS][CAM_SHUT_MAX][BUT_PROP], "", ButtonData[CAMERAS][WIN_BUTS][CAM_SHUT_MAX][BUT_DEFAULT]))+"\n")
				if (GetProperty(Object, ButtonData[CAMERAS][WIN_BUTS][CAM_DOF][BUT_PROP])): objectCode.append("DepthOfField "+str(GetProperty(Object, ButtonData[CAMERAS][WIN_BUTS][CAM_FSTOP][BUT_PROP], "", ButtonData[CAMERAS][WIN_BUTS][CAM_FSTOP][BUT_DEFAULT]))+" "+str(GetProperty(Object, ButtonData[CAMERAS][WIN_BUTS][CAM_FOCAL][BUT_PROP], "", ButtonData[CAMERAS][WIN_BUTS][CAM_FOCAL][BUT_DEFAULT]))+" "+str(Object.getData().dofDist)+"\n")
				isImage	= 				GetProperty(Object, ButtonData[CAMERAS][WIN_BUTS][CAM_IMAGE][BUT_PROP])
				if (isImage and isImage != 'NONE'):	objectCode.extend(RibifyShader(Scene, Object, isImage)) #Parse image shader
			elif (objectType == 'Lamp'):
				print "\tExporting Light Perspective: "+Object.name
				objectCode.append("Clipping 0.1 "+str(Object.getData().getDist())+"\n")
				objectCode.append("Projection \"perspective\" \"fov\" [ "+str(Object.getData().getSpotSize())+" ]\n")
			else:
				print "\tExporting Object Perspective: "+Object.name
				objectCode.append("Clipping 0.1 10000.0\n")
				objectCode.append("Projection \"perspective\" \"fov\" [ 65.0 ]\n")
			objectCode.append(ParseTokens(Scene, Object, "##CameraOrientation <FROM_P> <TO_P>\n"))
			objectCode.extend(MotionBlock(Scene, RibifyTransform, Object, [], True, GetProperty(Object, ButtonData[CAMERAS][WIN_BUTS][CAM_MBLUR][BUT_PROP], "", ButtonData[CAMERAS][WIN_BUTS][CAM_MBLUR][BUT_DEFAULT]), GetProperty(Object, ButtonData[CAMERAS][WIN_BUTS][CAM_FRAMES][BUT_PROP], "", ButtonData[CAMERAS][WIN_BUTS][CAM_FRAMES][BUT_DEFAULT]), 1))
			if (objectType == "Camera"):
				isCameraCode	= GetProperty(Object, ButtonData[CAMERAS][WIN_BUTS][CAM_END_CODE][BUT_PROP])
				if (isCameraCode and isCameraCode != 'NONE'): objectCode.extend(ParseFragment(Scene, Object, isCameraCode)) #Parse custom end code
			objectCode = RibifyInstance(Object, "Archives"+sys.sep+"Cameras"+sys.sep, Scene.name+Object.name+"Ca", objectCode, Frame, GetProperty(Object, ButtonData[CAMERAS][WIN_BUTS][CAM_ARCH][BUT_PROP], "", ButtonData[CAMERAS][WIN_BUTS][CAM_ARCH][BUT_TITLE][ButtonData[CAMERAS][WIN_BUTS][CAM_ARCH][BUT_DEFAULT]]), [], TabLevel)
		else:
			print "\tExporting Active Window Perspective:"
			objectCode.append("Clipping 0.1 10000.0\n")
			objectCode.append("Projection \"perspective\" \"fov\" [ 65.0 ]\n")
			objectCode.extend(RibifyTransform("", [], True))
			objectCode = AddTabs(objectCode, 1)
		return objectCode					#Return early so if this is a object camera its not rendered twice!
	
	elif (objectType == "Lamp"):
		isLampCode			= GetProperty(Object, ButtonData[LIGHTS][WIN_BUTS][LIGHT_BEGIN_CODE][BUT_PROP])
		if (isLampCode and isLampCode != 'NONE'):	objectCode.extend(ParseFragment(Scene, Object, isLampCode)) #Parse custom begin code
		isLampShader			= GetProperty(Object, ButtonData[LIGHTS][WIN_BUTS][LIGHT_SHADER][BUT_PROP])
		if (isLampShader and isLampShader != 'NONE'):
			objectCode.extend(MotionBlock(Scene, RibifyShader, Scene, Object, isLampShader, GetProperty(Object, ButtonData[LIGHTS][WIN_BUTS][LIGHT_MBLUR][BUT_PROP], "", ButtonData[LIGHTS][WIN_BUTS][LIGHT_MBLUR][BUT_DEFAULT]), GetProperty(Object, ButtonData[LIGHTS][WIN_BUTS][LIGHT_FRAMES][BUT_PROP], "", ButtonData[LIGHTS][WIN_BUTS][LIGHT_FRAMES][BUT_DEFAULT]), 1)) #Parse light shader
		elif (Object.getData().getType() == 1): objectCode.append(ParseTokens(Scene, Object, defaultDistantlight))	#If this is a default distant light
		elif (Object.getData().getType() == 2): objectCode.append(ParseTokens(Scene, Object, defaultSpotlight))		#If this is a default spot light
		elif (Object.getData().getType() == 3): objectCode.append(ParseTokens(Scene, Object, defaultAmbientlight))	#If this is a default ambient light
		else: 			 		objectCode.append(ParseTokens(Scene, Object, defaultPointlight))	#Otherwise make default point light
		isLampCode			= GetProperty(Object, ButtonData[LIGHTS][WIN_BUTS][LIGHT_END_CODE][BUT_PROP])
		if (isLampCode and isLampCode != 'NONE'):	objectCode.extend(ParseFragment(Scene, Object, isLampCode)) #Parse custom end code
		objectCode = RibifyInstance(Object, "Archives"+sys.sep+"Lights"+sys.sep, Object.name+"La", RibifyInstance(Object, "", Object.name, objectCode, Frame, "Attribute Block"), Frame, GetProperty(Object, ButtonData[LIGHTS][WIN_BUTS][LIGHT_ARCH][BUT_PROP], "", ButtonData[LIGHTS][WIN_BUTS][LIGHT_ARCH][BUT_TITLE][ButtonData[LIGHTS][WIN_BUTS][LIGHT_ARCH][BUT_DEFAULT]]), [], TabLevel)
	
	elif (objectType == "Mesh" or objectType == "Curve" or objectType == "Surf"):
		objectState			= False			#Keep track if any object was actually created
		if (CheckInstance(Object, Object.name+"Ob", Frame, not GetProperty(Object, ButtonData[GEOMETRY][WIN_BUTS][GEO_ANIM_OBJECT][BUT_PROP], "", ButtonData[GEOMETRY][WIN_BUTS][GEO_ANIM_OBJECT][BUT_DEFAULT]), ButtonData[ACTIONS][WIN_BUTS][ACT_CREATE_SEL][BUTTON].val)): #Check if this object needs to be exported
			if (Object.DupObjects):				#If we have dupliobjects then pass them through the loop
				isDupli		= True
				objectList	= Object.DupObjects
				totalDupli	= len(objectList)
			else:						#If we dont then just pass current object through loop
				isDupli		= False
				objectList	= [[Object, []]]
				totalDupli	= 1
			currentDupli		= 0			#Keep count of what dupli number we are for user output
			for object, matrix in objectList:		#Cycle through any dupliobjects if none then just process current object
				currentDupli	= currentDupli+1
				transformCode	= []
				instanceCode	= []
				geoState	= False			#Keep track if any geometry was created
				if (not isDupli or CheckInstance(object, object.name+"Dup", Frame, not GetProperty(object, ButtonData[GEOMETRY][WIN_BUTS][GEO_ANIM_OBJECT][BUT_PROP], "", ButtonData[GEOMETRY][WIN_BUTS][GEO_ANIM_OBJECT][BUT_DEFAULT]))):
					if (isDupli):	print "\t\tProcessing Dupli Object: "+object.name+" ("+str(currentDupli)+" of "+str(totalDupli)+")"
					else:		print "\t\tProcessing Geometry:"
					isObjectCode	= GetProperty(object, ButtonData[GEOMETRY][WIN_BUTS][GEO_BEGINOBJ_CODE][BUT_PROP])
					if (isObjectCode and isObjectCode != 'NONE'): instanceCode.extend(ParseFragment(Scene, object, isObjectCode)) #Parse custom object begin code
					shadingRate	= GetProperty(object, ButtonData[GEOMETRY][WIN_BUTS][GEO_SHADE_RATE][BUT_PROP], "", ButtonData[GEOMETRY][WIN_BUTS][GEO_SHADE_RATE][BUT_DEFAULT]) #Set object shading rate
					if (shadingRate): instanceCode.append("ShadingRate "+str(shadingRate)+"\n")
					isDispBound	= GetProperty(object, ButtonData[GEOMETRY][WIN_BUTS][GEO_DISP_BOUND][BUT_PROP])
					if (isDispBound and isDispBound > 0.0): instanceCode.append("Attribute \"displacementbound\" \"sphere\" [ "+str(isDispBound)+" ] \"coordinatesystem\" [ \""+GetProperty(object, ButtonData[GEOMETRY][WIN_BUTS][GEO_COOR_SYS][BUT_PROP], "", ButtonData[GEOMETRY][WIN_BUTS][GEO_COOR_SYS][BUT_DEFAULT])+"\" ]\n")
					isAtmoShader	= GetProperty(object, ButtonData[GEOMETRY][WIN_BUTS][GEO_ATMO][BUT_PROP])
					if (isAtmoShader and isAtmoShader != 'NONE'): instanceCode.extend(RibifyShader(Scene, "", isAtmoShader)) #Parse atmosphere shader
					dataBlock	= object.getData(False, True)
					materials	= dataBlock.materials
					modStack	= []
					modTags		= ""
					for modifier in object.modifiers: #Cycle through object modifiers that need to be pre-processed
						modTags = modTags+modifier.name[0:2] #Try to tag modifiers to detect geometry changes on shared datablocks
						if (modifier.type == Modifier.Types.SUBSURF):
							modStack.insert(0, modifier[Modifier.Settings.RENDER])
							modStack.insert(0, modifier[Modifier.Settings.REALTIME])
							modifier[Modifier.Settings.RENDER]	= False
							modifier[Modifier.Settings.REALTIME]	= False
					if (not materials): materials = [""] #If no material then force none material so renderer will use default for geometry
					for matIndex, material in enumerate(materials):
						print "\t\t- Material Pass: "+str(matIndex+1)+" of "+str(len(materials))
						effects		= object.effects
						attributeCode	= []
						partCode	= []
						geoCode		= []
						matCode		= []
						if (dataBlock):
							if (objectType != "Mesh" or dataBlock.mode&Mesh.Modes.TWOSIDED): attributeCode.append("Sides 2\n")
							else: attributeCode.append("Sides 1\n")
							renderEmitter	= True	#Always render geometry by default
							geoMblur	= GetProperty(object, ButtonData[GEOMETRY][WIN_BUTS][GEO_GEO_MBLUR][BUT_PROP], "", ButtonData[GEOMETRY][WIN_BUTS][GEO_GEO_MBLUR][BUT_DEFAULT])
							geoFrames	= GetProperty(object, ButtonData[GEOMETRY][WIN_BUTS][GEO_GEO_FRAMES][BUT_PROP], "", ButtonData[GEOMETRY][WIN_BUTS][GEO_GEO_FRAMES][BUT_DEFAULT])
							geoArchive	= GetProperty(object, ButtonData[GEOMETRY][WIN_BUTS][GEO_DATA_ARCH][BUT_PROP], "", ButtonData[GEOMETRY][WIN_BUTS][GEO_DATA_ARCH][BUT_TITLE][ButtonData[GEOMETRY][WIN_BUTS][GEO_DATA_ARCH][BUT_DEFAULT]])
							if (geoArchive == "Inline Code"): 	archiveIndex = "IC"
							elif (geoArchive == "Instance Object"):	archiveIndex = "IO"
							elif (geoArchive == "Read Archive"):	archiveIndex = "RA"
							if (effects):
								partName	= object.name+archiveIndex+"Pa"+str(matIndex)
								if (not effects[0].getFlag()&Effect.Flags.EMESH): renderEmitter = False #Should we process emitter geometry
								if (CheckInstance(object, partName, Frame)): #Check if particles needs to be exported
									partCode = MotionBlock(Scene, RibifyParticles, object, matIndex, "", geoMblur, geoFrames, 3)
									if (partCode != 'NORIB'):
										partCode.insert(0, "Basis \"bezier\" 3 \"bezier\" 3\n")
										partCode.insert(0, "Declare \"N\" \"varying normal\"\n")
								else: print "\t\t\tInstanced Particles"
								attributeCode.extend(RibifyInstance(object, "Archives"+sys.sep+"Geometry"+sys.sep, partName, partCode, Frame, geoArchive))
							else:	partCode	= 'NORIB'
							if (renderEmitter): #Process geometry
								geoName		= dataBlock.name+archiveIndex+modTags+objectType[0:2]+str(matIndex)
								if (CheckInstance(dataBlock, geoName, Frame)): #Check if geometry needs to be exported
									if (objectType == "Mesh"):
										print "\t\t\tProcessing Mesh: "+dataBlock.name
										geoCode = MotionBlock(Scene, RibifyMesh, object, matIndex, "", geoMblur, geoFrames, 3)
										if (geoCode != 'NORIB'):
											geoCode.insert(0, "Declare \"st\" \"facevarying float[2]\"\n")
											geoCode.insert(0, "Declare \"N\" \"facevarying normal\"\n")
											geoCode.insert(0, "Declare \"Cs\" \"facevarying color\"\n")
									elif (objectType == "Curve"):
										print "\t\t\tProcessing Curve: "+dataBlock.name
										geoCode = MotionBlock(Scene, RibifyCurve, object, matIndex, "", geoMblur, geoFrames, 3)
										if (geoCode != 'NORIB'):
											geoCode.insert(0, "Basis \"bezier\" 3 \"bezier\" 3\n")
											geoCode.insert(0, "Declare \"N\" \"varying normal\"\n")
									elif (objectType == "Surf"):
										print "\t\t\tProcessing Surface: "+dataBlock.name
										for surfData in object.getData(False, True):
											surf	= MotionBlock(Scene, RibifySurface, object, matIndex, surfData, geoMblur, geoFrames, 3)
											if (surf != 'NORIB'):
												geoCode.extend(surf) #Process surfaces in object (doing this here so motion block works)
											else:
												geoCode = surf #If there was an error pass through
												break
										if (geoCode != 'NORIB'):
											geoCode.insert(0, "Basis \"bezier\" 3 \"bezier\" 3\n")
								else: print "\t\t\tInstance of: "+dataBlock.name
								attributeCode.extend(RibifyInstance(dataBlock, "Archives"+sys.sep+"Geometry"+sys.sep, geoName, geoCode, Frame, geoArchive))
							else: geoCode	= 'NORIB'
							isGeoCode	= GetProperty(object, ButtonData[GEOMETRY][WIN_BUTS][GEO_GEO_CODE][BUT_PROP])
							if (isGeoCode and isGeoCode != 'NONE'): attributeCode.extend(ParseFragment(Scene, object, isGeoCode)) #Parse custom geometry code
						if ((isGeoCode and isGeoCode != 'NONE') or partCode != 'NORIB' or geoCode != 'NORIB'): #Make sure there is actually geometry to handle
							geoState	= True
							if (material):
								matShaders	= []
								if(material.lightGroup):	matName = material.name+Scene.name+"Ma" #Extend material archive name with scene name if using light groups
								else:				matName = material.name+"Ma" #Otherwise just use material name
								matMblur	= GetProperty(material, ButtonData[MATERIALS][WIN_BUTS][MAT_MBLUR][BUT_PROP], "", ButtonData[MATERIALS][WIN_BUTS][MAT_MBLUR][BUT_DEFAULT])
								matFrames	= GetProperty(material, ButtonData[MATERIALS][WIN_BUTS][MAT_FRAMES][BUT_PROP], "", ButtonData[MATERIALS][WIN_BUTS][MAT_FRAMES][BUT_DEFAULT])
								matArchive	= GetProperty(material, ButtonData[MATERIALS][WIN_BUTS][MAT_ARCH][BUT_PROP], "", ButtonData[MATERIALS][WIN_BUTS][MAT_ARCH][BUT_TITLE][ButtonData[MATERIALS][WIN_BUTS][MAT_ARCH][BUT_DEFAULT]])
								if (CheckInstance(material, matName, Frame)):
									print "\t\t\tMaterial Shaders: "+matName
									matShaders.extend(RibifyMaterial(Scene, object, material))
								else: print "\t\t\tMaterial Shaders Instance: "+matName
								matCode.extend(RibifyInstance(material, "Archives"+sys.sep+"Materials"+sys.sep, matName, matShaders, Frame, matArchive)) #Create material code
								print "\t\t\t- Material color"
								matCode.extend(MotionBlock(Scene, RibifyColor, material, "", "", matMblur, matFrames, 3)) #Material color
								print "\t\t\t- Material opacity"
								matCode.extend(MotionBlock(Scene, RibifyOpacity, material, "", "", matMblur, matFrames, 3)) #Material alpha
							elif (not material):
								matName		= "Default Surface"
								print "\t\t\tMaterial Shaders: "+matName
								matCode.extend(defaultSurface) #If no materials then make default matte material
							instanceCode.extend(RibifyInstance(dataBlock, "", matName, matCode+attributeCode, Frame, "Attribute Block")) #Wrap geometry and its attributes in a attribute block
						else:	print "\t\t\tNO GEOMETRY FOR THIS MATERIAL!!"
					for modifier in object.modifiers: #Restore any modifier settings from stack
						if (modifier.type == Modifier.Types.SUBSURF):
							modifier[Modifier.Settings.RENDER]	= modStack.pop()
							modifier[Modifier.Settings.REALTIME]	= modStack.pop()
				else:
					print "\t\tProcessing Dupli Instance: "+object.name+" ("+str(currentDupli)+" of "+str(totalDupli)+")"
					geoState		= True	#Automatically make geometry valid if it is an instance
				if (geoState):				#Only process if there is instance code
					objectState		= True	#Show that some code was actually created
					if (instanceCode):		#Only add custom end code if this is not a instance
						isObjectCode	= GetProperty(object, ButtonData[GEOMETRY][WIN_BUTS][GEO_ENDOBJ_CODE][BUT_PROP])
						if (isObjectCode and isObjectCode != 'NONE'): instanceCode.extend(ParseFragment(Scene, object, isObjectCode)) #Parse custom object end code
					if (isDupli):
						boundB		= RibifyBounds(Scene, object) #Calculate bounds for dupliobject
						instanceCode	= RibifyInstance(object, "Archives"+sys.sep+"Objects"+sys.sep, object.name+"Dup", instanceCode, Frame, GetProperty(object, ButtonData[GEOMETRY][WIN_BUTS][GEO_OBJ_ARCH][BUT_PROP], "", ButtonData[GEOMETRY][WIN_BUTS][GEO_OBJ_ARCH][BUT_TITLE][ButtonData[GEOMETRY][WIN_BUTS][GEO_OBJ_ARCH][BUT_DEFAULT]]), boundB)
						transformCode.extend(MotionBlock(Scene, RibifyTransform, Object, matrix, False, GetProperty(object, ButtonData[GEOMETRY][WIN_BUTS][GEO_OBJ_MBLUR][BUT_PROP], "", ButtonData[GEOMETRY][WIN_BUTS][GEO_OBJ_MBLUR][BUT_DEFAULT]), GetProperty(object, ButtonData[GEOMETRY][WIN_BUTS][GEO_OBJ_FRAMES][BUT_PROP], "", ButtonData[GEOMETRY][WIN_BUTS][GEO_OBJ_FRAMES][BUT_DEFAULT]), 1))
						transformCode.append("Bound "+str(boundB[0])+" "+str(boundB[1])+" "+str(boundB[2])+" "+str(boundB[3])+" "+str(boundB[4])+" "+str(boundB[5])+"\n") #Create bounding box
						if (object.drawType == Blender.Object.DrawTypes.BOUNDBOX): transformCode.extend(ShowBounds(boundB)) #Show bounding box if object draw type is bounding box
						objectCode.extend(RibifyInstance(object, "", object.name, transformCode+instanceCode, Frame, "Attribute Block"))
					else:	objectCode 	= instanceCode
		else:
			print "\t\tProcessing Object Instance:"
			objectState = True		#Automatically make object valid if it is an instance
		if (objectState):					#Only process this object if it actually had any geometry
			headerCode	= []				#Will contain transform and bounds info for object (needs to be separate so dupliobjects are easier to manage)
			boundB		= RibifyBounds(Scene, Object)	#Calculate bounding box for parent object (needed for delayed read archive)
			archiveTYPE	= GetProperty(Object, ButtonData[GEOMETRY][WIN_BUTS][GEO_OBJ_ARCH][BUT_PROP], "", ButtonData[GEOMETRY][WIN_BUTS][GEO_OBJ_ARCH][BUT_TITLE][ButtonData[GEOMETRY][WIN_BUTS][GEO_OBJ_ARCH][BUT_DEFAULT]])
			if (archiveTYPE == "Delayed Archive" or objectCode): #Only use header if this is a delayed archive or this archive needs to be regenerated!
				headerCode.extend(MotionBlock(Scene, RibifyTransform, Object, [], False, GetProperty(Object, ButtonData[GEOMETRY][WIN_BUTS][GEO_OBJ_MBLUR][BUT_PROP], "", ButtonData[GEOMETRY][WIN_BUTS][GEO_OBJ_MBLUR][BUT_DEFAULT]), GetProperty(Object, ButtonData[GEOMETRY][WIN_BUTS][GEO_OBJ_FRAMES][BUT_PROP], "", ButtonData[GEOMETRY][WIN_BUTS][GEO_OBJ_FRAMES][BUT_DEFAULT]), 1))
				headerCode.append("Bound "+str(boundB[0])+" "+str(boundB[1])+" "+str(boundB[2])+" "+str(boundB[3])+" "+str(boundB[4])+" "+str(boundB[5])+"\n") #Create bounding box
				if (Object.drawType == Blender.Object.DrawTypes.BOUNDBOX): headerCode.extend(ShowBounds(boundB)) #Show bounding box if object draw type is bounding box
			##If this is a delayed archive we need to put the transform before the archive call so the delayed bounds can use local space, otherwise place it after to put all object code in archive
			if (archiveTYPE == "Delayed Archive"):	objectCode = RibifyInstance(Object, "", Object.name, headerCode+RibifyInstance(Object, "Archives"+sys.sep+"Objects"+sys.sep, Object.name+"Ob", objectCode, Frame, archiveTYPE, boundB, TabLevel), Frame, "Attribute Block")
			else:					objectCode = RibifyInstance(Object, "Archives"+sys.sep+"Objects"+sys.sep, Object.name+"Ob", RibifyInstance(Object, "", Object.name, headerCode+objectCode, Frame, "Attribute Block"), Frame, archiveTYPE, boundB, TabLevel)
	return objectCode


#### Check passed objects "archive" properties to determine if instance needs to be re-exported, returns True to redo export
def CheckInstance(Object, ObjectName, Frame, noAnim = False, onlySelect = False):
	archiveID	= GetProperty(Object, ObjectName+"ID")
	archiveTYPE	= GetProperty(Object, ObjectName+"TYPE")
	archiveFRAME	= GetProperty(Object, ObjectName+"FRAME")
	archiveLOC	= GetProperty(Object, ObjectName+"LOC")
	if (onlySelect and type(Object) == Blender.Types.ObjectType and not Object.sel and
	    (GetProperty(Object, ButtonData[GEOMETRY][WIN_BUTS][GEO_OBJ_ARCH][BUT_PROP], "", ButtonData[GEOMETRY][WIN_BUTS][GEO_OBJ_ARCH][BUT_TITLE][ButtonData[GEOMETRY][WIN_BUTS][GEO_OBJ_ARCH][BUT_DEFAULT]]) == "Read Archive" or
	     GetProperty(Object, ButtonData[GEOMETRY][WIN_BUTS][GEO_OBJ_ARCH][BUT_PROP], "", ButtonData[GEOMETRY][WIN_BUTS][GEO_OBJ_ARCH][BUT_TITLE][ButtonData[GEOMETRY][WIN_BUTS][GEO_OBJ_ARCH][BUT_DEFAULT]]) == "Delayed Archive")): return False #If object is using onlySelect and is an archive and not selected then dont generate
	if ((noAnim or archiveFRAME == Frame) and archiveTYPE != "Inline Code" and archiveLOC and archiveID): return False #If archive is already made or using noAnim then don't generate code
	return True


#### This function will archive the passed code according to the type passed. If this is a read type archive it will search for a archive in directory that has the same data as code unless 'NORIB' is passed.
#### If it finds a match it will reuse the older archive by passing its handle back, if there is no match then it will make a new archive as "ObjectName_Frame.rib". If the type is a attribute
#### block it will just pass back Code with attribute begin and end and proper tabbing. If type is a instance then it will search the main rib for a Code match if no match it will append Code to the main rib.
#### TabLevel will add specified number of tabs to passed code, ForceArchive will force the creation of the archive without checking for a ealier match
#### This function passes info about the coding and archiving of the passed object by adding the following properties to it: archiveID property: [objectId, archiveType, FrameNum, archiveLocation (seekPos or directory)]
def RibifyInstance(Object, Directory, ObjectName, Code, Frame = 1, Type = "Inline Code", BoundingBox = [-1.0, 1.0, -1.0, 1.0, -1.0, 1.0], TabLevel = 0, forceArchive = False):
	global RibOutput, instanceCount
	if (Code == 'NORIB'):	return []				#If there was an rib code then do nothing
	
	if (Type == "Read Archive" or Type == "Delayed Archive"):	#File archive type
		archiveName	= ObjectName+"F"+str(Frame)+".rib"	#Create archive name from current information
		archiveID	= GetProperty(Object, ObjectName+"ID", "", archiveName)
		archiveTYPE	= GetProperty(Object, ObjectName+"TYPE", "", Type)
		archiveLOC	= GetProperty(Object, ObjectName+"LOC", "", Directory)
		if (Code):
			Code.insert(0, "##RenderMan RIB-Structure 1.1 Entity\n") #Insert Entity comments
			Code.insert(1, "version 3.03\n")
			if (not forceArchive and sys.exists(archiveLOC+archiveID)): #See if last pointed archive exists
				archive		= open(archiveLOC+archiveID, 'rb')
				archiveList	= archive.readlines()
				archive.close()
				if (archiveList != Code): forceArchive = True
			elif (not forceArchive): forceArchive = True
			if (forceArchive):
				archiveID	= archiveName
				archiveTYPE	= Type
				archiveLOC	= Directory
				archive		= open(Directory+archiveName, 'wb') #Make the archive
				archive.writelines(Code)
				archive.close()
			Object.properties[ObjectName+"FRAME"]	= Frame
			Object.properties[ObjectName+"ID"]	= archiveID
			Object.properties[ObjectName+"TYPE"]	= archiveTYPE
			Object.properties[ObjectName+"LOC"]	= archiveLOC
		
		if (sys.exists(archiveLOC+archiveID)):			#Be sure archive actually exists before we return a handle to it!
			if (Type == "Read Archive"):
				Code = ["##Include "+archiveLOC+archiveID+"\n"]
				Code.append("ReadArchive \""+archiveID+"\"\n")
			elif (Type == "Delayed Archive"):
				Code = ["##Include "+archiveLOC+archiveID+"\n"]
				Code.append("Procedural \"DelayedReadArchive\" [ \""+archiveID+"\" ] [ "+str(BoundingBox[0])+" "+str(BoundingBox[1])+" "+str(BoundingBox[2])+" "+str(BoundingBox[3])+" "+str(BoundingBox[4])+" "+str(BoundingBox[5])+" ]\n")
	elif (Type == "Instance Object"):				#Instance archive type
		archiveID	= GetProperty(Object, ObjectName+"ID", "", -1)
		archiveTYPE	= GetProperty(Object, ObjectName+"TYPE", "", Type)
		archiveLOC	= GetProperty(Object, ObjectName+"LOC", "", 0)
		if (Code and sys.exists(GetProjectFolder()+RibOutput)):
			archive = open(GetProjectFolder()+RibOutput, 'rb') #Get file to check instances in
			archive.seek(archiveLOC)			#Point to last instance for this object
			archiveList = archive.readlines()[1:len(Code)+1]
			archive.close()
			Code = AddTabs(Code, 1)				#Go ahead and add tabs to code so it matches instance
			if (Code != archiveList):			#If last object does not match current object then make new instance
				archive		= open(GetProjectFolder()+RibOutput, 'ab') #Append new instance to end of main rib
				archiveID	= instanceCount
				instanceCount	= instanceCount+1
				archiveTYPE	= Type
				archiveLOC	= int(archive.tell())
				archive.write("ObjectBegin "+str(archiveID)+" #Instance \""+ObjectName+"\"\n")
				archive.writelines(Code)
				archive.write("ObjectEnd\n")
				archive.close()
			Object.properties[ObjectName+"FRAME"]	= Frame
			Object.properties[ObjectName+"ID"]	= archiveID
			Object.properties[ObjectName+"TYPE"]	= archiveTYPE
			Object.properties[ObjectName+"LOC"]	= archiveLOC
		if (archiveID != -1): Code = ["ObjectInstance "+str(archiveID)+" #Instance \""+ObjectName+"\"\n"]
	elif (Type == "Attribute Block"):				#Pass code straight through but with added attribute block
		if (Code):
			Code.insert(0, "Attribute \"identifier\" \"name\" [ \""+ObjectName+"\" ]\n")
			Code = AddTabs(Code, 1)
			Code.insert(0, "AttributeBegin\n")
			Code.append("AttributeEnd\n")
	return AddTabs(Code, TabLevel)


#### Prepares project folders and processes shaders and textures, returns 1 if errors otherwise 0
def PrepareProject(CompileShaders = True, ExportMaps = True):
	global CompilerBin, RenderDir, Filters, TexmakeBin, lightList
	OutputDir = GetProjectFolder()
	lightList = []							#Reset light lists for current render pass/s
	
	print "\nStarting export process..."
	
	if (not RenderDir or not RenderBin or not CompilerBin):		#Check if output directory, Renderer and shader compiler have been set
		ErrorPopup("Please setup the output directory and RenderMan binaries under the \"MOSAIC Settings\" tab!")
		return 1
	
	print "Setting up output directories..."
	DrawProgressBar(0.0, "Setting up directories...")
	if (SetupDirectories(OutputDir)):				#Make sure output directories exist, if they couldn't be made then abort render
		DrawProgressBar(0.0, "")				#Reset progress bar
		DrawProgressBar(1.0, "")				#Reset progress bar
		return 1
	
	if (CompileShaders):						#Only output shader source if we are set to compile shaders
		print "Processing shaders..."
		DrawProgressBar(0.0, "Processing shaders...")
		os.chdir(OutputDir+"Shaders")
		for shaderInclude in [text for text in Blender.Text.Get() if text.name.count(Filters[7])]: #Cycle through all text files looking for includes
			if (ExportText(shaderInclude)):
				return 1
		for shader in [text for text in Blender.Text.Get() if text.name.count(Filters[1])]: #Cycle through all text files looking for shaders
			if (CompileShader(shader)):
				return 1
	
	if (ExportMaps):						#Only export maps if we are set to export maps
		print "Processing maps..."
		DrawProgressBar(0.0, "Processing maps...")
		os.chdir(OutputDir+"Maps")
		for image in Blender.Image.Get():
			if (image.source&Blender.Image.Sources.STILL and not image.source&Blender.Image.Sources.GENERATED):
				originalpath	= image.getFilename()
				imageName	= sys.basename(originalpath)
				print "\tWriting Texture "+imageName+"..."
				image.setFilename(OutputDir+"Maps"+sys.sep+imageName)
				try:					#Write temporary image for render or report error if problems
					image.save()
					if (TexmakeBin):
						print "\tOptimizing Texture "+imageName+"..."
						maketexCall = TexmakeBin
						if (maketexCall.count("<TEX>")): maketexCall = maketexCall.replace("<TEX>", "\""+imageName+"\"")
						else: maketexCall = maketexCall+" \""+imageName+"\" \""+imageName+"\""
						os.system(maketexCall)	#Optimize texture
				except: ErrorPopup("Could not write image "+OutputDir+"Maps"+sys.sep+imageName+", check paths and permissions!")
				image.setFilename(originalpath)			#Be sure to restore original path to image
	return 0


#### Prepares temporary scene object properties for new export
def CleanupScenes():
	global instanceCount
	instanceCount	= 0
	print "Processing scenes..."
	DrawProgressBar(0.0, "Processing scenes...")
	for item in [Blender.Scene.Get(), Blender.Object.Get(), Blender.Material.Get(), Blender.Mesh.Get(), Blender.Curve.Get(), Blender.Metaball.Get()]: #Cycle through all scenes, objects, materials, and datablocks and clear mosaic render state properties
		for subItem in item:
			for key in subItem.properties:
				if (key.count("FRAME") or key.count("ID") or key.count("TYPE") or key.count("LOC")):
					del subItem.properties[key]
	
	for scene in Blender.Scene.Get():				#Cycle through group properties and remove properties for removed groups
		for group in [key for key, value in scene.properties.iteritems() if type(value) == Blender.Types.IDGroupType and list(value).count("Group Block")]: #Make sure property is a group type and for a scene group
			try:	Blender.Group.Get(group)
			except:	del scene.properties[group]


#### Main scene export code, return render commandline for scene
def RibifyScene(scene, fraStart = 1, fraEnd = 1, RibOutputName = "Mosaic.rib", Preview = False, GenerateCode = True):
	global ButtonData, RenderBin, RibOutput, killExport, lightList
	RibOutput	= RibOutputName					#Transfer ribs output file name to global
	originalFrame	= scene.render.currentFrame()			#Get current frame so we can reset it later
	OutputDir	= GetProjectFolder()
	
	#### Setup the main ribs header in preparation for the frame blocks	
	os.chdir(OutputDir) 						#Change to output directory
	if (Preview or GenerateCode):
		print "Exporting scenes to RIB . . ."
		DrawProgressBar(0.0, "Exporting scenes...")
		mainrib = open(RibOutput, 'wb') 			#Open main rib for output
		mainrib.write("##RenderMan RIB-Structure 1.1\n")
		mainrib.write("##Scene: "+scene.name+"\n")
		mainrib.write("##Creator: MOSAIC "+__version__+" for Blender\n")
		mainrib.write("##CreationDate: "+strftime("%I:%M%p %m/%d/%Y", localtime()).lower()+"\n")
		mainrib.write("##For: "+OutputDir+"\n")
		mainrib.write("##Frames: "+str(fraEnd-fraStart+1)+"\n")
		mainrib.write("version 3.03\n")
		rootScene	= Blender.Scene.Get()[0]
		archives	= GetProperty(rootScene, ButtonData[PROJECT][WIN_BUTS][PROJECT_ARCHIVES][BUT_PROP], "", ButtonData[PROJECT][WIN_BUTS][PROJECT_ARCHIVES][BUT_DEFAULT])
		shaders		= GetProperty(rootScene, ButtonData[PROJECT][WIN_BUTS][PROJECT_SHADERS][BUT_PROP], "", ButtonData[PROJECT][WIN_BUTS][PROJECT_SHADERS][BUT_DEFAULT])
		textures	= GetProperty(rootScene, ButtonData[PROJECT][WIN_BUTS][PROJECT_TEXTURES][BUT_PROP], "", ButtonData[PROJECT][WIN_BUTS][PROJECT_TEXTURES][BUT_DEFAULT])
		displays	= GetProperty(rootScene, ButtonData[PROJECT][WIN_BUTS][PROJECT_DISPLAYS][BUT_PROP], "", ButtonData[PROJECT][WIN_BUTS][PROJECT_DISPLAYS][BUT_DEFAULT])
		procedurals	= GetProperty(rootScene, ButtonData[PROJECT][WIN_BUTS][PROJECT_PROCEDURALS][BUT_PROP], "", ButtonData[PROJECT][WIN_BUTS][PROJECT_PROCEDURALS][BUT_DEFAULT])
		resources	= GetProperty(rootScene, ButtonData[PROJECT][WIN_BUTS][PROJECT_RESOURCES][BUT_PROP], "", ButtonData[PROJECT][WIN_BUTS][PROJECT_RESOURCES][BUT_DEFAULT])
		if (archives != 'NONE'):	mainrib.write("Option \"searchpath\" \"archive\" [ \""+archives+"\" ]\n")
		if (shaders != 'NONE'):		mainrib.write("Option \"searchpath\" \"shader\" [ \""+shaders+"\" ]\n")
		if (textures != 'NONE'):	mainrib.write("Option \"searchpath\" \"texture\" [ \""+textures+"\" ]\n")
		if (displays != 'NONE'):	mainrib.write("Option \"searchpath\" \"display\" [ \""+displays+"\" ]\n")
		if (procedurals != 'NONE'):	mainrib.write("Option \"searchpath\" \"procedural\" [ \""+procedurals+"\" ]\n")
		if (resources != 'NONE'):	mainrib.write("Option \"searchpath\" \"resource\" [ \""+resources+"\" ]\n")
		bucketsize		= GetProperty(scene, ButtonData[SCENES][WIN_BUTS][SCENE_BUCKET][BUT_PROP], "", ButtonData[SCENES][WIN_BUTS][SCENE_BUCKET][BUT_DEFAULT])
		gridsize		= GetProperty(scene, ButtonData[SCENES][WIN_BUTS][SCENE_GRID][BUT_PROP], "", ButtonData[SCENES][WIN_BUTS][SCENE_GRID][BUT_DEFAULT])
		eyesplits		= GetProperty(scene, ButtonData[SCENES][WIN_BUTS][SCENE_EYES][BUT_PROP], "", ButtonData[SCENES][WIN_BUTS][SCENE_EYES][BUT_DEFAULT])
		othreshold		= GetProperty(scene, ButtonData[SCENES][WIN_BUTS][SCENE_OTHRESHOLD][BUT_PROP], "", ButtonData[SCENES][WIN_BUTS][SCENE_OTHRESHOLD][BUT_DEFAULT])
		if (bucketsize > 0):	mainrib.write("Option \"limits\" \"bucketsize\" [ "+str(bucketsize)+" "+str(bucketsize)+" ]\n")
		if (gridsize > 0):	mainrib.write("Option \"limits\" \"gridsize\" [ "+str(gridsize)+" ]\n")
		if (eyesplits > 0):	mainrib.write("Option \"limits\" \"eyesplits\" [ "+str(eyesplits)+" ]\n")
		if (othreshold > 0):	mainrib.write("Option \"limits\" \"othreshold\" [ "+str(othreshold)+" "+str(othreshold)+" "+str(othreshold)+" ]\n")
		isHeaderCode		= GetProperty(scene, ButtonData[SCENES][WIN_BUTS][SCENE_HEADER_CODE][BUT_PROP])
		if (isHeaderCode and isHeaderCode != 'NONE'): mainrib.writelines(ParseFragment(scene, "", isHeaderCode)) #Write any custom header code
		mainrib.close() #Go ahead and close file, any objects using RiInstance will be appended to file before each frame block is written so... header+RiInstances+frame1+RiInstances+frame2, ect...
		
		#### Main translation loop
		for frame in range(fraStart, fraEnd+1):			#Cycle through scene frames
			print "Exporting scene \""+scene.name+"\" frame "+str(frame)
			#Local Variables
			scene.render.currentFrame(frame)		#Set defined frame
			translationOrder	= [["Lights", "Inline Code", []], ["Objects", "Inline Code", []]] #Ordered object list for translation
			objectCount		= 0
			objectTotal		= 0
			progress		= 0
			DrawProgressBar(progress, "obj:"+str(objectCount)+"-"+str(objectTotal)+" fr:"+str(frame)+"-"+str(fraEnd))
			
			#### Collect objects in scene into translationOrder array so we know proper render order and associations
			for Object in scene.objects:
				#Only pass object if it is in a visible layer
				if (not [sceneLayer for sceneLayer in scene.getLayers() if [objectLayer for objectLayer in Object.layers if objectLayer == sceneLayer]]): continue
				objectType = Object.getType()		#Get object type
				if (objectType == "Lamp"):		#Assign light
					translationOrder[0][2].insert(0, Object) #Insert standard light at top of list
					objectTotal = objectTotal+1
				elif (objectType == "Curve" or objectType == "Mesh" or objectType == "Surf"):
					#If object has a arealight shader in any of its materials then assign object to the lights group
					for material in Object.getData(False, True).materials:
						result = GetProperty(material, ButtonData[MATERIALS][WIN_BUTS][MAT_AREA][BUT_PROP])
						if (result and result != "NONE"):
							translationOrder[0][2].append(Object) #Insert area light at bottom of list
							objectTotal = objectTotal+1
							break		#No reason to look at anymore
					else:				#If this is not a arealight then separate geometry by any associated groups
						for group in [groups for groups in Blender.Group.Get() if GetProperty(scene, groups.name, ButtonData[GROUPS][WIN_BUTS][GRP_ARCH][BUT_PROP]) == "Attribute Block" and list(groups.objects).count(Object)]: #Pass groups with Object and archive type
							groupIndex	= [index for index, item in enumerate(translationOrder) if item[0] == group.name] #See if group already exists in list
							if (groupIndex): #If the group is already in list
								translationOrder[groupIndex[0]][2].append(Object) #Add object to group list
								objectTotal	= objectTotal+1
							else:		#If group does not exist in list
								translationOrder.append([group.name, "Attribute Block", [Object]]) #Create new group in list amd add object
								objectTotal	= objectTotal+1
							break		#Dont look for any other groups for this object
						else:			#If object is not in group
							translationOrder[1][2].append(Object) #Add object to non-group list
							objectTotal	= objectTotal+1
			
			for light in lightList: light[1] = False	#Turn oll lights from previous pass off
			for light in translationOrder[0][2]:		#Create a list of lights for light export and group exclusions
				if (not lightList.count([light, False])): lightList.append([light, True]) #If light didn't already exist then add new light
			for light in lightList:				#Turn any existing lights that are in this scene back on
				if (translationOrder[0][2].count(light[0])): light[1] = True
			
			#### Build frame block
			frameCode = ["FrameBegin "+str(frame)+"\n"]
			isFraBeginCode	= GetProperty(scene, ButtonData[SCENES][WIN_BUTS][SCENE_BEGINFRAME_CODE][BUT_PROP])
			if (isFraBeginCode and isFraBeginCode != 'NONE'): frameCode.extend(ParseFragment(scene, "", isFraBeginCode, 1)) #Parse frames begin custom code
			## Insert display drivers
			if (GetProperty(scene, ButtonData[SCENES][WIN_BUTS][SCENE_USE_DISPLAY][BUT_PROP], "", True) and Preview == False): #Make file display from code
				frameCode.append(ParseTokens(scene, "", "\t"+GetProperty(scene, ButtonData[SCENES][WIN_BUTS][SCENE_DISPLAY_CODE][BUT_PROP], "", ButtonData[SCENES][WIN_BUTS][SCENE_DISPLAY_CODE][BUT_DEFAULT])+"\n"))
			if (GetProperty(scene, ButtonData[SCENES][WIN_BUTS][SCENE_USE_FRAME][BUT_PROP], "", True) or Preview == True): #Make framebuffer display from code
				frameCode.append(ParseTokens(scene, "", "\t"+GetProperty(scene, ButtonData[SCENES][WIN_BUTS][SCENE_FRAMEBUF_CODE][BUT_PROP], "", ButtonData[SCENES][WIN_BUTS][SCENE_FRAMEBUF_CODE][BUT_DEFAULT])+"\n"))
			## Insert camera RIB
			if (Preview):	camera = ""
			else:		camera = scene.objects.camera
			frameCode.extend(RibifyObject(scene, camera, frame, 1, True))
			
			## Insert world block
			frameCode.append("\tWorldBegin\n")
			isWorldCode			= GetProperty(scene, ButtonData[SCENES][WIN_BUTS][SCENE_BEGINWORLD_CODE][BUT_PROP])
			if (isWorldCode and isWorldCode != 'NONE'): frameCode.extend(ParseFragment(scene, "", isWorldCode, 2)) #Parse worlds begin custom code
			isSceneAtmoShader		= GetProperty(scene, ButtonData[SCENES][WIN_BUTS][SCENE_ATMO][BUT_PROP])
			if (isSceneAtmoShader and isSceneAtmoShader != 'NONE'): frameCode.extend(AddTabs(RibifyShader(scene, "", isSceneAtmoShader), 2)) #Parse atmosphere shader
			for index, group in enumerate(translationOrder): #Cycle through object groups
				groupCode		= []
				isGroupCode		= GetProperty(scene, translationOrder[index][0], ButtonData[GROUPS][WIN_BUTS][GRP_BEGIN_CODE][BUT_PROP])
				if (isGroupCode and isGroupCode != 'NONE'): groupCode.extend(ParseFragment(scene, "", isGroupCode)) #Parse groups custom begin code
				isGrpAtmoShader		= GetProperty(scene, translationOrder[index][0], ButtonData[GROUPS][WIN_BUTS][GRP_ATMO][BUT_PROP])
				if (isGrpAtmoShader and isGrpAtmoShader != 'NONE'): groupCode.extend(RibifyShader(scene, "", isGrpAtmoShader)) #Parse atmosphere shader
				for groupObject in translationOrder[index][2]: #Cycle through all objects in current group
					objectCount	= objectCount+1
					progress	= (objectCount/float(objectTotal))-0.1
					DrawProgressBar(progress, "obj:"+str(objectCount)+"-"+str(objectTotal)+" fr:"+str(frame)+"-"+str(fraEnd))
					parent = groupObject
					while (parent.parent): parent = parent.parent #See if base parent object is using dupli's
					if (groupObject == parent or not parent.DupObjects): #If this is not a dupli root object
						while QTest():		#Cycle through events looking for an esc
							if (QRead()[0] == ESCKEY): #If user escaped
								killExport = True
					
						if (not Preview or (Preview and (groupObject.sel or lightList.count([groupObject, True])))): #If previewing only render selected objects and lights
							print "\tExporting Object: "+groupObject.name
							groupCode.extend(RibifyObject(scene, groupObject, frame))
					
						if (killExport):	#If esc was hit then stop translation
							scene.render.currentFrame(originalFrame) #Reset scene and frame
							DrawProgressBar(0.0, "") #Reset progress bar
							DrawProgressBar(1.0, "") #Reset progress bar
							print "!!!Process Canceled!!!"
							return		#Stop translations
				if (index == 0):			#Build light RiIlluminate starts
					groupCode.append("##Scene light illuminates\n")
					for lightIndex, light in enumerate(lightList):
						if (light[1]): groupCode.append("Illuminate "+str(lightIndex+1)+" 1\n")
				isGroupCode		= GetProperty(scene, translationOrder[index][0], ButtonData[GROUPS][WIN_BUTS][GRP_END_CODE][BUT_PROP])
				if (isGroupCode and isGroupCode != 'NONE'): groupCode.extend(ParseFragment(scene, "", isGroupCode)) #Parse groups custom end code
				frameCode.extend(RibifyInstance(scene, "", translationOrder[index][0], groupCode, frame, translationOrder[index][1], [], 2))
			isWorldCode			= GetProperty(scene, ButtonData[SCENES][WIN_BUTS][SCENE_ENDWORLD_CODE][BUT_PROP])
			if (isWorldCode and isWorldCode != 'NONE'): frameCode.extend(ParseFragment(scene, "", isWorldCode, 2)) #Parse worlds end custom code
			frameCode.append("\tWorldEnd\n")
			isFraEndCode	= GetProperty(scene, ButtonData[SCENES][WIN_BUTS][SCENE_ENDFRAME_CODE][BUT_PROP])
			if (isFraEndCode and isFraEndCode != 'NONE'): frameCode.extend(ParseFragment(scene, "", isFraEndCode, 1)) #Parse frames end custom code
			frameCode.append("FrameEnd\n")
			
			#Write this frames translations into archive or main RIB
			mainrib = open(RibOutput, 'ab')
			mainrib.writelines(RibifyInstance(scene, "Archives"+sys.sep+"Scenes"+sys.sep, scene.name+"Sc", frameCode, frame, GetProperty(scene, ButtonData[SCENES][WIN_BUTS][SCENE_FRAME_ARCH][BUT_PROP], "", ButtonData[SCENES][WIN_BUTS][SCENE_FRAME_ARCH][BUT_TITLE][ButtonData[SCENES][WIN_BUTS][SCENE_FRAME_ARCH][BUT_DEFAULT]]), [], 0, True)) #Add frame to rib
			mainrib.close()
		
		scene.render.currentFrame(originalFrame)		#Reset frame
	
	DrawProgressBar(0.0, "")					#Reset progress bar
	DrawProgressBar(1.0, "")					#Reset progress bar
	
	manualRender	= GetProperty(scene, ButtonData[SCENES][WIN_BUTS][SCENE_CUSTOM_RENDER][BUT_PROP]) #Get custom render call if available
	if (manualRender and manualRender.strip()): renderCall = manualRender #If theres a custom render make it active
	else: renderCall = RenderBin					#Otherwise use default render call
	if (renderCall.count("<RIB>")): renderCall = renderCall.replace("<RIB>", "\""+RibOutput+"\"") #Parse any calls to insert rib in render options
	else: renderCall = renderCall+" \""+RibOutput+"\""		#Otherwise just add rib to end of options
	
	return renderCall						#Return render call string so it can be used or stored


####################################################################### START GUI GLOBAL FUNCTIONS
#### Renders current scene in current frame
def RenderFrame():
	global ButtonData, killExport
	killExport	= False
	scene		= Blender.Scene.GetCurrent()
	frame		= scene.render.currentFrame()
	Render		= ButtonData[ACTIONS][WIN_BUTS][ACT_RENDER_RIB][BUTTON].val
	Create		= ButtonData[ACTIONS][WIN_BUTS][ACT_CREATE_RIB][BUTTON].val
	Compile		= ButtonData[ACTIONS][WIN_BUTS][ACT_COMPILE_SL][BUTTON].val
	Export		= ButtonData[ACTIONS][WIN_BUTS][ACT_EXPORT_MAPS][BUTTON].val
	CleanupScenes()
	if (not PrepareProject(Compile, Export)):
		renderCall = RibifyScene(scene, frame, frame, "Pass0.rib", False, Create) #Export current scene and frame
		print "Export Complete!"
		if (Render and renderCall):
			print "Rendering Frame With: "+renderCall
			os.system(renderCall)				#Lets render it!!!
			print "Process Complete!"


#### Renders current scene from sta to end
def RenderAnimation():
	global ButtonData, killExport
	killExport	= False
	renderPassCalls	= []
	Render		= ButtonData[ACTIONS][WIN_BUTS][ACT_RENDER_RIB][BUTTON].val
	Create		= ButtonData[ACTIONS][WIN_BUTS][ACT_CREATE_RIB][BUTTON].val
	Compile		= ButtonData[ACTIONS][WIN_BUTS][ACT_COMPILE_SL][BUTTON].val
	Export		= ButtonData[ACTIONS][WIN_BUTS][ACT_EXPORT_MAPS][BUTTON].val
	userScene	= Blender.Scene.GetCurrent()			#Get current scene so we can return to it later
	
	if (not PrepareProject(Compile, Export)):			#If project folders are ready then process animation
		renderPasses	= GetProperty(Blender.Scene.Get()[0], ButtonData[PROJECT][WIN_BUTS][PROJECT_PASSES][BUT_PROP]) #Get custom render passes if specified
		passList	= []
		
		if (renderPasses and renderPasses.strip()):		#If theres custom render passes and its not whitespace then process
			for passString in renderPasses.split(','):	#Split pass string by scene separators
				try:
					passParameters	= passString.split(':') #Split scene string by parameter separator
					passRange	= passParameters[1].split('-') #Split parameter string by range separator (always assume a range is given)
					if (len(passRange) == 1): passRange.extend(passRange) #If only one range then set to as from
					passList.append([Blender.Scene.Get(passParameters[0].strip()), int(passRange[0]), int(passRange[1])]) #Put it all in pass list
				except:
					ErrorPopup("Could not parse render passes string, check scene names and separators usage!")
					return
		else:							#Otherwise render current scene from "sta" to "end"
			scene		= Blender.Scene.GetCurrent()
			passList	= [[scene, scene.render.sFrame, scene.render.eFrame]]
		
		CleanupScenes()						#Reset scnene properties before passes so data can be shared between passes
		for passIndex, passData in enumerate(passList):		#Cycle through passes and call export scene and render per pass
			passData[0].makeCurrent()			#Make renderpass scene current
			renderPassCalls.append(RibifyScene(passData[0], passData[1], passData[2], "Pass"+str(passIndex)+".rib", False, Create)) #Make RIBS and collect rendercalls
			if (killExport): break				#If killExport then stop scene passes
		
		print "Export Complete!"
		userScene.makeCurrent()					#Return scene user was last on
		
		if (Render and renderPassCalls):			#If we are supposed to lets render passes!
			for passIndex, renderCall in enumerate(renderPassCalls): #Cycle through render calls
				if (renderCall):			#Make sure theres an actual call
					print "Rendering Pass"+str(passIndex)+" With: "+renderCall
					os.system(renderCall)		#Lets render it!!!
				else:	print "Could not render Pass"+str(passIndex)+"!"
			print "Process Complete!"

#### Renders a preview from last 3d view
def RenderPreview():
	global ButtonData, killExport
	killExport	= False
	scene		= Blender.Scene.GetCurrent()
	frame		= scene.render.currentFrame()
	Compile		= ButtonData[ACTIONS][WIN_BUTS][ACT_COMPILE_SL][BUTTON].val
	Export		= ButtonData[ACTIONS][WIN_BUTS][ACT_EXPORT_MAPS][BUTTON].val
	CleanupScenes()
	if (not PrepareProject(Compile, Export)):
		renderCall = RibifyScene(scene, frame, frame, "Preview.rib", True, True) #Export current scene and frame but use 3D view matrix
		print "Export Complete!"
		if (renderCall):
			print "Rendering Preview With: "+renderCall
			os.system(renderCall)				#Lets render it!!!
			print "Process Complete!"


#### Passes current sub-window settings as defaults for new windows
def SetDefaults(subWindow):
	global ButtonData
	try:
		for index, default in enumerate(ButtonData[subWindow][WIN_BUTS]):
			if (ButtonData[subWindow][WIN_BUTS][index][BUTTON]): ButtonData[subWindow][WIN_BUTS][index][BUT_DEFAULT] = ButtonData[subWindow][WIN_BUTS][index][BUTTON].val
		PupMenu("New Defaults Set")
	except:
		ErrorPopup("Defaults could not be set!")


#### Show script help
def ShowHelp(script = "mosaic.py"):
	Blender.ShowHelp(script)


#### Callback function for render directory selection
def RenderDirCallback(filename):
	global RenderDir, ButtonData
	RenderDir = filename.rstrip()
	ButtonData[SETTINGS][WIN_BUTS][SET_OUTPUT_DIR][BUT_TIP] = "Render to: "+RenderDir
	UpdateRegistry()


#### Find and select object with Name and make active
def SelectObject(Name=""):
	scene = Blender.Scene.GetCurrent()
	object = [item for item in scene.objects if item.name == Name]
	object[0].select(True)
	scene.objects.selected = object


#### Set ID Properties in ArrayIndex of ButtonData array to object selected in first menu item of choosen subwindow
def SetProperties(ArrayIndex, selection):
	global ButtonData
	for index, item in enumerate(ButtonData[ArrayIndex][WIN_BUTS][1:]): #Cycle through all settings under this subwindow and assign there values to an ID property of selected object
		if (ButtonData[ArrayIndex][WIN_BUTS][index+1][BUTTON] and ButtonData[ArrayIndex][WIN_BUTS][index+1][BUT_PROP] and selection): #Make sure button is created and its property has name
			if (ButtonData[ArrayIndex][WIN_BUTS][index+1][BUT_TYPE] == 1): #If this is a list menu and menu has been created then find selection from menu
				if (ButtonData[ArrayIndex][WIN_BUTS][index+1][BUT_MENU]): selection.properties[ButtonData[ArrayIndex][WIN_BUTS][index+1][BUT_PROP]] = ButtonData[ArrayIndex][WIN_BUTS][index+1][BUT_MENU][ButtonData[ArrayIndex][WIN_BUTS][index+1][BUTTON].val]
			else:						#Otherwise then pass value straight through
				selection.properties[ButtonData[ArrayIndex][WIN_BUTS][index+1][BUT_PROP]] = ButtonData[ArrayIndex][WIN_BUTS][index+1][BUTTON].val


#### Create a filtered and sorted string of names suitable for PupMenu, type determines what blender objects are listed or pass Array of items through List
#### also returns each name in order in array for position/name reference later. Type info: (-1=nothing, 0=Texts, 1=Scenes, 2=Cameras, 3=Groups, 4=Geometry, 5=Lamps, 6=Materials)
def CreateMenu(Title="Menu Title", Filter="", Type=-1, List=[], FirstItem="", Sort=True):
	Title = Title + ":%t"
	
	if (not List):
		if (Type == 0):	  					#List TEXT FILES
			List = [item.name for item in Blender.Text.Get()]
		elif (Type == 1): 					#List SCENES
			List = [item.name for item in Blender.Scene.Get()]
		elif (Type == 2): 					#List CAMERAS
			List = [item.name for item in Blender.Scene.GetCurrent().objects if item.getType() == "Camera"]
		elif (Type == 3): 					#List GROUPS
			List = [item.name for item in Blender.Group.Get()]
		elif (Type == 4): 					#list EXPORTABLE GEOMETRY
			List = [item.name for item in Blender.Scene.GetCurrent().objects if item.getType() == "Mesh" or item.getType() == "Curve" or item.getType() == "Surf"]
		elif (Type == 5): 					#List LAMPS
			List = [item.name for item in Blender.Scene.GetCurrent().objects if item.getType() == "Lamp"]
		elif (Type == 6): 					#List MATERIALS
			List = [item.name for item in Blender.Material.Get()]
	
	menu = [item for item in List if not Filter or item.find(Filter) > -1] #Get filtered names in list
	if (Sort == True): menu.sort()					#Sort list
	if (FirstItem):	menu.insert(0, FirstItem)			#Insert manual first item if present
	
	for item in menu:						#Create popup menu string from sorted list
		Title = Title + '|' + item
	menu.insert(0, Title)						#Put menu string at top of list
	return menu


#### Utility for automatically generating or re-using a shader code fragment in blender from a shader source file or from shader name in environment variables from OS
#### Pass the name of the "shader" and set "source" to True if shader name is a blender text shader source file
def ShaderUtility(shader, source = True):
	global Tokens, Filters, DialogData, InfoBin
	shaderTypes	= ["Surface", "Displacement", "Volume", "Imager", "Light"]
	paraClasses	= ["constant", "uniform", "varying"]
	paraTypes	= ["integer", "float", "color", "point", "vector", "normal", "matrix", "hpoint", "string"]
	fragmentName	= ""
	shaderName	= ""
	shaderType	= []
	shaderText	= []
	paraClass	= []
	paraType	= []
	paraIndex	= 0
	paraName	= ""
	paraDefault	= ""
	default		= False
	
	if (not InfoBin):
		ErrorPopup("Must set shader info binary under \"MOSAIC setting\" tab!")
		return
	
	if (shader):							#Only process if theres a shader name
		print "Creating shader fragment"
		OutputDir = GetProjectFolder()				#Get the project folder name so we can check it
		if (SetupDirectories(OutputDir)): return		#Setup output directories incase they aren't set yet
		os.chdir(OutputDir+"Cache")				#Make sure current directory is in projects "Cache" folder
		print "\tCleaning Cache Folder..."
		DelTree(OutputDir+"Cache")				#Be sure to clean cache so no ealier files exist
		
		if (source):						#If set to source then compile shader before getting info
			for shaderInclude in [text for text in Blender.Text.Get() if text.name.count(Filters[7])]: #Cycle through all text files looking for includes
				ExportText(shaderInclude)
			try:
				if(CompileShader(Blender.Text.Get(shader))): #Try to get blender text file and compile it
					ErrorPopup("Could not write shader, check folder and permissions!")
					return
			except:
				ErrorPopup("Shader text file does not exist!")
				return
		
		shaderName = sys.splitext(sys.basename(shader))[0]	#Get shader name from stripped shader parameter (this means shader output name must match .sl file name!)
		print "\tGetting Info For "+shaderName+"..."
		os.system(InfoBin+" \""+shaderName+"\">shaderinfo")	#Create a shaderinfo file from shader info binary output
		if (not sys.exists("shaderinfo")):			#Make sure shaderinfo was made
			ErrorPopup("Could not generate shader info, check console for details!")
			return
		shaderinfo = open("shaderinfo", 'rb')			#Open shaderinfo to processing
		for line in shaderinfo.readlines():
			if (line.strip()):				#If theres something in this line
				if (not shaderType):			#Make sure we determine shader type first
					shaderType	= [sType for sType in shaderTypes if line.lower().split()[0].count(sType.lower())] #See if first word of this line has the shader type and if so then set type accordingly
					if (shaderType):		#If type has been determined then lets create a shader fragment
						DialogData[1][0][1].val = Filters[shaderTypes.index(shaderType[0])+2]+shaderName #Show dialog to make fragment name defaults to filtertype+shadername
						result			= Blender.Draw.PupBlock("Shader Fragment Name", DialogData[1])
						if (result > 0):	fragmentName = DialogData[1][0][1].val
						else:			break #Leave if no name given
						try:
							shaderText	= Blender.Text.Get(fragmentName) #See if fragment already exists
							oldLines	= shaderText.asLines() #Capture old fragment to reuse lines
							shaderText.clear() #Clear it so it can be remade
						except:
							shaderText	= Blender.Text.New(fragmentName) #If fragment doesnt exist then make new
							oldLines	= [] #Make empty so we dont check for old parameter values
						if (shaderType[0] == shaderTypes[4]):
							result = PupMenu(CreateMenu("Select Light Shader Type", "", 0, ["RiLightSource", "RiAreaLightSource"], "", False)[0], 27) #Ask user to specify what light type to make
							if (result == 1):	shaderType = ["LightSource"]
							elif (result == 2):	shaderType = ["AreaLightSource"]
							else:			shaderType = ["LightSource"] #Assume default if no selection
						elif (shaderType[0] == shaderTypes[2]):
							result = PupMenu(CreateMenu("Select Volume Shader Type", "", 0, ["RiAtmosphere", "RiInterior", "RiExterior"], "", False)[0], 27) #Ask user to specify what volume type to make
							if (result == 1):	shaderType = ["Atmosphere"]
							elif (result == 2):	shaderType = ["Interior"]
							elif (result == 3):	shaderType = ["Exterior"]
							else:			shaderType = ["Atmosphere"] #Assume default if no selection
						shaderText.write(shaderType[0]+" \""+shaderName+"\"")
						if (shaderType[0] == "LightSource" or shaderType[0] == "AreaLightSource"): shaderText.write(" <LightID_I>") #Add light ID token if this is a light
				elif(not default):			#If not default then look for parameter info
					paraWords	= line.replace("\"", "").split() #Split separate words out of current line
					if (len(paraWords) > 2):	#Be sure theres enough words for valid parameters
						paraType	= [[paraWords[len(paraWords)-1], index] for index, pType in enumerate(paraTypes) if paraWords[len(paraWords)-1].lower().count(pType)] #Find this parameters type
						paraClass	= [paraWords[len(paraWords)-2] for pClass in paraClasses if paraWords[len(paraWords)-2].lower().count(pClass)] #Find this parameters class
						if (paraType):
							paraName	= line.split()[0].replace("\"", "")
							paraIndex	= paraType[0][1]
							shaderText.write("\n")
							reUse		= 2 #Default to remaking parameter
							if (len(oldLines) >= shaderText.nlines and oldLines[shaderText.nlines-1].count(paraName)): #See if parameter already exists in previous fragment
								reUse = PupMenu(CreateMenu("Reuse existing parameter for "+paraType[0][0]+" "+paraName+"?", "", 0, ["YES (default)", "NO"], "", False)[0], 27)
							if (not oldLines or reUse > 1): #If there is no previous fragment or they selected not to reuse parameter then remake it
								shaderText.write("\t\"")
								if (paraClass): shaderText.write(paraClass[0]+" ")
								shaderText.write(paraType[0][0]+" ")
								shaderText.write(paraName+"\" ")
								default = True
								continue
							else:		#If were reusing old fragment then just write current line of old fragment to new and go to next parameter
								shaderText.write(oldLines[shaderText.nlines-1])
								default = False
								continue
				elif(default):				#If default then look for default value
					if (line.count(":")):		#Assume default line will have ":" before default value
						paraDefault	= line.lower().split(":")[1].replace("{", "").replace("}", "").replace("[", "").replace("]", "").replace(",", "") #Make list of values
						if (paraIndex != 8 and paraDefault.count("\"")): paraDefault = paraDefault[paraDefault.rfind("\"")+1:] #If this is not a string type then strip any commented words out
						paraDefault	= "[ "+paraDefault.lstrip().rstrip()+" ]" #Strip and bracket for use
						if (shaderType[0] == "LightSource"):										tokenIndex = 0
						elif (shaderType[0] == "Surface" or shaderType[0] == "Displacement" or shaderType[0] == "AreaLightSource"):	tokenIndex = 1
						elif (shaderType[0] == "Imager"):										tokenIndex = 2
						else:														tokenIndex = 4
						tokenMenu	= CreateMenu(shaderType[0]+" "+shaderName+"( "+paraType[0][0]+" "+paraName+" )", "", -1, Tokens[tokenIndex][paraIndex]+Tokens[3][paraIndex], paraDefault, True) #Make token selection menu
						tokenResult	= PupMenu(tokenMenu[0], 27)
						if (tokenResult > 0):
							paraDefault = tokenMenu[tokenResult]
							if (tokenResult > 1): #If token is greater than default token then process it
								if (paraDefault == "Add User Value"): #Let user manually enter value if choosen
									DialogData[8][0][1].val	= tokenMenu[1] #Start it at shader parameters default
									stringResult		= Blender.Draw.PupBlock("Manually enter parameter", DialogData[8])
									paraDefault		= DialogData[8][0][1].val
								else:
									if (paraDefault.count("_X")):	#Show texture channel selection menu if using "_X" in token
										texMenu = CreateMenu("Select texture channel for \""+tokenMenu[tokenResult]+"\"", "", 0, ['1','2','3','4','5','6','7','8','9','10'], "", False) #Make channel selection menu
										texResult = PupMenu(texMenu[0], 27)
										if (texResult == 0): texResult = 1 #Assume default if no selection
										paraDefault = paraDefault.replace("_X", "_X"+texMenu[texResult]) #If channel was selected append it to "_X"
									if (paraIndex < 2): #If this is a integer or float call the range adjust dialog
										rangeIndex = [index for index, item in enumerate(StandardRanges) if item[0] == paraDefault] #See if there are some pre-defined ranges for this control...
										if (rangeIndex): #If so then apply them as default to the range dialog
											DialogData[7][0][1].val = StandardRanges[rangeIndex[0]][2]
											DialogData[7][1][1].val = StandardRanges[rangeIndex[0]][1]
										else:
											DialogData[7][0][1].val = "1.0"
											DialogData[7][1][1].val = "0.0"
										stringResult		= Blender.Draw.PupBlock("Adjust control value range", DialogData[7])
										paraDefault		= paraDefault+"_M"+str(DialogData[7][0][1].val)+"_A"+str(DialogData[7][1][1].val)
									paraDefault = paraDefault+"_"+paraTypes[paraIndex][0].upper() #Add type to token
									paraDefault = "<"+paraDefault+">" #Close out the token for processing
						else:	paraDefault = tokenMenu[1] #Assume default option on no selection
						shaderText.write(paraDefault)
						default = False
		if (not shaderType):	ErrorPopup("Could not determine shader type, check console for details!")
		else:			print "Shader fragment "+fragmentName+" created"
		shaderinfo.close()


#### Update selected sub-window ButtonData values based on current selections and attached object data (also handles object validation, and button/subwindow collapse states)
def UpdateMenuData(ArrayIndex):
	global ButtonData, Filters
	selection = ""
	
	if (ButtonData[ArrayIndex]):
		ArrayItem = ButtonData[ArrayIndex]
		#Figure Buttons
		for index, item in enumerate(ButtonData[ArrayIndex][WIN_BUTS]):
			if (ButtonData[ArrayIndex][WIN_BUTS][index][BUT_SHOW] == True): #Is button set to show
				if (ButtonData[ArrayIndex][WIN_BUTS][index][BUT_TYPE] == 1): #If this is supposed to be a list menu...
					#Get old menu information to extract string selection and compare to current selection
					OldMenu = ButtonData[ArrayIndex][WIN_BUTS][index][BUT_MENU]
					MenuIndex = ButtonData[ArrayIndex][WIN_BUTS][index][BUTTON].val
					
					#Create or pass menu based on title selection
					if (ButtonData[ArrayIndex][WIN_BUTS][index][BUT_TITLE] == "CodeF"): ButtonData[ArrayIndex][WIN_BUTS][index][BUT_MENU] = CreateMenu(ButtonData[ArrayIndex][WIN_BUTS][index][BUT_PROP], Filters[0], 0, [], "NONE")
					elif (ButtonData[ArrayIndex][WIN_BUTS][index][BUT_TITLE] == "SourceF"): ButtonData[ArrayIndex][WIN_BUTS][index][BUT_MENU] = CreateMenu(ButtonData[ArrayIndex][WIN_BUTS][index][BUT_PROP], Filters[1], 0, [], "NONE")
					elif (ButtonData[ArrayIndex][WIN_BUTS][index][BUT_TITLE] == "SurfaceF"): ButtonData[ArrayIndex][WIN_BUTS][index][BUT_MENU] = CreateMenu(ButtonData[ArrayIndex][WIN_BUTS][index][BUT_PROP], Filters[2], 0, [], "NONE")
					elif (ButtonData[ArrayIndex][WIN_BUTS][index][BUT_TITLE] == "DisplacementF"): ButtonData[ArrayIndex][WIN_BUTS][index][BUT_MENU] = CreateMenu(ButtonData[ArrayIndex][WIN_BUTS][index][BUT_PROP], Filters[3], 0, [], "NONE")
					elif (ButtonData[ArrayIndex][WIN_BUTS][index][BUT_TITLE] == "VolumeF"): ButtonData[ArrayIndex][WIN_BUTS][index][BUT_MENU] = CreateMenu(ButtonData[ArrayIndex][WIN_BUTS][index][BUT_PROP], Filters[4], 0, [], "NONE")
					elif (ButtonData[ArrayIndex][WIN_BUTS][index][BUT_TITLE] == "ImageF"): ButtonData[ArrayIndex][WIN_BUTS][index][BUT_MENU] = CreateMenu(ButtonData[ArrayIndex][WIN_BUTS][index][BUT_PROP], Filters[5], 0, [], "NONE")
					elif (ButtonData[ArrayIndex][WIN_BUTS][index][BUT_TITLE] == "LightF"): ButtonData[ArrayIndex][WIN_BUTS][index][BUT_MENU] = CreateMenu(ButtonData[ArrayIndex][WIN_BUTS][index][BUT_PROP], Filters[6], 0, [], "NONE")
					elif (ButtonData[ArrayIndex][WIN_BUTS][index][BUT_TITLE] == "SceneF"): ButtonData[ArrayIndex][WIN_BUTS][index][BUT_MENU] = CreateMenu(ButtonData[ArrayIndex][WIN_BUTS][index][BUT_PROP], "", 1, [], "")
					elif (ButtonData[ArrayIndex][WIN_BUTS][index][BUT_TITLE] == "CameraF"): ButtonData[ArrayIndex][WIN_BUTS][index][BUT_MENU] = CreateMenu(ButtonData[ArrayIndex][WIN_BUTS][index][BUT_PROP], "", 2, [], "NONE")
					elif (ButtonData[ArrayIndex][WIN_BUTS][index][BUT_TITLE] == "GroupF"): ButtonData[ArrayIndex][WIN_BUTS][index][BUT_MENU] = CreateMenu(ButtonData[ArrayIndex][WIN_BUTS][index][BUT_PROP], "", 3, [], "NONE")
					elif (ButtonData[ArrayIndex][WIN_BUTS][index][BUT_TITLE] == "GeometryF"): ButtonData[ArrayIndex][WIN_BUTS][index][BUT_MENU] = CreateMenu(ButtonData[ArrayIndex][WIN_BUTS][index][BUT_PROP], "", 4, [], "NONE")
					elif (ButtonData[ArrayIndex][WIN_BUTS][index][BUT_TITLE] == "LampF"): ButtonData[ArrayIndex][WIN_BUTS][index][BUT_MENU] = CreateMenu(ButtonData[ArrayIndex][WIN_BUTS][index][BUT_PROP], "", 5, [], "NONE")
					elif (ButtonData[ArrayIndex][WIN_BUTS][index][BUT_TITLE] == "MaterialF"): ButtonData[ArrayIndex][WIN_BUTS][index][BUT_MENU] = CreateMenu(ButtonData[ArrayIndex][WIN_BUTS][index][BUT_PROP], "", 6, [], "NONE")
					else: ButtonData[ArrayIndex][WIN_BUTS][index][BUT_MENU] = ButtonData[ArrayIndex][WIN_BUTS][index][BUT_TITLE]
					
					#If previous menu hasnt been initialized then initialize it!
					if (len(OldMenu) == 0): OldMenu = ButtonData[ArrayIndex][WIN_BUTS][index][BUT_MENU]
					
					if (OldMenu != ButtonData[ArrayIndex][WIN_BUTS][index][BUT_MENU]): #If the old and new menus dont match then we need to correct the selections index
						try: ButtonData[ArrayIndex][WIN_BUTS][index][BUTTON].val = ButtonData[ArrayIndex][WIN_BUTS][index][BUT_MENU].index(OldMenu[MenuIndex]) #Find the buttons selection in new menu
						except: ButtonData[ArrayIndex][WIN_BUTS][index][BUTTON].val = ButtonData[ArrayIndex][WIN_BUTS][index][BUT_DEFAULT] #If old selection cant be found assume its been deleted and reset menu to default
					
					if (index == 0):	#If the first button in sub is a menu and set to NONE then hide all options below button in subwindow
						if (ButtonData[ArrayIndex][WIN_BUTS][index][BUT_MENU][ButtonData[ArrayIndex][WIN_BUTS][index][BUTTON].val] == "NONE"):
							for index2, item2 in enumerate(ButtonData[ArrayIndex][WIN_BUTS][1:]): ButtonData[ArrayIndex][WIN_BUTS][index2+1][BUT_SHOW] = False
						else:		#If this is the first button and not NONE then unhide all following buttons in sub and select object pointed too
							for index2, item2 in enumerate(ButtonData[ArrayIndex][WIN_BUTS][1:]): ButtonData[ArrayIndex][WIN_BUTS][index2+1][BUT_SHOW] = True
							#Select object based on subwindow type
							if (ArrayIndex == SCENES or ArrayIndex == GROUPS): selection = Blender.Scene.Get(ButtonData[SCENES][WIN_BUTS][SCENE_SELECT][BUT_MENU][ButtonData[SCENES][WIN_BUTS][SCENE_SELECT][BUTTON].val]) #Scene selction
							elif (ArrayIndex == MATERIALS): selection = Blender.Material.Get(ButtonData[ArrayIndex][WIN_BUTS][index][BUT_MENU][ButtonData[ArrayIndex][WIN_BUTS][index][BUTTON].val]) #Material Selection
							else: selection = Blender.Object.Get(ButtonData[ArrayIndex][WIN_BUTS][index][BUT_MENU][ButtonData[ArrayIndex][WIN_BUTS][index][BUTTON].val]) #Object Selection
					else:			#If this is not the first button get property from object into menu
						if (ArrayIndex == GROUPS): #If this is a subgroup extraction
							try: ButtonData[ArrayIndex][WIN_BUTS][index][BUTTON].val = ButtonData[ArrayIndex][WIN_BUTS][index][BUT_MENU].index(selection.properties[ButtonData[ArrayIndex][WIN_BUTS][0][BUT_MENU][ButtonData[ArrayIndex][WIN_BUTS][0][BUTTON].val]][ButtonData[ArrayIndex][WIN_BUTS][index][BUT_PROP]])
							except: ButtonData[ArrayIndex][WIN_BUTS][index][BUTTON].val = ButtonData[ArrayIndex][WIN_BUTS][index][BUT_DEFAULT] #If no property then set button to default
						else:		#If this is NOT a subgroup extraction
							#If theres a selection and it has a property and that property name is in menu then return the index back to menu as new selection for current selection
							try: ButtonData[ArrayIndex][WIN_BUTS][index][BUTTON].val = ButtonData[ArrayIndex][WIN_BUTS][index][BUT_MENU].index(selection.properties[ButtonData[ArrayIndex][WIN_BUTS][index][BUT_PROP]])
							except: ButtonData[ArrayIndex][WIN_BUTS][index][BUTTON].val = ButtonData[ArrayIndex][WIN_BUTS][index][BUT_DEFAULT] #If no property then set button to default
				elif (ButtonData[ArrayIndex][WIN_BUTS][index][BUT_TYPE] > 4): continue #If this is a graphic then skip
				elif (ButtonData[ArrayIndex][WIN_BUTS][index][BUT_TYPE] != 0):#If this is not a list menu or a pushbutton then...
					if (ArrayIndex == PROJECT): selection = Blender.Scene.Get()[0]
					if (ArrayIndex == GROUPS): #If this is a subgroup extraction
						try: ButtonData[ArrayIndex][WIN_BUTS][index][BUTTON].val = selection.properties[ButtonData[ArrayIndex][WIN_BUTS][0][BUT_MENU][ButtonData[ArrayIndex][WIN_BUTS][0][BUTTON].val]][ButtonData[ArrayIndex][WIN_BUTS][index][BUT_PROP]]
						except: ButtonData[ArrayIndex][WIN_BUTS][index][BUTTON].val = ButtonData[ArrayIndex][WIN_BUTS][index][BUT_DEFAULT] #If no property then set button to default
					else:			#If this is NOT a subgroup extraction
						try: ButtonData[ArrayIndex][WIN_BUTS][index][BUTTON].val = selection.properties[ButtonData[ArrayIndex][WIN_BUTS][index][BUT_PROP]] #Pass value straight through
						except: ButtonData[ArrayIndex][WIN_BUTS][index][BUTTON].val = ButtonData[ArrayIndex][WIN_BUTS][index][BUT_DEFAULT] #If no property then set button to default


#### Draws a fancy titled subframe, return the final height of the window (uses global ButtonData draw windows and buttons)
def SubFrame(x = 0, y = 100, width = 100, ArrayIndex = 0): #ArrayIndex is the index in ButtonData to the sub-window to draw in ButtonData array
	global ButtonData, MousePos
	TitleHeight	= 15
	TextOffset	= TitleHeight/2+4
	Bevel		= 6
	ArrowSize	= 4
	WindowGap	= 6
	ButtonGap	= 3
	PosInc		= y
	
	#Grab colors applied to standard areas of Blender so interface looks built in
	TitleColor	= Theme.Get()[0].get('BUTS').header		#Color of menu title
	TextColor	= Theme.Get()[0].get('BUTS').text_hi		#Color of submenu text
	TextColor2	= Theme.Get()[0].get('ui').menu_text		#Color of menu text
	TabColor	= [TitleColor[0]/4*3, TitleColor[1]/4*3, TitleColor[2]/4*3] #Color of System submenu tabs
	BackColor	= Theme.Get()[0].get('BUTS').panel		#Color of System submenu backgrounds
	
	#Collapse button if left mouse click in title subWindow title area
	if (MousePos[0] > x and MousePos[0] < x+width and MousePos[1] > y-TitleHeight and MousePos[1] < y):
		ButtonData[ArrayIndex][WIN_COLLAPSE] = not ButtonData[ArrayIndex][WIN_COLLAPSE]
	
	#Make sure menu data is revised for visible subs
	if (not ButtonData[ArrayIndex][WIN_COLLAPSE]): UpdateMenuData(ArrayIndex)
	
	#Draw Tab
	glColor3f(TabColor[0]/256.0*ButtonData[ArrayIndex][WIN_COLOR][0], TabColor[1]/256.0*ButtonData[ArrayIndex][WIN_COLOR][1], TabColor[2]/256.0*ButtonData[ArrayIndex][WIN_COLOR][2])
	glBegin(GL_POLYGON)
	glVertex2i(x, y-TitleHeight+Bevel)
	glVertex2i(x, y-Bevel)
	glVertex2i(x+Bevel/3, y-Bevel/3)
	glVertex2i(x+Bevel, y)
	glVertex2i(x+width-Bevel, y)
	glVertex2i(x+width-Bevel/3, y-Bevel/3)
	glVertex2i(x+width, y-Bevel)
	if (ButtonData[ArrayIndex][WIN_COLLAPSE]):			#Change titles bottom radius effect based on collapse state
		glVertex2i(x+width-Bevel/3, y-TitleHeight+Bevel/3)
		glVertex2i(x+width-Bevel, y-TitleHeight)
		glVertex2i(x+Bevel, y-TitleHeight)
		glVertex2i(x+Bevel/3, y-TitleHeight+Bevel/3)
	else:
		glVertex2i(x+width, y-TitleHeight)
		glVertex2i(x, y-TitleHeight)
	glEnd()
	
	PosInc = PosInc-TitleHeight
	
	if (not ButtonData[ArrayIndex][WIN_COLLAPSE]):			#Draw Buttons and Background according to Collapse state
		
		#Draw BackGround Top
		glEnable(GL_BLEND)
		glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
		glColor4f(BackColor[0]/256.0*ButtonData[ArrayIndex][WIN_COLOR][0], BackColor[1]/256.0*ButtonData[ArrayIndex][WIN_COLOR][1], BackColor[2]/256.0*ButtonData[ArrayIndex][WIN_COLOR][2], BackColor[WIN_COLOR]/256.0*ButtonData[ArrayIndex][WIN_COLOR][3])
		glRecti(x, PosInc, x+width, PosInc-WindowGap+ButtonGap)
		glDisable(GL_BLEND)
		
		PosInc = PosInc-WindowGap+ButtonGap
				
		#Draw Buttons
		for index, item in enumerate(ButtonData[ArrayIndex][WIN_BUTS]):
			if (ButtonData[ArrayIndex][WIN_BUTS][index][BUT_SHOW] == True):	#Is button set to show
				
				if (ButtonData[ArrayIndex][WIN_BUTS][index][BUT_TYPE] == 5):	ButtonHeight = 3 #If this is a line
				else:								ButtonHeight = 18 #Otherwise this is a button
				ButWidth = (width-WindowGap*2)/ButtonData[ArrayIndex][WIN_BUTS][index][BUT_WIDTH_DIV]-ButtonGap #Figure button with divider in array if greater than 1 then divide
				ButX = x+WindowGap+((ButWidth+ButtonGap)*ButtonData[ArrayIndex][WIN_BUTS][index][BUT_DIV_POS]) #Figure button position according to divider position in array
				if (ButtonData[ArrayIndex][WIN_BUTS][index][BUT_DIV_POS] == 0):	#If position in array is set to zero move down to next button otherwise stay in place
					#Draw Button BackGround
					glEnable(GL_BLEND)
					glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
					glColor4f(BackColor[0]/256.0*ButtonData[ArrayIndex][WIN_COLOR][0], BackColor[1]/256.0*ButtonData[ArrayIndex][WIN_COLOR][1], BackColor[2]/256.0*ButtonData[ArrayIndex][WIN_COLOR][2], BackColor[3]/256.0*ButtonData[ArrayIndex][WIN_COLOR][3])
					glRecti(x, PosInc, x+width, PosInc-ButtonGap-ButtonHeight)
					glDisable(GL_BLEND)
					PosInc = PosInc-ButtonGap-ButtonHeight
								
				if (ButtonData[ArrayIndex][WIN_BUTS][index][BUT_TYPE] == 0):	#If this is supposed to be a button...
					ButtonData[ArrayIndex][WIN_BUTS][index][BUTTON] = PushButton(ButtonData[ArrayIndex][WIN_BUTS][index][BUT_TITLE], ButtonData[ArrayIndex][WIN_EVENT]+index, ButX, PosInc, ButWidth, ButtonHeight, ButtonData[ArrayIndex][WIN_BUTS][index][BUT_TIP])
				
				elif (ButtonData[ArrayIndex][WIN_BUTS][index][BUT_TYPE] == 1): #If this is supposed to be a list menu...
					#Draw menu description
					glColor3f(TextColor2[0]/256.0, TextColor2[1]/256.0, TextColor2[2]/256.0)
					glRasterPos2d(ButX, PosInc+5)
					Text(ButtonData[ArrayIndex][WIN_BUTS][index][BUT_PROP], 'normal')
					ButX = ButX+130
					ButWidth = ButWidth-130
					#Draw Menu
					ButtonData[ArrayIndex][WIN_BUTS][index][BUTTON] = Menu(ButtonData[ArrayIndex][WIN_BUTS][index][BUT_MENU][0], ButtonData[ArrayIndex][WIN_EVENT]+index, ButX, PosInc, ButWidth, ButtonHeight, ButtonData[ArrayIndex][WIN_BUTS][index][BUTTON].val, ButtonData[ArrayIndex][WIN_BUTS][index][BUT_TIP])
				
				elif (ButtonData[ArrayIndex][WIN_BUTS][index][BUT_TYPE] == 2): #If this is supposed to be a number button...
					ButtonData[ArrayIndex][WIN_BUTS][index][BUTTON] = Number(ButtonData[ArrayIndex][WIN_BUTS][index][BUT_TITLE], ButtonData[ArrayIndex][WIN_EVENT]+index, ButX, PosInc, ButWidth, ButtonHeight, ButtonData[ArrayIndex][WIN_BUTS][index][BUTTON].val, ButtonData[ArrayIndex][WIN_BUTS][index][BUT_MIN], ButtonData[ArrayIndex][WIN_BUTS][index][BUT_MAX], ButtonData[ArrayIndex][WIN_BUTS][index][BUT_TIP])
					
				elif (ButtonData[ArrayIndex][WIN_BUTS][index][BUT_TYPE] == 3): #If this is supposed to be a toggle button...
					ButtonData[ArrayIndex][WIN_BUTS][index][BUTTON] = Toggle(ButtonData[ArrayIndex][WIN_BUTS][index][BUT_TITLE], ButtonData[ArrayIndex][WIN_EVENT]+index, ButX, PosInc, ButWidth, ButtonHeight, ButtonData[ArrayIndex][WIN_BUTS][index][BUTTON].val, ButtonData[ArrayIndex][WIN_BUTS][index][BUT_TIP])
					
				elif (ButtonData[ArrayIndex][WIN_BUTS][index][BUT_TYPE] == 4): #If this is supposed to be a string button...
					if (ButtonData[ArrayIndex][WIN_BUTS][index][BUT_WIDTH_DIV] == 1): #If text is all on one line separate description, otherwise show in text
						#Draw text description
						glColor3f(TextColor2[0]/256.0, TextColor2[1]/256.0, TextColor2[2]/256.0)
						glRasterPos2d(ButX, PosInc+5)
						Text(ButtonData[ArrayIndex][WIN_BUTS][index][BUT_TITLE], 'normal')
						ButX = ButX+130
						ButWidth = ButWidth-130
						ButtonData[ArrayIndex][WIN_BUTS][index][BUTTON] = String("", ButtonData[ArrayIndex][WIN_EVENT]+index, ButX, PosInc, ButWidth, ButtonHeight, ButtonData[ArrayIndex][WIN_BUTS][index][BUTTON].val, ButtonData[ArrayIndex][WIN_BUTS][index][BUT_MAX], ButtonData[ArrayIndex][WIN_BUTS][index][BUT_TIP])
					else:
						ButtonData[ArrayIndex][WIN_BUTS][index][BUTTON] = String(ButtonData[ArrayIndex][WIN_BUTS][index][BUT_TITLE], ButtonData[ArrayIndex][WIN_EVENT]+index, ButX, PosInc, ButWidth, ButtonHeight, ButtonData[ArrayIndex][WIN_BUTS][index][BUTTON].val, ButtonData[ArrayIndex][WIN_BUTS][index][BUT_MAX], ButtonData[ArrayIndex][WIN_BUTS][index][BUT_TIP])
				elif (ButtonData[ArrayIndex][WIN_BUTS][index][BUT_TYPE] == 5): #If this is supposed to be a line...
					glColor3f(TabColor[0]/256.0*ButtonData[ArrayIndex][WIN_COLOR][0], TabColor[1]/256.0*ButtonData[ArrayIndex][WIN_COLOR][1], TabColor[2]/256.0*ButtonData[ArrayIndex][WIN_COLOR][2])
					endGap		= 5
					glLineWidth(1)
					glBegin(GL_LINES)
					glVertex2i(x+endGap, PosInc+ButtonHeight/2)
					glVertex2i(x+width-endGap, PosInc+ButtonHeight/2)
					glEnd()
		
		#Draw BackGround Bottom
		glEnable(GL_BLEND)
		glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
		glColor4f(BackColor[0]/256.0*ButtonData[ArrayIndex][WIN_COLOR][0], BackColor[1]/256.0*ButtonData[ArrayIndex][WIN_COLOR][1], BackColor[2]/256.0*ButtonData[ArrayIndex][WIN_COLOR][2], BackColor[3]/256.0*ButtonData[ArrayIndex][WIN_COLOR][3])
		glRecti(x, PosInc, x+width, PosInc-WindowGap)
		glDisable(GL_BLEND)
		
		PosInc = PosInc-WindowGap
	
	glColor3f(TextColor[0]/256.0, TextColor[1]/256.0, TextColor[2]/256.0)
								
	#Draw Arrow (rotate 90deg according to collapse boolean state)
	glPushMatrix()
	glTranslated(x+ButtonGap*4, y-TitleHeight/2-1, 0)
	glRotated(-90*ButtonData[ArrayIndex][WIN_COLLAPSE], 0, 0, -1)
	glBegin(GL_POLYGON)
	glVertex2i(0, -ArrowSize)
	glVertex2i(-ArrowSize, ArrowSize)
	glVertex2i(ArrowSize, ArrowSize)
	glEnd()
	glPopMatrix()
	
	#Draw Tab Text
	glRasterPos2d(x+WindowGap*6, y-TextOffset)
	Text(ButtonData[ArrayIndex][WIN_TITLE], 'small')
	return y-PosInc							#Return the final height of sub-window


#### Main drawing routine
def draw():
	global EVENT_NONE, RenderDir, RenderBin, ScrollPos, ScrollState, ButtonData, LastScene, LastObject
	
	#Make sure current scene is updated if changed
	CurrentScene = Blender.Scene.GetCurrent()
	if (CurrentScene and CurrentScene != LastScene):
		ButtonData[SCENES][WIN_BUTS][SCENE_SELECT][BUT_MENU] = CreateMenu(ButtonData[SCENES][WIN_BUTS][SCENE_SELECT][BUT_PROP], "", 1, [], "") #Create a new menu array from current scene
		ButtonData[SCENES][WIN_BUTS][SCENE_SELECT][BUTTON].val = ButtonData[SCENES][WIN_BUTS][SCENE_SELECT][BUT_MENU].index(CurrentScene.name) #Pass index number of current scene to button
		UpdateMenuData(SCENES)
		if (LastScene): SetProperties(SCENES, CurrentScene)		#Make sure properties are set
		LastScene = CurrentScene				#Update last selection
	
	#Make sure current active object is updated if changed
	ActiveObject = Blender.Object.GetSelected()
	if (ActiveObject and ActiveObject != LastObject):
		TypeIndex = 0
		ObjectType = ActiveObject[0].getType()			#Get object type
		if (ObjectType == "Mesh" or ObjectType == "Curve" or ObjectType == "Surf"): SubIndex = GEOMETRY; TypeIndex = 4
		elif (ObjectType == "Lamp"): SubIndex = LIGHTS; TypeIndex = 5
		elif (ObjectType == "Camera"): SubIndex = CAMERAS; TypeIndex = 2
		if (TypeIndex != 0):
			ButtonData[SubIndex][WIN_BUTS][0][BUT_MENU] = CreateMenu(ButtonData[SubIndex][WIN_BUTS][0][BUT_PROP], "", TypeIndex, [], "") #Create a new menu array from current selection
			ButtonData[SubIndex][WIN_BUTS][0][BUTTON].val = ButtonData[SubIndex][WIN_BUTS][0][BUT_MENU].index(ActiveObject[0].name) #Pass index number of current proper button
			UpdateMenuData(SubIndex)
			if (LastObject): SetProperties(SubIndex, ActiveObject[0]) #Make sure properties are set
		LastObject = ActiveObject				#Update last selection
	
	#Local variables
	TitleColor		= Theme.Get()[0].get('BUTS').header	#Color of menu title
	BackColor		= Theme.Get()[0].get('BUTS').back	#Color of menu background
	TextColor		= Theme.Get()[0].get('ui').menu_text	#Color of menu text
	ScrollState		= 0
	AreaDims		= GetAreaSize()				#Get AreaSize for widget placement
	SubPosYInc		= AreaDims[1]+ScrollPos			#Increment by ScrollPos	
	TitleHeight		= 28					#Height of top title bar
	WindowGap		= 6					#Distance between and around sub-windows
	SubPosXInc		= WindowGap
	SubPosYStart		= SubPosYInc-TitleHeight-WindowGap
	SubMinimum		= 300
	if (AreaDims[0] < SubMinimum): SubWidth = AreaDims[0]
	else: SubWidth = AreaDims[0]/int(AreaDims[0]/SubMinimum)
	
	#Clear background
	glClearColor(BackColor[0]/256.0, BackColor[1]/256.0, BackColor[2]/256.0, 1.0)
	glClear(GL_COLOR_BUFFER_BIT)
	
	#Draw Title
	glColor3f(TitleColor[0]/256.0, TitleColor[1]/256.0, TitleColor[2]/256.0)
	glRecti(0, SubPosYInc, AreaDims[0], SubPosYInc-TitleHeight)
	glColor3f(TextColor[0]/256.0, TextColor[1]/256.0, TextColor[2]/256.0)
	glRasterPos2d(10, SubPosYInc-TitleHeight/2-4)
	Text("MOSAIC "+__version__+" RenderMan(R) System")
	SubPosYInc = SubPosYStart
	
	#Draw Subwindows from ButtonData array
	for index, item in enumerate(ButtonData):			#Cycle through all subwindows in ButtonData array
		SubPosYInc = SubPosYInc - SubFrame(SubPosXInc, SubPosYInc, SubWidth-WindowGap*2, index) - WindowGap	#Draw SubWindow
		if (SubPosYInc-ScrollPos-TitleHeight < 0):
			if (ScrollState > SubPosYInc):			#Stop scrolling at last subwindow
				ScrollState = SubPosYInc
			if (SubPosXInc+SubWidth <= AreaDims[0]):	#If area wide stack subwindows from left to right otherwise top down
				SubPosYInc = SubPosYStart
				SubPosXInc = SubPosXInc+SubWidth
	
	#Show scroll down message at bottom if menu is past available area
	if (ScrollState < 0 and ScrollPos == 0 ):
		Toggle("use mouse wheel or arrows to scroll", EVENT_NONE, -5, 0, AreaDims[0]+10, 18, 0)


#### Standard event handler
def event(evt, val):
	global MousePos, ScrollPos, ScrollState, ButtonData, LastObject, LastScene
	ScrollInc = 15
	
	#Manage GUI events
	if (evt == WHEELDOWNMOUSE):					#Scroll area down
		if (ScrollState < 0):
			ScrollPos = ScrollPos+ScrollInc
		Draw()
	elif (evt == WHEELUPMOUSE):					#Scroll area up
		if (ScrollPos > 0):
			ScrollPos = ScrollPos-ScrollInc
		else: ScrollPos = 0
		Draw()
	if (evt == DOWNARROWKEY):					#Scroll area down
		if (ScrollState < 0):
			ScrollPos = ScrollPos+ScrollInc
		Draw()
	elif (evt == UPARROWKEY):					#Scroll area up
		if (ScrollPos > 0):
			ScrollPos = ScrollPos-ScrollInc
		else: ScrollPos = 0
		Draw()
	elif (evt == LEFTMOUSE and val):				#Calculate mouse position in this area
		areaVert =  [item['vertices'] for item in GetScreenInfo() if item['id'] == GetAreaID()]
		MouseCor = GetMouseCoords()
		MousePos[0] = MouseCor[0]-areaVert[0][0]
		MousePos[1] = MouseCor[1]-areaVert[0][1]
		Draw()
	elif (evt == LEFTMOUSE and not val):				#If button up then clear mouse position
		MousePos[0] = 0
		MousePos[1] = 0
	elif (evt == RIGHTMOUSE and val):				#Collapse or expand all subWindows based on popmenu choice
		result = PupMenu("Render Scene|Render Anim|Expand all|Collapse all|Exit",27)
		if (result == 1):
			RenderFrame()
		if (result == 2):
			RenderAnimation()
		if (result == 3):
			for index, item in enumerate(ButtonData):
				ButtonData[index][WIN_COLLAPSE] = False
			ScrollPos = 0
		if (result == 4):
			for index, item in enumerate(ButtonData):
				ButtonData[index][WIN_COLLAPSE] = True
			ScrollPos = 0
		if (result == 5):
			Shutdown()
		Draw()
	elif (evt == HKEY and not val):
		ShowHelp()
	elif (evt == RKEY and not val):
		RenderFrame()
	elif (evt == PKEY and not val):
		RenderPreview()
	elif (evt == MOUSEX or evt == MOUSEY):				#Update area if mouse is over it and scene or active object has changed
		MousePos[0] = 0						#Set mouse position to zero to prevent LEFTMOUSE tab collapse flashing while moving
		MousePos[1] = 0
		CurrentScene = Blender.Scene.GetCurrent()
		CurrentObject = Blender.Object.GetSelected()
		if ((LastScene != CurrentScene and CurrentScene) or (LastObject != CurrentObject and CurrentObject)):
			Draw()
	elif (evt == QKEY and not val):
		Shutdown()
	elif (evt == ESCKEY and not val):
		Shutdown()


#### Button event handler
def buttonevent(evt):
	global EVENT_WIDTH, EVENT_NONE, EVENT_ACTIONS_SET, EVENT_SETTINGS_SET, EVENT_UTILITY_SET, EVENT_SCENE_SET, EVENT_CAMERA_SET, EVENT_GROUP_SET, EVENT_GEOM_SET, EVENT_LIGHT_SET, EVENT_MAT_SET
	global ButtonData, DialogData, Filters, RenderBin, CompilerBin, RenderDir, TexmakeBin, InfoBin
	
	#Manage button events as sets of sub-windows with event numbers beginning at windows event set and count up by button order in ButtonArray
	if (evt >= EVENT_ACTIONS_SET and evt < EVENT_ACTIONS_SET+EVENT_WIDTH):
		if (evt == EVENT_ACTIONS_SET+ACT_RENDER): RenderFrame()
		elif (evt == EVENT_ACTIONS_SET+ACT_ANIMATION): RenderAnimation()
		elif (evt == EVENT_ACTIONS_SET+ACT_PREVIEW): RenderPreview()
		elif (evt == EVENT_ACTIONS_SET+ACT_RENDER_RIB): ButtonData[ACTIONS][WIN_BUTS][ACT_RENDER_RIB][BUT_DEFAULT] = ButtonData[ACTIONS][WIN_BUTS][ACT_RENDER_RIB][BUTTON].val
		elif (evt == EVENT_ACTIONS_SET+ACT_CREATE_RIB): ButtonData[ACTIONS][WIN_BUTS][ACT_CREATE_RIB][BUT_DEFAULT] = ButtonData[ACTIONS][WIN_BUTS][ACT_CREATE_RIB][BUTTON].val
		elif (evt == EVENT_ACTIONS_SET+ACT_CREATE_SEL): ButtonData[ACTIONS][WIN_BUTS][ACT_CREATE_SEL][BUT_DEFAULT] = ButtonData[ACTIONS][WIN_BUTS][ACT_CREATE_SEL][BUTTON].val
		elif (evt == EVENT_ACTIONS_SET+ACT_COMPILE_SL): ButtonData[ACTIONS][WIN_BUTS][ACT_COMPILE_SL][BUT_DEFAULT] = ButtonData[ACTIONS][WIN_BUTS][ACT_COMPILE_SL][BUTTON].val
		elif (evt == EVENT_ACTIONS_SET+ACT_EXPORT_MAPS): ButtonData[ACTIONS][WIN_BUTS][ACT_EXPORT_MAPS][BUT_DEFAULT] = ButtonData[ACTIONS][WIN_BUTS][ACT_EXPORT_MAPS][BUTTON].val
		elif (evt == EVENT_ACTIONS_SET+ACT_HELP): ShowHelp()
		elif (evt == EVENT_ACTIONS_SET+ACT_QUIT): Shutdown()
		Redraw(1)
	if (evt >= EVENT_SETTINGS_SET and evt < EVENT_SETTINGS_SET+EVENT_WIDTH):
		if (evt == EVENT_SETTINGS_SET+SET_OUTPUT_DIR): FileSelector(RenderDirCallback, "Select Directory", " ")
		elif (evt == EVENT_SETTINGS_SET+SET_RENDER_BIN):
			result = Blender.Draw.PupBlock("Renderer and Options", DialogData[2])
			if (result > 0):
				RenderBin = DialogData[2][0][1].val
				ButtonData[SETTINGS][WIN_BUTS][SET_RENDER_BIN][BUT_TIP] = "Renderer: "+RenderBin
				UpdateRegistry()
		elif (evt == EVENT_SETTINGS_SET+SET_SHADER_BIN):
			result = Blender.Draw.PupBlock("Shader Compiler and Options", DialogData[3])
			if (result > 0):
				CompilerBin = DialogData[3][0][1].val
				ButtonData[SETTINGS][WIN_BUTS][SET_SHADER_BIN][BUT_TIP] = "Compiler: "+CompilerBin
				UpdateRegistry()
		elif (evt == EVENT_SETTINGS_SET+SET_TEXMAKE_BIN):
			result = Blender.Draw.PupBlock("Tex Optimizer and Options", DialogData[4])
			if (result > 0):
				TexmakeBin = DialogData[4][0][1].val
				ButtonData[SETTINGS][WIN_BUTS][SET_TEXMAKE_BIN][BUT_TIP] = "Leave blank to disable: "+TexmakeBin
				UpdateRegistry()
		elif (evt == EVENT_SETTINGS_SET+SET_INFO_BIN):
			result = Blender.Draw.PupBlock("Shader Info and Options", DialogData[5])
			if (result > 0):
				InfoBin = DialogData[5][0][1].val
				ButtonData[SETTINGS][WIN_BUTS][SET_INFO_BIN][BUT_TIP] = "Shader Info: "+InfoBin
				UpdateRegistry()
		elif (evt == EVENT_SETTINGS_SET+SET_TEXT_FILTER):
			result = Blender.Draw.PupBlock("Text Name Filters", DialogData[0])
			if (result > 0):
				for index, item in enumerate(Filters):
					Filters[index]	= DialogData[0][index][1].val
				UpdateRegistry()
		Redraw(1)
	if (evt >= EVENT_UTILITY_SET and evt < EVENT_UTILITY_SET+EVENT_WIDTH):
		if (evt == EVENT_UTILITY_SET+UTIL_LIBRARY_FRAG):
			result = Blender.Draw.PupBlock("Type shaders name", DialogData[6])
			if (result > 0):
				ShaderUtility(DialogData[6][0][1].val, False)
				DialogData[6][0][1].val = ""
		if (evt == EVENT_UTILITY_SET+UTIL_SOURCE_FRAG):
			menu = CreateMenu("Select Shader Source", Filters[1], 0)
			result = PupMenu(menu[0],27)
			if (result > -1):
				ShaderUtility(menu[result])
		elif (evt == EVENT_UTILITY_SET+UTIL_CLEAN_DIR):
			if (RenderDir):
				try:
					print "Cleaning output directory..."
					DelTree(GetProjectFolder(), True)
					doneText = "Output directory clean"
					print doneText
					PupMenu(doneText)
				except:
					ErrorPopup("Some files or folders are locked, quit any programs using the project folder and try again!")
			else: ErrorPopup("Output directory is not set, please set ouput directory under settings!")
		elif (evt == EVENT_UTILITY_SET+UTIL_COPY_PROP):
			try:
				selections = Blender.Object.GetSelected() #Get all current selections
				if (len(selections) > 1):
					for object in selections[1:]: #Cycle through selections skipping the active selection and only modifing objects with the same type as active object
						if (object.getType() == selections[0].getType()):
							for key in selections[0].properties: #Copy properties from active object to other objects
								object.properties[key] = selections[0].properties[key]
					PupMenu("Properties copied")
				else: ErrorPopup("Must have more than one object selected!")
			except: ErrorPopup("Could not copy active objects properties to other selections!")
		elif (evt == EVENT_UTILITY_SET+UTIL_CLEAR_PROP):
			try:
				for object in Blender.Object.GetSelected(): #Cycle through selections and clear properties of each
					for key in object.properties:
						del object.properties[key]
				PupMenu("Properties cleared")
			except: ErrorPopup("Could not clear all objects properties!")
		Redraw(1)
	if (evt >= EVENT_PROJECT_SET and evt < EVENT_PROJECT_SET+EVENT_WIDTH):
		if (evt == EVENT_PROJECT_SET+PROJECT_FOLDER):
			projectFolder = ButtonData[PROJECT][WIN_BUTS][PROJECT_FOLDER][BUTTON].val
			if (projectFolder): Blender.Scene.Get()[0].properties[ButtonData[PROJECT][WIN_BUTS][PROJECT_FOLDER][BUT_PROP]] = projectFolder
			else: Blender.Scene.Get()[0].properties[ButtonData[PROJECT][WIN_BUTS][PROJECT_FOLDER][BUT_PROP]] = ButtonData[PROJECT][WIN_BUTS][PROJECT_FOLDER][BUT_DEFAULT]
		elif (evt == EVENT_PROJECT_SET+PROJECT_ARCHIVES):
			archives = ButtonData[PROJECT][WIN_BUTS][PROJECT_ARCHIVES][BUTTON].val
			if (archives): Blender.Scene.Get()[0].properties[ButtonData[PROJECT][WIN_BUTS][PROJECT_ARCHIVES][BUT_PROP]] = archives
			else: Blender.Scene.Get()[0].properties[ButtonData[PROJECT][WIN_BUTS][PROJECT_ARCHIVES][BUT_PROP]] = ButtonData[PROJECT][WIN_BUTS][PROJECT_ARCHIVES][BUT_DEFAULT]
		elif (evt == EVENT_PROJECT_SET+PROJECT_SHADERS):
			shaders = ButtonData[PROJECT][WIN_BUTS][PROJECT_SHADERS][BUTTON].val
			if (shaders): Blender.Scene.Get()[0].properties[ButtonData[PROJECT][WIN_BUTS][PROJECT_SHADERS][BUT_PROP]] = shaders
			else: Blender.Scene.Get()[0].properties[ButtonData[PROJECT][WIN_BUTS][PROJECT_SHADERS][BUT_PROP]] = ButtonData[PROJECT][WIN_BUTS][PROJECT_SHADERS][BUT_DEFAULT]
		elif (evt == EVENT_PROJECT_SET+PROJECT_TEXTURES):
			textures = ButtonData[PROJECT][WIN_BUTS][PROJECT_TEXTURES][BUTTON].val
			if (textures): Blender.Scene.Get()[0].properties[ButtonData[PROJECT][WIN_BUTS][PROJECT_TEXTURES][BUT_PROP]] = textures
			else: Blender.Scene.Get()[0].properties[ButtonData[PROJECT][WIN_BUTS][PROJECT_TEXTURES][BUT_PROP]] = ButtonData[PROJECT][WIN_BUTS][PROJECT_TEXTURES][BUT_DEFAULT]
		elif (evt == EVENT_PROJECT_SET+PROJECT_DISPLAYS):
			displays = ButtonData[PROJECT][WIN_BUTS][PROJECT_DISPLAYS][BUTTON].val
			if (displays): Blender.Scene.Get()[0].properties[ButtonData[PROJECT][WIN_BUTS][PROJECT_DISPLAYS][BUT_PROP]] = displays
			else: Blender.Scene.Get()[0].properties[ButtonData[PROJECT][WIN_BUTS][PROJECT_DISPLAYS][BUT_PROP]] = ButtonData[PROJECT][WIN_BUTS][PROJECT_DISPLAYS][BUT_DEFAULT]
		elif (evt == EVENT_PROJECT_SET+PROJECT_PROCEDURALS):
			procedurals = ButtonData[PROJECT][WIN_BUTS][PROJECT_PROCEDURALS][BUTTON].val
			if (procedurals): Blender.Scene.Get()[0].properties[ButtonData[PROJECT][WIN_BUTS][PROJECT_PROCEDURALS][BUT_PROP]] = procedurals
			else: Blender.Scene.Get()[0].properties[ButtonData[PROJECT][WIN_BUTS][PROJECT_PROCEDURALS][BUT_PROP]] = ButtonData[PROJECT][WIN_BUTS][PROJECT_PROCEDURALS][BUT_DEFAULT]
		elif (evt == EVENT_PROJECT_SET+PROJECT_RESOURCES):
			resources = ButtonData[PROJECT][WIN_BUTS][PROJECT_RESOURCES][BUTTON].val
			if (resources): Blender.Scene.Get()[0].properties[ButtonData[PROJECT][WIN_BUTS][PROJECT_RESOURCES][BUT_PROP]] = resources
			else: Blender.Scene.Get()[0].properties[ButtonData[PROJECT][WIN_BUTS][PROJECT_RESOURCES][BUT_PROP]] = ButtonData[PROJECT][WIN_BUTS][PROJECT_RESOURCES][BUT_DEFAULT]
		elif (evt == EVENT_PROJECT_SET+PROJECT_PASSES): Blender.Scene.Get()[0].properties[ButtonData[PROJECT][WIN_BUTS][PROJECT_PASSES][BUT_PROP]] = ButtonData[PROJECT][WIN_BUTS][PROJECT_PASSES][BUTTON].val
		Redraw(1)
	if (evt >= EVENT_SCENE_SET and evt < EVENT_SCENE_SET+EVENT_WIDTH):
		try:
			SelectedScene = Blender.Scene.Get(ButtonData[SCENES][WIN_BUTS][SCENE_SELECT][BUT_MENU][ButtonData[SCENES][WIN_BUTS][SCENE_SELECT][BUTTON].val])
			if (evt == EVENT_SCENE_SET+SCENE_SELECT):
				SelectedScene.makeCurrent()
				UpdateMenuData(SCENES)
			elif (evt == EVENT_SCENE_SET+SCENE_DEFAULT): SetDefaults(SCENES)
			SetProperties(SCENES, SelectedScene)
			if (evt == EVENT_SCENE_SET+SCENE_DISPLAY_CODE):
				display = ButtonData[SCENES][WIN_BUTS][SCENE_DISPLAY_CODE][BUTTON].val
				if (display): SelectedScene.properties[ButtonData[SCENES][WIN_BUTS][SCENE_DISPLAY_CODE][BUT_PROP]] = display
				else: SelectedScene.properties[ButtonData[SCENES][WIN_BUTS][SCENE_DISPLAY_CODE][BUT_PROP]] = ButtonData[SCENES][WIN_BUTS][SCENE_DISPLAY_CODE][BUT_DEFAULT]
			elif (evt == EVENT_SCENE_SET+SCENE_FRAMEBUF_CODE):
				framebuffer = ButtonData[SCENES][WIN_BUTS][SCENE_FRAMEBUF_CODE][BUTTON].val
				if (framebuffer): SelectedScene.properties[ButtonData[SCENES][WIN_BUTS][SCENE_FRAMEBUF_CODE][BUT_PROP]] = framebuffer
				else: SelectedScene.properties[ButtonData[SCENES][WIN_BUTS][SCENE_FRAMEBUF_CODE][BUT_PROP]] = ButtonData[SCENES][WIN_BUTS][SCENE_FRAMEBUF_CODE][BUT_DEFAULT]
		except: ButtonData[SCENES][WIN_BUTS][SCENE_SELECT][BUTTON].val = ButtonData[SCENES][WIN_BUTS][SCENE_SELECT][BUT_DEFAULT]
		Redraw(1)
	if (evt >= EVENT_CAMERA_SET and evt < EVENT_CAMERA_SET+EVENT_WIDTH):
		try:
			object = Blender.Object.Get(ButtonData[CAMERAS][WIN_BUTS][CAM_SELECT][BUT_MENU][ButtonData[CAMERAS][WIN_BUTS][CAM_SELECT][BUTTON].val])
			if (evt == EVENT_CAMERA_SET+CAM_SELECT):
				SelectObject(object.name)
				UpdateMenuData(CAMERAS)
			elif (evt == EVENT_CAMERA_SET+CAM_DEFAULT): SetDefaults(CAMERAS)
			SetProperties(CAMERAS, object)
		except: ButtonData[CAMERAS][WIN_BUTS][CAM_SELECT][BUTTON].val = ButtonData[CAMERAS][WIN_BUTS][CAM_SELECT][BUT_DEFAULT]
		Redraw(1)
	if (evt >= EVENT_GROUP_SET and evt < EVENT_GROUP_SET+EVENT_WIDTH):
		try:
			if (evt == EVENT_GROUP_SET+GRP_SELECT): UpdateMenuData(GROUPS)
			elif (evt == EVENT_GROUP_SET+GRP_DEFAULT): SetDefaults(GROUPS)
			SelectedScene = Blender.Scene.GetCurrent()
			SelectedScene.properties[ButtonData[GROUPS][WIN_BUTS][GRP_SELECT][BUT_MENU][ButtonData[GROUPS][WIN_BUTS][GRP_SELECT][BUTTON].val]] = {"Group Begin Code": ButtonData[GROUPS][WIN_BUTS][GRP_BEGIN_CODE][BUT_MENU][ButtonData[GROUPS][WIN_BUTS][GRP_BEGIN_CODE][BUTTON].val],
																			      "Group End Code": ButtonData[GROUPS][WIN_BUTS][GRP_END_CODE][BUT_MENU][ButtonData[GROUPS][WIN_BUTS][GRP_END_CODE][BUTTON].val],
																			      "Atmosphere Shader": ButtonData[GROUPS][WIN_BUTS][GRP_ATMO][BUT_MENU][ButtonData[GROUPS][WIN_BUTS][GRP_ATMO][BUTTON].val],
																			      "Group Block": ButtonData[GROUPS][WIN_BUTS][GRP_ARCH][BUT_MENU][ButtonData[GROUPS][WIN_BUTS][GRP_ARCH][BUTTON].val]}
		except: ButtonData[GROUPS][WIN_BUTS][GRP_SELECT][BUTTON].val = ButtonData[GROUPS][WIN_BUTS][GRP_SELECT][BUT_DEFAULT]
		Redraw(1)
	if (evt >= EVENT_GEOM_SET and evt < EVENT_GEOM_SET+EVENT_WIDTH):
		try:
			object = Blender.Object.Get(ButtonData[GEOMETRY][WIN_BUTS][GEO_SELECT][BUT_MENU][ButtonData[GEOMETRY][WIN_BUTS][GEO_SELECT][BUTTON].val])
			if (evt == EVENT_GEOM_SET+GEO_SELECT):
				SelectObject(object.name)
				UpdateMenuData(GEOMETRY)
			elif (evt == EVENT_GEOM_SET+GEO_DEFAULT): SetDefaults(GEOMETRY)
			SetProperties(GEOMETRY, object)
		except: ButtonData[GEOMETRY][WIN_BUTS][GEO_SELECT][BUTTON].val = ButtonData[GEOMETRY][WIN_BUTS][GEO_SELECT][BUT_DEFAULT]
		Redraw(1)
	if (evt >= EVENT_LIGHT_SET and evt < EVENT_LIGHT_SET+EVENT_WIDTH):
		try:
			object = Blender.Object.Get(ButtonData[LIGHTS][WIN_BUTS][LIGHT_SELECT][BUT_MENU][ButtonData[LIGHTS][WIN_BUTS][LIGHT_SELECT][BUTTON].val])
			if (evt == EVENT_LIGHT_SET+LIGHT_SELECT):
				SelectObject(object.name)
				UpdateMenuData(LIGHTS)
			elif (evt == EVENT_LIGHT_SET+LIGHT_DEFAULT): SetDefaults(LIGHTS)
			SetProperties(LIGHTS, object)
		except: ButtonData[LIGHTS][WIN_BUTS][LIGHT_SELECT][BUTTON].val = ButtonData[LIGHTS][WIN_BUTS][LIGHT_SELECT][BUT_DEFAULT]
		Redraw(1)
	if (evt >= EVENT_MAT_SET and evt < EVENT_MAT_SET+EVENT_WIDTH):
		try:
			SelectedMaterial = Blender.Material.Get(ButtonData[MATERIALS][WIN_BUTS][MAT_SELECT][BUT_MENU][ButtonData[MATERIALS][WIN_BUTS][MAT_SELECT][BUTTON].val])
			if (evt == EVENT_MAT_SET+MAT_SELECT): UpdateMenuData(MATERIALS)
			elif (evt == EVENT_MAT_SET+MAT_DEFAULT): SetDefaults(MATERIALS)
			SetProperties(MATERIALS, SelectedMaterial)
		except: ButtonData[MATERIALS][WIN_BUTS][MAT_SELECT][BUTTON].val = ButtonData[MATERIALS][WIN_BUTS][MAT_SELECT][BUT_DEFAULT]
		Redraw(1)


####################################################################### LETS DO IT!
Register(draw, event, buttonevent)