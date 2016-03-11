#!/usr/bin/env python
# encoding: utf-8


a = xrange(2)
b = xrange(5)
print zip(a, b)
zip()


import itertools

x = itertools.izip_longest(a, b)
print list(x)


x = itertools.izip_longest(a, b, '')
print list(x)


x = itertools.izip_longest(a, b, fillvalue='')
print list(x)
