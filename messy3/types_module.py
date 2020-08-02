#!/usr/bin/env python
# -*- coding: utf-8 -*-

import types


def func(*args, **kwargs):
    pass


class Window(object):
    def open(self):
        pass

    @property
    def color(self):
        return 'green'

    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def sub(cls, a, b):
        assert cls is Window
        return a - b


if __name__ == '__main__':
    assert type(func) is types.FunctionType
    assert type(Window.open) is types.FunctionType
    assert type(Window().open) is types.MethodType
    assert type(Window.add) is types.FunctionType  # not staticmethod
    assert Window.add(1, 2) == 3
    assert type(Window.sub) is types.MethodType  # not classmethod
    assert Window.sub(1, 2) == -1
    assert type(Window.color) is property
    assert type(Window) is type
