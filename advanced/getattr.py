#!/usr/bin/env python
# encoding: utf-8


class Person(object):
    country = 'cn'
    def __getattr__(self, name):
        return object.__getattribute__(self, name)

    def show(self):
        print 'hello'
        return self.country

p = Person()
attr = getattr(p, 'show')
if callable(attr):
    print attr()
else:
    print attr
attr = getattr(p, 'country')
print attr
print '-' * 30


class A(object):  # new style class
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

a = A()
print a.__dict__
print a.a
print getattr(a, 'a')
print a.x
print a.__dict__
try:
    print getattr(a, 'y')
except AttributeError as e:
    print e.message
print '-' * 30


class A():  # old style class
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

a = A()
print a.__dict__
print a.a
print getattr(a, 'a')
print a.x
print a.__dict__
try:
    print getattr(a, 'y')
except AttributeError as e:
    print e.message
