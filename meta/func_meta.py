#!/usr/bin/env python
# -*- coding: utf-8 -*-


def get_type_string(cls):
    return f'{cls.__module__}.{cls.__name__}'


class IntegerField(object):
    def __init__(self, name=None, db_column=None):
        self.name = name
        self.db_column = db_column


class AliasFieldMixin(object):
    def say_hello(self):
        print('hello...')


def say_hi(self):
    print(f'hi, {self.db_column}')


def makeAliasField(target_field, *args, **kwargs):
    cls = type(
        "AliasField",
        (AliasFieldMixin, target_field.__class__),
        {'say_hi': say_hi}
    )
    assert issubclass(cls, AliasFieldMixin)
    assert issubclass(cls, IntegerField)
    return cls(db_column=target_field.name, *args, **kwargs)


class AliasField(object):
    pass


if __name__ == '__main__':
    obj = AliasField()
    assert type(obj) is AliasField
    pid = IntegerField('id')
    assert type(pid) is IntegerField
    pk = makeAliasField(pid)
    Class = type(pk)
    assert get_type_string(Class) == get_type_string(AliasField) == '__main__.AliasField'
    assert not (Class is AliasField)
    pk.say_hello()
    pk.say_hi()
