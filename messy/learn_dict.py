#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_sub_dict(less, more):
    return less.viewitems() <= more.viewitems()


def dict_has_subset(more, less):
    for k, v in less.iteritems():
        if k not in more:
            return False
        if more[k] != v:
            return False
    return True


def test_is_sub_dict():
    less = {'a': 1}
    more = {'a': 1, 'b': 2}
    assert is_sub_dict(less, more)
    assert dict_has_subset(more, less)
    less.update(a='a')
    assert is_sub_dict(less, more) is False
    assert dict_has_subset(more, less) is False


if __name__ == '__main__':
    test_is_sub_dict()
