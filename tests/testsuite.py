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
from pyadf import Adf, AdfIOException, AdfVersionInfo, create_empty_adf


class PyadfTest(unittest.TestCase):
    
    def setUp(self):
        self.adf_canonfilename = 'pyadftest.adf'
        self.adf_testfilename = 'testsuite_pyadftest.adf'  # TODO use tempfile?
        self.adf_canonfilename = os.path.join(test_directory, 'data', self.adf_canonfilename )
        # move below into re-copy method?
        shutil.copy(self.adf_canonfilename, self.adf_testfilename)
        self._fileperms = stat.S_IWRITE|stat.S_IREAD
        os.chmod(self.adf_testfilename, self._fileperms)
        self.adfobj = None

    def open(self, adf_filename=None, mode='r'):
        adf_filename = adf_filename or self.adf_testfilename
        self.adfobj = Adf(adf_filename, mode=mode)
        return self.adfobj

    def tearDown(self):
        if self.adfobj:
            #del self.adfobj
            self.adfobj.close()
        if os.path.exists(self.adf_testfilename):
            # If adfobj has not been destroyed, unlink will fail under Windows (permssion denied. file in use)
            os.unlink(self.adf_testfilename)

    def testMissingOpen(self):
        """Open a missing ADF file"""
        adf_filename = 'doesnotexist.adf'
        def open_non_existent():
            adfobj = self.open(adf_filename)
        self.failIf(os.path.exists(adf_filename), '%r should not exist!'%adf_filename)
        self.failUnlessRaises(AdfIOException, open_non_existent)

    def list_and_compare(self, expect_result, adf_filename=None):
        """Directory listing from an ADF"""
        adf_filename = adf_filename or self.adf_testfilename
        adfobj = self.open(adf_filename)
        list_dir_res = adfobj.ls_dir()
        result = []
        for x in list_dir_res:
            # for now just tests names
            result.append(x.fname)
        expect_result.sort()
        result.sort()
        adfobj.close()
        self.failUnlessEqual(expect_result, result)
    
    def testListRoot(self):
        """Directory listing from an ADF"""
        expect_result = ['A Christmas Carol stave1 by Ch', 'unixtext.txt', 'read_file.py', 'juggler.png', 'wintext.txt', 'file with spaces.txt', 'juggler_adnim.gif', 'maximum_file_length_of_30.txt', 'AmigaLogo.iff', 'dir1', 'UPPERCASEDIR', 'readme.txt', 'MixedCaseDir']
        self.list_and_compare(expect_result)

    def get_datafile(self, filename):
        """get a data file from example directory"""
        canon_filename = os.path.join(test_directory, 'data', 'example_files', filename)
        f = open(canon_filename, 'rb')
        result = f.read()
        f.close()
        return result
    
    def get_and_compare(self, filename, filename_in_adf=None):
        """get a file from an ADF"""
        filename_in_adf = filename_in_adf or filename
        adf_filename = self.adf_testfilename
        adfobj = self.open()
        canon_filename = os.path.join(test_directory, 'data', 'example_files', filename)
        f = open(canon_filename, 'rb')
        expect_result = f.read()
        f.close()
        result = adfobj.get_file(filename_in_adf)
        adfobj.close()
        self.failUnlessEqual(expect_result, result)
    
    def testGetSmall(self):
        """get a file small sized from an ADF"""
        self.get_and_compare('unixtext.txt')
    
    def testGetSmallSubDir1(self):
        """get a file small sized from an ADF from a sub dir"""
        self.get_and_compare('dir1/a.txt')
    
    def testGetSmallSubDir2(self):
        """get a file small sized from an ADF from a sub dir. Full path"""
        self.get_and_compare('dir1/a.txt', '/dir1/a.txt')
    
    def testGetMedium(self):
        """get a binary file medium sized from an ADF"""
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
        adfobj = self.open(mode='w')
        data = self.get_datafile('A Christmas Carol stave1 by Charles Dickens.txt')
        adfobj.push_file('carols1.txt', data)
        adfobj.close()
        self.get_and_compare('A Christmas Carol stave1 by Charles Dickens.txt', 'carols1.txt')

    def testPutSmallUnix(self):
        """put a file into an ADF"""
        adf_filename = self.adf_testfilename
        testfilename = 'unixtext.txt'
        new_tmpfilename = 'tmpfile.tmp'
        adfobj = self.open(mode='w')
        data = self.get_datafile(testfilename)
        adfobj.push_file(new_tmpfilename, data)
        adfobj.close()
        self.get_and_compare(testfilename, new_tmpfilename)

    def testPutSmallWin(self):
        """put a file into an ADF"""
        adf_filename = self.adf_testfilename
        testfilename = 'wintext.txt'
        new_tmpfilename = 'tmpfile.tmp'
        adfobj = self.open(mode='w')
        data = self.get_datafile(testfilename)
        adfobj.push_file(new_tmpfilename, data)
        adfobj.close()
        self.get_and_compare(testfilename, new_tmpfilename)

    def testPutMediumBin(self):
        """put a file into an ADF"""
        adf_filename = self.adf_testfilename
        testfilename = 'juggler_adnim.gif'
        new_tmpfilename = 'tmpfile.tmp'
        adfobj = self.open(mode='w')
        data = self.get_datafile(testfilename)
        adfobj.push_file(new_tmpfilename, data)
        adfobj.close()
        self.get_and_compare(testfilename, new_tmpfilename)

    def testPutTooBig(self):
        """put a file into an ADF that is larger than the ADG size. I.e. test Disk Full"""
        self.failIf(True)  # adflib does not appear to error when fille is too big! Appears to be a bug in (c) ADFlib
        adf_filename = self.adf_testfilename
        testfilename = 'juggler_adnim.gif'
        new_tmpfilename = 'tmpfile.tmp'
        adfobj = self.open(mode='w')
        data = '*' * 901120  # size of a regular ADF image file so should be way too big
        adfobj.push_file(new_tmpfilename, data)
        adfobj.close()

    def testRenameFile(self):
        """Rename a file from an ADF, use list to confirm"""
        adf_filename = self.adf_testfilename
        adfobj = self.open(mode='w')
        adfobj.rename('juggler_adnim.gif', 'juggler_anim.gif')
        adfobj.close()
        expect_result = ['A Christmas Carol stave1 by Ch', 'unixtext.txt', 'read_file.py', 'juggler.png', 'wintext.txt', 'file with spaces.txt', 'juggler_anim.gif', 'maximum_file_length_of_30.txt', 'AmigaLogo.iff', 'dir1', 'UPPERCASEDIR', 'readme.txt', 'MixedCaseDir']
        self.list_and_compare(expect_result)
        ## TODO maybe get too as a sanity check?

    def testRenameReadOnlyMount(self):
        """Rename a file when adf opened in readonly mode"""
        adf_filename = self.adf_testfilename
        adfobj = self.open(mode='r')
        def do_rename():
            adfobj.rename('juggler_adnim.gif', 'juggler_anim.gif')
        self.failUnlessRaises(AdfIOException, do_rename)
        adfobj.close()
        expect_result = ['A Christmas Carol stave1 by Ch', 'unixtext.txt', 'read_file.py', 'juggler.png', 'wintext.txt', 'file with spaces.txt', 'juggler_adnim.gif', 'maximum_file_length_of_30.txt', 'AmigaLogo.iff', 'dir1', 'UPPERCASEDIR', 'readme.txt', 'MixedCaseDir']
        self.list_and_compare(expect_result)
        ## TODO maybe get too as a sanity check?

    def testRenameNonExistent(self):
        """Rename a file that does not exist"""
        adf_filename = self.adf_testfilename
        adfobj = self.open(mode='w')
        def do_rename():
            adfobj.rename('renamenotexist.gif', 'juggler_anim.gif')
        self.failUnlessRaises(AdfIOException, do_rename)
        adfobj.close()
        expect_result = ['A Christmas Carol stave1 by Ch', 'unixtext.txt', 'read_file.py', 'juggler.png', 'wintext.txt', 'file with spaces.txt', 'juggler_adnim.gif', 'maximum_file_length_of_30.txt', 'AmigaLogo.iff', 'dir1', 'UPPERCASEDIR', 'readme.txt', 'MixedCaseDir']
        self.list_and_compare(expect_result)
        ## TODO maybe get too as a sanity check?

    def testRenameInSub(self):
        """Rename a file that is in a subdirectory"""
        adf_filename = self.adf_testfilename
        adfobj = self.open()
        self.failIf(True)

    def testDelFile(self):
        """Delete a file from an ADF, use list to confirm"""
        file_to_delete = 'juggler_adnim.gif'
        adf_filename = self.adf_testfilename
        adfobj = self.open(mode='w')
        adfobj.unlink(file_to_delete)
        adfobj.close()
        expect_result = ['A Christmas Carol stave1 by Ch', 'unixtext.txt', 'read_file.py', 'juggler.png', 'wintext.txt', 'file with spaces.txt', 'juggler_adnim.gif', 'maximum_file_length_of_30.txt', 'AmigaLogo.iff', 'dir1', 'UPPERCASEDIR', 'readme.txt', 'MixedCaseDir']
        expect_result.remove(file_to_delete)
        self.list_and_compare(expect_result)
        ## TODO maybe get too as a sanity check?

    def testDelFileTwoAdfs(self):
        """Delete different files from different ADFs, use list to confirm"""
        mode = 'w'
        adf_filename1 = 'testsuite_pyadftest1.adf'
        file_to_delete1 = 'juggler_adnim.gif'
        shutil.copy(self.adf_canonfilename, adf_filename1)
        os.chmod(adf_filename1, self._fileperms)
        adfobj1 = Adf(adf_filename1, mode=mode)
        
        adf_filename2 = 'testsuite_pyadftest2.adf'
        file_to_delete2 = 'UPPERCASEDIR'
        shutil.copy(self.adf_canonfilename, adf_filename2)
        os.chmod(adf_filename2, self._fileperms)
        adfobj2 = Adf(adf_filename2, mode=mode)
        
        adfobj1.unlink(file_to_delete1)
        adfobj2.unlink(file_to_delete2)
        
        adfobj1.close()
        adfobj2.close()

        expect_result1 = ['A Christmas Carol stave1 by Ch', 'unixtext.txt', 'read_file.py', 'juggler.png', 'wintext.txt', 'file with spaces.txt', 'juggler_adnim.gif', 'maximum_file_length_of_30.txt', 'AmigaLogo.iff', 'dir1', 'UPPERCASEDIR', 'readme.txt', 'MixedCaseDir']
        expect_result1.remove(file_to_delete1)
        self.list_and_compare(expect_result1, adf_filename=adf_filename1)
        
        expect_result2 = ['A Christmas Carol stave1 by Ch', 'unixtext.txt', 'read_file.py', 'juggler.png', 'wintext.txt', 'file with spaces.txt', 'juggler_adnim.gif', 'maximum_file_length_of_30.txt', 'AmigaLogo.iff', 'dir1', 'UPPERCASEDIR', 'readme.txt', 'MixedCaseDir']
        expect_result2.remove(file_to_delete2)
        self.list_and_compare(expect_result2, adf_filename=adf_filename2)
        # remote temp adf files, NOTE if we get a failure cleanup here will not run
        os.unlink(adf_filename1)
        os.unlink(adf_filename2)




    def testDelDir(self):
        """Delete a(n empty) directory from an ADF, use list to confirm"""
        file_to_delete = 'UPPERCASEDIR'
        adf_filename = self.adf_testfilename
        adfobj = self.open(mode='w')
        adfobj.unlink(file_to_delete)
        adfobj.close()
        expect_result = ['A Christmas Carol stave1 by Ch', 'unixtext.txt', 'read_file.py', 'juggler.png', 'wintext.txt', 'file with spaces.txt', 'juggler_adnim.gif', 'maximum_file_length_of_30.txt', 'AmigaLogo.iff', 'dir1', 'UPPERCASEDIR', 'readme.txt', 'MixedCaseDir']
        expect_result.remove(file_to_delete)
        self.list_and_compare(expect_result)
        ## TODO maybe get too as a sanity check?

    def testDelNonExistent(self):
        """Attempt to delete a file from an ADF that does not exist"""
        adf_filename = self.adf_testfilename
        adfobj = self.open(mode='w')
        def do_del():
            adfobj.unlink('doesnotexist.gif')
        self.failUnlessRaises(AdfIOException, do_del)
        adfobj.close()
        # consider simply calling testListRoot
        expect_result = ['A Christmas Carol stave1 by Ch', 'unixtext.txt', 'read_file.py', 'juggler.png', 'wintext.txt', 'file with spaces.txt', 'juggler_adnim.gif', 'maximum_file_length_of_30.txt', 'AmigaLogo.iff', 'dir1', 'UPPERCASEDIR', 'readme.txt', 'MixedCaseDir']
        self.list_and_compare(expect_result)

    def testDelNonEmptyDir(self):
        """Attempt to delete a directory from an ADF that is not empty"""
        file_to_delete = 'dir1'
        adf_filename = self.adf_testfilename
        adfobj = self.open(mode='w')
        def do_del():
            adfobj.unlink(file_to_delete)
        self.failUnlessRaises(AdfIOException, do_del)
        adfobj.close()
        # consider simply calling testListRoot
        expect_result = ['A Christmas Carol stave1 by Ch', 'unixtext.txt', 'read_file.py', 'juggler.png', 'wintext.txt', 'file with spaces.txt', 'juggler_adnim.gif', 'maximum_file_length_of_30.txt', 'AmigaLogo.iff', 'dir1', 'UPPERCASEDIR', 'readme.txt', 'MixedCaseDir']
        self.list_and_compare(expect_result)

    def testMakeDir(self):
        """Test various create directory call(s)"""
        adf_filename = self.adf_testfilename
        adfobj = self.open()
        self.failIf(True)

    def testChangeDir(self):
        """Test various "cd" calls, use pwd to confirm expected"""
        adf_filename = self.adf_testfilename
        adfobj = self.open()
        self.failIf(True)

    def testCreateEmptyAdf(self):
        """Create a new ADF file that is empty"""
        adf_filename = self.adf_testfilename
        os.unlink(self.adf_testfilename)
        self.failIf(os.path.exists(adf_filename), '%r should not exist!'%adf_filename)
        create_empty_adf(adf_filename)
        expect_result = []
        self.list_and_compare(expect_result)
        # TODO add new test; check volume name)

    def testCreateAlreadyExistsAdf(self):
        """Attempt to create a new ADF file when file already exists"""
        adf_filename = self.adf_testfilename
        self.failIf(not os.path.exists(adf_filename), '%r should exist!'%adf_filename)
        def do_task():
            create_empty_adf(adf_filename)
        self.failUnlessRaises(AdfIOException, do_task)
        
    def testCreateAdfPutSmallUnix(self):
        """create blank adf, put a file into an ADF"""
        adf_filename = self.adf_testfilename
        os.unlink(self.adf_testfilename)
        self.failIf(os.path.exists(adf_filename), '%r should not exist!'%adf_filename)
        create_empty_adf(adf_filename)
        testfilename = 'unixtext.txt'
        new_tmpfilename = 'tmpfile.tmp'
        adfobj = self.open(mode='w')
        data = self.get_datafile(testfilename)
        adfobj.push_file(new_tmpfilename, data)
        adfobj.close()
        # check contents
        self.get_and_compare(testfilename, new_tmpfilename)
        expect_result = [new_tmpfilename]
        # check directory listing
        self.list_and_compare(expect_result)


def main(argv=None):
    if argv is None:
        argv = sys.argv
    
    unittest.main()
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
