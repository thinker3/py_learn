#!/usr/bin/env python
# encoding: utf-8

import cytoolz as toolz
from operator import itemgetter
from utils.decorators import (
    segregate,
    isolate,
    separate,
)


@segregate
def test():
    # l = [[1],[1],[2]]  # TypeError: unhashable type: 'list'
    l = [(1,), (1,), (2,)]
    s = set(l)
    print(s)

    l = [1, 2, 3]
    t = tuple(l)
    print(t)

    t = tuple()
    print(t)
    # t.append(1) #no attr append, since tuples are immutable

test()


@segregate
def init_set_test():
    s = set()
    print(s)
    # s = {}  # dict, actually
    s = {None}
    print(s)

init_set_test()


@separate()
def set_add_test():
    s = {0, 1, 2, }
    s.add('a')
    print(s)

set_add_test()


# @isolate
@isolate()
def set_operations_test():
    # set union intersection difference | & -
    a = set([1, 2, 3, 4])
    b = set([1, 4, 7])
    print(a, b)
    print(a | b)
    print(a & b)
    print(a - b)

    a = set([1, 2, 3, 4])
    b = set([1, 4, 7])
    c = set([2, 4])
    d = [a, b, c]
    print(set.intersection(*d))
    print(set.union(*d))

    a = set(range(10))
    b = set([2, 4, 6, 12])
    print(a.difference(b))
    print(a)
    print(a.difference_update(b))
    print(a)

set_operations_test()


# @isolate(sep='#', length=50)
# @isolate('#')
# @isolate(sep='#')
@isolate(length=50)
def unique_test(func, seq):
    print(func(seq))


def unique(seq):
    temp = []
    for x in seq:
        # if not x in temp:
        if x not in temp:
            temp.append(x)
    return temp

t = [1, 2, 2, 3, 2, 5, 1, 3, 6, 5, 2, 7]
unique_test(unique, t)


def unique(seq):
    temp = []
    seen = set()
    for x in seq:
        if x not in seen:
            temp.append(x)
            seen.add(x)
    return temp

t = [1, 2, 2, 3, 2, 5, 1, 3, 6, 5, 2, 7]
unique_test(unique, t)

fs = frozenset([1, 2, 3])
# fs.add(4)


duplicate_dicts = [
    {'id': 1, 'name': 'Jim'},
    {'id': 2, 'name': 'Tom'},
    {'id': 1, 'name': 'Jim'},
    {'id': 3, 'name': 'Jack'},
]
print(list(toolz.unique(duplicate_dicts, key=itemgetter('id'))))
