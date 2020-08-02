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
