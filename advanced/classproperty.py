#!/usr/bin/env python
# -*- coding: utf-8 -*-


class ClassPropertyMeta(type):
    @property
    def number(cls):  # noqa
        return cls.x


class Foo(object):
    __metaclass__ = ClassPropertyMeta
    x = 1


print Foo.number
# AttributeError: 'Foo' object has no attribute 'number'
# print Foo().number
