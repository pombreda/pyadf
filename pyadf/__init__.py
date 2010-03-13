#!/bin/env python
# -*- coding: ascii -*-
# vim:ts=4:sw=4:softtabstop=4:smarttab:expandtab
#

import os

from adflib import *

class AdfBaseException(Exception):
    '''Base ADF I/O exception'''

class AdfIOException(AdfBaseException):
    '''I/O exception'''

adflib_init = False

# FIXME These are naive, if there are multiple calls we could end up free'ing things that are still in use
def adf_setup():
    global adflib_init
    if not adflib_init:
        adfEnvInitDefault()
        adflib_init = True

def adf_cleanup():
    global adflib_init
    if not adflib_init:
        adfEnvCleanUp()
        adflib_init = False

Entry_Ptr = POINTER(Entry)


class AdfFileInfo(object):
    """Right now this is basically an expensive named tuple
    """
    def __init__(self, ftype, fsize, fdate, fpath, fname, fcomment=None, fsector=None):
        """fdate is a tuple (year, month, days, hour, mins, secs)
        """
        self.ftype = ftype
        self.fsize = fsize
        self.fdate = fdate
        self.fpath = fpath
        self.fsector = fsector
        self.fname = fname
        self.fcomment = fcomment
    
    def __repr__(self):
        return repr(self.__dict__)
    

def process_entry(vol_ptr, entry_ptr, file_path):
    """Simple print file information (uses print) output goes to stdout
    """
    vol = vol_ptr[0]
    entry = entry_ptr[0]
    # do not print the links entries, ADFlib do not support them yet properly
    if entry.type==ST_LFILE or entry.type==ST_LDIR or entry.type==ST_LSOFT:
        return
    
    tmp_comment = None
    if entry.comment and len(entry.comment)>0:
        tmp_comment = str(entry.comment)
    
    #print type(entry.type), type(entry.size), type(entry.year), type(entry.month), type(entry.days), type(entry.hour), type(entry.mins), type(entry.secs), type(file_path), type(entry.name), type(tmp_comment), type(entry.sector)
    result = AdfFileInfo(entry.type, entry.size, (entry.year, entry.month, entry.days, entry.hour, entry.mins, entry.secs), file_path, str(entry.name), tmp_comment, entry.sector)
    return result

class Adf(object):
    """A pythonic api wrapper around ADFlib
    """
    def __init__(self, adf_filename, volnum = 0):
        if not os.path.exists(adf_filename):
            raise AdfIOException('%s filename does not exist' % adf_filename)
        
        self.adf_filename = adf_filename
        self.vol = None
        self.dev = None
        self.volnum = volnum
        
        self._curdir = None
        
        self.open()  # kinda nasty doing work in the constructor....
    
    def ls_dir(self, dirname=None):
        vol = self.vol
        if dirname:
            # kinda hokey, go back to parentdir at end
            for tmpdir in dirname.split('/'):
                if tmpdir:
                    adfChangeDir(vol, tmpdir)
            #raise NotImplementedError('directory names not support')
        result = []
        list = adfGetDirEnt(vol, vol[0].curDirPtr)
        cell = list 
        while cell:
            tmp_content = cell[0].content
            tmp_content = cast(tmp_content, Entry_Ptr)
            fentry = process_entry(vol, tmp_content, "")
            if fentry:
                result.append(fentry)
            cell = cell[0].next
        
        adfFreeDirList(list)
        if dirname:
            adfToRootDir(vol)
        return result
    
    def open(self):
        ## not sure about name
        adf_setup()
        if not self.dev:
            self.dev = adfMountDev(self.adf_filename, True)
        if not self.vol:
            self.vol = adfMount(self.dev, self.volnum, True)

    def close(self):
        ## not sure about name
        if self.vol:
            adfUnMount(self.vol)
        if self.dev:
            adfUnMountDev(self.dev)

        adf_cleanup()
    
    def __del__(self):
        self.close()

