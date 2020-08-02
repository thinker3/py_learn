from time import sleep
import os, sys
import atexit

filepath = os.path.expanduser('~/num.txt') # for home dir
try:
    f = open(filepath, 'r')
    num = f.readline()
    num = int(num)
    f.close()
except:
    num = 1

def save(num):
    f = open(filepath, 'w+')
    f.write(str(num))
    f.close()

try:
    while 1:
        print('hello %d' % num)
        sleep(0.1)
        num += 1
        a = 1/(num - 120)
except KeyboardInterrupt:
    pass # or raise it to higher handler
except:
    print('ctrl c')
    save(num)
    os._exit(0) # This line here will prevent finally and atexit from executing
finally:
    print('finally')

atexit.register(save, num)
