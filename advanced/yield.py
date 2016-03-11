#!/usr/bin/env python
# encoding: utf-8


def grep(pattern):
    print "looking for %s" % pattern
    while True:
        line = yield
        if pattern in line:
            print line

g = grep("python")
# g.next()
g.send(None)
g.send("Yeah, but no, but yeah, but no.")
g.send("python generators rock!")
print '*' * 30


def test():
    while True:
        print 'here'
        yield

c = test()
# c.send(1)  # TypeError: can't send non-None value to a just-started generator
c.send(None)
c.send(None)
c.send(None)
c.close()
# c.send(None)
