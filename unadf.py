#!/bin/env python
# -*- coding: ascii -*-
# vim:ts=4:sw=4:softtabstop=4:smarttab:expandtab
#
"""Simple partial unadf.c clone
See http://cvs.sourceforge.net/viewvc/adflib/adflib/Demo/unadf.c?revision=1.1.1.1&view=markup

Relies on (prebuilt shared library/DLL) adflib from
http://sourceforge.net/projects/adflib

NOTE names for functions, constants, etc. come from adf lib so this code is
not 100% pep8 compliant.
"""

#from pyadf import *
from pyadf.adflib import *

def printEnt(vol_ptr, entry_ptr, file_path, sect):
    """Simple print file information (uses print) output goes to stdout
    """
    vol = vol_ptr[0]
    entry = entry_ptr[0]
    # do not print the links entries, ADFlib do not support them yet properly
    if entry.type==ST_LFILE or entry.type==ST_LDIR or entry.type==ST_LSOFT:
        return
    
    if entry.type==ST_DIR:
        print " " *13,
    else:
        print "%7ld  " %(entry.size,),
    
    print "%4d/%02d/%02d  %2d:%02d:%02d " % (entry.year, entry.month, entry.days, entry.hour, entry.mins, entry.secs),
    if sect:
        print " %06ld "%(entry.sector,),

    if len(file_path)>0:
        print " %s/"%(file_path,),
    else:
        print " ",
    if entry.type==ST_DIR:
        print "%s/"%(entry.name,),
    else:
        print "%s"%(entry.name,),
    if entry.comment and len(entry.comment)>0:
        print ", %s"%(entry.comment,),
    
    print ''

def main(argv=None):
    if argv is None:
        argv = sys.argv
    
    ## TEMP code
    adffilename = 'workbench13.adf'
    class TempOpt(object):
        pass
    
    opt = TempOpt()
    opt.list = True
    
    
    devname = adffilename
    volnum = 0
    sflag = False
    
    adfEnvInitDefault()
    
    dev = adfMountDev(devname,True)
    vol = adfMount(dev, volnum, True)
    volrec = vol[0]
    
    if opt.list:
        # TODO dircache stuff?
        struct_Entry_Ptr = POINTER(struct_Entry)
        
        list = adfGetDirEnt(vol, vol[0].curDirPtr)
        cell = list 
        while cell:
            tmp_content = cell[0].content
            tmp_content = cast(tmp_content, struct_Entry_Ptr)
            printEnt(vol, tmp_content, "", sflag)
            cell = cell[0].next
        
        adfFreeDirList(list)
    
    ########
    # clean up
    adfUnMount(vol)
    adfUnMountDev(dev)
    adfEnvCleanUp()


    return 0


if __name__ == "__main__":
    sys.exit(main())
