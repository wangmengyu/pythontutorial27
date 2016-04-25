# -*- coding: utf-8 -*
import sys
try:
    f = open('mylife.txt')
    s = f.readline()
    i = int(s.strip())
    print i
    print 1/0
except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)
except ValueError:
    print "Coud not conver data to an intenger."
except:
    print "Unexpected error:", sys.exc_info()[0]
    raise # 重新抛出异常
