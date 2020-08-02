#!/usr/bin/env python
# encoding: utf-8

from overridee import aclass

before = 'before'
_aclass_show = aclass.show


def aclass_show(a, b=0, c=None):
    if b > 0:
        print(a, b)
    else:
        _aclass_show(a, b, c)
aclass.show = aclass_show
after = 'after'

if __name__ == '__main__':
    _aclass_show(1, -2)
    aclass.show(1, -2)
    _aclass_show(1, -2, 3)
    aclass.show(1, -2, 3)
    _aclass_show(1, 2)
    aclass.show(1, 2)
    _aclass_show(1, 2, 3)
    aclass.show(1, 2, 3)
