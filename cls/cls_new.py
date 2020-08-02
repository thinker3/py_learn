#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import (
    date,
)


class Person(object):

    def __new__(cls, *args, **kwargs):
        print('doing Person.__new__...')
        assert cls is Person
        print(args)
        print(kwargs)
        # TypeError: object.__new__() takes exactly one argument (the type to instantiate)
        return super().__new__(cls)

    def __init__(self, name, birthday):
        print('doing Person.__init__...')
        self.name = name
        self.birthday = birthday

    def __call__(self, *args, **kwargs):
        print('doing Person.__call__...')
        # AttributeError: 'super' object has no attribute '__call__'
        # return super().__call__(*args, **kwargs)
        print(args)
        print(kwargs)

    @property
    def age(self):
        return (date.today() - self.birthday).days // 365

    def introduce(self):
        print(f'My name is {self.name}, I am {self.age} years old.')


if __name__ == '__main__':
    jack = Person('Jack', birthday=date(1998, 1, 1))
    jack.introduce()
    jack('a', b=2)
