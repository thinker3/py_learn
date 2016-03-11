#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import namedtuple

# Point = namedtuple('Point', ['x', 'y'], verbose=True)
Point = namedtuple('Point', ['x', 'y'], verbose=False)
print Point._fields
nt = Point(x=3, y=4)
t = nt.x, nt.y
print t, type(t)
print nt[0], nt[1]
print nt[:]
print

ant = Point._make([8, 9])
t = ant.x, ant.y
print t
d = ant._asdict()
print d['x'], d['y']
rant = ant._replace(x=3)
print rant

Point3D = namedtuple('Point', 'x y z', verbose=False)
print Point3D._fields
Point4D = namedtuple('Point4D', Point3D._fields + ('t',))
print Point4D._fields
p = Point3D(1, 2, 3)
print p
print p[:]
# print Point4D(p + (4,))
print Point4D(*p, t=4)
# print Point4D(*p[:], 4)
print Point4D(*p[:], t=4)
d = p._asdict()
d.update(t=4)
print Point4D(**d)


