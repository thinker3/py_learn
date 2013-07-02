from time import sleep
import os
filepath = os.path.expanduser('~/num.txt')

f = open(filepath, 'r')
num = f.readline()
num = int(num)
f.close()

try:
    while 1:
        print 'hello'
        sleep(0.1)
except:
    pass
finally:
    print 'ctrl c'
    f = open(filepath, 'w+')
    f.write(str(num+1))
    f.close()
