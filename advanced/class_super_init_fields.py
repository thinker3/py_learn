#!/usr/bin/env python
# encoding: utf-8


class Base(object):
    here = 'here'
    member = 'Base'

    def __init__(self, *args, **kwargs):
        self.init = 'init_base'
        self.init_here = 'init_here'
        # a class member and an object member
        self.length = len(self.there)  # key point
        print self.init


class Derived(Base):
    there = 'there'
    member = 'Derived'
    words = []

    '''
    def __init__(self, *args, **kwargs):
        # AttributeError: 'Derived' object has no attribute 'init_here'
        #super(Base, self).__init__(*args, **kwargs)
        super(Derived, self).__init__(*args, **kwargs)
        self.init = 'init_derived'
        self.init_there = 'init_there'
        print self.init
    '''

d = Derived()
print '*' * 30
print d.length
print d.here
print d.there
print d.member
print d.init
print d.init_here
#print d.init_there

print '*' * 30
d.there = 'changed'
d.words.append('hello')
e = Derived()
print d.there
print e.there

print '*' * 30
d.there = 'hidden'
e.there = 'showing'
print d.there
print e.there

# class variable or instance variable? may be the same if it is immutable
# but if it is mutable...

print '*' * 30
e.words.append('world')
print d.words
print e.words
f = Derived()
f.words.append('!')
print d.words
print e.words
print f.words
print d.there
print e.there
print f.there
