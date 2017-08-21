#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib


class DictObject(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def update(self, **kwargs):
        self.__dict__.update(kwargs)

    def __str__(self):
        return str(self.__dict__)

    @property
    def _dict(self):
        return self.__dict__


def dict2query(params):
    query = []
    for k, v in params.iteritems():
        if type(v) in ['list', 'tuple', 'set']:
            for i in v:
                temp = '%s=%s' % (k, i)
                query.append(temp)
        else:
            temp = '%s=%s' % (k, v)
            query.append(temp)
    query = '&'.join(query)
    return query


def get_url(base_url, params=None):
    base_url = urllib.quote(base_url.encode('utf-8'), safe=':/')
    if not params:
        return base_url
    query_string = urllib.urlencode(params, doseq=True)
    url = '%s?%s' % (base_url, query_string)
    return url


class Dict(dict):

    def __setattr__(self, name, value):
        self[name] = value

    def __getattr__(self, name):
        return self[name]


def test_DictObject():
    do = DictObject(a=1, b=2)
    print do
    do.update(c=3)
    print do
    dao = DictObject(**do._dict)
    print dao


def test_Dict():
    do = Dict(a=1, b=2)
    print do
    temp = {'a': 1, 'b': 2}
    do = Dict(temp)
    print do
    do = Dict(**do)
    print do
    do = Dict()
    do.a = 1
    print do.a
    do.update(b=2)
    print do.b


if __name__ == '__main__':
    # test_DictObject()
    # test_Dict()
    pass
