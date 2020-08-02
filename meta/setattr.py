#!/usr/bin/env python
# -*- coding: utf-8 -*-


class ClassPropertyMeta(type):
    def __setattr__(cls, key, value):
        obj = cls.__dict__.get(key)
        if isinstance(obj, ClassProperty):
            return obj.fset(cls, value)
        return type.__setattr__(cls, key, value)


class ClassProperty(object):
    def __init__(self, fget):
        self.fget = fget

    def setter(self, fset):
        self.fset = fset
        return self

    def __get__(self, instance, instance_type):
        return self.fget(instance_type)

    def __set__(self, obj, value):
        self.fset(obj, value)


class Person(metaclass=ClassPropertyMeta):
    __x = 0

    @ClassProperty
    def x(cls):
        return cls.__x + 0.5

    @x.setter
    def x(cls, value):
        cls.__x = value


class Human(metaclass=ClassPropertyMeta):
    __x = 1

    @ClassProperty
    def x(cls):
        return cls.__x + 0.6

    @x.setter
    def x(cls, value):
        cls.__x = value


if __name__ == '__main__':
    assert Person.x == 0.5
    Person.x = 1
    assert Person.x == 1.5
    assert Person().x == 1.5
    Person.y = 10
    assert Person.y == 10
    assert Person().y == 10

    assert Human.x == 1.6
    Human.x = 2
    assert Human.x == 2.6
    assert Human().x == 2.6
