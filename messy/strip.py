#!/usr/bin/env python
# -*- coding: utf-8 -*-


def ltrim(string, sub):
    if string.startswith(sub):
        string = string[len(sub):]
        return ltrim(string, sub)
    return string


def rtrim(string, sub):
    if string.endswith(sub):
        string = string[:len(sub) * -1]
        return rtrim(string, sub)
    return string


def trim(string, sub):
    return ltrim(rtrim(string, sub), sub)


string = 'abccbaxxxbacabc'
assert string.strip('abc') == 'xxx'
assert ltrim(string, 'abc') == 'cbaxxxbacabc'
assert rtrim(string, 'abc') == 'abccbaxxxbac'
assert trim(string, 'abc') == 'cbaxxxbac'


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
