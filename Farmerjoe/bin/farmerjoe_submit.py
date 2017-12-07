#!BPY

"""
Name: 'Farmerjoe Submit Render'
Blender: 242
Group: 'Render'
Tooltip: 'Submit render to Farmer joe the render farmer'
"""

__author__ = "Mitch Hughes (lobo_nz)"
__url__ = ("blender", "Author's homepage, http://blender.formworks.co.nz")
_v_ersion__ = "0.1.3 Alpha"

__bpydoc__ = """\
This script submits the current blend file to a Farmerjoe render server.

Usage:
    
Add the script to your blender/scripts directory
Execute this script from the "Scripts->Render" menu and choose "Farmerjoe Submit",
click "Submit" to send the job.
"""

# $Id: farmerjoe_submit.py,v 2006/08/29 10:27:10$
#
# --------------------------------------------------------------------------
# Farmerjoe by Mitch Hughes (AKA lobo_nz)
# --------------------------------------------------------------------------
# ***** BEGIN GPL LICENSE BLOCK *****
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
# ***** END GPL LICENCE BLOCK *****
# --------------------------------------------------------------------------

import sys

platform = sys.platform

import Blender
from Blender import *
import string
import os
import time


################### Get some variables ##############
sc=Scene.GetCurrent()
context = sc.getRenderingContext()

#variables
v_ = {
'blend_filename'   :Blender.sys.basename(Blender.Get('filename')),
'sep'              :Blender.sys.sep,
'os'               :'linux',
'startFrame'       :context.startFrame(),
'endFrame'         :context.endFrame(),
'totalframes'      :context.endFrame() - context.startFrame() + 1,
'render_type'      :'frames',
'image_x'          :context.imageSizeX(),
'image_y'          :context.imageSizeY(),
'origRenderPath'   :context.getRenderPath(),
'origFileType'     :context.imageType,
'extensions'       :{ 'Targa':'.tga', 'Jpeg':'.jpg', 'PNG':'.png', 'BMP':'.bmp' },
'filetypes'        :( 'Targa', 'Jpeg', 'PNG', 'BMP' ),
'filetype_const'   :{ 'Targa':Scene.Render.TARGA, 'Jpeg':Scene.Render.JPEG, 'PNG':Scene.Render.PNG, 'BMP':Scene.Render.BMP },
'linux_farmerjoe'  :'Farmerjoe.linux',
'windows_farmerjoe'  :'Farmerjoe.exe',
'osx_farmerjoe'  :'Farmerjoe.osx'
}
#controls
c_ = {
'fj_root'     :Draw.Create("/render"),
'fj_jobs'     :Draw.Create("jobs"),
'fj_name'     :Draw.Create(v_['blend_filename']),
'fj_xparts'   :Draw.Create(1),
'fj_yparts'   :Draw.Create(1),
'copydirs'    :Draw.Create('textures,fluidsimdata'),
'filetype'    :Draw.Create(2),
'rgb'         :Draw.Create(1),
'rgba'        :Draw.Create(0),
'step'        :Draw.Create(0),
'timeout'     :Draw.Create(200),
'submitRender':Draw.Create(0),
'status'      :Draw.Create("Message:")
     }
#events
e_ = { 'noevent'      :1,
       'submitRender' :2,
       'rgb'          :3,
       'rgba'         :4,
       'exit'         :5,
       'choose_dir'   :6,
       'setFiletype'  :7,
       'save_root'    :8
     }

if platform == 'win32':
    c_['fj_root'].val = 'r:'
    v_['os'] = 'MSWin32'
elif platform == 'darwin':
    c_['fj_root'].val = '/render'
    v_['os'] = 'OSX'
    
#else we go with linux :) and the original variables


if v_['totalframes'] > 1:
    v_['render_type'] = 'frames'
else:
    v_['render_type'] = 'bucket'
    
context.enableRGBColor()
context.setImageType(Scene.Render.JPEG)

####### Get the user preference for Farmer joe Root #######

def update_registry():
    d = {'FARMERJOE_ROOT': c_['fj_root'].val  }
    Registry.SetKey('farmerjoe_submit', d, True)

regdict = Registry.GetKey('farmerjoe_submit', True)

if regdict:
    try:
        c_['fj_root'].val = regdict['FARMERJOE_ROOT']
    except: update_registry()
else:
  update_registry()

############################################################

def sys_copy(src,dest):
    global c_,e_,v_
    
    if v_['os'] == 'linux' and (os.path.isdir(src) or os.path.isfile(src)):
        if os.path.isdir(src):
            os.system('cp -R "' + src + '" "' + dest + '"')
        elif os.path.isfile(src):
            os.system('cp "' + src + '" "' + dest + '"')
    elif v_['os'] == 'MSWin32':
        if os.path.isdir(src):
            os.system('xcopy /k "' + src + '" "' + dest + '" /e /i')
        elif os.path.isfile(src):
            os.system('copy "' + src + '" "' + dest + '"')
    elif v_['os'] == 'OSX' and (os.path.isdir(src) or os.path.isfile(src)):
        if os.path.isdir(src):
            os.system('cp -R "' + src + '" "' + dest + '"')
        elif os.path.isfile(src):
            os.system('cp "' + src + '" "' + dest + '"')

def submit():
    global c_,e_,v_
    #set render path to frames dir relative to file
    context.setRenderPath('//frames/')
    
    # Make new dir for this job using a timestamp
    t = time.localtime()
    timestamp = "%s-%s-%s_%s-%s-%s" %(t[0],t[1],t[2],t[3],t[4],t[4])
    
    render_dir_name = c_['fj_name'].val + '.' + timestamp
    render_dir = c_['fj_root'].val + v_['sep'] + c_['fj_jobs'].val + v_['sep'] + render_dir_name
    frames_dir = render_dir + v_['sep'] + 'frames'
    
    jobfilename = v_['blend_filename'] + '.job'
    job_path = render_dir + v_['sep'] + jobfilename
    
    #########################################
    ## MAKE THE DIRECTORIES TO STORE THE JOB
    #########################################
    print 'Making ' + str(render_dir)
    os.system('mkdir "' + render_dir +'"')
    print 'Making ' + str(frames_dir)
    os.system('mkdir "' + frames_dir +'"')
    
    #########################################
    ## Save the blend 
    ######################################### 
    Blender.Save(Blender.Get('filename'),1)
    
    #########################################
    ## Write the job file
    ######################################### 
    
    #filename     # vr.blend
    #startframe   # 1
    #endframe     # 360
    #step         # 5
    #timeout      # 180
    #jobdir       # jobdir
    #jobname      # name
    #image_x      # 800
    #image_y      # 600
    #xparts       # 4
    #yparts       # 4
    
    data = v_['blend_filename'] + '\n'\
     + str(v_['startFrame']) + '\n' \
     + str(v_['endFrame']) + '\n' \
     + str(c_['step'].val) + '\n' \
     + str(c_['timeout'].val*60) + '\n'\
     + render_dir_name + '\n'\
     + str(c_['fj_name'].val) + '\n'\
     + str(v_['image_x']) + '\n'\
     + str(v_['image_y']) + '\n'\
     + str(c_['fj_xparts'].val) + '\n'\
     + str(c_['fj_yparts'].val)
     
    #########################################
    ## Copy the blend file and extra directories
    #########################################
    sys_copy(Blender.Get('filename'),render_dir + v_['sep'] + v_['blend_filename'])
    extra_dirs = c_['copydirs'].val.split(',') # split on comma
    for directory in extra_dirs:
        sys_copy(Blender.sys.dirname(Blender.Get('filename')) + v_['sep'] + directory,render_dir + v_['sep'] + directory)

    jobfile = file(job_path,"w")
    jobfile.write(data)
    jobfile.close()
    print data
    
    if v_['os'] == 'linux':
        submit_cmd = c_['fj_root'].val + v_['sep'] + v_['linux_farmerjoe'] + ' --submit "%s" "%s"'%(render_dir_name,jobfilename)
    elif v_['os'] == 'MSWin32':
        submit_cmd = c_['fj_root'].val + v_['sep'] + v_['windows_farmerjoe'] + ' --submit "%s" "%s"'%(render_dir_name,jobfilename)
    elif v_['os'] == 'OSX':
	    submit_cmd = c_['fj_root'].val + v_['sep'] + v_['osx_farmerjoe'] + ' --submit "%s" "%s"'%(render_dir_name,jobfilename)
		
    print submit_cmd
    result = os.system(submit_cmd)
    if result != 0:
        print "Submit Failed for: " + c_['fj_name'].val
        submit_status = "FAILED"
    else:
        print "Submit Suceeded for: " + c_['fj_name'].val
        submit_status = "OK"
    #set render path back to normal
    context.setRenderPath(v_['origRenderPath'])
    context.setImageType(v_['origFileType'])
    
    result = Draw.PupMenu("Submit Status for: " + c_['fj_name'].val + "%t|"+submit_status)
    bevent(e_['exit'])

def menuNameFromList(menu_title, menu_entries):
    menu_name = menu_title + " %t"
    counter = 0
    for entry in menu_entries:
        counter = counter + 1
        menu_name = menu_name +"|"+ entry +" %x"+ str(counter)
    return menu_name

def DRAWY(val):
	global g_drawy
	if val >= 0:
		g_drawy=g_drawy-val
		return g_drawy
	else:
		g_drawy = val*-1
		return g_drawy
		
        
def gui():
    global c_,e_,v_
    
    DRAWY(-450)
    width = 260
    
    BGL.glClearColor(0.6, 0.6, 0.6, 0.0)
    BGL.glClear(Blender.BGL.GL_COLOR_BUFFER_BIT)
    
    title = "Farmerjoe Submit "+_v_ersion__
    size = Draw.GetStringWidth(title,"large")
    BGL.glRasterPos2d((width/2)-(size/2), DRAWY(0))
    Draw.Text(title,"large")
    
    BGL.glRasterPos2d(10, DRAWY(30))
    Draw.Text("Path to Farmerjoe")
    Draw.Button("Select",e_['choose_dir'],180,DRAWY(5),80,18)

    c_['fj_root'] = Draw.String("", e_['save_root'], 10, DRAWY(25), 250, 18,
							c_['fj_root'].val, 255, "Path to Farmerjoe (leave off trailing slash)")
                            
    #BGL.glRasterPos2d(10, DRAWY(30))
    #Draw.Text("Set Job Parameters")
    
    BGL.glRasterPos2d(10, DRAWY(30))
    Draw.Text("Job Name")
    offset = Draw.GetStringWidth("Job Name")+20
    size = width - offset
    c_['fj_name'] = Draw.String("", e_['noevent'], offset, DRAWY(5), size, 18,
							c_['fj_name'].val, 255, "Job Name (can be anything)")
    #add toggle buttons here for frame/bucket
    
    if v_['render_type'] == 'frames':
        c_['step'] = Draw.Slider("Render Step: ", e_['noevent'], 10, DRAWY(30), 250, 18, c_['step'].val, 1, v_['totalframes'], 1, "Number of frames each client will render in 1 go")
    else:
        c_['step'].val = 1
        BGL.glRasterPos2d(10, DRAWY(30))
        Draw.Text("Single Frame Render: Frame " + str(context.startFrame()))
        
        BGL.glRasterPos2d(10, DRAWY(30))
        Draw.Text("Set X Parts and Y Parts for Bucket render")
        BGL.glRasterPos2d(10, DRAWY(15))
        Draw.Text("Leave 1 x 1 for normal render")
        
        tempy = DRAWY(30)
        c_['fj_xparts'] = Draw.Number("X Parts: ", e_['noevent'], 10, tempy, 125, 18, c_['fj_xparts'].val, 1, 8, "How many Columns to divide into")
        c_['fj_yparts'] = Draw.Number("Y Parts: ", e_['noevent'], 135, tempy, 125, 18, c_['fj_yparts'].val, 1, 8, "How many Rows to divide into")
        

        
    c_['timeout'] = Draw.Number("Timeout (mins): ", e_['noevent'], 10, DRAWY(40), 250, 18, c_['timeout'].val, 1, 1440, "Time to wait for a client to render each frame before re-assigning to another client")
    
    BGL.glRasterPos2d(10, DRAWY(30))
    Draw.Text("Extra Directories to Copy")
    c_['copydirs'] = Draw.String("", e_['noevent'], 10, DRAWY(25), 250, 18,
							c_['copydirs'].val, 255, "Directories must be in same directory as .blend")
    
    BGL.glRasterPos2d(10, DRAWY(30))
    Draw.Text("Set output parameters")
    
    c_['filetype'] = Blender.Draw.Menu(menuNameFromList("Save image as:",v_['filetypes']), e_['setFiletype'], 10, DRAWY(30), 150, 20, c_['filetype'].val, "Filetype")
    c_['rgb'] = Draw.Toggle("RGB", e_['rgb'], 170, DRAWY(0), 40, 20, c_['rgb'].val)
    c_['rgba'] = Draw.Toggle("RGBA", e_['rgba'], 220, DRAWY(0), 40, 20, c_['rgba'].val)
    
    Draw.Button("Submit Render", e_['submitRender'], 10, DRAWY(40), 180, 20)
    Draw.Button("Exit", e_['exit'], 200, DRAWY(0), 60, 20)
    

def filename_callback(filename_in_dir):
    global v_,c_,e_
    g_file_name = Blender.sys.basename(filename_in_dir)
    # Get the target directory
    c_['fj_root'].val = Blender.sys.dirname(filename_in_dir)
    update_registry()
	
    
def event(evt, mode):
   if evt == Blender.Draw.ESCKEY: Blender.Draw.Exit()
   if evt == Blender.Draw.QKEY: Blender.Draw.Exit()
   
def bevent(evt):
    global c_,e_,v_
    
    if evt == e_['submitRender']:
         submit()
    
    if evt == e_['choose_dir']:
        Blender.Window.FileSelector(filename_callback, "Select Directory")
        
    if evt == e_['exit']:
        Blender.Draw.Exit()
        
    if evt == e_['setFiletype']:
        context.setImageType(v_['filetype_const'][v_['filetypes'][c_['filetype'].val-1]])
        
    if evt == e_['rgb']:
        if c_['rgb'].val == 1:
            c_['rgba'].val = 0
            context.enableRGBColor()
        else:
            c_['rgba'].val = 1
            context.enableRGBAColor()
            
    if evt == e_['rgba']:
        if c_['rgba'].val == 1:
            c_['rgb'].val = 0
            context.enableRGBAColor()
        else:
            c_['rgb'].val = 1
            context.enableRGBColor()
    if evt == e_['save_root']:
        update_registry()
        
    Draw.Redraw(1)
    
Blender.Draw.Register(gui,event,bevent)
