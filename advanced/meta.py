#!/usr/bin/env python
# -*- coding: utf-8 -*-


def class_maker(name, *args, **kwargs):
    return type(name, *args, **kwargs)


print('-' * 30)
print(class_maker.__name__)
B = class_maker('Foo', (object,), {'x': 1})
f = B()
print(f.x)
print(B.__name__)
print(B.__base__)


def class_maker(name, args, kwargs):
    for k in kwargs:
        if k.startswith('_'):
            kwargs[k] = 0
    return type(name, args, kwargs)


print('-' * 30)
C = class_maker('Foo', (object,), {'_x': 1, 'y': 2})
c = C()
print(c._x)
print(c.y)

print('-' * 30)
print(type.__new__)


class Printable(type):
    def whoami(cls):  # noqa
        print("I am a", cls.__name__)  # instance method


D = Printable('Foo', (), {})  # D is an instance
D.whoami()


class Bar(object, metaclass=Printable):
    def foomethod(self):
        print('foo')


Bar.whoami()  # Bar is an instance just as D
print(Bar.__base__)  # Bar is not a subclass of Printable but its instance
Bar().foomethod()


class Final(type):
    def __new__(cls, name, bases, classdict):
        print(classdict)
        for b in bases:
            if isinstance(b, Final):
                raise TypeError("Sealed class %s!" % b.__name__)
        return type.__new__(cls, name, bases, classdict)

    def show(self):
        print(self.__name__)


print('-' * 30)


class Foo(object, metaclass=Final):
    def hello(self):
        print('hello')


#class Bar(Foo): pass
Foo.show()
Foo().hello()


class Call(type):
    def __call__(cls):  # noqa
        print(100)

    def show(self):
        print(self.__name__)


print('-' * 30)


class Foo(object, metaclass=Call):
    pass


Foo.show()
f = Foo()
print(f)
