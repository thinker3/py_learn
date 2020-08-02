#!/usr/bin/env python
# encoding: utf-8

import hashlib


def separate():
    print('*' * 50)


def small(s='hello world'):
    separate()
    m = hashlib.md5(s)
    # <md5 HASH object @ 0x7fb8709359e0> <type '_hashlib.HASH'>
    print(m, type(m))
    #assert isinstance(m, HASH)
    print(m.digest_size)
    print(m.digest())
    print(m.hexdigest())


def large(n=10):
    separate()
    m = hashlib.md5()
    s = '*' * 100
    while n > 0:
        m.update(s)
        n -= 1
    print(m.hexdigest())


#small()
#small('How to get MD5 sum of a string?')
large()
small('*' * 1000)
large(100)
small('*' * 10000)

separate()
