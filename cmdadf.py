#!/bin/env python
# -*- coding: ascii -*-
# vim:ts=4:sw=4:softtabstop=4:smarttab:expandtab
#
"""Simple command tool for examing adf files

Should be pep8 compliant.
"""

import sys
import shlex
import cmd

from pyadf import Adf, AdfIOException, AdfVersionInfo

class AdfCmdInterpreter(cmd.Cmd):
    
    def __init__(self, adf_filename, mode='r'):
        cmd.Cmd.__init__(self)
        self.adf_filename = adf_filename
        self.mode = mode
        self.adfobj = Adf(self.adf_filename, mode=self.mode)
        
    def do_version(self, line=None):
        """adflib version info"""
        version_info = AdfVersionInfo()
        print version_info
    do_ver = do_version
    
    def do_print(self, line=None):
        """print file to stdout"""
        filename = line
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
    
    def do_get(self, line=None):
        """get file to local filesystem
                get adf_name [local_name]
        * Use double "quotes" around names.
        * local_name defaults to adf_name is ommited
        """
        ## TODO sanitize filenames for local filesystem?
        filename = line
        if filename:
            lexed_names = shlex.split(filename)
            if len(lexed_names) >=2:
                filename = lexed_names[0]
                local_filename = lexed_names[1]
            else:
                local_filename = filename
            print 'get %r' % filename
            try:
                result = self.adfobj.get_file(filename)
            except AdfIOException, info:
                print 'error reading file'
                print '\t%s' % info
                return

            print '%d bytes read from %s' % (len(result), filename)
            f = open(local_filename, 'wb')
            f.write(result)
            f.close()
        else:
            print 'missing filename'
    
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
                print 'unable to change directory'
                print '\t%s' % info
        else:
            # Windows style show current directory
            print self.adfobj._curdir
    do_cd = do_chdir
    
    def do_ls(self, line=None):
        """Directory listing. Flags are NOT supported only directory name/path"""
        if line is None:
            list_dir_res = self.adfobj.ls_dir()
        else:
            try:
                list_dir_res = self.adfobj.ls_dir(line)
            except AdfIOException, info:
                print 'bad directory specified'
                print '\t%s' % info
                return
        for x in list_dir_res:
            print x.pretty_str()
    do_list = do_ls
    do_dir = do_ls

    def do_rename(self, line=None):
        """rename file/empty-directory
        """
        filename = line
        if filename:
            lexed_names = shlex.split(filename)
            if len(lexed_names) >=2:
                old = lexed_names[0]
                new = lexed_names[1]
            else:
                print 'missing names'
                return
            try:
                result = self.adfobj.rename(old, new)
            except AdfIOException, info:
                print 'error renaming'
                print '\t%s' % info
                return
        else:
            print 'missing names'
    do_ren = do_rename
    do_mv = do_rename

    def do_delete(self, line=None):
        """delte file """
        filename = line
        if filename:
            try:
                result = self.adfobj.unlink(filename)
            except AdfIOException, info:
                print 'error deleting file'
                print '\t%s' % info
                return
        else:
            print 'missing filename'
    do_del = do_delete
    do_rm = do_delete
    do_unlink = do_delete

    def do_exit(self, line=None):
        """Quit/Exit"""
        print "Quitting..."
        return 1
    do_quit = do_exit
    do_bye = do_exit


def main(argv=None):
    if argv is None:
        argv = sys.argv
    
    adffilename = argv[1]
    
    mode='r'
    #mode='w' # enable write, e.g. rename, delete, add files
    interpreter = AdfCmdInterpreter(adffilename, mode=mode)
    interpreter.cmdloop()

    return 0


if __name__ == "__main__":
    sys.exit(main())
