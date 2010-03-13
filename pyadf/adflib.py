'''Wrapper for adflib.h

Generated with:
D:\documents\drive_f_share\python\ctypesgen\ctypesgen.py -l adflib -o adflib.py adflib.h --save-preprocessed-headers=mytmp.h -a

Do not modify this file.
'''

__docformat__ =  'restructuredtext'

# Begin preamble

import ctypes, os, sys
from ctypes import *

_int_types = (c_int16, c_int32)
if hasattr(ctypes, 'c_int64'):
    # Some builds of ctypes apparently do not have c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (c_int64,)
for t in _int_types:
    if sizeof(t) == sizeof(c_size_t):
        c_ptrdiff_t = t
del t
del _int_types

class c_void(Structure):
    # c_void_p is a buggy return type, converting to int, so
    # POINTER(None) == c_void_p is actually written as
    # POINTER(c_void), so it can be treated as a real pointer.
    _fields_ = [('dummy', c_int)]

def POINTER(obj):
    p = ctypes.POINTER(obj)

    # Convert None to a real NULL pointer to work around bugs
    # in how ctypes handles None on 64-bit platforms
    if not isinstance(p.from_param, classmethod):
        def from_param(cls, x):
            if x is None:
                return cls()
            else:
                return x
        p.from_param = classmethod(from_param)

    return p

class UserString:
    def __init__(self, seq):
        if isinstance(seq, basestring):
            self.data = seq
        elif isinstance(seq, UserString):
            self.data = seq.data[:]
        else:
            self.data = str(seq)
    def __str__(self): return str(self.data)
    def __repr__(self): return repr(self.data)
    def __int__(self): return int(self.data)
    def __long__(self): return long(self.data)
    def __float__(self): return float(self.data)
    def __complex__(self): return complex(self.data)
    def __hash__(self): return hash(self.data)

    def __cmp__(self, string):
        if isinstance(string, UserString):
            return cmp(self.data, string.data)
        else:
            return cmp(self.data, string)
    def __contains__(self, char):
        return char in self.data

    def __len__(self): return len(self.data)
    def __getitem__(self, index): return self.__class__(self.data[index])
    def __getslice__(self, start, end):
        start = max(start, 0); end = max(end, 0)
        return self.__class__(self.data[start:end])

    def __add__(self, other):
        if isinstance(other, UserString):
            return self.__class__(self.data + other.data)
        elif isinstance(other, basestring):
            return self.__class__(self.data + other)
        else:
            return self.__class__(self.data + str(other))
    def __radd__(self, other):
        if isinstance(other, basestring):
            return self.__class__(other + self.data)
        else:
            return self.__class__(str(other) + self.data)
    def __mul__(self, n):
        return self.__class__(self.data*n)
    __rmul__ = __mul__
    def __mod__(self, args):
        return self.__class__(self.data % args)

    # the following methods are defined in alphabetical order:
    def capitalize(self): return self.__class__(self.data.capitalize())
    def center(self, width, *args):
        return self.__class__(self.data.center(width, *args))
    def count(self, sub, start=0, end=sys.maxint):
        return self.data.count(sub, start, end)
    def decode(self, encoding=None, errors=None): # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.decode(encoding, errors))
            else:
                return self.__class__(self.data.decode(encoding))
        else:
            return self.__class__(self.data.decode())
    def encode(self, encoding=None, errors=None): # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.encode(encoding, errors))
            else:
                return self.__class__(self.data.encode(encoding))
        else:
            return self.__class__(self.data.encode())
    def endswith(self, suffix, start=0, end=sys.maxint):
        return self.data.endswith(suffix, start, end)
    def expandtabs(self, tabsize=8):
        return self.__class__(self.data.expandtabs(tabsize))
    def find(self, sub, start=0, end=sys.maxint):
        return self.data.find(sub, start, end)
    def index(self, sub, start=0, end=sys.maxint):
        return self.data.index(sub, start, end)
    def isalpha(self): return self.data.isalpha()
    def isalnum(self): return self.data.isalnum()
    def isdecimal(self): return self.data.isdecimal()
    def isdigit(self): return self.data.isdigit()
    def islower(self): return self.data.islower()
    def isnumeric(self): return self.data.isnumeric()
    def isspace(self): return self.data.isspace()
    def istitle(self): return self.data.istitle()
    def isupper(self): return self.data.isupper()
    def join(self, seq): return self.data.join(seq)
    def ljust(self, width, *args):
        return self.__class__(self.data.ljust(width, *args))
    def lower(self): return self.__class__(self.data.lower())
    def lstrip(self, chars=None): return self.__class__(self.data.lstrip(chars))
    def partition(self, sep):
        return self.data.partition(sep)
    def replace(self, old, new, maxsplit=-1):
        return self.__class__(self.data.replace(old, new, maxsplit))
    def rfind(self, sub, start=0, end=sys.maxint):
        return self.data.rfind(sub, start, end)
    def rindex(self, sub, start=0, end=sys.maxint):
        return self.data.rindex(sub, start, end)
    def rjust(self, width, *args):
        return self.__class__(self.data.rjust(width, *args))
    def rpartition(self, sep):
        return self.data.rpartition(sep)
    def rstrip(self, chars=None): return self.__class__(self.data.rstrip(chars))
    def split(self, sep=None, maxsplit=-1):
        return self.data.split(sep, maxsplit)
    def rsplit(self, sep=None, maxsplit=-1):
        return self.data.rsplit(sep, maxsplit)
    def splitlines(self, keepends=0): return self.data.splitlines(keepends)
    def startswith(self, prefix, start=0, end=sys.maxint):
        return self.data.startswith(prefix, start, end)
    def strip(self, chars=None): return self.__class__(self.data.strip(chars))
    def swapcase(self): return self.__class__(self.data.swapcase())
    def title(self): return self.__class__(self.data.title())
    def translate(self, *args):
        return self.__class__(self.data.translate(*args))
    def upper(self): return self.__class__(self.data.upper())
    def zfill(self, width): return self.__class__(self.data.zfill(width))

class MutableString(UserString):
    """mutable string objects

    Python strings are immutable objects.  This has the advantage, that
    strings may be used as dictionary keys.  If this property isn't needed
    and you insist on changing string values in place instead, you may cheat
    and use MutableString.

    But the purpose of this class is an educational one: to prevent
    people from inventing their own mutable string class derived
    from UserString and than forget thereby to remove (override) the
    __hash__ method inherited from UserString.  This would lead to
    errors that would be very hard to track down.

    A faster and better solution is to rewrite your program using lists."""
    def __init__(self, string=""):
        self.data = string
    def __hash__(self):
        raise TypeError("unhashable type (it is mutable)")
    def __setitem__(self, index, sub):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data): raise IndexError
        self.data = self.data[:index] + sub + self.data[index+1:]
    def __delitem__(self, index):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data): raise IndexError
        self.data = self.data[:index] + self.data[index+1:]
    def __setslice__(self, start, end, sub):
        start = max(start, 0); end = max(end, 0)
        if isinstance(sub, UserString):
            self.data = self.data[:start]+sub.data+self.data[end:]
        elif isinstance(sub, basestring):
            self.data = self.data[:start]+sub+self.data[end:]
        else:
            self.data =  self.data[:start]+str(sub)+self.data[end:]
    def __delslice__(self, start, end):
        start = max(start, 0); end = max(end, 0)
        self.data = self.data[:start] + self.data[end:]
    def immutable(self):
        return UserString(self.data)
    def __iadd__(self, other):
        if isinstance(other, UserString):
            self.data += other.data
        elif isinstance(other, basestring):
            self.data += other
        else:
            self.data += str(other)
        return self
    def __imul__(self, n):
        self.data *= n
        return self

class String(MutableString, Union):

    _fields_ = [('raw', POINTER(c_char)),
                ('data', c_char_p)]

    def __init__(self, obj=""):
        if isinstance(obj, (str, unicode, UserString)):
            self.data = str(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0
    
    def from_param(cls, obj):
        # Convert None or 0
        if obj is None or obj == 0:
            return cls(POINTER(c_char)())

        # Convert from String
        elif isinstance(obj, String):
            return obj

        # Convert from str
        elif isinstance(obj, str):
            return cls(obj)
        
        # Convert from c_char_p
        elif isinstance(obj, c_char_p):
            return obj
        
        # Convert from POINTER(c_char)
        elif isinstance(obj, POINTER(c_char)):
            return obj
        
        # Convert from raw pointer
        elif isinstance(obj, int):
            return cls(cast(obj, POINTER(c_char)))

        # Convert from object
        else:
            return String.from_param(obj._as_parameter_)
    from_param = classmethod(from_param)

def ReturnString(obj, func, arguments):
    return String.from_param(obj)

# As of ctypes 1.0, ctypes does not support custom error-checking
# functions on callbacks, nor does it support custom datatypes on
# callbacks, so we must ensure that all callbacks return
# primitive datatypes.
#
# Non-primitive return values wrapped with UNCHECKED won't be
# typechecked, and will be converted to c_void_p.
def UNCHECKED(type):
    if (hasattr(type, "_type_") and isinstance(type._type_, str)
        and type._type_ != "P"):
        return type
    else:
        return c_void_p

# ctypes doesn't have direct support for variadic functions, so we have to write
# our own wrapper class
class _variadic_function(object):
    def __init__(self,func,restype,argtypes):
        self.func=func
        self.func.restype=restype
        self.argtypes=argtypes
    def _as_parameter_(self):
        # So we can pass this variadic function as a function pointer
        return self.func
    def __call__(self,*args):
        fixed_args=[]
        i=0
        for argtype in self.argtypes:
            # Typecheck what we can
            fixed_args.append(argtype.from_param(args[i]))
            i+=1
        return self.func(*fixed_args+list(args[i:]))


# End preamble

_libs = {}
_libdirs = []

# Begin loader

# ----------------------------------------------------------------------------
# Copyright (c) 2008 David James
# Copyright (c) 2006-2008 Alex Holkner
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions 
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright 
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

import os.path, re, sys, glob
import ctypes
import ctypes.util

def _environ_path(name):
    if name in os.environ:
        return os.environ[name].split(":")
    else:
        return []

class LibraryLoader(object):
    def __init__(self):
        self.other_dirs=[]
    
    def load_library(self,libname):
        """Given the name of a library, load it."""
        paths = self.getpaths(libname)
        
        for path in paths:
            if os.path.exists(path):
                return self.load(path)
        
        raise ImportError("%s not found." % libname)
    
    def load(self,path):
        """Given a path to a library, load it."""
        try:
            # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead
            # of the default RTLD_LOCAL.  Without this, you end up with
            # libraries not being loadable, resulting in "Symbol not found"
            # errors
            if sys.platform == 'darwin':
                return ctypes.CDLL(path, ctypes.RTLD_GLOBAL)
            else:
                return ctypes.cdll.LoadLibrary(path)
        except OSError,e:
            raise ImportError(e)
    
    def getpaths(self,libname):
        """Return a list of paths where the library might be found."""
        if os.path.isabs(libname):
            yield libname
        
        else:
            for path in self.getplatformpaths(libname):
                yield path
            
            path = ctypes.util.find_library(libname)
            if path: yield path
    
    def getplatformpaths(self, libname):
        return []

# Darwin (Mac OS X)

class DarwinLibraryLoader(LibraryLoader):
    name_formats = ["lib%s.dylib", "lib%s.so", "lib%s.bundle", "%s.dylib",
                "%s.so", "%s.bundle", "%s"]
    
    def getplatformpaths(self,libname):
        if os.path.pathsep in libname:
            names = [libname]
        else:
            names = [format % libname for format in self.name_formats]
        
        for dir in self.getdirs(libname):
            for name in names:
                yield os.path.join(dir,name)
    
    def getdirs(self,libname):
        '''Implements the dylib search as specified in Apple documentation:
        
        http://developer.apple.com/documentation/DeveloperTools/Conceptual/
            DynamicLibraries/Articles/DynamicLibraryUsageGuidelines.html

        Before commencing the standard search, the method first checks
        the bundle's ``Frameworks`` directory if the application is running
        within a bundle (OS X .app).
        '''

        dyld_fallback_library_path = _environ_path("DYLD_FALLBACK_LIBRARY_PATH")
        if not dyld_fallback_library_path:
            dyld_fallback_library_path = [os.path.expanduser('~/lib'),
                                          '/usr/local/lib', '/usr/lib']
        
        dirs = []
        
        if '/' in libname:
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
        else:
            dirs.extend(_environ_path("LD_LIBRARY_PATH"))
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))

        dirs.extend(self.other_dirs)
        dirs.append(".")
        
        if hasattr(sys, 'frozen') and sys.frozen == 'macosx_app':
            dirs.append(os.path.join(
                os.environ['RESOURCEPATH'],
                '..',
                'Frameworks'))

        dirs.extend(dyld_fallback_library_path)
        
        return dirs

# Posix

class PosixLibraryLoader(LibraryLoader):
    _ld_so_cache = None
    
    def _create_ld_so_cache(self):
        # Recreate search path followed by ld.so.  This is going to be
        # slow to build, and incorrect (ld.so uses ld.so.cache, which may
        # not be up-to-date).  Used only as fallback for distros without
        # /sbin/ldconfig.
        #
        # We assume the DT_RPATH and DT_RUNPATH binary sections are omitted.

        directories = []
        for name in ("LD_LIBRARY_PATH",
                     "SHLIB_PATH", # HPUX
                     "LIBPATH", # OS/2, AIX
                     "LIBRARY_PATH", # BE/OS
                    ):
            if name in os.environ:
                directories.extend(os.environ[name].split(os.pathsep))
        directories.extend(self.other_dirs)
        directories.append(".")

        try: directories.extend([dir.strip() for dir in open('/etc/ld.so.conf')])
        except IOError: pass

        directories.extend(['/lib', '/usr/lib', '/lib64', '/usr/lib64'])

        cache = {}
        lib_re = re.compile(r'lib(.*)\.s[ol]')
        ext_re = re.compile(r'\.s[ol]$')
        for dir in directories:
            try:
                for path in glob.glob("%s/*.s[ol]*" % dir):
                    file = os.path.basename(path)

                    # Index by filename
                    if file not in cache:
                        cache[file] = path
                    
                    # Index by library name
                    match = lib_re.match(file)
                    if match:
                        library = match.group(1)
                        if library not in cache:
                            cache[library] = path
            except OSError:
                pass

        self._ld_so_cache = cache
    
    def getplatformpaths(self, libname):
        if self._ld_so_cache is None:
            self._create_ld_so_cache()

        result = self._ld_so_cache.get(libname)
        if result: yield result

        path = ctypes.util.find_library(libname)
        if path: yield os.path.join("/lib",path)

# Windows

class _WindowsLibrary(object):
    def __init__(self, path):
        self.cdll = ctypes.cdll.LoadLibrary(path)
        self.windll = ctypes.windll.LoadLibrary(path)

    def __getattr__(self, name):
        try: return getattr(self.cdll,name)
        except AttributeError:
            try: return getattr(self.windll,name)
            except AttributeError:
                raise

class WindowsLibraryLoader(LibraryLoader):
    name_formats = ["%s.dll", "lib%s.dll"]
    
    def load_library(self, libname):
        try:
            result = LibraryLoader.load_library(self, libname)
        except ImportError:
            try:
                result = getattr(ctypes.cdll, libname)
            except WindowsError:
                raise ImportError("%s not found." % libname)
        return result
    
    def load(self, path):
        return _WindowsLibrary(path)
    
    def getplatformpaths(self, libname):
        if os.path.sep not in libname:
            for name in self.name_formats:
                path = ctypes.util.find_library(name % libname)
                if path:
                    yield path

# Platform switching

# If your value of sys.platform does not appear in this dict, please contact
# the Ctypesgen maintainers.

loaderclass = {
    "darwin":   DarwinLibraryLoader,
    "cygwin":   WindowsLibraryLoader,
    "win32":    WindowsLibraryLoader
}

loader = loaderclass.get(sys.platform, PosixLibraryLoader)()

def add_library_search_dirs(other_dirs):
    loader.other_dirs = other_dirs

load_library = loader.load_library

del loaderclass

# End loader

add_library_search_dirs([])

# Begin libraries

_libs["adflib"] = load_library("adflib")

# 1 libraries
# End libraries

# No modules

wint_t = c_uint # J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/include/stddef.h: 354

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 139
class struct__iobuf(Structure):
    pass

struct__iobuf.__slots__ = [
    '_ptr',
    '_cnt',
    '_base',
    '_flag',
    '_file',
    '_charbuf',
    '_bufsiz',
    '_tmpfname',
]
struct__iobuf._fields_ = [
    ('_ptr', String),
    ('_cnt', c_int),
    ('_base', String),
    ('_flag', c_int),
    ('_file', c_int),
    ('_charbuf', c_int),
    ('_bufsiz', c_int),
    ('_tmpfname', String),
]

FILE = struct__iobuf # J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 139

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 154
for _lib in _libs.values():
    try:
        _iob = (POINTER(FILE)).in_dll(_lib, '_iob')
        break
    except:
        pass

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 169
for _lib in _libs.values():
    if hasattr(_lib, 'fopen'):
        fopen = _lib.fopen
        fopen.restype = POINTER(FILE)
        fopen.argtypes = [String, String]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 170
for _lib in _libs.values():
    if hasattr(_lib, 'freopen'):
        freopen = _lib.freopen
        freopen.restype = POINTER(FILE)
        freopen.argtypes = [String, String, POINTER(FILE)]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 171
for _lib in _libs.values():
    if hasattr(_lib, 'fflush'):
        fflush = _lib.fflush
        fflush.restype = c_int
        fflush.argtypes = [POINTER(FILE)]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 172
for _lib in _libs.values():
    if hasattr(_lib, 'fclose'):
        fclose = _lib.fclose
        fclose.restype = c_int
        fclose.argtypes = [POINTER(FILE)]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 174
for _lib in _libs.values():
    if hasattr(_lib, 'remove'):
        remove = _lib.remove
        remove.restype = c_int
        remove.argtypes = [String]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 175
for _lib in _libs.values():
    if hasattr(_lib, 'rename'):
        rename = _lib.rename
        rename.restype = c_int
        rename.argtypes = [String, String]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 176
for _lib in _libs.values():
    if hasattr(_lib, 'tmpfile'):
        tmpfile = _lib.tmpfile
        tmpfile.restype = POINTER(FILE)
        tmpfile.argtypes = []
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 177
for _lib in _libs.values():
    if hasattr(_lib, 'tmpnam'):
        tmpnam = _lib.tmpnam
        tmpnam.restype = String
        tmpnam.argtypes = [String]
        tmpnam.errcheck = ReturnString
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 180
for _lib in _libs.values():
    if hasattr(_lib, '_tempnam'):
        _tempnam = _lib._tempnam
        _tempnam.restype = String
        _tempnam.argtypes = [String, String]
        _tempnam.errcheck = ReturnString
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 181
for _lib in _libs.values():
    if hasattr(_lib, '_rmtmp'):
        _rmtmp = _lib._rmtmp
        _rmtmp.restype = c_int
        _rmtmp.argtypes = []
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 182
for _lib in _libs.values():
    if hasattr(_lib, '_unlink'):
        _unlink = _lib._unlink
        _unlink.restype = c_int
        _unlink.argtypes = [String]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 185
for _lib in _libs.values():
    if hasattr(_lib, 'tempnam'):
        tempnam = _lib.tempnam
        tempnam.restype = String
        tempnam.argtypes = [String, String]
        tempnam.errcheck = ReturnString
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 186
for _lib in _libs.values():
    if hasattr(_lib, 'rmtmp'):
        rmtmp = _lib.rmtmp
        rmtmp.restype = c_int
        rmtmp.argtypes = []
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 187
for _lib in _libs.values():
    if hasattr(_lib, 'unlink'):
        unlink = _lib.unlink
        unlink.restype = c_int
        unlink.argtypes = [String]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 191
for _lib in _libs.values():
    if hasattr(_lib, 'setvbuf'):
        setvbuf = _lib.setvbuf
        setvbuf.restype = c_int
        setvbuf.argtypes = [POINTER(FILE), String, c_int, c_size_t]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 193
for _lib in _libs.values():
    if hasattr(_lib, 'setbuf'):
        setbuf = _lib.setbuf
        setbuf.restype = None
        setbuf.argtypes = [POINTER(FILE), String]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 204
for _lib in _libs.values():
    if hasattr(_lib, '__mingw_fprintf'):
        _func = _lib.__mingw_fprintf
        _restype = c_int
        _argtypes = [POINTER(FILE), String]
        __mingw_fprintf = _variadic_function(_func,_restype,_argtypes)

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 205
for _lib in _libs.values():
    if hasattr(_lib, '__mingw_printf'):
        _func = _lib.__mingw_printf
        _restype = c_int
        _argtypes = [String]
        __mingw_printf = _variadic_function(_func,_restype,_argtypes)

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 206
for _lib in _libs.values():
    if hasattr(_lib, '__mingw_sprintf'):
        _func = _lib.__mingw_sprintf
        _restype = c_int
        _argtypes = [String, String]
        __mingw_sprintf = _variadic_function(_func,_restype,_argtypes)

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 207
for _lib in _libs.values():
    if hasattr(_lib, '__mingw_snprintf'):
        _func = _lib.__mingw_snprintf
        _restype = c_int
        _argtypes = [String, c_size_t, String]
        __mingw_snprintf = _variadic_function(_func,_restype,_argtypes)

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 208
for _lib in _libs.values():
    if hasattr(_lib, '__mingw_vfprintf'):
        __mingw_vfprintf = _lib.__mingw_vfprintf
        __mingw_vfprintf.restype = c_int
        __mingw_vfprintf.argtypes = [POINTER(FILE), String, String]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 209
for _lib in _libs.values():
    if hasattr(_lib, '__mingw_vprintf'):
        __mingw_vprintf = _lib.__mingw_vprintf
        __mingw_vprintf.restype = c_int
        __mingw_vprintf.argtypes = [String, String]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 210
for _lib in _libs.values():
    if hasattr(_lib, '__mingw_vsprintf'):
        __mingw_vsprintf = _lib.__mingw_vsprintf
        __mingw_vsprintf.restype = c_int
        __mingw_vsprintf.argtypes = [String, String, String]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 211
for _lib in _libs.values():
    if hasattr(_lib, '__mingw_vsnprintf'):
        __mingw_vsnprintf = _lib.__mingw_vsnprintf
        __mingw_vsnprintf.restype = c_int
        __mingw_vsnprintf.argtypes = [String, c_size_t, String, String]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 293
for _lib in _libs.values():
    if hasattr(_lib, 'fprintf'):
        _func = _lib.fprintf
        _restype = c_int
        _argtypes = [POINTER(FILE), String]
        fprintf = _variadic_function(_func,_restype,_argtypes)

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 294
for _lib in _libs.values():
    if hasattr(_lib, 'printf'):
        _func = _lib.printf
        _restype = c_int
        _argtypes = [String]
        printf = _variadic_function(_func,_restype,_argtypes)

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 295
for _lib in _libs.values():
    if hasattr(_lib, 'sprintf'):
        _func = _lib.sprintf
        _restype = c_int
        _argtypes = [String, String]
        sprintf = _variadic_function(_func,_restype,_argtypes)

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 296
for _lib in _libs.values():
    if hasattr(_lib, 'vfprintf'):
        vfprintf = _lib.vfprintf
        vfprintf.restype = c_int
        vfprintf.argtypes = [POINTER(FILE), String, String]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 297
for _lib in _libs.values():
    if hasattr(_lib, 'vprintf'):
        vprintf = _lib.vprintf
        vprintf.restype = c_int
        vprintf.argtypes = [String, String]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 298
for _lib in _libs.values():
    if hasattr(_lib, 'vsprintf'):
        vsprintf = _lib.vsprintf
        vsprintf.restype = c_int
        vsprintf.argtypes = [String, String, String]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 308
for _lib in _libs.values():
    if hasattr(_lib, '__msvcrt_fprintf'):
        _func = _lib.__msvcrt_fprintf
        _restype = c_int
        _argtypes = [POINTER(FILE), String]
        __msvcrt_fprintf = _variadic_function(_func,_restype,_argtypes)

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 309
for _lib in _libs.values():
    if hasattr(_lib, '__msvcrt_printf'):
        _func = _lib.__msvcrt_printf
        _restype = c_int
        _argtypes = [String]
        __msvcrt_printf = _variadic_function(_func,_restype,_argtypes)

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 310
for _lib in _libs.values():
    if hasattr(_lib, '__msvcrt_sprintf'):
        _func = _lib.__msvcrt_sprintf
        _restype = c_int
        _argtypes = [String, String]
        __msvcrt_sprintf = _variadic_function(_func,_restype,_argtypes)

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 311
for _lib in _libs.values():
    if hasattr(_lib, '__msvcrt_vfprintf'):
        __msvcrt_vfprintf = _lib.__msvcrt_vfprintf
        __msvcrt_vfprintf.restype = c_int
        __msvcrt_vfprintf.argtypes = [POINTER(FILE), String, String]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 312
for _lib in _libs.values():
    if hasattr(_lib, '__msvcrt_vprintf'):
        __msvcrt_vprintf = _lib.__msvcrt_vprintf
        __msvcrt_vprintf.restype = c_int
        __msvcrt_vprintf.argtypes = [String, String]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 313
for _lib in _libs.values():
    if hasattr(_lib, '__msvcrt_vsprintf'):
        __msvcrt_vsprintf = _lib.__msvcrt_vsprintf
        __msvcrt_vsprintf.restype = c_int
        __msvcrt_vsprintf.argtypes = [String, String, String]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 319
for _lib in _libs.values():
    if hasattr(_lib, '_snprintf'):
        _func = _lib._snprintf
        _restype = c_int
        _argtypes = [String, c_size_t, String]
        _snprintf = _variadic_function(_func,_restype,_argtypes)

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 320
for _lib in _libs.values():
    if hasattr(_lib, '_vsnprintf'):
        _vsnprintf = _lib._vsnprintf
        _vsnprintf.restype = c_int
        _vsnprintf.argtypes = [String, c_size_t, String, String]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 330
for _lib in _libs.values():
    if hasattr(_lib, 'snprintf'):
        _func = _lib.snprintf
        _restype = c_int
        _argtypes = [String, c_size_t, String]
        snprintf = _variadic_function(_func,_restype,_argtypes)

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 331
for _lib in _libs.values():
    if hasattr(_lib, 'vsnprintf'):
        vsnprintf = _lib.vsnprintf
        vsnprintf.restype = c_int
        vsnprintf.argtypes = [String, c_size_t, String, String]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 333
for _lib in _libs.values():
    if hasattr(_lib, 'vscanf'):
        vscanf = _lib.vscanf
        vscanf.restype = c_int
        vscanf.argtypes = [String, String]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 334
for _lib in _libs.values():
    if hasattr(_lib, 'vfscanf'):
        vfscanf = _lib.vfscanf
        vfscanf.restype = c_int
        vfscanf.argtypes = [POINTER(FILE), String, String]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 336
for _lib in _libs.values():
    if hasattr(_lib, 'vsscanf'):
        vsscanf = _lib.vsscanf
        vsscanf.restype = c_int
        vsscanf.argtypes = [String, String, String]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 345
for _lib in _libs.values():
    if hasattr(_lib, 'fscanf'):
        _func = _lib.fscanf
        _restype = c_int
        _argtypes = [POINTER(FILE), String]
        fscanf = _variadic_function(_func,_restype,_argtypes)

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 346
for _lib in _libs.values():
    if hasattr(_lib, 'scanf'):
        _func = _lib.scanf
        _restype = c_int
        _argtypes = [String]
        scanf = _variadic_function(_func,_restype,_argtypes)

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 347
for _lib in _libs.values():
    if hasattr(_lib, 'sscanf'):
        _func = _lib.sscanf
        _restype = c_int
        _argtypes = [String, String]
        sscanf = _variadic_function(_func,_restype,_argtypes)

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 352
for _lib in _libs.values():
    if hasattr(_lib, 'fgetc'):
        fgetc = _lib.fgetc
        fgetc.restype = c_int
        fgetc.argtypes = [POINTER(FILE)]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 353
for _lib in _libs.values():
    if hasattr(_lib, 'fgets'):
        fgets = _lib.fgets
        fgets.restype = String
        fgets.argtypes = [String, c_int, POINTER(FILE)]
        fgets.errcheck = ReturnString
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 354
for _lib in _libs.values():
    if hasattr(_lib, 'fputc'):
        fputc = _lib.fputc
        fputc.restype = c_int
        fputc.argtypes = [c_int, POINTER(FILE)]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 355
for _lib in _libs.values():
    if hasattr(_lib, 'fputs'):
        fputs = _lib.fputs
        fputs.restype = c_int
        fputs.argtypes = [String, POINTER(FILE)]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 356
for _lib in _libs.values():
    if hasattr(_lib, 'gets'):
        gets = _lib.gets
        gets.restype = String
        gets.argtypes = [String]
        gets.errcheck = ReturnString
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 357
for _lib in _libs.values():
    if hasattr(_lib, 'puts'):
        puts = _lib.puts
        puts.restype = c_int
        puts.argtypes = [String]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 358
for _lib in _libs.values():
    if hasattr(_lib, 'ungetc'):
        ungetc = _lib.ungetc
        ungetc.restype = c_int
        ungetc.argtypes = [c_int, POINTER(FILE)]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 366
for _lib in _libs.values():
    if hasattr(_lib, '_filbuf'):
        _filbuf = _lib._filbuf
        _filbuf.restype = c_int
        _filbuf.argtypes = [POINTER(FILE)]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 367
for _lib in _libs.values():
    if hasattr(_lib, '_flsbuf'):
        _flsbuf = _lib._flsbuf
        _flsbuf.restype = c_int
        _flsbuf.argtypes = [c_int, POINTER(FILE)]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 411
for _lib in _libs.values():
    if hasattr(_lib, 'fread'):
        fread = _lib.fread
        fread.restype = c_size_t
        fread.argtypes = [POINTER(None), c_size_t, c_size_t, POINTER(FILE)]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 412
for _lib in _libs.values():
    if hasattr(_lib, 'fwrite'):
        fwrite = _lib.fwrite
        fwrite.restype = c_size_t
        fwrite.argtypes = [POINTER(None), c_size_t, c_size_t, POINTER(FILE)]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 418
for _lib in _libs.values():
    if hasattr(_lib, 'fseek'):
        fseek = _lib.fseek
        fseek.restype = c_int
        fseek.argtypes = [POINTER(FILE), c_long, c_int]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 419
for _lib in _libs.values():
    if hasattr(_lib, 'ftell'):
        ftell = _lib.ftell
        ftell.restype = c_long
        ftell.argtypes = [POINTER(FILE)]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 420
for _lib in _libs.values():
    if hasattr(_lib, 'rewind'):
        rewind = _lib.rewind
        rewind.restype = None
        rewind.argtypes = [POINTER(FILE)]
        break

fpos_t = c_longlong # J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 454

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 459
for _lib in _libs.values():
    if hasattr(_lib, 'fgetpos'):
        fgetpos = _lib.fgetpos
        fgetpos.restype = c_int
        fgetpos.argtypes = [POINTER(FILE), POINTER(fpos_t)]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 460
for _lib in _libs.values():
    if hasattr(_lib, 'fsetpos'):
        fsetpos = _lib.fsetpos
        fsetpos.restype = c_int
        fsetpos.argtypes = [POINTER(FILE), POINTER(fpos_t)]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 466
for _lib in _libs.values():
    if hasattr(_lib, 'feof'):
        feof = _lib.feof
        feof.restype = c_int
        feof.argtypes = [POINTER(FILE)]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 467
for _lib in _libs.values():
    if hasattr(_lib, 'ferror'):
        ferror = _lib.ferror
        ferror.restype = c_int
        ferror.argtypes = [POINTER(FILE)]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 479
for _lib in _libs.values():
    if hasattr(_lib, 'clearerr'):
        clearerr = _lib.clearerr
        clearerr.restype = None
        clearerr.argtypes = [POINTER(FILE)]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 480
for _lib in _libs.values():
    if hasattr(_lib, 'perror'):
        perror = _lib.perror
        perror.restype = None
        perror.argtypes = [String]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 487
for _lib in _libs.values():
    if hasattr(_lib, '_popen'):
        _popen = _lib._popen
        _popen.restype = POINTER(FILE)
        _popen.argtypes = [String, String]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 488
for _lib in _libs.values():
    if hasattr(_lib, '_pclose'):
        _pclose = _lib._pclose
        _pclose.restype = c_int
        _pclose.argtypes = [POINTER(FILE)]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 491
for _lib in _libs.values():
    if hasattr(_lib, 'popen'):
        popen = _lib.popen
        popen.restype = POINTER(FILE)
        popen.argtypes = [String, String]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 492
for _lib in _libs.values():
    if hasattr(_lib, 'pclose'):
        pclose = _lib.pclose
        pclose.restype = c_int
        pclose.argtypes = [POINTER(FILE)]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 498
for _lib in _libs.values():
    if hasattr(_lib, '_flushall'):
        _flushall = _lib._flushall
        _flushall.restype = c_int
        _flushall.argtypes = []
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 499
for _lib in _libs.values():
    if hasattr(_lib, '_fgetchar'):
        _fgetchar = _lib._fgetchar
        _fgetchar.restype = c_int
        _fgetchar.argtypes = []
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 500
for _lib in _libs.values():
    if hasattr(_lib, '_fputchar'):
        _fputchar = _lib._fputchar
        _fputchar.restype = c_int
        _fputchar.argtypes = [c_int]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 501
for _lib in _libs.values():
    if hasattr(_lib, '_fdopen'):
        _fdopen = _lib._fdopen
        _fdopen.restype = POINTER(FILE)
        _fdopen.argtypes = [c_int, String]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 502
for _lib in _libs.values():
    if hasattr(_lib, '_fileno'):
        _fileno = _lib._fileno
        _fileno.restype = c_int
        _fileno.argtypes = [POINTER(FILE)]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 503
for _lib in _libs.values():
    if hasattr(_lib, '_fcloseall'):
        _fcloseall = _lib._fcloseall
        _fcloseall.restype = c_int
        _fcloseall.argtypes = []
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 504
for _lib in _libs.values():
    if hasattr(_lib, '_fsopen'):
        _fsopen = _lib._fsopen
        _fsopen.restype = POINTER(FILE)
        _fsopen.argtypes = [String, String, c_int]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 506
for _lib in _libs.values():
    if hasattr(_lib, '_getmaxstdio'):
        _getmaxstdio = _lib._getmaxstdio
        _getmaxstdio.restype = c_int
        _getmaxstdio.argtypes = []
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 507
for _lib in _libs.values():
    if hasattr(_lib, '_setmaxstdio'):
        _setmaxstdio = _lib._setmaxstdio
        _setmaxstdio.restype = c_int
        _setmaxstdio.argtypes = [c_int]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 521
for _lib in _libs.values():
    if hasattr(_lib, 'fgetchar'):
        fgetchar = _lib.fgetchar
        fgetchar.restype = c_int
        fgetchar.argtypes = []
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 522
for _lib in _libs.values():
    if hasattr(_lib, 'fputchar'):
        fputchar = _lib.fputchar
        fputchar.restype = c_int
        fputchar.argtypes = [c_int]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 523
for _lib in _libs.values():
    if hasattr(_lib, 'fdopen'):
        fdopen = _lib.fdopen
        fdopen.restype = POINTER(FILE)
        fdopen.argtypes = [c_int, String]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 524
for _lib in _libs.values():
    if hasattr(_lib, 'fileno'):
        fileno = _lib.fileno
        fileno.restype = c_int
        fileno.argtypes = [POINTER(FILE)]
        break

time_t = c_long # J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/sys/types.h: 27

_off_t = c_long # J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/sys/types.h: 38

off_t = _off_t # J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/sys/types.h: 41

_dev_t = c_uint # J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/sys/types.h: 49

dev_t = _dev_t # J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/sys/types.h: 55

_ino_t = c_short # J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/sys/types.h: 62

ino_t = _ino_t # J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/sys/types.h: 65

_pid_t = c_int # J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/sys/types.h: 72

pid_t = _pid_t # J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/sys/types.h: 75

_mode_t = c_ushort # J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/sys/types.h: 82

mode_t = _mode_t # J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/sys/types.h: 85

_sigset_t = c_int # J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/sys/types.h: 92

sigset_t = _sigset_t # J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/sys/types.h: 95

_ssize_t = c_long # J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/sys/types.h: 101

ssize_t = _ssize_t # J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/sys/types.h: 104

fpos64_t = c_longlong # J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/sys/types.h: 110

off64_t = c_longlong # J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/sys/types.h: 115

useconds_t = c_uint # J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/sys/types.h: 119

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 539
for _lib in _libs.values():
    if hasattr(_lib, 'fseeko64'):
        fseeko64 = _lib.fseeko64
        fseeko64.restype = c_int
        fseeko64.argtypes = [POINTER(FILE), c_int64, c_int]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 548
for _lib in _libs.values():
    try:
        pos = (fpos_t).in_dll(_lib, 'pos')
        break
    except:
        pass

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 562
for _lib in _libs.values():
    if hasattr(_lib, 'fwprintf'):
        _func = _lib.fwprintf
        _restype = c_int
        _argtypes = [POINTER(FILE), POINTER(c_wchar)]
        fwprintf = _variadic_function(_func,_restype,_argtypes)

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 563
for _lib in _libs.values():
    if hasattr(_lib, 'wprintf'):
        _func = _lib.wprintf
        _restype = c_int
        _argtypes = [POINTER(c_wchar)]
        wprintf = _variadic_function(_func,_restype,_argtypes)

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 564
for _lib in _libs.values():
    if hasattr(_lib, '_snwprintf'):
        _func = _lib._snwprintf
        _restype = c_int
        _argtypes = [POINTER(c_wchar), c_size_t, POINTER(c_wchar)]
        _snwprintf = _variadic_function(_func,_restype,_argtypes)

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 565
for _lib in _libs.values():
    if hasattr(_lib, 'vfwprintf'):
        vfwprintf = _lib.vfwprintf
        vfwprintf.restype = c_int
        vfwprintf.argtypes = [POINTER(FILE), POINTER(c_wchar), String]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 566
for _lib in _libs.values():
    if hasattr(_lib, 'vwprintf'):
        vwprintf = _lib.vwprintf
        vwprintf.restype = c_int
        vwprintf.argtypes = [POINTER(c_wchar), String]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 567
for _lib in _libs.values():
    if hasattr(_lib, '_vsnwprintf'):
        _vsnwprintf = _lib._vsnwprintf
        _vsnwprintf.restype = c_int
        _vsnwprintf.argtypes = [POINTER(c_wchar), c_size_t, POINTER(c_wchar), String]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 568
for _lib in _libs.values():
    if hasattr(_lib, 'fwscanf'):
        _func = _lib.fwscanf
        _restype = c_int
        _argtypes = [POINTER(FILE), POINTER(c_wchar)]
        fwscanf = _variadic_function(_func,_restype,_argtypes)

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 569
for _lib in _libs.values():
    if hasattr(_lib, 'wscanf'):
        _func = _lib.wscanf
        _restype = c_int
        _argtypes = [POINTER(c_wchar)]
        wscanf = _variadic_function(_func,_restype,_argtypes)

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 570
for _lib in _libs.values():
    if hasattr(_lib, 'swscanf'):
        _func = _lib.swscanf
        _restype = c_int
        _argtypes = [POINTER(c_wchar), POINTER(c_wchar)]
        swscanf = _variadic_function(_func,_restype,_argtypes)

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 571
for _lib in _libs.values():
    if hasattr(_lib, 'fgetwc'):
        fgetwc = _lib.fgetwc
        fgetwc.restype = wint_t
        fgetwc.argtypes = [POINTER(FILE)]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 572
for _lib in _libs.values():
    if hasattr(_lib, 'fputwc'):
        fputwc = _lib.fputwc
        fputwc.restype = wint_t
        fputwc.argtypes = [c_wchar, POINTER(FILE)]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 573
for _lib in _libs.values():
    if hasattr(_lib, 'ungetwc'):
        ungetwc = _lib.ungetwc
        ungetwc.restype = wint_t
        ungetwc.argtypes = [c_wchar, POINTER(FILE)]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 577
for _lib in _libs.values():
    if hasattr(_lib, 'swprintf'):
        _func = _lib.swprintf
        _restype = c_int
        _argtypes = [POINTER(c_wchar), POINTER(c_wchar)]
        swprintf = _variadic_function(_func,_restype,_argtypes)

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 578
for _lib in _libs.values():
    if hasattr(_lib, 'vswprintf'):
        vswprintf = _lib.vswprintf
        vswprintf.restype = c_int
        vswprintf.argtypes = [POINTER(c_wchar), POINTER(c_wchar), String]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 582
for _lib in _libs.values():
    if hasattr(_lib, 'fgetws'):
        fgetws = _lib.fgetws
        fgetws.restype = POINTER(c_wchar)
        fgetws.argtypes = [POINTER(c_wchar), c_int, POINTER(FILE)]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 583
for _lib in _libs.values():
    if hasattr(_lib, 'fputws'):
        fputws = _lib.fputws
        fputws.restype = c_int
        fputws.argtypes = [POINTER(c_wchar), POINTER(FILE)]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 584
for _lib in _libs.values():
    if hasattr(_lib, 'getwc'):
        getwc = _lib.getwc
        getwc.restype = wint_t
        getwc.argtypes = [POINTER(FILE)]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 585
for _lib in _libs.values():
    if hasattr(_lib, 'getwchar'):
        getwchar = _lib.getwchar
        getwchar.restype = wint_t
        getwchar.argtypes = []
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 586
for _lib in _libs.values():
    if hasattr(_lib, '_getws'):
        _getws = _lib._getws
        _getws.restype = POINTER(c_wchar)
        _getws.argtypes = [POINTER(c_wchar)]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 587
for _lib in _libs.values():
    if hasattr(_lib, 'putwc'):
        putwc = _lib.putwc
        putwc.restype = wint_t
        putwc.argtypes = [wint_t, POINTER(FILE)]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 588
for _lib in _libs.values():
    if hasattr(_lib, '_putws'):
        _putws = _lib._putws
        _putws.restype = c_int
        _putws.argtypes = [POINTER(c_wchar)]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 589
for _lib in _libs.values():
    if hasattr(_lib, 'putwchar'):
        putwchar = _lib.putwchar
        putwchar.restype = wint_t
        putwchar.argtypes = [wint_t]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 590
for _lib in _libs.values():
    if hasattr(_lib, '_wfdopen'):
        _wfdopen = _lib._wfdopen
        _wfdopen.restype = POINTER(FILE)
        _wfdopen.argtypes = [c_int, POINTER(c_wchar)]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 591
for _lib in _libs.values():
    if hasattr(_lib, '_wfopen'):
        _wfopen = _lib._wfopen
        _wfopen.restype = POINTER(FILE)
        _wfopen.argtypes = [POINTER(c_wchar), POINTER(c_wchar)]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 592
for _lib in _libs.values():
    if hasattr(_lib, '_wfreopen'):
        _wfreopen = _lib._wfreopen
        _wfreopen.restype = POINTER(FILE)
        _wfreopen.argtypes = [POINTER(c_wchar), POINTER(c_wchar), POINTER(FILE)]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 593
for _lib in _libs.values():
    if hasattr(_lib, '_wfsopen'):
        _wfsopen = _lib._wfsopen
        _wfsopen.restype = POINTER(FILE)
        _wfsopen.argtypes = [POINTER(c_wchar), POINTER(c_wchar), c_int]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 594
for _lib in _libs.values():
    if hasattr(_lib, '_wtmpnam'):
        _wtmpnam = _lib._wtmpnam
        _wtmpnam.restype = POINTER(c_wchar)
        _wtmpnam.argtypes = [POINTER(c_wchar)]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 595
for _lib in _libs.values():
    if hasattr(_lib, '_wtempnam'):
        _wtempnam = _lib._wtempnam
        _wtempnam.restype = POINTER(c_wchar)
        _wtempnam.argtypes = [POINTER(c_wchar), POINTER(c_wchar)]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 596
for _lib in _libs.values():
    if hasattr(_lib, '_wrename'):
        _wrename = _lib._wrename
        _wrename.restype = c_int
        _wrename.argtypes = [POINTER(c_wchar), POINTER(c_wchar)]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 597
for _lib in _libs.values():
    if hasattr(_lib, '_wremove'):
        _wremove = _lib._wremove
        _wremove.restype = c_int
        _wremove.argtypes = [POINTER(c_wchar)]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 598
for _lib in _libs.values():
    if hasattr(_lib, '_wperror'):
        _wperror = _lib._wperror
        _wperror.restype = None
        _wperror.argtypes = [POINTER(c_wchar)]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 599
for _lib in _libs.values():
    if hasattr(_lib, '_wpopen'):
        _wpopen = _lib._wpopen
        _wpopen.restype = POINTER(FILE)
        _wpopen.argtypes = [POINTER(c_wchar), POINTER(c_wchar)]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 603
for _lib in _libs.values():
    if hasattr(_lib, 'snwprintf'):
        _func = _lib.snwprintf
        _restype = c_int
        _argtypes = [POINTER(c_wchar), c_size_t, POINTER(c_wchar)]
        snwprintf = _variadic_function(_func,_restype,_argtypes)

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 607
for _lib in _libs.values():
    if hasattr(_lib, 'vwscanf'):
        vwscanf = _lib.vwscanf
        vwscanf.restype = c_int
        vwscanf.argtypes = [POINTER(c_wchar), String]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 608
for _lib in _libs.values():
    if hasattr(_lib, 'vfwscanf'):
        vfwscanf = _lib.vfwscanf
        vfwscanf.restype = c_int
        vfwscanf.argtypes = [POINTER(FILE), POINTER(c_wchar), String]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 610
for _lib in _libs.values():
    if hasattr(_lib, 'vswscanf'):
        vswscanf = _lib.vswscanf
        vswscanf.restype = c_int
        vswscanf.argtypes = [POINTER(c_wchar), POINTER(c_wchar), String]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 620
for _lib in _libs.values():
    if hasattr(_lib, 'wpopen'):
        wpopen = _lib.wpopen
        wpopen.restype = POINTER(FILE)
        wpopen.argtypes = [POINTER(c_wchar), POINTER(c_wchar)]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 627
for _lib in _libs.values():
    if hasattr(_lib, '_fgetwchar'):
        _fgetwchar = _lib._fgetwchar
        _fgetwchar.restype = wint_t
        _fgetwchar.argtypes = []
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 628
for _lib in _libs.values():
    if hasattr(_lib, '_fputwchar'):
        _fputwchar = _lib._fputwchar
        _fputwchar.restype = wint_t
        _fputwchar.argtypes = [wint_t]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 629
for _lib in _libs.values():
    if hasattr(_lib, '_getw'):
        _getw = _lib._getw
        _getw.restype = c_int
        _getw.argtypes = [POINTER(FILE)]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 630
for _lib in _libs.values():
    if hasattr(_lib, '_putw'):
        _putw = _lib._putw
        _putw.restype = c_int
        _putw.argtypes = [c_int, POINTER(FILE)]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 633
for _lib in _libs.values():
    if hasattr(_lib, 'fgetwchar'):
        fgetwchar = _lib.fgetwchar
        fgetwchar.restype = wint_t
        fgetwchar.argtypes = []
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 634
for _lib in _libs.values():
    if hasattr(_lib, 'fputwchar'):
        fputwchar = _lib.fputwchar
        fputwchar.restype = wint_t
        fputwchar.argtypes = [wint_t]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 635
for _lib in _libs.values():
    if hasattr(_lib, 'getw'):
        getw = _lib.getw
        getw.restype = c_int
        getw.argtypes = [POINTER(FILE)]
        break

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 636
for _lib in _libs.values():
    if hasattr(_lib, 'putw'):
        putw = _lib.putw
        putw.restype = c_int
        putw.argtypes = [c_int, POINTER(FILE)]
        break

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_blk.h: 88
class struct_bBootBlock(Structure):
    pass

struct_bBootBlock.__slots__ = [
    'dosType',
    'checkSum',
    'rootBlock',
    'data',
]
struct_bBootBlock._fields_ = [
    ('dosType', c_char * 4),
    ('checkSum', c_ulong),
    ('rootBlock', c_long),
    ('data', c_ubyte * (500 + 512)),
]

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_blk.h: 96
class struct_bRootBlock(Structure):
    pass

struct_bRootBlock.__slots__ = [
    'type',
    'headerKey',
    'highSeq',
    'hashTableSize',
    'firstData',
    'checkSum',
    'hashTable',
    'bmFlag',
    'bmPages',
    'bmExt',
    'cDays',
    'cMins',
    'cTicks',
    'nameLen',
    'diskName',
    'r2',
    'days',
    'mins',
    'ticks',
    'coDays',
    'coMins',
    'coTicks',
    'nextSameHash',
    'parent',
    'extension',
    'secType',
]
struct_bRootBlock._fields_ = [
    ('type', c_long),
    ('headerKey', c_long),
    ('highSeq', c_long),
    ('hashTableSize', c_long),
    ('firstData', c_long),
    ('checkSum', c_ulong),
    ('hashTable', c_long * 72),
    ('bmFlag', c_long),
    ('bmPages', c_long * 25),
    ('bmExt', c_long),
    ('cDays', c_long),
    ('cMins', c_long),
    ('cTicks', c_long),
    ('nameLen', c_char),
    ('diskName', c_char * (30 + 1)),
    ('r2', c_char * 8),
    ('days', c_long),
    ('mins', c_long),
    ('ticks', c_long),
    ('coDays', c_long),
    ('coMins', c_long),
    ('coTicks', c_long),
    ('nextSameHash', c_long),
    ('parent', c_long),
    ('extension', c_long),
    ('secType', c_long),
]

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_blk.h: 126
class struct_bFileHeaderBlock(Structure):
    pass

struct_bFileHeaderBlock.__slots__ = [
    'type',
    'headerKey',
    'highSeq',
    'dataSize',
    'firstData',
    'checkSum',
    'dataBlocks',
    'r1',
    'r2',
    'access',
    'byteSize',
    'commLen',
    'comment',
    'r3',
    'days',
    'mins',
    'ticks',
    'nameLen',
    'fileName',
    'r4',
    'real',
    'nextLink',
    'r5',
    'nextSameHash',
    'parent',
    'extension',
    'secType',
]
struct_bFileHeaderBlock._fields_ = [
    ('type', c_long),
    ('headerKey', c_long),
    ('highSeq', c_long),
    ('dataSize', c_long),
    ('firstData', c_long),
    ('checkSum', c_ulong),
    ('dataBlocks', c_long * 72),
    ('r1', c_long),
    ('r2', c_long),
    ('access', c_long),
    ('byteSize', c_ulong),
    ('commLen', c_char),
    ('comment', c_char * (79 + 1)),
    ('r3', c_char * (91 - (79 + 1))),
    ('days', c_long),
    ('mins', c_long),
    ('ticks', c_long),
    ('nameLen', c_char),
    ('fileName', c_char * (30 + 1)),
    ('r4', c_long),
    ('real', c_long),
    ('nextLink', c_long),
    ('r5', c_long * 5),
    ('nextSameHash', c_long),
    ('parent', c_long),
    ('extension', c_long),
    ('secType', c_long),
]

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_blk.h: 159
class struct_bFileExtBlock(Structure):
    pass

struct_bFileExtBlock.__slots__ = [
    'type',
    'headerKey',
    'highSeq',
    'dataSize',
    'firstData',
    'checkSum',
    'dataBlocks',
    'r',
    'info',
    'nextSameHash',
    'parent',
    'extension',
    'secType',
]
struct_bFileExtBlock._fields_ = [
    ('type', c_long),
    ('headerKey', c_long),
    ('highSeq', c_long),
    ('dataSize', c_long),
    ('firstData', c_long),
    ('checkSum', c_ulong),
    ('dataBlocks', c_long * 72),
    ('r', c_long * 45),
    ('info', c_long),
    ('nextSameHash', c_long),
    ('parent', c_long),
    ('extension', c_long),
    ('secType', c_long),
]

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_blk.h: 177
class struct_bDirBlock(Structure):
    pass

struct_bDirBlock.__slots__ = [
    'type',
    'headerKey',
    'highSeq',
    'hashTableSize',
    'r1',
    'checkSum',
    'hashTable',
    'r2',
    'access',
    'r4',
    'commLen',
    'comment',
    'r5',
    'days',
    'mins',
    'ticks',
    'nameLen',
    'dirName',
    'r6',
    'real',
    'nextLink',
    'r7',
    'nextSameHash',
    'parent',
    'extension',
    'secType',
]
struct_bDirBlock._fields_ = [
    ('type', c_long),
    ('headerKey', c_long),
    ('highSeq', c_long),
    ('hashTableSize', c_long),
    ('r1', c_long),
    ('checkSum', c_ulong),
    ('hashTable', c_long * 72),
    ('r2', c_long * 2),
    ('access', c_long),
    ('r4', c_long),
    ('commLen', c_char),
    ('comment', c_char * (79 + 1)),
    ('r5', c_char * (91 - (79 + 1))),
    ('days', c_long),
    ('mins', c_long),
    ('ticks', c_long),
    ('nameLen', c_char),
    ('dirName', c_char * (30 + 1)),
    ('r6', c_long),
    ('real', c_long),
    ('nextLink', c_long),
    ('r7', c_long * 5),
    ('nextSameHash', c_long),
    ('parent', c_long),
    ('extension', c_long),
    ('secType', c_long),
]

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_blk.h: 208
class struct_bOFSDataBlock(Structure):
    pass

struct_bOFSDataBlock.__slots__ = [
    'type',
    'headerKey',
    'seqNum',
    'dataSize',
    'nextData',
    'checkSum',
    'data',
]
struct_bOFSDataBlock._fields_ = [
    ('type', c_long),
    ('headerKey', c_long),
    ('seqNum', c_long),
    ('dataSize', c_long),
    ('nextData', c_long),
    ('checkSum', c_ulong),
    ('data', c_ubyte * 488),
]

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_blk.h: 221
class struct_bBitmapBlock(Structure):
    pass

struct_bBitmapBlock.__slots__ = [
    'checkSum',
    'map',
]
struct_bBitmapBlock._fields_ = [
    ('checkSum', c_ulong),
    ('map', c_ulong * 127),
]

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_blk.h: 227
class struct_bBitmapExtBlock(Structure):
    pass

struct_bBitmapExtBlock.__slots__ = [
    'bmPages',
    'nextBlock',
]
struct_bBitmapExtBlock._fields_ = [
    ('bmPages', c_long * 127),
    ('nextBlock', c_long),
]

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_blk.h: 233
class struct_bLinkBlock(Structure):
    pass

struct_bLinkBlock.__slots__ = [
    'type',
    'headerKey',
    'r1',
    'checkSum',
    'realName',
    'r2',
    'days',
    'mins',
    'ticks',
    'nameLen',
    'name',
    'r3',
    'realEntry',
    'nextLink',
    'r4',
    'nextSameHash',
    'parent',
    'r5',
    'secType',
]
struct_bLinkBlock._fields_ = [
    ('type', c_long),
    ('headerKey', c_long),
    ('r1', c_long * 3),
    ('checkSum', c_ulong),
    ('realName', c_char * 64),
    ('r2', c_long * 83),
    ('days', c_long),
    ('mins', c_long),
    ('ticks', c_long),
    ('nameLen', c_char),
    ('name', c_char * (30 + 1)),
    ('r3', c_long),
    ('realEntry', c_long),
    ('nextLink', c_long),
    ('r4', c_long * 5),
    ('nextSameHash', c_long),
    ('parent', c_long),
    ('r5', c_long),
    ('secType', c_long),
]

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_blk.h: 259
class struct_bDirCacheBlock(Structure):
    pass

struct_bDirCacheBlock.__slots__ = [
    'type',
    'headerKey',
    'parent',
    'recordsNb',
    'nextDirC',
    'checkSum',
    'records',
]
struct_bDirCacheBlock._fields_ = [
    ('type', c_long),
    ('headerKey', c_long),
    ('parent', c_long),
    ('recordsNb', c_long),
    ('nextDirC', c_long),
    ('checkSum', c_ulong),
    ('records', c_ubyte * 488),
]

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_str.h: 62
class struct_Device(Structure):
    pass

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_str.h: 22
class struct_Volume(Structure):
    pass

struct_Volume.__slots__ = [
    'dev',
    'firstBlock',
    'lastBlock',
    'rootBlock',
    'dosType',
    'bootCode',
    'readOnly',
    'datablockSize',
    'blockSize',
    'volName',
    'mounted',
    'bitmapSize',
    'bitmapBlocks',
    'bitmapTable',
    'bitmapBlocksChg',
    'curDirPtr',
]
struct_Volume._fields_ = [
    ('dev', POINTER(struct_Device)),
    ('firstBlock', c_long),
    ('lastBlock', c_long),
    ('rootBlock', c_long),
    ('dosType', c_char),
    ('bootCode', c_int),
    ('readOnly', c_int),
    ('datablockSize', c_int),
    ('blockSize', c_int),
    ('volName', String),
    ('mounted', c_int),
    ('bitmapSize', c_long),
    ('bitmapBlocks', POINTER(c_long)),
    ('bitmapTable', POINTER(POINTER(struct_bBitmapBlock))),
    ('bitmapBlocksChg', POINTER(c_int)),
    ('curDirPtr', c_long),
]

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_str.h: 48
class struct_Partition(Structure):
    pass

struct_Partition.__slots__ = [
    'startCyl',
    'lenCyl',
    'volName',
    'volType',
]
struct_Partition._fields_ = [
    ('startCyl', c_long),
    ('lenCyl', c_long),
    ('volName', String),
    ('volType', c_int),
]

struct_Device.__slots__ = [
    'devType',
    'readOnly',
    'size',
    'nVol',
    'volList',
    'cylinders',
    'heads',
    'sectors',
    'isNativeDev',
    'nativeDev',
]
struct_Device._fields_ = [
    ('devType', c_int),
    ('readOnly', c_int),
    ('size', c_long),
    ('nVol', c_int),
    ('volList', POINTER(POINTER(struct_Volume))),
    ('cylinders', c_long),
    ('heads', c_long),
    ('sectors', c_long),
    ('isNativeDev', c_int),
    ('nativeDev', POINTER(None)),
]

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_str.h: 81
class struct_File(Structure):
    pass

struct_File.__slots__ = [
    'volume',
    'fileHdr',
    'currentData',
    'currentExt',
    'nDataBlock',
    'curDataPtr',
    'pos',
    'posInDataBlk',
    'posInExtBlk',
    'eof',
    'writeMode',
]
struct_File._fields_ = [
    ('volume', POINTER(struct_Volume)),
    ('fileHdr', POINTER(struct_bFileHeaderBlock)),
    ('currentData', POINTER(None)),
    ('currentExt', POINTER(struct_bFileExtBlock)),
    ('nDataBlock', c_long),
    ('curDataPtr', c_long),
    ('pos', c_ulong),
    ('posInDataBlk', c_int),
    ('posInExtBlk', c_int),
    ('eof', c_int),
    ('writeMode', c_int),
]

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_str.h: 100
class struct_Entry(Structure):
    pass

struct_Entry.__slots__ = [
    'type',
    'name',
    'sector',
    'real',
    'parent',
    'comment',
    'size',
    'access',
    'year',
    'month',
    'days',
    'hour',
    'mins',
    'secs',
]
struct_Entry._fields_ = [
    ('type', c_int),
    ('name', String),
    ('sector', c_long),
    ('real', c_long),
    ('parent', c_long),
    ('comment', String),
    ('size', c_ulong),
    ('access', c_long),
    ('year', c_int),
    ('month', c_int),
    ('days', c_int),
    ('hour', c_int),
    ('mins', c_int),
    ('secs', c_int),
]

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_str.h: 113
class struct_CacheEntry(Structure):
    pass

struct_CacheEntry.__slots__ = [
    'header',
    'size',
    'protect',
    'days',
    'mins',
    'ticks',
    'type',
    'nLen',
    'cLen',
    'name',
    'comm',
]
struct_CacheEntry._fields_ = [
    ('header', c_long),
    ('size', c_long),
    ('protect', c_long),
    ('days', c_short),
    ('mins', c_short),
    ('ticks', c_short),
    ('type', c_char),
    ('nLen', c_char),
    ('cLen', c_char),
    ('name', c_char * (30 + 1)),
    ('comm', c_char * (79 + 1)),
]

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_str.h: 126
class struct_DateTime(Structure):
    pass

struct_DateTime.__slots__ = [
    'year',
    'mon',
    'day',
    'hour',
    'min',
    'sec',
]
struct_DateTime._fields_ = [
    ('year', c_int),
    ('mon', c_int),
    ('day', c_int),
    ('hour', c_int),
    ('min', c_int),
    ('sec', c_int),
]

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_str.h: 143
class struct_Env(Structure):
    pass

struct_Env.__slots__ = [
    'vFct',
    'wFct',
    'eFct',
    'notifyFct',
    'useNotify',
    'rwhAccess',
    'useRWAccess',
    'progressBar',
    'useProgressBar',
    'useDirCache',
    'nativeFct',
]
struct_Env._fields_ = [
    ('vFct', CFUNCTYPE(UNCHECKED(None), String)),
    ('wFct', CFUNCTYPE(UNCHECKED(None), String)),
    ('eFct', CFUNCTYPE(UNCHECKED(None), String)),
    ('notifyFct', CFUNCTYPE(UNCHECKED(None), c_long, c_int)),
    ('useNotify', c_int),
    ('rwhAccess', CFUNCTYPE(UNCHECKED(None), c_long, c_long, c_int)),
    ('useRWAccess', c_int),
    ('progressBar', CFUNCTYPE(UNCHECKED(None), c_int)),
    ('useProgressBar', c_int),
    ('useDirCache', c_int),
    ('nativeFct', POINTER(None)),
]

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_str.h: 164
class struct_List(Structure):
    pass

struct_List.__slots__ = [
    'content',
    'subdir',
    'next',
]
struct_List._fields_ = [
    ('content', POINTER(None)),
    ('subdir', POINTER(struct_List)),
    ('next', POINTER(struct_List)),
]

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_str.h: 170
class struct_GenBlock(Structure):
    pass

struct_GenBlock.__slots__ = [
    'sect',
    'parent',
    'type',
    'secType',
    'name',
]
struct_GenBlock._fields_ = [
    ('sect', c_long),
    ('parent', c_long),
    ('type', c_int),
    ('secType', c_int),
    ('name', String),
]

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_str.h: 178
class struct_FileBlocks(Structure):
    pass

struct_FileBlocks.__slots__ = [
    'header',
    'nbExtens',
    'extens',
    'nbData',
    'data',
]
struct_FileBlocks._fields_ = [
    ('header', c_long),
    ('nbExtens', c_long),
    ('extens', POINTER(c_long)),
    ('nbData', c_long),
    ('data', POINTER(c_long)),
]

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_str.h: 186
class struct_bEntryBlock(Structure):
    pass

struct_bEntryBlock.__slots__ = [
    'type',
    'headerKey',
    'r1',
    'checkSum',
    'hashTable',
    'r2',
    'access',
    'byteSize',
    'commLen',
    'comment',
    'r3',
    'days',
    'mins',
    'ticks',
    'nameLen',
    'name',
    'r4',
    'realEntry',
    'nextLink',
    'r5',
    'nextSameHash',
    'parent',
    'extension',
    'secType',
]
struct_bEntryBlock._fields_ = [
    ('type', c_long),
    ('headerKey', c_long),
    ('r1', c_long * 3),
    ('checkSum', c_ulong),
    ('hashTable', c_long * 72),
    ('r2', c_long * 2),
    ('access', c_long),
    ('byteSize', c_long),
    ('commLen', c_char),
    ('comment', c_char * (79 + 1)),
    ('r3', c_char * (91 - (79 + 1))),
    ('days', c_long),
    ('mins', c_long),
    ('ticks', c_long),
    ('nameLen', c_char),
    ('name', c_char * (30 + 1)),
    ('r4', c_long),
    ('realEntry', c_long),
    ('nextLink', c_long),
    ('r5', c_long * 5),
    ('nextSameHash', c_long),
    ('parent', c_long),
    ('extension', c_long),
    ('secType', c_long),
]

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adflib.h: 31
if hasattr(_libs['adflib'], 'newCell'):
    newCell = _libs['adflib'].newCell
    newCell.restype = POINTER(struct_List)
    newCell.argtypes = [POINTER(struct_List), POINTER(None)]

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adflib.h: 32
if hasattr(_libs['adflib'], 'freeList'):
    freeList = _libs['adflib'].freeList
    freeList.restype = None
    freeList.argtypes = [POINTER(struct_List)]

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adflib.h: 35
if hasattr(_libs['adflib'], 'adfToRootDir'):
    adfToRootDir = _libs['adflib'].adfToRootDir
    adfToRootDir.restype = c_long
    adfToRootDir.argtypes = [POINTER(struct_Volume)]

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adflib.h: 36
if hasattr(_libs['adflib'], 'adfCreateDir'):
    adfCreateDir = _libs['adflib'].adfCreateDir
    adfCreateDir.restype = c_long
    adfCreateDir.argtypes = [POINTER(struct_Volume), c_long, String]

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adflib.h: 37
if hasattr(_libs['adflib'], 'adfChangeDir'):
    adfChangeDir = _libs['adflib'].adfChangeDir
    adfChangeDir.restype = c_long
    adfChangeDir.argtypes = [POINTER(struct_Volume), String]

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adflib.h: 38
if hasattr(_libs['adflib'], 'adfParentDir'):
    adfParentDir = _libs['adflib'].adfParentDir
    adfParentDir.restype = c_long
    adfParentDir.argtypes = [POINTER(struct_Volume)]

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adflib.h: 39
if hasattr(_libs['adflib'], 'adfRemoveEntry'):
    adfRemoveEntry = _libs['adflib'].adfRemoveEntry
    adfRemoveEntry.restype = c_long
    adfRemoveEntry.argtypes = [POINTER(struct_Volume), c_long, String]

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adflib.h: 40
if hasattr(_libs['adflib'], 'adfGetDirEnt'):
    adfGetDirEnt = _libs['adflib'].adfGetDirEnt
    adfGetDirEnt.restype = POINTER(struct_List)
    adfGetDirEnt.argtypes = [POINTER(struct_Volume), c_long]

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adflib.h: 41
if hasattr(_libs['adflib'], 'adfGetRDirEnt'):
    adfGetRDirEnt = _libs['adflib'].adfGetRDirEnt
    adfGetRDirEnt.restype = POINTER(struct_List)
    adfGetRDirEnt.argtypes = [POINTER(struct_Volume), c_long, c_int]

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adflib.h: 42
if hasattr(_libs['adflib'], 'printEntry'):
    printEntry = _libs['adflib'].printEntry
    printEntry.restype = None
    printEntry.argtypes = [POINTER(struct_Entry)]

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adflib.h: 43
if hasattr(_libs['adflib'], 'adfFreeDirList'):
    adfFreeDirList = _libs['adflib'].adfFreeDirList
    adfFreeDirList.restype = None
    adfFreeDirList.argtypes = [POINTER(struct_List)]

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adflib.h: 44
if hasattr(_libs['adflib'], 'adfFreeEntry'):
    adfFreeEntry = _libs['adflib'].adfFreeEntry
    adfFreeEntry.restype = None
    adfFreeEntry.argtypes = [POINTER(struct_Entry)]

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adflib.h: 45
if hasattr(_libs['adflib'], 'adfRenameEntry'):
    adfRenameEntry = _libs['adflib'].adfRenameEntry
    adfRenameEntry.restype = c_long
    adfRenameEntry.argtypes = [POINTER(struct_Volume), c_long, String, c_long, String]

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adflib.h: 46
if hasattr(_libs['adflib'], 'adfSetEntryAccess'):
    adfSetEntryAccess = _libs['adflib'].adfSetEntryAccess
    adfSetEntryAccess.restype = c_long
    adfSetEntryAccess.argtypes = [POINTER(struct_Volume), c_long, String, c_long]

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adflib.h: 47
if hasattr(_libs['adflib'], 'adfSetEntryComment'):
    adfSetEntryComment = _libs['adflib'].adfSetEntryComment
    adfSetEntryComment.restype = c_long
    adfSetEntryComment.argtypes = [POINTER(struct_Volume), c_long, String, String]

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adflib.h: 50
if hasattr(_libs['adflib'], 'adfFileRealSize'):
    adfFileRealSize = _libs['adflib'].adfFileRealSize
    adfFileRealSize.restype = c_long
    adfFileRealSize.argtypes = [c_ulong, c_int, POINTER(c_long), POINTER(c_long)]

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adflib.h: 51
if hasattr(_libs['adflib'], 'adfOpenFile'):
    adfOpenFile = _libs['adflib'].adfOpenFile
    adfOpenFile.restype = POINTER(struct_File)
    adfOpenFile.argtypes = [POINTER(struct_Volume), String, String]

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adflib.h: 52
if hasattr(_libs['adflib'], 'adfCloseFile'):
    adfCloseFile = _libs['adflib'].adfCloseFile
    adfCloseFile.restype = None
    adfCloseFile.argtypes = [POINTER(struct_File)]

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adflib.h: 53
if hasattr(_libs['adflib'], 'adfReadFile'):
    adfReadFile = _libs['adflib'].adfReadFile
    adfReadFile.restype = c_long
    adfReadFile.argtypes = [POINTER(struct_File), c_long, POINTER(c_ubyte)]

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adflib.h: 54
if hasattr(_libs['adflib'], 'adfEndOfFile'):
    adfEndOfFile = _libs['adflib'].adfEndOfFile
    adfEndOfFile.restype = c_int
    adfEndOfFile.argtypes = [POINTER(struct_File)]

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adflib.h: 55
if hasattr(_libs['adflib'], 'adfWriteFile'):
    adfWriteFile = _libs['adflib'].adfWriteFile
    adfWriteFile.restype = c_long
    adfWriteFile.argtypes = [POINTER(struct_File), c_long, POINTER(c_ubyte)]

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adflib.h: 56
if hasattr(_libs['adflib'], 'adfFlushFile'):
    adfFlushFile = _libs['adflib'].adfFlushFile
    adfFlushFile.restype = None
    adfFlushFile.argtypes = [POINTER(struct_File)]

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adflib.h: 57
if hasattr(_libs['adflib'], 'adfFileSeek'):
    adfFileSeek = _libs['adflib'].adfFileSeek
    adfFileSeek.restype = None
    adfFileSeek.argtypes = [POINTER(struct_File), c_ulong]

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adflib.h: 60
if hasattr(_libs['adflib'], 'adfInstallBootBlock'):
    adfInstallBootBlock = _libs['adflib'].adfInstallBootBlock
    adfInstallBootBlock.restype = c_long
    adfInstallBootBlock.argtypes = [POINTER(struct_Volume), POINTER(c_ubyte)]

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adflib.h: 61
if hasattr(_libs['adflib'], 'adfMount'):
    adfMount = _libs['adflib'].adfMount
    adfMount.restype = POINTER(struct_Volume)
    adfMount.argtypes = [POINTER(struct_Device), c_int, c_int]

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adflib.h: 62
if hasattr(_libs['adflib'], 'adfUnMount'):
    adfUnMount = _libs['adflib'].adfUnMount
    adfUnMount.restype = None
    adfUnMount.argtypes = [POINTER(struct_Volume)]

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adflib.h: 63
if hasattr(_libs['adflib'], 'adfVolumeInfo'):
    adfVolumeInfo = _libs['adflib'].adfVolumeInfo
    adfVolumeInfo.restype = None
    adfVolumeInfo.argtypes = [POINTER(struct_Volume)]

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adflib.h: 66
if hasattr(_libs['adflib'], 'adfDeviceInfo'):
    adfDeviceInfo = _libs['adflib'].adfDeviceInfo
    adfDeviceInfo.restype = None
    adfDeviceInfo.argtypes = [POINTER(struct_Device)]

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adflib.h: 67
if hasattr(_libs['adflib'], 'adfMountDev'):
    adfMountDev = _libs['adflib'].adfMountDev
    adfMountDev.restype = POINTER(struct_Device)
    adfMountDev.argtypes = [String, c_int]

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adflib.h: 68
if hasattr(_libs['adflib'], 'adfUnMountDev'):
    adfUnMountDev = _libs['adflib'].adfUnMountDev
    adfUnMountDev.restype = None
    adfUnMountDev.argtypes = [POINTER(struct_Device)]

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adflib.h: 69
if hasattr(_libs['adflib'], 'adfCreateHd'):
    adfCreateHd = _libs['adflib'].adfCreateHd
    adfCreateHd.restype = c_long
    adfCreateHd.argtypes = [POINTER(struct_Device), c_int, POINTER(POINTER(struct_Partition))]

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adflib.h: 70
if hasattr(_libs['adflib'], 'adfCreateFlop'):
    adfCreateFlop = _libs['adflib'].adfCreateFlop
    adfCreateFlop.restype = c_long
    adfCreateFlop.argtypes = [POINTER(struct_Device), String, c_int]

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adflib.h: 71
for _lib in _libs.values():
    if hasattr(_lib, 'adfCreateHdFile'):
        adfCreateHdFile = _lib.adfCreateHdFile
        adfCreateHdFile.restype = c_long
        adfCreateHdFile.argtypes = [POINTER(struct_Device), String, c_int]
        break

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adflib.h: 74
for _lib in _libs.values():
    if hasattr(_lib, 'adfCreateDumpDevice'):
        adfCreateDumpDevice = _lib.adfCreateDumpDevice
        adfCreateDumpDevice.restype = POINTER(struct_Device)
        adfCreateDumpDevice.argtypes = [String, c_long, c_long, c_long]
        break

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adflib.h: 77
if hasattr(_libs['adflib'], 'adfEnvInitDefault'):
    adfEnvInitDefault = _libs['adflib'].adfEnvInitDefault
    adfEnvInitDefault.restype = None
    adfEnvInitDefault.argtypes = []

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adflib.h: 78
if hasattr(_libs['adflib'], 'adfEnvCleanUp'):
    adfEnvCleanUp = _libs['adflib'].adfEnvCleanUp
    adfEnvCleanUp.restype = None
    adfEnvCleanUp.argtypes = []

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adflib.h: 79
if hasattr(_libs['adflib'], 'adfChgEnvProp'):
    adfChgEnvProp = _libs['adflib'].adfChgEnvProp
    adfChgEnvProp.restype = None
    adfChgEnvProp.argtypes = [c_int, POINTER(None)]

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adflib.h: 80
if hasattr(_libs['adflib'], 'adfGetVersionNumber'):
    adfGetVersionNumber = _libs['adflib'].adfGetVersionNumber
    adfGetVersionNumber.restype = String
    adfGetVersionNumber.argtypes = []
    adfGetVersionNumber.errcheck = ReturnString

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adflib.h: 81
if hasattr(_libs['adflib'], 'adfGetVersionDate'):
    adfGetVersionDate = _libs['adflib'].adfGetVersionDate
    adfGetVersionDate.restype = String
    adfGetVersionDate.argtypes = []
    adfGetVersionDate.errcheck = ReturnString

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adflib.h: 83
if hasattr(_libs['adflib'], 'adfSetEnvFct'):
    adfSetEnvFct = _libs['adflib'].adfSetEnvFct
    adfSetEnvFct.restype = None
    adfSetEnvFct.argtypes = [CFUNCTYPE(UNCHECKED(None), String), CFUNCTYPE(UNCHECKED(None), String), CFUNCTYPE(UNCHECKED(None), String)]

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adflib.h: 86
if hasattr(_libs['adflib'], 'adfBlockPtr2EntryName'):
    adfBlockPtr2EntryName = _libs['adflib'].adfBlockPtr2EntryName
    adfBlockPtr2EntryName.restype = c_long
    adfBlockPtr2EntryName.argtypes = [POINTER(struct_Volume), c_long, c_long, POINTER(POINTER(c_char)), POINTER(c_long)]

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adflib.h: 89
if hasattr(_libs['adflib'], 'adfGetDelEnt'):
    adfGetDelEnt = _libs['adflib'].adfGetDelEnt
    adfGetDelEnt.restype = POINTER(struct_List)
    adfGetDelEnt.argtypes = [POINTER(struct_Volume)]

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adflib.h: 90
if hasattr(_libs['adflib'], 'adfUndelEntry'):
    adfUndelEntry = _libs['adflib'].adfUndelEntry
    adfUndelEntry.restype = c_long
    adfUndelEntry.argtypes = [POINTER(struct_Volume), c_long, c_long]

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adflib.h: 91
if hasattr(_libs['adflib'], 'adfFreeDelList'):
    adfFreeDelList = _libs['adflib'].adfFreeDelList
    adfFreeDelList.restype = None
    adfFreeDelList.argtypes = [POINTER(struct_List)]

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adflib.h: 92
if hasattr(_libs['adflib'], 'adfCheckEntry'):
    adfCheckEntry = _libs['adflib'].adfCheckEntry
    adfCheckEntry.restype = c_long
    adfCheckEntry.argtypes = [POINTER(struct_Volume), c_long, c_int]

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adflib.h: 96
if hasattr(_libs['adflib'], 'isSectNumValid'):
    isSectNumValid = _libs['adflib'].isSectNumValid
    isSectNumValid.restype = c_int
    isSectNumValid.argtypes = [POINTER(struct_Volume), c_long]

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adflib.h: 100
if hasattr(_libs['adflib'], 'adfReadBlock'):
    adfReadBlock = _libs['adflib'].adfReadBlock
    adfReadBlock.restype = c_long
    adfReadBlock.argtypes = [POINTER(struct_Volume), c_long, POINTER(c_ubyte)]

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adflib.h: 101
if hasattr(_libs['adflib'], 'adfWriteBlock'):
    adfWriteBlock = _libs['adflib'].adfWriteBlock
    adfWriteBlock.restype = c_long
    adfWriteBlock.argtypes = [POINTER(struct_Volume), c_long, POINTER(c_ubyte)]

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adflib.h: 102
if hasattr(_libs['adflib'], 'adfCountFreeBlocks'):
    adfCountFreeBlocks = _libs['adflib'].adfCountFreeBlocks
    adfCountFreeBlocks.restype = c_long
    adfCountFreeBlocks.argtypes = [POINTER(struct_Volume)]

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adflib.h: 2
try:
    ADFLIB_H = 1
except:
    pass

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_defs.h: 12
try:
    _ADF_DEFS_H = 1
except:
    pass

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_defs.h: 14
try:
    ADFLIB_VERSION = '0.7.10'
except:
    pass

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_defs.h: 15
try:
    ADFLIB_DATE = '16 November, 2002'
except:
    pass

SECTNUM = c_long # D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_defs.h: 17

RETCODE = c_long # D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_defs.h: 18

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_defs.h: 20
try:
    TRUE = 1
except:
    pass

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_defs.h: 21
try:
    FALSE = 0
except:
    pass

ULONG = c_ulong # D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_defs.h: 23

USHORT = c_ushort # D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_defs.h: 24

UCHAR = c_ubyte # D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_defs.h: 25

BOOL = c_int # D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_defs.h: 26

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_defs.h: 32
def max(a, b):
    return (a > b) and a or b

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_defs.h: 35
def min(a, b):
    return (a < b) and a or b

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_defs.h: 41
def Short(p):
    return (((p [0]) << 8) | (p [1]))

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_defs.h: 42
def Long(p):
    return ((((Short (p)).value) << 16) | ((Short ((p + 2))).value))

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_defs.h: 47
def swapShort(p):
    return (((p [0]) << 8) | (p [1]))

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_defs.h: 48
def swapLong(p):
    return ((((swapShort (p)).value) << 16) | ((swapShort ((p + 2))).value))

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_str.h: 2
try:
    _ADF_STR_H = 1
except:
    pass

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/_mingw.h: 26
try:
    __MINGW32_MAJOR_VERSION = 3
except:
    pass

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/_mingw.h: 27
try:
    __MINGW32_MINOR_VERSION = 15
except:
    pass

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/_mingw.h: 28
try:
    __MINGW32_PATCHLEVEL = 2
except:
    pass

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/_mingw.h: 67
try:
    __MINGW_ANSI_STDIO__ = 1L
except:
    pass

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/_mingw.h: 72
try:
    __MINGW_LC_EXTENSIONS__ = 80L
except:
    pass

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/_mingw.h: 73
try:
    __MINGW_LC_MESSAGES__ = 16L
except:
    pass

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/_mingw.h: 74
try:
    __MINGW_LC_ENVVARS__ = 64L
except:
    pass

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/_mingw.h: 147
def __MINGW_GNUC_PREREQ(major, minor):
    return 0

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/_mingw.h: 166
def __UNUSED_PARAM(x):
    return x

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/_mingw.h: 213
try:
    __MSVCRT_VERSION__ = 1536
except:
    pass

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 33
try:
    _IOREAD = 1
except:
    pass

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 34
try:
    _IOWRT = 2
except:
    pass

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 35
try:
    _IORW = 128
except:
    pass

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 42
try:
    STDIN_FILENO = 0
except:
    pass

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 43
try:
    STDOUT_FILENO = 1
except:
    pass

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 44
try:
    STDERR_FILENO = 2
except:
    pass

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 47
try:
    EOF = (-1)
except:
    pass

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 55
try:
    FILENAME_MAX = 260
except:
    pass

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 62
try:
    FOPEN_MAX = 20
except:
    pass

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 65
try:
    TMP_MAX = 32767
except:
    pass

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 72
try:
    _P_tmpdir = '\\'
except:
    pass

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 74
try:
    P_tmpdir = _P_tmpdir
except:
    pass

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 84
try:
    L_tmpnam = 16
except:
    pass

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 86
try:
    _IOFBF = 0
except:
    pass

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 87
try:
    _IOLBF = 64
except:
    pass

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 88
try:
    _IONBF = 4
except:
    pass

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 90
try:
    _IOMYBUF = 8
except:
    pass

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 91
try:
    _IOEOF = 16
except:
    pass

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 92
try:
    _IOERR = 32
except:
    pass

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 93
try:
    _IOSTRG = 64
except:
    pass

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 101
try:
    BUFSIZ = 512
except:
    pass

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 106
try:
    SEEK_SET = 0
except:
    pass

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 107
try:
    SEEK_CUR = 1
except:
    pass

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 108
try:
    SEEK_END = 2
except:
    pass

__VALIST = String # J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 116

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 158
try:
    stdin = pointer((_iob [STDIN_FILENO]))
except:
    pass

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 159
try:
    stdout = pointer((_iob [STDOUT_FILENO]))
except:
    pass

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 160
try:
    stderr = pointer((_iob [STDERR_FILENO]))
except:
    pass

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 475
def feof(__F):
    return (((__F.contents._flag).value) & _IOEOF)

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 476
def ferror(__F):
    return (((__F.contents._flag).value) & _IOERR)

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 527
def _fileno(__F):
    return (__F.contents._file)

# J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 529
def fileno(__F):
    return (__F.contents._file)

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_blk.h: 13
try:
    ADF_BLK_H = 1
except:
    pass

ULONG = c_ulong # D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_blk.h: 15

USHORT = c_ushort # D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_blk.h: 16

UCHAR = c_ubyte # D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_blk.h: 17

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_blk.h: 19
try:
    LOGICAL_BLOCK_SIZE = 512
except:
    pass

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_blk.h: 23
try:
    FSMASK_FFS = 1
except:
    pass

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_blk.h: 24
try:
    FSMASK_INTL = 2
except:
    pass

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_blk.h: 25
try:
    FSMASK_DIRCACHE = 4
except:
    pass

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_blk.h: 27
def isFFS(c):
    return (c & FSMASK_FFS)

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_blk.h: 28
def isOFS(c):
    return (not (c & FSMASK_FFS))

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_blk.h: 29
def isINTL(c):
    return (c & FSMASK_INTL)

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_blk.h: 30
def isDIRCACHE(c):
    return (c & FSMASK_DIRCACHE)

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_blk.h: 37
try:
    ACCMASK_D = (1 << 0)
except:
    pass

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_blk.h: 38
try:
    ACCMASK_E = (1 << 1)
except:
    pass

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_blk.h: 39
try:
    ACCMASK_W = (1 << 2)
except:
    pass

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_blk.h: 40
try:
    ACCMASK_R = (1 << 3)
except:
    pass

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_blk.h: 41
try:
    ACCMASK_A = (1 << 4)
except:
    pass

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_blk.h: 42
try:
    ACCMASK_P = (1 << 5)
except:
    pass

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_blk.h: 43
try:
    ACCMASK_S = (1 << 6)
except:
    pass

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_blk.h: 44
try:
    ACCMASK_H = (1 << 7)
except:
    pass

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_blk.h: 46
def hasD(c):
    return (c & ACCMASK_D)

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_blk.h: 47
def hasE(c):
    return (c & ACCMASK_E)

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_blk.h: 48
def hasW(c):
    return (c & ACCMASK_W)

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_blk.h: 49
def hasR(c):
    return (c & ACCMASK_R)

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_blk.h: 50
def hasA(c):
    return (c & ACCMASK_A)

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_blk.h: 51
def hasP(c):
    return (c & ACCMASK_P)

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_blk.h: 52
def hasS(c):
    return (c & ACCMASK_S)

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_blk.h: 53
def hasH(c):
    return (c & ACCMASK_H)

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_blk.h: 60
try:
    BM_VALID = (-1)
except:
    pass

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_blk.h: 61
try:
    BM_INVALID = 0
except:
    pass

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_blk.h: 63
try:
    HT_SIZE = 72
except:
    pass

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_blk.h: 64
try:
    BM_SIZE = 25
except:
    pass

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_blk.h: 65
try:
    MAX_DATABLK = 72
except:
    pass

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_blk.h: 67
try:
    MAXNAMELEN = 30
except:
    pass

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_blk.h: 68
try:
    MAXCMMTLEN = 79
except:
    pass

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_blk.h: 73
try:
    T_HEADER = 2
except:
    pass

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_blk.h: 74
try:
    ST_ROOT = 1
except:
    pass

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_blk.h: 75
try:
    ST_DIR = 2
except:
    pass

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_blk.h: 76
try:
    ST_FILE = (-3)
except:
    pass

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_blk.h: 77
try:
    ST_LFILE = (-4)
except:
    pass

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_blk.h: 78
try:
    ST_LDIR = 4
except:
    pass

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_blk.h: 79
try:
    ST_LSOFT = 3
except:
    pass

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_blk.h: 80
try:
    T_LIST = 16
except:
    pass

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_blk.h: 81
try:
    T_DATA = 8
except:
    pass

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_blk.h: 82
try:
    T_DIRC = 33
except:
    pass

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_err.h: 13
def hasRC(rc, c):
    return (rc & c)

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_err.h: 15
try:
    RC_OK = 0
except:
    pass

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_err.h: 16
try:
    RC_ERROR = (-1)
except:
    pass

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_err.h: 18
try:
    RC_MALLOC = 1
except:
    pass

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_err.h: 19
try:
    RC_VOLFULL = 2
except:
    pass

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_err.h: 22
try:
    RC_FOPEN = (1 << 10)
except:
    pass

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_err.h: 23
try:
    RC_NULLPTR = (1 << 12)
except:
    pass

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_err.h: 27
try:
    RC_BLOCKTYPE = 1
except:
    pass

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_err.h: 28
try:
    RC_BLOCKSTYPE = (1 << 1)
except:
    pass

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_err.h: 29
try:
    RC_BLOCKSUM = (1 << 2)
except:
    pass

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_err.h: 30
try:
    RC_HEADERKEY = (1 << 3)
except:
    pass

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_err.h: 31
try:
    RC_BLOCKREAD = (1 << 4)
except:
    pass

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_err.h: 34
try:
    RC_BLOCKWRITE = (1 << 4)
except:
    pass

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_err.h: 38
try:
    RC_BLOCKOUTOFRANGE = 1
except:
    pass

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_err.h: 39
try:
    RC_BLOCKNATREAD = (1 << 1)
except:
    pass

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_err.h: 43
try:
    RC_BLOCKNATWRITE = (1 << 1)
except:
    pass

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_err.h: 44
try:
    RC_BLOCKREADONLY = (1 << 2)
except:
    pass

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_err.h: 52
try:
    RC_BLOCKSHORTREAD = 1
except:
    pass

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_err.h: 53
try:
    RC_BLOCKFSEEK = (1 << 1)
except:
    pass

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_err.h: 57
try:
    RC_BLOCKSHORTWRITE = 1
except:
    pass

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_err.h: 62
try:
    RC_BLOCKID = (1 << 5)
except:
    pass

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_str.h: 57
try:
    DEVTYPE_FLOPDD = 1
except:
    pass

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_str.h: 58
try:
    DEVTYPE_FLOPHD = 2
except:
    pass

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_str.h: 59
try:
    DEVTYPE_HARDDISK = 3
except:
    pass

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_str.h: 60
try:
    DEVTYPE_HARDFILE = 4
except:
    pass

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_str.h: 132
try:
    PR_VFCT = 1
except:
    pass

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_str.h: 133
try:
    PR_WFCT = 2
except:
    pass

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_str.h: 134
try:
    PR_EFCT = 3
except:
    pass

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_str.h: 135
try:
    PR_NOTFCT = 4
except:
    pass

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_str.h: 136
try:
    PR_USEDIRC = 5
except:
    pass

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_str.h: 137
try:
    PR_USE_NOTFCT = 6
except:
    pass

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_str.h: 138
try:
    PR_PROGBAR = 7
except:
    pass

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_str.h: 139
try:
    PR_USE_PROGBAR = 8
except:
    pass

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_str.h: 140
try:
    PR_RWACCESS = 9
except:
    pass

# D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_str.h: 141
try:
    PR_USE_RWACCESS = 10
except:
    pass

_iobuf = struct__iobuf # J:/MinGW/bin/../lib/gcc/mingw32/3.4.5/../../../../include/stdio.h: 139

bBootBlock = struct_bBootBlock # D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_blk.h: 88

bRootBlock = struct_bRootBlock # D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_blk.h: 96

bFileHeaderBlock = struct_bFileHeaderBlock # D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_blk.h: 126

bFileExtBlock = struct_bFileExtBlock # D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_blk.h: 159

bDirBlock = struct_bDirBlock # D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_blk.h: 177

bOFSDataBlock = struct_bOFSDataBlock # D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_blk.h: 208

bBitmapBlock = struct_bBitmapBlock # D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_blk.h: 221

bBitmapExtBlock = struct_bBitmapExtBlock # D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_blk.h: 227

bLinkBlock = struct_bLinkBlock # D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_blk.h: 233

bDirCacheBlock = struct_bDirCacheBlock # D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_blk.h: 259

Device = struct_Device # D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_str.h: 62

Volume = struct_Volume # D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_str.h: 22

Partition = struct_Partition # D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_str.h: 48

File = struct_File # D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_str.h: 81

Entry = struct_Entry # D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_str.h: 100

CacheEntry = struct_CacheEntry # D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_str.h: 113

DateTime = struct_DateTime # D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_str.h: 126

Env = struct_Env # D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_str.h: 143

List = struct_List # D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_str.h: 164

GenBlock = struct_GenBlock # D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_str.h: 170

FileBlocks = struct_FileBlocks # D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_str.h: 178

bEntryBlock = struct_bEntryBlock # D:\\documents\\drive_f_share\\python\\adflib\\csrc\\adflib\\Lib\\adf_str.h: 186

# No inserted files

