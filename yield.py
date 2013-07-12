#!/usr/bin/env python
def grep(pattern):
		print "looking for %s" % pattern
		while True:
				line = (yield)
				if pattern in line:
						print line,

g = grep("python")
print 1
g.next()
print 2
g.send("Yeah, but no, but yeah, but no")
g.send("python generators rock")
print

def Gen(x):
		for i in xrange(x):
				yield i
		yield None

h = Gen(5)
for i in h:
		print i
