#============================================================================
# This library is free software; you can redistribute it and/or
# modify it under the terms of version 2.1 of the GNU Lesser General Public
# License as published by the Free Software Foundation.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#============================================================================
# Copyright (C) 2005-2006 XenSource Inc.
#============================================================================


import os
import os.path
import sys

_path = sys.path[0]

def execute(exe, args = None):
    exepath = pathTo(exe)
    a = [ exepath ]
    if args:
        a.extend(args)
    os.execv(exepath, a)


def pathTo(exe):
    return os.path.join(path(), exe)


def path():
    return _path


def root():
    return os.path.realpath(os.path.join(path(), '..'))


def libpath():
    return os.path.realpath(os.path.join(path(), '../lib'))
