#!BPY

"""
Name: 'Farmerjoe Bucket Render'
Blender: 242
Group: 'Render'
Tooltip: 'Render Part of a single frame (Bucket render)'
"""

__author__ = "Mitch Hughes (lobo_nz)"
__url__ = ("blender", "Author's homepage, http://blender.formworks.co.nz")
_v_ersion__ = "0.1 Alpha"

__bpydoc__ = """\
This script Renders Part of a single frame (Bucket render).

Usage:
    
No need to use this its used by Farmerjoe.pl when doing a bucket render.
"""

# $Id: farmerjoe_bucket.py,v 0.1 2006/08/29 10:27:10$
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

import Blender
from Blender import Scene
import os

x1 = float(os.getenv('x1'))
x2 = float(os.getenv('x2'))
y1 = float(os.getenv('y1'))
y2 = float(os.getenv('y2'))
part = str(os.getenv('part'))

border = [x1,y1,x2,y2]
    
scene  = Scene.getCurrent()
context = scene.getRenderingContext()

context.enableBorderRender(1)
context.enableRGBAColor()
context.setImageType(Scene.Render.TARGA)
#context.enableCropping(1)
context.partsX(1)
context.partsY(1)

context.enableExtensions(1)
context.setRenderPath('//render_parts/' + "part_"+ part +"_") # // is the currentdir
#w,h = context.imageSizeX(),context.imageSizeY()
print border[0]
print border[1]
print border[2]
print border[3] 
context.setBorder(border[0], border[1], border[2], border[3] )

context.renderAnim()
#context.render()
#context.saveRenderedImage("test")

scene.update(1)