#!/usr/bin/env python
# encoding: utf-8


def convert_hex_string_to_decimal_int(hex_string):
    # int16
    return int(hex_string, 16)


def convert_binary_string_to_decimal_int(binary_string):
    # int2
    return int(binary_string, 2)


def invert(i):
    d = {
            '0': '1',
            '1': '0',
            }
    s = map(lambda v: d[v], bin(i)[2:])
    s = '0b' + ''.join(s)
    i = convert_binary_string_to_decimal_int(s)
    return s, i

mode_with_quick_edit = 231
mode_without_quick_edit = 167
quick_edit = 0x40

# ~: complement, invert, inverse, inversion, bitwise not
# ^: bitwise xor, exclusive or
print mode_with_quick_edit & (~quick_edit)
print mode_without_quick_edit | quick_edit
print quick_edit  # 64
print ~quick_edit  # -65, ~n = -n - 1
print bin(~64)
print bin(64)
s, i = invert(quick_edit)
print s, i
print mode_with_quick_edit & (~64)
print mode_without_quick_edit | 64
print mode_with_quick_edit & i  # so, does not work
print mode_with_quick_edit & (-65)

v = hex(mode_with_quick_edit)
print type(v), v
v = convert_hex_string_to_decimal_int(v)
print type(v), v
