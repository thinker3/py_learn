#!/usr/bin/env python
# -*- coding: utf-8 -*-


class HelloType(type):
    def greet(cls):
        print(f'Hi, {cls.name}')

    @property
    def greeting(cls):
        return f'Hi, {cls.name}'


class Hello(metaclass=HelloType):
    name = 'Jack'


if __name__ == '__main__':
    assert isinstance(type, type)
    assert issubclass(type, type)
    assert isinstance(object, object)
    assert issubclass(object, object)

    assert isinstance(type, object)
    assert isinstance(object, type)
    assert issubclass(type, object)
    assert issubclass(object, type) is False

    assert isinstance(HelloType, type)
    assert issubclass(HelloType, type)
    assert isinstance(Hello, HelloType)
    assert issubclass(Hello, HelloType) is False

    assert isinstance(HelloType, object)
    assert issubclass(HelloType, object)
    assert isinstance(Hello, object)
    assert issubclass(Hello, object)

    Hello.greet()
    print(Hello.greeting)
