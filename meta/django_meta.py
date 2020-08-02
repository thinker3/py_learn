#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Options(object):
    def __init__(self, meta):
        self.abstract = meta.abstract


class ModelBase(type):
    def __new__(metacls, name, bases, attrs):
        super_new = super().__new__
        parents = [b for b in bases if isinstance(b, ModelBase)]
        if not parents:
            return super_new(metacls, name, bases, attrs)
        module = attrs.pop('__module__')
        new_attrs = {'__module__': module}
        new_class = super_new(metacls, name, bases, new_attrs)
        meta = attrs.pop('Meta', None)
        meta.abstract = getattr(meta, 'abstract', False)
        new_class._meta = Options(meta)
        meta.abstract = False
        new_class.Meta = meta
        return new_class


class Model(metaclass=ModelBase):
    pass


class BaseModel(Model):
    class Meta:
        abstract = True


class Person(BaseModel):
    class Meta(BaseModel.Meta):
        pass


assert BaseModel._meta.abstract is True
assert BaseModel.Meta.abstract is False
assert Person._meta.abstract is False
assert Person.Meta.abstract is False
