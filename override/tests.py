#!/usr/bin/env python
# encoding: utf-8

import overridee
import importlib


def line():
    print('*' * 50)


def test0():
    line()
    from overridee import aclass
    aclass.show(1, 2, 3)
    from overrider import aclass
    aclass.show(1, 2, 3)
    from overrider import _aclass_show
    _aclass_show(1, 2, 3)
    from overrider import aclass_show
    aclass_show(1, 2, 3)


def test1():
    line()
    from overrider import aclass
    aclass.show(1, 2, 3)
    importlib.reload(overridee)  # has no effects
    print('overridee reloaded')
    aclass.show(1, 2, 3)
    from overridee import aclass
    aclass.show(1, 2, 3)


def test2():
    line()
    from overridee import aclass
    aclass.show(1, 2, 3)
    from overrider import before
    print(before)
    aclass.show(1, 2, 3)
    from overrider import after  # has no effects
    print(after)
    aclass.show(1, 2, 3)

test0()
test1()
test2()

line()
