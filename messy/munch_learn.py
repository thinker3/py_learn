#!/usr/bin/env python
# -*- coding: utf-8 -*-

from munch import Munch


def test():
    data = {
        'a': 1,
        'b': 2,
    }
    obj = Munch(**data)
    for k, v in obj.iteritems():
        print k, v
    print obj.keys()
    print obj.values()
    assert obj.a == 1
    obj.update(b=-2)
    data = dict(**obj)
    assert data['b'] == -2


class DictObject(Munch):
    pass


def test_DictObject():  # noqa
    data = {
        'a': 1,
        'b': 2,
    }
    obj = DictObject(data)
    assert obj.a == 1


if __name__ == '__main__':
    test()
    test_DictObject()
    pass
