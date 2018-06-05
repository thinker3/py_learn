#!/usr/bin/env python
# -*- coding: utf-8 -*-


def trim(s, sub):
    if s.startswith(sub):
        s = s[len(sub):]
    if s.endswith(sub):
        s = s[:len(s) - len(sub)]
    return s


def strip(s, sub):
    sub = set(sub)
    while s:
        if s[0] in sub:
            s = s[1:]
        else:
            break
    while s:
        if s[-1] in sub:
            s = s[:-1]
        else:
            break
    return s


s = 'abcab'
assert s.strip('ab') == 'c'
assert s.strip('ba') == 'c'
assert trim(s, 'ab') == 'c'
assert trim(s, 'ba') == s
assert strip(s, 'ba') == 'c'

s = 'abcba'
assert s.strip('ab') == 'c'
assert s.strip('ba') == 'c'
assert trim(s, 'ab') == 'cba'
assert trim(s, 'ba') == 'abc'
assert strip(s, 'ab') == 'c'
