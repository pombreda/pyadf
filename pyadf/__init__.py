#!/bin/env python
# -*- coding: ascii -*-
# vim:ts=4:sw=4:softtabstop=4:smarttab:expandtab
#

import os
import ctypes

import adflib

class AdfBaseException(Exception):
    '''Base ADF I/O exception'''

class AdfIOException(AdfBaseException):
    '''I/O exception'''

class AdfVersionInfo(object):
    """There are 2 kinds of version information available:
        * what verson of ADFLib was adflib.py created with?
        * what verson of adflib.dll or adf.so (etc.) are we running with?
    """
    def __init__(self):
        # what was adflib.py "created" with?
        self.headers_version = adflib.ADFLIB_VERSION
        self.headers_date = adflib.ADFLIB_DATE
        
        # what version of adflib are we running with?
        self.lib_version = adflib.adfGetVersionNumber()
        self.lib_date = adflib.adfGetVersionDate()
    
    def __repr__(self):
        return repr(self.__dict__)


adflib_init = False

# FIXME These are naive, if there are multiple calls we could end up free'ing things that are still in use
def adf_setup():
    global adflib_init
    if not adflib_init:
        adflib.adfEnvInitDefault()
        adflib_init = True

def adf_cleanup():
    global adflib_init
    if not adflib_init:
        adflib.adfEnvCleanUp()
        adflib_init = False


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
    
    def pretty_str(self):
        """return pretty output for the file entry"""
        date_str = "%4d/%02d/%02d  %2d:%02d:%02d" % self.fdate
        if self.fpath:
            name_str = "%s/"%(self.fpath,)
        else:
            name_str = ""
        if self.ftype == adflib.ST_DIR:
            name_str += "%s/"%(self.fname,)
            size_str = ' ' * 7
        else:
            name_str += "%s"%(self.fname,)
            size_str = "%7d" %(self.fsize,)
        
        return date_str + ' ' + size_str + ' ' + name_str 
    

def process_entry(vol_ptr, entry_ptr, file_path):
    """Simple print file information (uses print) output goes to stdout
    """
    vol = vol_ptr[0]
    entry = entry_ptr[0]
    # do not print the links entries, ADFlib do not support them yet properly
    if entry.type==adflib.ST_LFILE or entry.type==adflib.ST_LDIR or entry.type==adflib.ST_LSOFT:
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
        
        self._curdir = '/'
        
        self.open()  # kinda nasty doing work in the constructor....
    
    def normpath(self, filepath):
        filepath = filepath.replace('\\', '/')  # Allow Windows style paths (just in case they slip in)
        filepath = filepath.replace(':', '/')  # Allow Amiga style paths (just in case they slip in)
        return filepath
    
    def splitpath(self, filepath):
        filepath = self.normpath(filepath)
        result = []
        for tmpdir in filepath.split('/'):
            if tmpdir:
                result.append(tmpdir)
        return result
    
    def chdir(self, dirname, ignore_error=False):
        vol = self.vol
        return self._chdir(dirname, ignore_error=ignore_error)
        
    def _chdir(self, dirname, update_curdir=True, ignore_error=False):
        vol = self.vol
        dirname = self.normpath(dirname)
        if dirname.startswith('/'):
            adflib.adfToRootDir(vol)
            if update_curdir:
                self._curdir = '/'
        if dirname == '/':
            return True
        else:
            for tmpdir in dirname.split('/'):
                if tmpdir:
                    result = adflib.adfChangeDir(vol, tmpdir)
                    if result == -1:
                        # FAIL
                        if ignore_error:
                            return False
                        else:
                            raise AdfIOException('error changing directory to %s in %s' % (tmpdir, dirname))
                    else:
                        if update_curdir:
                            self._curdir += dirname+'/'
        return True
    
    def ls_dir(self, dirname=None):
        vol = self.vol
        if dirname:
            self._chdir(dirname, update_curdir=False)
        else:
            self._chdir(self._curdir)
        result = []
        Entry_Ptr = adflib.POINTER(adflib.Entry)
        list = adflib.adfGetDirEnt(vol, vol[0].curDirPtr)
        cell = list 
        while cell:
            tmp_content = cell[0].content
            tmp_content = adflib.cast(tmp_content, Entry_Ptr)
            fentry = process_entry(vol, tmp_content, "")
            if fentry:
                result.append(fentry)
            cell = cell[0].next
        
        adflib.adfFreeDirList(list)
        if dirname:
            self._chdir(self._curdir)
        return result
    
    def get_file(self, filename):
        """return Python string which is the file contents.
        NOTE/FIXME filename needs to be a file in the current directory at the moment.
        FIXME if a directory name is passed in need to fail!
        """
        vol = self.vol
        filename = self.normpath(filename)
        splitpaths = self.splitpath(filename)
        if len(splitpaths) >1:
            #if filename.startswith('/'):
            # trim leading slash
            #filename = filename[1:]
            filename = splitpaths[-1]
            tmp_dirname = splitpaths[:-1]
            tmp_dirname= '/'.join(tmp_dirname)
            self._chdir(tmp_dirname, update_curdir=False, ignore_error=False)
        file_in_adf = adflib.adfOpenFile(vol, filename, "r");
        if not file_in_adf:
            # file probably not there
            self._chdir(self._curdir)
            raise AdfIOException('unable to filename %s for read' % filename)
            return
        
        #print 'adffile', repr(file_in_adf)
        #print 'type adffile', type(file_in_adf)
        #print 'dir adffile', dir(file_in_adf)
        #print 'adffile[0]', repr(file_in_adf[0])
        #adffile = adffile[0]
        tmp_buffer_size = 1024*8
        mybuff_type = ctypes.c_ubyte * tmp_buffer_size
        mybuff = mybuff_type() ## probably a better way than this
        #mybuff_ptr = ctypes.pointer(mybuff)
        eof_yet = adflib.adfEndOfFile(file_in_adf)
        #print 'eof_yet ', eof_yet 
        #print 'eof_yet ', type(eof_yet )
        tmp_str = []
        while not eof_yet:
            n = adflib.adfReadFile(file_in_adf, tmp_buffer_size, ctypes.byref(mybuff))
            eof_yet = adflib.adfEndOfFile(file_in_adf)
            #print 'eof_yet ', eof_yet 
            #print 'eof_yet ', type(eof_yet )
            #print 'n', n
            #print 'mybuff', mybuff
            #print 'mybuff', dir(mybuff)
            #print 'mybuff', str(mybuff)
            # FIXME performance of this is poor
            for x in mybuff[:n]:
                tmp_str.append(chr(x))
            #print 'tmp_str', tmp_str
            #print 'len tmp_str', len(tmp_str)
        self._chdir(self._curdir)
        return ''.join(tmp_str)
        
    
    def open(self):
        ## not sure about name
        adf_setup()
        if not self.dev:
            self.dev = adflib.adfMountDev(self.adf_filename, True)
        if not self.vol:
            self.vol = adflib.adfMount(self.dev, self.volnum, True)

    def close(self):
        ## not sure about name
        if self.vol:
            adflib.adfUnMount(self.vol)
        if self.dev:
            adflib.adfUnMountDev(self.dev)

        adf_cleanup()
    
    def __del__(self):
        self.close()

