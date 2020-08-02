#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Field(object):
    def __init__(self, value=0):
        self._value = value

    def get_value(self):
        return self._value

    def __get__(self, instance, owner):
        print(f'instance: {instance}')
        assert owner is Model
        if instance:
            assert type(instance) is owner
        return self._value

    def __set__(self, instance, value):
        self._value = value


class Model(object):
    status = Field()


status = Model.__dict__['status']


if __name__ == '__main__':
    print(Field.get_value)  # function, not unbound method
    print(Field.__dict__['get_value'])

    assert Field()._value == 0  # Field.__get__ not called

    model = Model()
    assert model.status == 0
    assert Model.status == 0

    model.status = 1
    status_here = Model.__dict__['status']
    assert status_here is status
    assert Model.status == 1
    print(status_here)

    Model.status = 2  # Field.__set__ not called
    status_here = Model.__dict__['status']
    assert not (status_here is status)
    assert Model.status == 2
    print(status_here)
