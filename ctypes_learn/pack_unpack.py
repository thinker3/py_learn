#!/usr/bin/env python
# -*- coding: utf-8 -*-

import struct


def test_little_endian():
    fmt = '<hhl'
    data = (1, 2, 3)
    packed = struct.pack(fmt, *data)
    assert packed == b'\x01\x00\x02\x00\x03\x00\x00\x00'
    unpacked = struct.unpack(fmt, packed)
    assert unpacked == data
    size = struct.calcsize(fmt)
    assert size == 2 + 2 + 4


def test_big_endian():
    fmt = '>hhl'
    data = (1, 2, 3)
    packed = struct.pack(fmt, *data)
    assert packed == b'\x00\x01\x00\x02\x00\x00\x00\x03'
    unpacked = struct.unpack(fmt, packed)
    assert unpacked == data
    size = struct.calcsize(fmt)
    assert size == 2 + 2 + 4


def test_B(integer, hex_data):  # noqa
    fmt = '>B'
    # data = ('1',)  # struct.error: cannot convert argument to integer
    # data = (256,)  # struct.error: ubyte format requires 0 <= number <= 255
    data = (integer,)
    packed = struct.pack(fmt, *data)
    assert packed == hex_data
    unpacked = struct.unpack(fmt, packed)
    assert unpacked == data
    size = struct.calcsize(fmt)
    assert size == 1


def test_nB(n):  # noqa
    fmt = '>%dB' % n
    data = tuple(range(n))
    packed = struct.pack(fmt, *data)
    print('%s, %r, %r' % (fmt, data, packed))
    unpacked = struct.unpack(fmt, packed)
    assert unpacked == data
    size = struct.calcsize(fmt)
    assert size == n


def test_B_special():  # noqa
    fmt = '>B'
    assert struct.unpack(fmt, b'\x0a') == (10,)
    assert struct.unpack(fmt, b'\n') == (10,)
    assert struct.unpack(fmt, b' ') == (32,)
    assert struct.unpack(fmt, b'1') == (49,)
    assert struct.unpack(fmt, b'A') == (65,)
    assert struct.unpack(fmt, b'a') == (97,)


def test_H(integer, hex_data):  # noqa
    fmt = '>H'
    # struct.error: 'H' format requires 0 <= number <= 65535
    data = (integer,)
    packed = struct.pack(fmt, *data)
    assert packed == hex_data
    unpacked = struct.unpack(fmt, packed)
    assert unpacked == data
    size = struct.calcsize(fmt)
    assert size == 2


def test_I(integer, hex_data):  # noqa
    fmt = '>I'
    # struct.error: 'I' format requires 0 <= number <= 4294967295
    data = (integer,)
    packed = struct.pack(fmt, *data)
    assert packed == hex_data
    unpacked = struct.unpack(fmt, packed)
    assert unpacked == data
    size = struct.calcsize(fmt)
    assert size == 4


def test_nI(integers, hex_data):
    n = len(integers)
    assert struct.pack('>%dI' % n, *integers) == hex_data
    assert struct.unpack('>%dI' % n, hex_data) == integers


if __name__ == '__main__':
    test_little_endian()
    test_big_endian()
    test_B(1, b'\x01')
    test_B(10, b'\n')
    test_B(255, b'\xff')
    test_nB(1)
    test_nB(3)
    test_B_special()
    test_H(1, b'\x00\x01')
    test_I(1, b'\x00\x00\x00\x01')
    test_I(2 ** 32 - 2, b'\xff\xff\xff\xfe')
    test_nI((255, 65535), b'\x00\x00\x00\xff\x00\x00\xff\xff')
    test_nI((255, 65535), b'\x00\x00\x00\xff' + b'\x00\x00\xff\xff')
    assert struct.pack('>1s', b'') == b'\x00'
    assert struct.pack('>1s', b'0') == b'0'
    for i in range(32, 127): print(f"{i}: {hex(i)}, '{chr(i)}'")
