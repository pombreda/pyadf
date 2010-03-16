#!/bin/env python
# -*- coding: ascii -*-
# vim:ts=4:sw=4:softtabstop=4:smarttab:expandtab
#

import sys


def main(argv=None):
    if argv is None:
        argv = sys.argv

    filename = argv[1]
    
    for fmode in ['rb', 'rU']:
        f = open(filename, fmode)
        data = f.read()
        f.close()
        print '%s in mode "%s: read %d bytes' % (filename, fmode, len(data))
    
    return 0

if __name__ == "__main__":
    sys.exit(main())

