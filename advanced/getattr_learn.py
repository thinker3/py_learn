#!/usr/bin/env python
# -*- coding: utf-8 -*-


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
    # test_old_style_class()
    # test_new_style_class()
    pass
