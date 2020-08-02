#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Slot(object):
    __slots__ = ('x', 'y')


obj = Slot()
# obj.__slots__ = ('x', 'y', 'z')  # AttributeError: 'Slot' object attribute '__slots__' is read-only


class ListSlot(object):
    __slots__ = ['x', 'y']

    def __init__(self):
        self.x = 1
        self.y = 2
        # self.z = 3  # AttributeError: 'ListSlot' object has no attribute 'z'

obj = ListSlot()
