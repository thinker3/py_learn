#!/usr/bin/env python
# -*- coding: utf-8 -*-

import types


class Window(object):

    @classmethod
    def show(cls, number):
        return f'{cls.__name__}#{number}'


if __name__ == '__main__':
    assert Window.show(1) == 'Window#1'
    show = getattr(Window, 'show')
    assert show(2) == 'Window#2'  # not show(Window, 2)
    assert type(show) is types.MethodType
    assert type(Window.show) is types.MethodType
