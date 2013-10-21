import os

# run in this floder and another folder respectively
print __file__, type(__file__)
filepath = os.path.abspath(__file__)
print filepath
print os.path.dirname(filepath)
print os.path.dirname(__file__)

print '-' * 100
print __name__, type(__name__)


print '-' * 100
class Foo(object):
    def __new__(self):
        print 1

    def __init__(self):
        print 2

f = Foo()

print '-' * 100
class Foo(object):
    def __new__(self):
        print 1
        return object.__new__(self)

    def __init__(self):
        print 2

f = Foo()

print '-' * 100
class Foo(object):
    def __new__(self, name):
        print self
        self.name = name
        return object.__new__(self)

    def __init__(self, name):
        print self
        print self.name
        self.name = name * 2
        print self.name

Foo('Jim')

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
        obj = cls.__new__(cls, *args, **kwargs)
        #obj.__init__(*args, **kwargs)
        return obj

class Foo(object):
    __metaclass__ = Meta

    def __new__(cls, *args, **kwargs):
        print 1
        return object.__new__(cls, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        print 2

    def show(self): print 'hello'

f = Foo('a')
f.show()

print '-' * 100
Foo.__new__(Foo)
#Foo.__new__()
#Foo.__init__(Foo)

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
    def show(cls): print cls

f = Foo()
f.show()
f.__new__(Foo)
f.__init__()
Foo.__new__(Foo)
print f.__new__
print Foo.__new__
print f.__init__
print Foo.__init__
print f.show
print Foo.show
#Foo.__new__()
#Foo.__init__(Foo)




