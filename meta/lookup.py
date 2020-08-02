#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Get(object):
    def __init__(self, v=0):
        self.v = v

    def __get__(self, obj, owner):
        print(f'Get.__get__, {obj}, {owner}')
        return self.v


class Set(Get):
    def __set__(self, cls, value):
        self.v = value


class Meta(type):
    m = 'm'

    def __getattribute__(cls, name):
        if cls is Foo:
            print(f'Meta.__getattribute__, {cls}, {name}')
        return super().__getattribute__(name)


class Type(Meta):
    s = Set('Type')

    def __getattribute__(cls, name):
        if cls is Bar:
            print(f'Type.__getattribute__, {cls}, {name}')
        return type.__getattribute__(cls, name)


class Base(object):
    base = 'Base'


class Foo(metaclass=Meta):
    pass


class Bar(Base, metaclass=Type):
    pass


class First(object):
    g = Get(1)


class Second(First):
    g = Get(2)
    s = Set(2)


class Third(Second, metaclass=Meta):
    pass


if __name__ == '__main__':
    assert Foo.m == 'm'
    assert Bar.m == 'm'
    assert Bar.base == 'Base'

    g = First.__dict__['g']
    assert isinstance(g, Get)
    assert First.g == 1
    assert Third.g == Second.g == 2

    assert Third.s == Second.s == 2
    s = Second.__dict__.get('s')
    assert isinstance(s, Set)
    Third.s = 3
    s = Third.__dict__.get('s')
    assert isinstance(s, int)
    assert Second.s == 2
    Second.s = 'Second'
    s = Second.__dict__.get('s')
    assert isinstance(s, str)

    assert type(Bar).s == 'Type'
    Bar.s = 'Bar'
    assert not ('s' in Bar.__dict__)
    assert type(Bar).s == 'Bar'
