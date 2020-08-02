#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import string
import urllib.request, urllib.parse, urllib.error
import shortuuid
from datetime import (
    datetime,
)

from utils import defines


class DictObject(object):
    _invalid_keys = (
        'update',
        '_data',
        '_safety_check',
        '__dict__',
    )

    def __init__(self, **kwargs):
        self._safety_check(kwargs)
        self.__dict__.update(kwargs)

    def update(self, **kwargs):
        self._safety_check(kwargs)
        self.__dict__.update(kwargs)

    @property
    def _data(self):
        return self.__dict__

    def _safety_check(self, kwargs):
        for key in self._invalid_keys:
            assert key not in kwargs

    def __getattr__(self, key):
        return self.__dict__.get(key)

    def __str__(self):
        return str(self.__dict__)


def dict2query(params):
    query = []
    for k, v in params.items():
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
    base_url = urllib.parse.quote(base_url.encode('utf-8'), safe=':/')
    if not params:
        return base_url
    query_string = urllib.parse.urlencode(params, doseq=True)
    url = '%s?%s' % (base_url, query_string)
    return url


class Dict(dict):

    def __setattr__(self, name, value):
        self[name] = value

    def __getattr__(self, name):
        return self[name]


def test_DictObject():  # noqa
    do = DictObject(a=1, b=2)
    print(do)
    do.update(c=3)
    print(do)
    dao = DictObject(**do._data)
    print(dao)


def test_Dict():  # noqa
    do = Dict(a=1, b=2)
    print(do)
    temp = {'a': 1, 'b': 2}
    do = Dict(temp)
    print(do)
    do = Dict(**do)
    print(do)
    do = Dict()
    do.a = 1
    print(do.a)
    do.update(b=2)
    print(do.b)


def format_time(t, fmt=defines.COMMON_TIME_FMT):
    return t.strftime(fmt)


def format_date(d, fmt=defines.COMMON_DATE_FMT):
    return d.strftime(fmt)


def format_datetime(dt, fmt=defines.COMMON_DATETIME_FMT):
    return dt.strftime(fmt)


def parse_datetime(dt_str, fmt=defines.COMMON_DATETIME_FMT):
    return datetime.strptime(dt_str, fmt)


def get_now():
    return datetime.now()


def get_now_str(fmt=defines.COMMON_DATETIME_FMT):
    return format_datetime(get_now(), fmt)


def get_uuid(length=10, letters_only=False):
    alphabet = None
    if letters_only:
        alphabet = list(string.letters)
    return shortuuid.ShortUUID(alphabet).random(length=length)


def convert_to_string(value):
    if isinstance(value, str):
        return value.encode('utf-8')
    if isinstance(value, (list, tuple, dict)):
        return json.dumps(value, ensure_ascii=False)
    return str(value)


if __name__ == '__main__':
    # test_DictObject()
    # test_Dict()
    pass
