#!/usr/bin/env python
# -*- coding: utf-8 -*-

import binascii

s = '\x01\xab\xcda1'
a = binascii.b2a_hex(s)
assert a == '01abcd6131'
b = binascii.a2b_hex(a)
assert b == s

a = binascii.b2a_base64(s)
assert a == 'AavNYTE=\n'
b = binascii.a2b_base64(a)
assert b == s

a = binascii.hexlify(s)
assert a == '01abcd6131'
b = binascii.unhexlify(a)
assert b == s

r = repr(s)
assert r == r"'\x01\xab\xcda1'"
t = eval(r)  # todo
assert s == t
