#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import uuid
import string
from struct import (
    pack,
    unpack,
)
import urllib.request, urllib.parse, urllib.error
import shortuuid
from datetime import (
    datetime,
)
import collections
from utils import defines


class JustObject(object): pass


def get_an_obj():
    return JustObject()


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


def deep_update(source, override):
    for key, override_value in override.items():
        source_value = source.get(key)
        if all([
            isinstance(source_value, collections.Mapping),
            isinstance(override_value, collections.Mapping),
        ]):
            deep_update(source_value, override_value)
        else:
            source[key] = override[key]
    return source


def get_uuid4():
    return str(uuid.uuid4())


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


def pack_json_objects_to_length_limited_stream(data, encoding='utf-8'):
    data = [json.dumps(one, ensure_ascii=False).encode(encoding) for one in data]
    data = [(len(one), one) for one in data]
    data = [pack(">I", length) + bstr for (length, bstr) in data]
    data = b''.join(data)
    return data


def unpack_length_limited_stream_to_json_objects(data, encoding='utf-8'):
    objs = []
    while data:
        length, data = data[:4], data[4:]
        length = unpack('>I', length)[0]
        jd, data = data[:length], data[length:]
        jd = jd.decode(encoding)
        obj = json.loads(jd)
        objs.append(obj)
    return objs


def pack_json_object_to_length_comma_limited_stream(obj, encoding='utf-8'):
    byte_data = json.dumps(obj, ensure_ascii=False).encode(encoding)
    length = str(len(byte_data)).encode()
    stream = length + b',' + byte_data
    return stream


def pack_json_objects_to_length_comma_limited_stream(data, encoding='utf-8'):
    data = [json.dumps(one, ensure_ascii=False).encode(encoding) for one in data]
    data = [(len(one), one) for one in data]
    data = [str(length).encode() + b',' + bstr for (length, bstr) in data]
    data = b''.join(data)
    return data


def unpack_length_comma_limited_stream_to_json_objects(data, encoding='utf-8'):
    objs = []
    while data:
        index = data.find(b',')
        if index > 0:
            length, data = data[:index], data[index + 1:]
            length = int(length.decode())
            jd, data = data[:length], data[length:]
            if len(jd) == length:
                jd = jd.decode(encoding)
                obj = json.loads(jd)
                objs.append(obj)
            else:
                data = str(length).encode() + b',' + jd
                break
        else:
            break
    return objs, data


if __name__ == '__main__':
    __import__('ipdb').set_trace()
    pass
