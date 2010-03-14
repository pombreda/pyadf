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
    adffilename = 'workbench13.adf'
    class TempOpt(object):
        pass
    
    opt = TempOpt()
    opt.list = True

    adfobj = Adf(adffilename)
    list_dir_res = adfobj.ls_dir()
    print list_dir_res
    
    mydirname = 'devs'
    print 'DIR:', mydirname
    list_dir_res = adfobj.ls_dir(mydirname)
    print list_dir_res

    print 'DIR:', '*NOT PASSED IN*'
    list_dir_res = adfobj.ls_dir()
    print list_dir_res

    mydirname = 'devs/keymaps'
    print 'DIR:', mydirname
    list_dir_res = adfobj.ls_dir(mydirname)
    print list_dir_res
    
    mydirname = 'devs/keymaps/'  # with trailing slash
    print 'DIR:', mydirname
    list_dir_res = adfobj.ls_dir(mydirname)
    print list_dir_res

    mydirname = '/devs/keymaps/'  # with leading and trailing slash
    print 'DIR:', mydirname
    list_dir_res = adfobj.ls_dir(mydirname)
    print list_dir_res

    mydirname = 'devs\\keymaps\\'  # with Windows style path
    print 'DIR:', mydirname
    list_dir_res = adfobj.ls_dir(mydirname)
    print list_dir_res

    print 'DIR:', '*NOT PASSED IN*'
    list_dir_res = adfobj.ls_dir()
    print list_dir_res

    print 'chdir', 'devs'
    adfobj.chdir('devs')
    
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

