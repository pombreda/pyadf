#!/bin/env python
# -*- coding: ascii -*-
# vim:ts=4:sw=4:softtabstop=4:smarttab:expandtab
#
"""Simple command tool for examing adf files

Should be pep8 compliant.
"""

import sys
import cmd

from pyadf import Adf, AdfIOException

class AdfCmdInterpreter(cmd.Cmd):
    
    def __init__(self, adf_filename):
        cmd.Cmd.__init__(self)
        self.adf_filename = adf_filename
        self.adfobj = Adf(self.adf_filename)
        
    def do_print(self, line=None):
        """print file to stdout"""
        filename = line
        #filename='Disk.info'
        #filename='/Disk.info' # bad (leading slash
        #filename='nothere' # bad its missing, duh!
        if filename:
            print 'accessing %r' % filename
            try:
                result = self.adfobj.get_file(filename)
            except AdfIOException, info:
                print 'error reading file'
                print '\t%s' % info
                return

            print '%d bytes read from %s' % (len(result), filename)
            print repr(result)
        else:
            print 'missing filename'
            
    def do_printraw(self, line=None):
        """print file to stdout"""
        filename = line
        #filename='Disk.info'
        #filename='/Disk.info' # bad (leading slash
        #filename='nothere' # bad its missing, duh!
        if filename:
            print 'accessing %r' % filename
            try:
                result = self.adfobj.get_file(filename)
            except AdfIOException, info:
                print 'error reading file'
                print '\t%s' % info
                return

            print '%d bytes read from %s' % (len(result), filename)
            print result
        else:
            print 'missing filename'
    
    def do_cd(self, line=None):
        """change directory"""
        return self.do_chdir(line)
    
    def do_chdir(self, line=None):
        """change directory"""
        if line:
            """
            result = self.adfobj.chdir(line, ignore_error=False)
            if not result :
                print 'unable to changed directory'
            """
            try:
                result = self.adfobj.chdir(line)
            except AdfIOException, info:
                print 'unable to changed directory'
                print '\t%s' % info
        else:
            # Windows style show current directory
            print self.adfobj._curdir
        
    def do_dir(self, line):
        """Directory listing"""
        return self.do_ls(line)
        
    def do_ls(self, line=None):
        """Directory listing, not flags are supported only directory name/path"""
        if line is None:
            list_dir_res = self.adfobj.ls_dir()
        else:
            try:
                list_dir_res = self.adfobj.ls_dir(line)
            except AdfIOException, info:
                print 'bad directory specified'
                print '\t%s' % info
                return
        #print list_dir_res
        for x in list_dir_res:
            print x.pretty_str()
    
    def do_exit(self, line=None):
        """Quit/Exit"""
        print "Quitting..."
        return 1

    def do_quit(self, line=None):
        """Quit/Exit"""
        return self.do_exit(line)




def main(argv=None):
    if argv is None:
        argv = sys.argv
    
    adffilename = argv[1]
    
    interpreter = AdfCmdInterpreter(adffilename)
    interpreter.cmdloop()

    return 0


if __name__ == "__main__":
    sys.exit(main())
