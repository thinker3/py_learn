#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils.classproperty import (
    ClassProperty,
    ClassPropertyMeta,
    classproperty,
    ClassPropertyType,
    classgetter,
)


class Foo(metaclass=ClassPropertyMeta):
    __foo = 1

    @ClassProperty
    def foo(cls):
        return cls.__foo + 0.5

    @foo.setter
    def foo(cls, value):
        cls.__foo = value


class Foo2(metaclass=ClassPropertyMeta):
    __foo = 1

    """
    @ClassProperty
    def foo(cls):  # AttributeError: type object 'Foo' has no attribute '_Foo2__foo'
        return cls.__foo + 0.4
    """

    @ClassProperty
    def foo2(cls):
        return cls.__foo + 0.4

    @foo2.setter
    def foo2(cls, value):
        cls.__foo = value


class Bar(metaclass=ClassPropertyType):
    __bar = 1

    @classproperty
    def bar(cls):
        return cls.__bar + 0.6

    @bar.setter
    def bar(cls, value):
        cls.__bar = value


class Bar2(metaclass=ClassPropertyType):
    __bar = 1

    @classproperty
    def bar(cls):
        return cls.__bar + 0.7

    @bar.setter
    def bar(cls, value):
        cls.__bar = value


class Toe(object):

    @classgetter
    def class_name(cls):
        return cls.__name__


class Human(object):
    planet = 'Earth'


class Person(Human, metaclass=ClassPropertyType):
    __x = 0

    @classproperty
    def x(cls):
        return cls.__x + 0.8

    @x.setter
    def x(cls, value):
        cls.__x = value


if __name__ == '__main__':
    Foo.foo = 2
    assert Foo.foo == 2.5 == Foo().foo

    Foo2.foo2 = 3
    assert Foo2.foo2 == 3.4 == Foo2().foo2
    assert Foo.foo == 2.5

    Bar.bar = 2
    assert Bar.bar == 2.6 == Bar().bar

    Bar2.bar = 3
    assert Bar2.bar == 3.7 == Bar2().bar
    assert Bar.bar == 2.6

    assert Toe.class_name == 'Toe'

    assert issubclass(Person, Human)
    assert Person.planet == 'Earth'
    Person.x = 1
    assert Person.x == 1.8
    assert Person().x == 1.8
