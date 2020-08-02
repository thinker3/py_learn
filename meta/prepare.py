#!/usr/bin/env python
# -*- coding: utf-8 -*-

import types


class Meta(type):
    @classmethod
    def __prepare__(meta, name, bases, **kwargs):
        namespace = super().__prepare__(meta, name, bases, **kwargs)
        assert namespace == {}
        return namespace

    def __new__(meta, name, bases, attrs, **kwargs):
        return super().__new__(meta, name, bases, attrs)

    def add(a, b):  # like staticmethod, but is not
        return a + b

    @classmethod
    def sub(meta, a, b):
        assert meta is Meta
        return a - b

    @staticmethod
    def times(a, b):
        return a * b


class Type(type):
    def __prepare__(name, bases, **kwargs):
        namespace = super.__prepare__(name, bases, **kwargs)
        assert namespace == {}
        return kwargs

    def __new__(meta, name, bases, attrs, **kwargs):
        return super().__new__(meta, name, bases, attrs)


class Base(object):
    pass


class Window(Base, metaclass=Meta, cells=4):
    has_glass = True

    def close(self):
        pass


class Door(metaclass=Type, width=1.2):
    color = 'white'

    def show(self):
        return self.color


if __name__ == '__main__':
    assert type(Meta.add) is types.FunctionType
    assert Meta.add(1, 2) == 3
    assert type(Meta.sub) is types.MethodType
    assert Meta.sub(1, 2) == -1
    assert type(Meta.times) is types.FunctionType
    assert Meta.times(2, 3) == 6
    assert type(Meta.__prepare__) is types.MethodType
    assert type(Type.__prepare__) is types.FunctionType
    assert not hasattr(Window, 'cells')
    assert Door.width == 1.2
