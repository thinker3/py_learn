#!/usr/bin/env python
# -*- coding: utf-8 -*-


class MetaMetaclass(type):
    def __new__(meta, name, bases, attrs):
        def _new_(meta, _name, bases, attrs):
            cls = super().__new__(meta, _name, bases, attrs)
            cls._label = '%s is made in %s' % (_name, name)
            return cls
        attrs['__new__'] = _new_
        return super().__new__(meta, name, bases, attrs)


class China(type, metaclass=MetaMetaclass):
    pass


class USA(type, metaclass=MetaMetaclass):
    pass


class Mi(metaclass=China):
    pass


class Mac(object, metaclass=USA):
    pass


assert Mi._label == 'Mi is made in China'
assert Mac._label == 'Mac is made in USA'
