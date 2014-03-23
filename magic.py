import os

# run in this floder and another folder respectively
print __file__, type(__file__)  # magic.py <type 'str'>
filepath = os.path.abspath(__file__)
print filepath
print os.path.dirname(filepath)
print os.path.dirname(__file__)

print '-' * 100
print __name__, type(__name__)  # __main__ <type 'str'>


print '-' * 100


class Foo(object):

    def __new__(cls):
        print 1

    def __init__(cls):
        print 2  # not be printed

f = Foo()

print '-' * 100


class Foo(object):

    def __new__(cls):
        print 1
        return object.__new__(cls)

    def __init__(self):
        print 2

    def __call__(self):
        print 3

f = Foo()
f()  # __call__ called here

print '-' * 100


class Foo(object):

    def __new__(cls, name):
        print cls  # <class '__main__.Foo'>
        cls.name = name
        what = object.__new__(cls)
        print what  # <__main__.Foo object at 0x7f16ff4831d0>
        return what

    '''
    # TypeError: __new__() takes exactly 1 argument (2 given)
    def __new__(cls):
        return object.__new__(cls)
    '''

    def __init__(self, name):
        print self  # <__main__.Foo object at 0x7f9f29cc3250>
        print self.name  # Jim
        self.name = name * 2
        print self.name  # JimJim
        print self.__class__.name  # Jim

f = Foo('Jim')
print f.__dict__
print Foo.__dict__

print '-' * 100


class Foo(object):

    def __new__(cls, name):
        print cls
        cls.name = name
        return object.__new__(cls, name, 'more', 'even more')

    def __init__(self, name):
        print self
        print self.name
        self.name = name * 2
        print self.name

Foo('Jim')

print '-' * 100


class Meta(type):

    def __call__(cls, *args, **kwargs):
        print cls  # <class '__main__.Foo'>
        print args  # ('a',)
        print kwargs  # {}
        obj = cls.__new__(cls, *args, **kwargs)  # 1
        print obj  # <__main__.Foo object at 0x7f7e4d90b350>
        print obj.__dict__  # {}
        print 'before'
        #obj.__init__(*args, **kwargs)
        print 'after'
        return obj


class Foo(object):
    __metaclass__ = Meta

    def __new__(cls, *args, **kwargs):
        print 1
        return object.__new__(cls, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        print 2  # be printed only if explicitly called

    def show(self):
        print 'hello'

f = Foo('a')
f.show()

print '-' * 100
Foo.__new__(Foo)
# Foo.__new__()
# Foo.__init__(Foo)

print '-' * 100


class Meta(type):

    def __call__(cls):
        obj = cls.__new__(cls)
        obj.__init__()
        return obj


class Foo(object):
    __metaclass__ = Meta

    def __new__(cls):
        print 1
        return object.__new__(cls)

    def __init__(self):
        print 2

    @classmethod
    def show(cls):
        print cls

f = Foo()
f.show()  # <class '__main__.Foo'>
print f.__new__  # <function __new__ at ...>
print Foo.__new__  # <function __new__ at ...>
f.__new__(Foo)
Foo.__new__(Foo)
print Foo.__init__  # <unbound method Foo.__init__>
# <bound method Foo.__init__ of <__main__.Foo object at ...>>
print f.__init__
f.__init__()  # 2
print f.show  # <bound method Meta.show of <class '__main__.Foo'>>
print Foo.show  # <bound method Meta.show of <class '__main__.Foo'>>
"""
f.__new__()  # TypeError: __new__() takes exactly 1 argument (0 given)
Foo.__new__()  # TypeError: __new__() takes exactly 1 argument (0 given)
"""
