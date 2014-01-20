total = 0

def add(n):
    global total
    for i in xrange(n):
        total += (i+1)
    print total

add(100)
print
print total
print

total = 0
for i in xrange(10):
    total += i+1
print total
print '-' * 20


def test():
    print total # 'total' is made local before calling test()???
    total = 0

import traceback
try:
    test()
except:
    traceback.print_exc()
print '-' * 20


def test():
    total += 0

import traceback
try:
    test()
except:
    traceback.print_exc()
print '-' * 20


def outer(num):
    def inner():
        global num
        num = 2
        print num, 'inner'
    print num
    inner()

outer(1)
print num + 1
print '-' * 20

#def test(num):
#    global num # SyntaxError: name 'num' is local and global







