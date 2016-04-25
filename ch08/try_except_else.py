# -*- coding: utf-8 -*
import sys
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except IOError:
        print 'cannot open', arg
    else: # try的else子句，在所有except子句之后执行。
        print arg, ' has', len(f.readlines()), 'lines'
        f.close()