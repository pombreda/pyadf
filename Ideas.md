# To Do #

  * test compress file support and document what is/isn't supported

For each feature above implement support in the command line tool cmdadf.py.


# Ideas #

  * implement a file system handler for http://code.google.com/p/pyfilesystem/
  * implement an ftp server using http://code.google.com/p/pyftpdlib implementing an AbstractedFS into the ADF. This would allow any ftp client to look inside an ADF (and rename, extract, add to, etc.) without the need for a "GUI"
  * implement an pyftpdlib AbstractedFS  that uses pyfilesystem