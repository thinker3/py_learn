#!/usr/bin/env python
# -*- coding: utf-8 -*-

import types
from datetime import (
    date,
)


class ABase(object):
    def say_hello(self):
        print('hello...')


class AType(type):
    def __new__(meta, name, bases, attrs, **kwargs):
        print('doing AType.__new__...')
        assert meta is AType
        print(name)
        print(bases)
        for key, value in attrs.items():
            print(f'{key}: {value}')
            if type(value) is types.FunctionType:
                print(f'    {key} is a function')
        print(kwargs)
        # TypeError: __init_subclass__() takes no keyword arguments
        return super().__new__(meta, name, bases, attrs)

    def __init__(cls, name, bases, attrs, **kwargs):
        print('doing AType.__init__...')
        assert isinstance(cls, AType)
        print(kwargs)
        return super().__init__(name, bases, attrs, **kwargs)

    def __call__(cls, *tp, **dic):
        print('doing AType.__call__...')
        assert isinstance(cls, AType)
        print(tp)
        print(dic)
        dic.pop('sex')
        return super().__call__(*tp, **dic)


class Person(ABase, metaclass=AType, gender=2):
    here = True

    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday

    @property
    def age(self):
        return (date.today() - self.birthday).days // 365

    def introduce(self):
        print(f'My name is {self.name}, I am {self.age} years old.')


if __name__ == '__main__':
    jack = Person('Jack', birthday=date(1998, 1, 1), sex=1)
    jack.introduce()
