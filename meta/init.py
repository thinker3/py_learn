#!/usr/bin/env python
# -*- coding: utf-8 -*-


class classproperty(object):  # noqa
    def __init__(self, getter):
        self.getter = getter

    def __get__(self, instance, owner):
        return self.getter(owner)


@classproperty
def _full_name(cls):
    return f'{cls.__module__}.{cls.__name__}'


class Type(type):
    def __init__(cls, *args, **kwargs):
        cls._full_name = _full_name


class Person(metaclass=Type):
    pass


if __name__ == '__main__':
    assert Person._full_name == '__main__.Person'
    assert Person()._full_name == '__main__.Person'
