#!/usr/bin/env python
# encoding: utf-8

import time
import itertools
import functools

"""
# python2.6 does not support step
for i in itertools.count(3, -1):
    print i
    time.sleep(1)
    if i == 1:
        break

print '*' * 20
for i in itertools.repeat('hello', 3):
    print i
    time.sleep(1)

print '*' * 20
for i in itertools.cycle(xrange(1, 5)):
    print i
    time.sleep(1)
"""

two_d_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print list(itertools.chain(*two_d_list))

strings = ['hello', 'world', 'zero']
print list(itertools.ifilter(lambda x: x.endswith('o'), strings))
print list(itertools.ifilter(lambda x: 'o' in x, strings))
print list(itertools.compress(strings, map(lambda i: strings[i].endswith('o'), xrange(len(strings)))))

print list(itertools.imap(str.upper, strings))
print list(itertools.imap(lambda x, y: x * y, strings, [3] * len(strings)))
print list(itertools.imap(lambda x, y, z: x * y + z.upper(), strings, [3] * len(strings), reversed(strings)))

points = [(2, 5, 4), (3, 5, 8), (10, 3, 7)]
print list(itertools.starmap(lambda x, y, z: x * y + z, points))

its = itertools.tee(xrange(9), 3)
for it in its:
    print it, list(it)

print '*' * 20
print list(itertools.dropwhile(lambda x: x < 5, [1, 4, 6, 4, 1, 7, 9, 8]))
print list(itertools.ifilterfalse(lambda x: x < 5, [1, 4, 6, 4, 1, 7, 9, 8]))

print list(itertools.takewhile(lambda x: x < 5, [1, 4, 6, 4, 1, 7, 9, 8]))
print list(itertools.ifilter(lambda x: x < 5, [1, 4, 6, 4, 1, 7, 9, 8]))

print list(itertools.izip('ABCDE', '123'))
print list(itertools.izip_longest('ABCDE', '123'))
print list(itertools.izip_longest('ABCDE', '123', fillvalue='/'))

print '*' * 20
print list(itertools.islice(xrange(10), 2)) # stop
print list(itertools.islice(xrange(10), 2, 8)) # start, stop
print list(itertools.islice(xrange(10), 2, 8, 2)) # start, stop, step

print '*' * 20
things = [
    ("vehicle", "car"),
    ("animal", "duck"),
    ("vehicle", "boat"),
    ("animal", "bear"),
    ("vehicle", "bus"),
]
for key, group in itertools.groupby(things, lambda x: x[0]):
    print key, list(group)

print '*' * 20
import operator
things.sort(key=operator.itemgetter(0, 1))
for key, group in itertools.groupby(things, lambda x: x[0]):
    print key, list(group)

print '*' * 20
y = [0, 0, 0, 1, 1, 1, 0, 0, 0, 0]
for key, group in itertools.groupby(xrange(10), lambda x: y[x]):
    print key, list(group)

print '*' * 20
for key, igroup in itertools.groupby(xrange(12), lambda x: x / 5):
    print key, list(igroup)

print '*' * 20
things = [
    (-1, -2.1),
    (-1, -3.5),
    (0, 0),
    (1, 2.2),
    (1, 1.2),
    (1, 0.8),
]
temp = {-1: [], 1: []}
for key, group in itertools.groupby(things, lambda x: x[0]):
    group = list(group)
    print key, group
    if key in temp:
        temp[key].append((sum(1 for i in group), sum(v for k, v in group)))
print temp
