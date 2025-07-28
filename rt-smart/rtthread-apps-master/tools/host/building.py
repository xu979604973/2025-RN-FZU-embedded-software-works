#
# File      : building.py
# This file is part of RT-Thread RTOS
# COPYRIGHT (C) 2006 - 2015, RT-Thread Development Team
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License along
#  with this program; if not, write to the Free Software Foundation, Inc.,
#  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# Change Logs:
# Date           Author       Notes
# 2015-01-20     Bernard      Add copyright information
#

import os
import sys
import string

from SCons.Script import *

BuildOptions = {}
Projects = []
Env = None

def GetCurrentDir():
    conscript = File('SConscript')
    fn = conscript.rfile()
    name = fn.name
    path = os.path.dirname(fn.abspath)
    return path

def PrepareHostModuleBuilding(env):
    global Env
    Env = env;

def GetDepend(depend):
    # always true
    return True

def MergeGroup(src_group, group):
    src_group['src'] = src_group['src'] + group['src']
    if 'CCFLAGS' in group:
        if 'CCFLAGS' in src_group:
            src_group['CCFLAGS'] = src_group['CCFLAGS'] + group['CCFLAGS']
        else:
            src_group['CCFLAGS'] = group['CCFLAGS']
    if 'CPPPATH' in group:
        if 'CPPPATH' in src_group:
            src_group['CPPPATH'] = src_group['CPPPATH'] + group['CPPPATH']
        else:
            src_group['CPPPATH'] = group['CPPPATH']
    if 'CPPDEFINES' in group:
        if 'CPPDEFINES' in src_group:
            src_group['CPPDEFINES'] = src_group['CPPDEFINES'] + group['CPPDEFINES']
        else:
            src_group['CPPDEFINES'] = group['CPPDEFINES']

    # for local CCFLAGS/CPPPATH/CPPDEFINES
    if 'LOCAL_CCFLAGS' in group:
        if 'LOCAL_CCFLAGS' in src_group:
            src_group['LOCAL_CCFLAGS'] = src_group['LOCAL_CCFLAGS'] + group['LOCAL_CCFLAGS']
        else:
            src_group['LOCAL_CCFLAGS'] = group['LOCAL_CCFLAGS']
    if 'LOCAL_CPPPATH' in group:
        if 'LOCAL_CPPPATH' in src_group:
            src_group['LOCAL_CPPPATH'] = src_group['LOCAL_CPPPATH'] + group['LOCAL_CPPPATH']
        else:
            src_group['LOCAL_CPPPATH'] = group['LOCAL_CPPPATH']
    if 'LOCAL_CPPDEFINES' in group:
        if 'LOCAL_CPPDEFINES' in src_group:
            src_group['LOCAL_CPPDEFINES'] = src_group['LOCAL_CPPDEFINES'] + group['LOCAL_CPPDEFINES']
        else:
            src_group['LOCAL_CPPDEFINES'] = group['LOCAL_CPPDEFINES']

    if 'LINKFLAGS' in group:
        if 'LINKFLAGS' in src_group:
            src_group['LINKFLAGS'] = src_group['LINKFLAGS'] + group['LINKFLAGS']
        else:
            src_group['LINKFLAGS'] = group['LINKFLAGS']
    if 'LIBS' in group:
        if 'LIBS' in src_group:
            src_group['LIBS'] = src_group['LIBS'] + group['LIBS']
        else:
            src_group['LIBS'] = group['LIBS']
    if 'LIBPATH' in group:
        if 'LIBPATH' in src_group:
            src_group['LIBPATH'] = src_group['LIBPATH'] + group['LIBPATH']
        else:
            src_group['LIBPATH'] = group['LIBPATH']

def DefineGroup(name, src, depend, **parameters):
    global Env
    if not GetDepend(depend):
        return []

    # find exist group and get path of group
    group_path = ''
    for g in Projects:
        if g['name'] == name:
            group_path = g['path']
    if group_path == '':
        group_path = GetCurrentDir()

    group = parameters
    group['name'] = name
    group['path'] = group_path
    if type(src) == type(['src1']):
        group['src'] = File(src)
    else:
        group['src'] = src

    if 'CCFLAGS' in group:
        Env.Append(CCFLAGS = group['CCFLAGS'])
    if 'CPPPATH' in group:
        Env.Append(CPPPATH = group['CPPPATH'])
    if 'CPPDEFINES' in group:
        Env.Append(CPPDEFINES = group['CPPDEFINES'])
    if 'LINKFLAGS' in group:
        Env.Append(LINKFLAGS = group['LINKFLAGS'])

    if 'LIBS' in group:
        Env.Append(LIBS = group['LIBS'])
    if 'LIBPATH' in group:
        Env.Append(LIBPATH = group['LIBPATH'])

    if 'LIBRARY' in group:
        objs = Env.Library(name, group['src'])
    else:
        objs = group['src']

    # merge group
    for g in Projects:
        if g['name'] == name:
            # merge to this group
            MergeGroup(g, group)
            return objs

    # add a new group
    Projects.append(group)

    return objs