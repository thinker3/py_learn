#!/usr/bin/env python
# encoding: utf-8


class Meta(type):
    def __getattribute__(*args):
        print "Metaclass getattribute invoked"
        return type.__getattribute__(*args)


class C(object):
    __metaclass__ = Meta

    def __len__(self):
        return 10

    def __getattribute__(*args):
        print "Class getattribute invoked"
        return object.__getattribute__(*args)

c = C()
print c.__len__()  # Explicit lookup via instance
print '*' * 30
print type(c).__len__(c)  # Explicit lookup via type
print '*' * 30
print len(c)  # Implicit lookup
print c.__class__.__dict__
print '*' * 30
print '*' * 30


class C(object):
    def __init__(self):
        self.c = 'C'

c = C()
print c.__class__.__dict__
print c.__class__.__dict__['__dict__']
print c.__dict__
print '*' * 30
c.__len__ = lambda: 5
print c.__class__.__dict__
print c.__dict__
print '*' * 30
print c.__len__()
print '*' * 30
#print len(c)  # TypeError: object of type 'C' has no len()
#C.__len__ = lambda: 15  # TypeError: <lambda>() takes no arguments (1 given)
C.__len__ = lambda x: 15
print c.__class__.__dict__
print len(c)
