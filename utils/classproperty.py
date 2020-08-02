#!/usr/bin/env python
# -*- coding: utf-8 -*-


class ClassPropertyMeta(type):
    def __new__(meta, name, bases, attrs):
        for k, v in attrs.items():
            if type(v) is ClassProperty:
                setattr(meta, k, v)
        return super().__new__(meta, name, bases, attrs)


class ClassProperty(object):
    def __init__(self, fget):
        self.fget = fget

    def setter(self, fset):
        self.fset = fset
        return self

    def __get__(self, instance, instance_type):
        if instance_type is ClassPropertyMeta:
            return self.fget(instance)
        return self.fget(instance_type)

    def __set__(self, obj, value):
        self.fset(obj, value)


#----------------------------------------------------------------------------------------------------------------------


def _create_type(meta, name, attrs):
    type_name = f'{name}Type'
    type_attrs = {}
    for k, v in attrs.items():
        if type(v) is _ClassPropertyDescriptor:
            type_attrs[k] = v
    return type(type_name, (meta,), type_attrs)


class ClassPropertyType(type):
    def __new__(meta, name, bases, attrs):
        Type = _create_type(meta, name, attrs)
        cls = super().__new__(meta, name, bases, attrs)
        cls.__class__ = Type
        return cls


class _ClassPropertyDescriptor(object):
    def __init__(self, fget, fset=None):
        self.fget = fget
        self.fset = fset

    def __get__(self, obj, owner):
        if self in obj.__dict__.values():
            return self.fget(obj)
        return self.fget(owner)

    def __set__(self, obj, value):
        if not self.fset:
            raise AttributeError("can't set attribute")
        return self.fset(obj, value)

    def setter(self, func):
        self.fset = func
        return self


def classproperty(func):
    return _ClassPropertyDescriptor(func)


#----------------------------------------------------------------------------------------------------------------------


class _ClassGetter(object):
    def __init__(self, fget):
        self.fget = fget

    def __get__(self, instance, instance_type):
        return self.fget(instance_type)


def classgetter(func):
    return _ClassGetter(func)
