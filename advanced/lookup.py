#!/usr/bin/env python
# encoding: utf-8

from pprint import pprint


class Meta(type):
    def __getattribute__(*args):
        print "Metaclass getattribute invoked"
        return type.__getattribute__(*args)


class Class(object):
    __metaclass__ = Meta

    def __len__(self):
        return 10

    def __getattribute__(*args):
        print "Class getattribute invoked"
        return object.__getattribute__(*args)


obj = Class()
obj.__len__()  # Explicit lookup via instance
Class.__len__(obj)  # Explicit lookup via type
len(obj)  # Implicit lookup, __getattribute__ not invoked
print


class Class(object):
    def __init__(self):
        self.name = 'Class'


obj = Class()
assert Class is obj.__class__ is type(obj)
print obj.__dict__
pprint(dict(Class.__dict__), indent=4)
dic = Class.__dict__['__dict__']
print type(dic)
assert dic.__get__(obj) == obj.__dict__

obj.__len__ = lambda: 5
assert obj.__len__() == 5
#len(obj)  # TypeError: object of type 'Class' has no len()
#Class.__len__ = lambda: 15  # TypeError: <lambda>() takes no arguments (1 given)
Class.__len__ = lambda x: 15
assert len(obj) == 15
