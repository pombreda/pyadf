#!/bin/env python
# -*- coding: ascii -*-
# vim:ts=4:sw=4:softtabstop=4:smarttab:expandtab
#
"""Simple small tests

"""

import sys
import os
import stat
import shutil

import unittest

test_directory = os.path.abspath(os.path.dirname(__file__))

# this path stuff doesn't really work
sys.path.append(os.path.dirname(test_directory))  # nasty path hack
sys.path.append(os.path.join(os.path.dirname(test_directory), "pyadf"))  # nasty path hack
from pyadf import Adf, AdfIOException, AdfVersionInfo


class PyadfTest(unittest.TestCase):
    
    def setUp(self):
        self.adf_canonfilename = 'pyadftest.adf'
        self.adf_testfilename = 'testsuite_pyadftest.adf'  # TODO use tempfile?
        self.adf_canonfilename = os.path.join(test_directory, 'data', self.adf_canonfilename )
        # move below into re-copy method?
        shutil.copy(self.adf_canonfilename, self.adf_testfilename)
        os.chmod(self.adf_testfilename, stat.S_IWRITE)
        self.adfobj = None

    def open(self, adf_filename=None):
        adf_filename = adf_filename or self.adf_testfilename
        self.adfobj = Adf(adf_filename)
        return self.adfobj

    def tearDown(self):
        if self.adfobj:
            #del self.adfobj
            self.adfobj.close()
        # If adfobj has not been destroyed, unlink will fail under Windows (permssion denied. file in use)
        os.unlink(self.adf_testfilename)

    def testMissingOpen(self):
        """Open a missing ADF file"""
        adf_filename = 'doesnotexist.adf'
        def open_non_existent():
            adfobj = self.open(adf_filename)
        self.failIf(os.path.exists(adf_filename), '%r should not exist!'%adf_filename)
        self.failUnlessRaises(AdfIOException, open_non_existent)

    def testListRoot(self):
        """Directory listing from an ADF"""
        adf_filename = self.adf_testfilename
        adfobj = self.open()
        list_dir_res = adfobj.ls_dir()
        expect_result = ['A Christmas Carol stave1 by Ch', 'unixtext.txt', 'read_file.py', 'juggler.png', 'wintext.txt', 'file with spaces.txt', 'juggler_adnim.gif', 'maximum_file_length_of_30.txt', 'AmigaLogo.iff', 'dir1', 'UPPERCASEDIR', 'readme.txt', 'MixedCaseDir']
        result = []
        for x in list_dir_res:
            # for now just tests names
            result.append(x.fname)
        expect_result.sort()
        result.sort()
        self.failUnlessEqual(expect_result, result)

    def get_and_compare(self, filename):
        """get a file from an ADF"""
        adf_filename = self.adf_testfilename
        adfobj = self.open()
        canon_filename = os.path.join(test_directory, 'data', 'example_files', filename)
        f = open(canon_filename, 'rb')
        expect_result = f.read()
        f.close()
        result = adfobj.get_file(filename)
        self.failUnlessEqual(expect_result, result)
    
    def testGetSmall(self):
        """get a file small sized from an ADF"""
        self.get_and_compare('unixtext.txt')
    
    def testGetSmallSubDir1(self):
        """get a file small sized from an ADF from a sub dir"""
        self.get_and_compare('dir1/a.txt')
    
    def testGetSmallSubDir2(self):
        """get a file small sized from an ADF from a sub dir. Full path"""
        self.get_and_compare('/dir1/a.txt')
    
    def testGetMedium(self):
        """get a file medium sizedfrom an ADF"""
        self.get_and_compare('juggler_adnim.gif')
    
    def testInvalidOpen(self):
        """Open an invalid ADF file"""
        adf_filename = 'notanadf.bin'
        # now create a adf_filename file with bogus data in it
        adfobj = self.open()
        self.failIf(True)

    def testPut(self):
        """put a file into an ADF"""
        adf_filename = self.adf_testfilename
        adfobj = self.open()
        self.failIf(True)

    def testPutTooBig(self):
        """put a file into an ADF that is larger than the ADG size. I.e. test Disk Full"""
        adf_filename = self.adf_testfilename
        adfobj = self.open()
        self.failIf(True)

    def testRenameFile(self):
        """Rename a file from an ADF, use list to confirm"""
        adf_filename = self.adf_testfilename
        adfobj = self.open()
        # rename juggler_adnim.gif to juggler_anim.gif
        self.failIf(True)

    def testRenameNonExistent(self):
        """Rename a file that does not exist"""
        adf_filename = self.adf_testfilename
        adfobj = self.open()
        self.failIf(True)

    def testDelFile(self):
        """Delete a file from an ADF, use list to confirm"""
        adf_filename = self.adf_testfilename
        adfobj = self.open()
        self.failIf(True)

    def testDelDir(self):
        """Delete a(n empty) directory from an ADF, use list to confirm"""
        adf_filename = self.adf_testfilename
        adfobj = self.open()
        self.failIf(True)

    def testDelNonExistent(self):
        """Attempt to delete a file from an ADF that does not exist"""
        adf_filename = self.adf_testfilename
        adfobj = self.open()
        self.failIf(True)

    def testDelNonEmptyDir(self):
        """Attempt to delete a directory from an ADF that is not empty"""
        adf_filename = self.adf_testfilename
        adfobj = self.open()
        self.failIf(True)

    def testChangeDir(self):
        """Test various "cd" calls, use pwd to confirm expected"""
        adf_filename = self.adf_testfilename
        adfobj = self.open()
        self.failIf(True)

def main(argv=None):
    if argv is None:
        argv = sys.argv
    
    unittest.main()
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
