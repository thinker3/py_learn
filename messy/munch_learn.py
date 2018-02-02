#!/usr/bin/env python
# -*- coding: utf-8 -*-

from munch import Munch  # DictObject


def test():
    data = {
        'a': 1,
        'b': 2,
    }
    obj = Munch(**data)
    assert isinstance(obj, dict)
    for k, v in obj.iteritems():
        print k, v
    print obj.keys()
    print obj.values()
    assert obj.a == 1
    obj.update(b=-2)
    data = dict(**obj)
    assert data['b'] == -2


class DictObject(Munch):
    @property
    def _data(self):
        return self


def test_DictObject():  # noqa
    data = {
        'a': 1,
        'b': 2,
    }
    obj = DictObject(data)
    assert obj.a == 1
    print obj._data
    assert obj._data is obj


if __name__ == '__main__':
    test()
    test_DictObject()
    pass
