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


class classproperty(object):  # noqa
    def __init__(self, getter):
        self.getter = getter

    def __get__(self, instance, owner):
        return self.getter(owner)


class Foo(object):
    x = 1

    @classproperty
    def number(cls):  # noqa
        return cls.x


print Foo().number
print Foo.number
