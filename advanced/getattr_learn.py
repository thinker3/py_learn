#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Person(object):
    country = 'cn'

    def __init__(self, name):
        self.name = name

    def __getattr__(self, name):
        print 'calling __getattr__ ...'
        try:
            # AttributeError: type object 'object' has no attribute '__getattr__'
            return object.__getattribute__(self, name)
        except AttributeError as e:
            print e


class Old():  # old style class
    def __init__(self):
        self.a = 1

    def __getattr__(self, name):
        print 'calling __getattr__ ...'
        if name == 'x':
            return 'x'
        else:
            raise AttributeError('No such attribute: %s' % name)

    def __getattribute__(self, name):
        print 'calling __getattribute__ ...'
        return object.__getattribute__(self, name)


class New(object):  # new style class
    def __init__(self):
        self.a = 1

    def __getattr__(self, name):
        print 'calling __getattr__ ...'
        if name == 'x':
            return 'x'
        else:
            raise AttributeError('No such attribute: %s' % name)

    def __getattribute__(self, name):
        print 'calling __getattribute__ ...'
        return object.__getattribute__(self, name)

    def show(self):
        print 'calling method show ...'
        return self.a


def test():
    p = Person('Jim')
    print p.__dict__
    print p.name
    print getattr(p, 'name')
    print p.country
    print getattr(p, 'country')
    x = getattr(p, 'x')
    assert x is None
    assert p.y is None
    print '-' * 80


def test_old_style_class():
    obj = Old()
    print obj.__dict__
    print obj.a
    print getattr(obj, 'a')
    print obj.x
    print obj.__dict__
    try:
        print getattr(obj, 'y')
    except AttributeError as e:
        print e.message
    print '-' * 80


def test_new_style_class():
    obj = New()
    print obj.__dict__
    print obj.a
    print getattr(obj, 'a')
    attr = getattr(obj, 'show')
    assert callable(attr)
    print attr()
    print obj.x
    print obj.__dict__
    try:
        print getattr(obj, 'y')
    except AttributeError as e:
        print e.message
    print '-' * 80


if __name__ == '__main__':
    test()
    test_old_style_class()
    test_new_style_class()
    pass
