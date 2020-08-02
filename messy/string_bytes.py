#!/usr/bin/env python
# encoding: utf-8

# bitarray, bitstring


def to_hex(s):
    print(s)
    print([c.encode('hex') for c in s])


to_hex('hello')
to_hex('hello')
to_hex(r'hello')
to_hex(b'hello')

to_hex('\r\n')
to_hex('\r\n')
to_hex(r'\r\n')
to_hex(b'\r\n')

to_hex('中文')
#to_hex(u'中文')
to_hex(r'中文')
to_hex(b'中文')


def to_utf_16_be(s):
    print(s)
    print([c.encode('utf_16_be') for c in s])


to_utf_16_be('hello')
to_utf_16_be('\r\n')
#to_utf_16_be('中文')
to_utf_16_be('中文')
#to_utf_16_be(r'中文')
#to_utf_16_be(b'中文')
