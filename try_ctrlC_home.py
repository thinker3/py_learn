from time import sleep
import os, sys
filepath = os.path.expanduser('~/num.txt')
try:
    f = open(filepath, 'r')
    num = f.readline()
    num = int(num)
    f.close()
except:
    num = 1

try:
    while 1:
        print 'hello %d' % num
        sleep(0.1)
        num += 1
except:
    print 'ctrl c'
    f = open(filepath, 'w+')
    f.write(str(num))
    f.close()
    sys.exit(0)
finally:
    print 'finally'
