#!/usr/bin/env python
# encoding: utf-8


a = range(2)
b = range(5)
print(list(zip(a, b)))
list(zip())


import itertools

x = itertools.zip_longest(a, b)
print(list(x))


x = itertools.zip_longest(a, b, '')
print(list(x))


x = itertools.zip_longest(a, b, fillvalue='')
print(list(x))
