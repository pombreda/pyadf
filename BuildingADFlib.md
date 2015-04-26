# ADFlib build tips #

## Unix/Linux ##

You need a shell environment as the Makefile spawns shells scripts.

Also the path needs to include "." as the makefile expects this

If using version 7.12 auto`*` toolkits are required, assuming Debian/Ubuntu:
```
sudo apt-get install autoconf
sudo apt-get install automake
sudo apt-get install libtool
sh autogen.sh
env LANG=c ./configure
env LANG=c make
```


TinyCoreLinux:

  * compiletc
  * automake
  * libtool

NOTE requires slight patches and change to build procedure:

```
tc@box:adflib$ hg diff
diff -r dca08a86d2e0 Makefile.am
--- a/Makefile.am       Sun Mar 28 02:37:28 2010 -0700
+++ b/Makefile.am       Sun Mar 28 03:55:05 2010 -0700
@@ -1,7 +1,8 @@
-SUBDIRS = src doc
-if EXAMPLES
-SUBDIRS += examples
-endif
+ACLOCAL_AMFLAGS = -I m4
+#if EXAMPLES
+##SUBDIRS += examples
+#SUBDIRS = examples
+#endif
 
 pkgconfigdir = $(libdir)/pkgconfig
 pkgconfig_DATA = adflib.pc
diff -r dca08a86d2e0 configure.ac
--- a/configure.ac      Sun Mar 28 02:37:28 2010 -0700
+++ b/configure.ac      Sun Mar 28 03:55:05 2010 -0700
@@ -25,7 +25,8 @@
 AC_PROG_INSTALL
 AC_PROG_LN_S
 AC_PROG_MAKE_SET
-AC_PROG_LIBTOOL
+#AC_PROG_LIBTOOL
+AC_PROG_LIBTOOL=libtool
 
 # Checks for libraries.
 
diff -r dca08a86d2e0 src/Makefile.am
--- a/src/Makefile.am   Sun Mar 28 02:37:28 2010 -0700
+++ b/src/Makefile.am   Sun Mar 28 03:55:05 2010 -0700
@@ -1,3 +1,5 @@
+LIBTOOL = libtool
+ACLOCAL_AMFLAGS = -I m4
 NATIVE_DIR = generic
 
 lib_LTLIBRARIES = libadf.la

```

Issue:

```
sh autogen.sh 
./configure
make  ## seems to do nothing
make src
cd src
make
```

Shared libs end up in src/.libs/

## Windows ##

Nmake files are present as of March 2010 in the ADFLib CVS repo.

```
mkdir Bin\Win32\Debug
nmake /f dynlib.mak
```

Project (dsp) files are for MSVC 6.0, can use .net 2003 (project files need upgrading by MS Studio).

NOTE the dll name appears to be adflibD.dll, note the D which is upper case here for clarity but is lowercase in the file system. pyadf expects the dll to be called adflib.dll

Consider using http://coapp.org approach to making Windows versions of the adf dll.