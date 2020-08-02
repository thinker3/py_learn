#!/usr/bin/env python
# -*- coding: utf-8 -*-

assert 2 ** 8 == 256
try:
    chr(256)  # chr() arg not in range(256)
except Exception as e:
    print(type(e), e)

assert bin(4) == '0b100'
assert bin(100) == '0b1100100'
assert int('0b1100100', 2) == 100

assert oct(8) == '010'
assert oct(100) == '0144'
assert 0o144 == 0o144
assert int('0144', 8) == 100

assert hex(16) == '0x10'  # no function xxx(16) == 0x10
assert hex(100) == '0x64'
assert int('0x64', 16) == 100

# ord order?
assert ord('d') == 100 == 0x64 == 0o144 == 0b1100100
assert chr(100) == chr(0x64) == chr(0o144) == chr(0b1100100) == 'd'

assert ord('中') == 20013
assert chr(20013) == '中'


def convert_0x_to_char(type_0x):
    type_0x_list = type_0x.split(' ')
    int_list = [int(one, 16) for one in type_0x_list]
    assert int_list == [15, 110, 15, 100, 14]
    char_list = list(map(chr, int_list))
    return char_list


def convert_char_to_0x(char_list):
    int_list = list(map(ord, char_list))
    assert int_list == [15, 110, 15, 100, 14]
    hex_list = list(map(hex, int_list))
    return hex_list


assert convert_0x_to_char('0xf 0x6e 0xf 0x64 0xe') == ['\x0f', 'n', '\x0f', 'd', '\x0e']
assert convert_char_to_0x(['\x0f', 'n', '\x0f', 'd', '\x0e']) == ['0xf', '0x6e', '0xf', '0x64', '0xe']
