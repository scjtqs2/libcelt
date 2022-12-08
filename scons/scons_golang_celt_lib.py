#!/usr/bin/env python
import os
import sys
import fnmatch

#remove a file list in file list
def remove_file_list_in_list(slst, dlst) :
	for u in dlst :
		slst.remove(os.path.abspath(u))

#remove a list in list
def remove_list_in_list(slst, dlst) :
	for u in dlst :
		slst.remove(u)

 #CC CXX
CC_TOOL = ARGUMENTS.get('build_cc', os.environ.get('CC'))
CXX_TOOL = ARGUMENTS.get('build_cxx', os.environ.get('CXX'))
AR_TOOL = ARGUMENTS.get('build_ar', os.environ.get('AR'))

if CC_TOOL == "" or CC_TOOL == None or CXX_TOOL == "" or CXX_TOOL == None :
	print("use default build environment")
	env = Environment()
else :
	print("use custom build environment")
	env = Environment(CC = CC_TOOL, CXX = CXX_TOOL)
	if AR_TOOL != "" and AR_TOOL != None : env.Replace(AR = AR_TOOL)

#paths
LOCAL_DIR = os.path.abspath(sys.path[0])
MAIN_SRC = LOCAL_DIR + '/../'


#source files
source_files = [
    MAIN_SRC + '/celt-0.7.1/libcelt/bands.c',
    MAIN_SRC + '/celt-0.7.1/libcelt/celt.c',
    MAIN_SRC + '/celt-0.7.1/libcelt/cwrs.c',
#    MAIN_SRC + '/celt-0.7.1/libcelt/dump_modes.c',
    MAIN_SRC + '/celt-0.7.1/libcelt/entcode.c',
    MAIN_SRC + '/celt-0.7.1/libcelt/entdec.c',
    MAIN_SRC + '/celt-0.7.1/libcelt/entenc.c',
    MAIN_SRC + '/celt-0.7.1/libcelt/header.c',
    MAIN_SRC + '/celt-0.7.1/libcelt/kiss_fft.c',
    MAIN_SRC + '/celt-0.7.1/libcelt/laplace.c',
    MAIN_SRC + '/celt-0.7.1/libcelt/mdct.c',
    MAIN_SRC + '/celt-0.7.1/libcelt/modes.c',
    MAIN_SRC + '/celt-0.7.1/libcelt/pitch.c',
 #   MAIN_SRC + '/libcelt/plc.c',
    MAIN_SRC + '/celt-0.7.1/libcelt/quant_bands.c',
    MAIN_SRC + '/celt-0.7.1/libcelt/rangedec.c',
    MAIN_SRC + '/celt-0.7.1/libcelt/rangeenc.c',
    MAIN_SRC + '/celt-0.7.1/libcelt/rate.c',
 #   MAIN_SRC + '/libcelt/testcelt.c',
    MAIN_SRC + '/celt-0.7.1/libcelt/vq.c',

]

source_files.extend(Split(ARGUMENTS.get('source_files', [])))
remove_file_list_in_list(source_files, Split(ARGUMENTS.get('exclude_source_files', [])))

#include path
source_file_paths = [
	MAIN_SRC,
    MAIN_SRC + '/../../libcelt/include',
]

source_file_paths.extend(Split(ARGUMENTS.get('source_file_paths', [])))
remove_file_list_in_list(source_file_paths, Split(ARGUMENTS.get('exclude_source_file_paths', [])))
remove_file_list_in_list(source_files, Split(ARGUMENTS.get('exclude_source_files', [])))



#build flags
build_flags = [

]

build_flags.extend(Split(ARGUMENTS.get('build_flags', [])))
remove_list_in_list(build_flags, Split(ARGUMENTS.get('exclude_build_flags', [])))

#librarys
libs = [
    'm',
    'dl',
]

libs.extend(Split(ARGUMENTS.get('libs', [])))
remove_list_in_list(libs, Split(ARGUMENTS.get('exclude_libs', [])))

#library paths
lib_paths = [
]
lib_paths.extend(Split(ARGUMENTS.get('lib_paths', [])))
remove_list_in_list(lib_paths, Split(ARGUMENTS.get('exclude_lib_paths', [])))

#link flags
link_flags = [
	'-static'
]
link_flags.extend(Split(ARGUMENTS.get('link_flags', [])))
remove_list_in_list(link_flags, Split(ARGUMENTS.get('exclude_link_flags', [])))

#source to obj
obj_path = ARGUMENTS.get('obj_path', 'objs/')
objs = []
for u in source_files :
        objs.append(env.Object(obj_path + '/' + os.path.basename(u) + '.o', u,
		CPPPATH = source_file_paths,
		CCFLAGS = build_flags,
		))

#build
bin = ARGUMENTS.get('bin', 'libcelt0')
print(libs)
env.StaticLibrary(
	bin,
	source = objs,
	CPPPATH = source_file_paths,
	CCFLAGS = build_flags,
	CPPFLAGS = build_flags,
	LIBS = libs,
	LIBPATH = lib_paths,
	LINKFLAGS= link_flags,
)