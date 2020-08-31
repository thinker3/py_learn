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

assert oct(8) == '0o10'
assert oct(100) == '0o144'
assert int('0144', 8) == int('0o144', 8) == 100

assert hex(16) == '0x10'  # no function xxx(16) == 0x10
assert hex(100) == '0x64'
assert int('0x64', 16) == 100

# ord order?
assert ord('d') == 100 == 0x64 == 0o144 == 0b1100100
assert chr(100) == chr(0x64) == chr(0o144) == chr(0b1100100) == 'd'

assert ord('中') == 20013
assert chr(20013) == '中'


def hex_literal_to_char(hex_literal):
    return chr(int(hex_literal, 16))


def char_to_hex_literal(char):
    return hex(ord(char))


assert hex_literal_to_char('0x0') == '\x00' != b'\x00'
assert hex_literal_to_char('0x00') == '\x00'
assert hex_literal_to_char('0x1f') == '\x1f'
assert hex_literal_to_char('0x20') == ' '
assert hex_literal_to_char('0x41') == 'A'

assert char_to_hex_literal('\x00') == '0x0' != '0x00'
assert char_to_hex_literal('\x1f') == '0x1f'
assert char_to_hex_literal(' ') == '0x20'
assert char_to_hex_literal('A') == '0x41'


def hex_literal_to_byte_literal(hex_literal):
    return rf'\x{hex_literal[2:]}'


assert hex_literal_to_byte_literal('0x0') == r'\x0'
assert hex_literal_to_byte_literal('0x00') == r'\x00'
assert hex_literal_to_byte_literal('0x1f') == r'\x1f'


if __name__ == '__main__':
    pass
