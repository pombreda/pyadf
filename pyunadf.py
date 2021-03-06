#!/bin/env python
# -*- coding: ascii -*-
# vim:ts=4:sw=4:softtabstop=4:smarttab:expandtab
#
"""Simple partial unadf.c clone using Pythonic API

Should be pep8 compliant.
"""

import sys

from pyadf import Adf

def main(argv=None):
    if argv is None:
        argv = sys.argv

    ## TEMP code
    adffilename = 'tests/data/pyadftest.adf'
    class TempOpt(object):
        pass
    
    opt = TempOpt()
    opt.list = True

    adfobj = Adf(adffilename)
    list_dir_res = adfobj.ls_dir()
    print list_dir_res
    
    mydirname = 'dir1'
    print 'DIR:', mydirname
    list_dir_res = adfobj.ls_dir(mydirname)
    print list_dir_res

    print 'DIR:', '*NOT PASSED IN*'
    list_dir_res = adfobj.ls_dir()
    print list_dir_res

    mydirname = 'dir1/subdir1'
    print 'DIR:', mydirname
    list_dir_res = adfobj.ls_dir(mydirname)
    print list_dir_res
    
    mydirname = 'dir1/subdir1/'  # with trailing slash
    print 'DIR:', mydirname
    list_dir_res = adfobj.ls_dir(mydirname)
    print list_dir_res

    mydirname = '/dir1/subdir1/'  # with leading and trailing slash
    print 'DIR:', mydirname
    list_dir_res = adfobj.ls_dir(mydirname)
    print list_dir_res

    mydirname = 'dir1\\subdir1\\'  # with Windows style path
    print 'DIR:', mydirname
    list_dir_res = adfobj.ls_dir(mydirname)
    print list_dir_res

    print 'DIR:', '*NOT PASSED IN*'
    list_dir_res = adfobj.ls_dir()
    print list_dir_res

    print 'chdir', 'dir1'
    adfobj.chdir('dir1')
    
    print 'DIR:', '*NOT PASSED IN*'
    list_dir_res = adfobj.ls_dir()
    print list_dir_res
    
    print 'chdir', '/'
    adfobj.chdir('/')
    
    print 'DIR:', '*NOT PASSED IN*'
    list_dir_res = adfobj.ls_dir()
    print list_dir_res
    

    return 0


if __name__ == "__main__":
    sys.exit(main())

