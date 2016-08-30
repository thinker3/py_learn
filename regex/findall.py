#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import regex

result = re.findall("[a-z]\d", "a1b2c3")
print result
print '*' * 30

sample = "taatbbtctdd"
result = re.findall("t..", sample)
print result  # ['taa', 'tbb', 'tct']

result = regex.findall("t..", sample, overlapped=True)
print result
print '*' * 30

sample = "Customer number: 232454, Date: February 12, 2011"
nums = re.findall("[0-9]+", sample)
print nums
print '*' * 30

result = re.findall('(\D)([\d.]+)', u'语80.5外92数96.5')
print repr(result).decode('unicode-escape')
print '*' * 30

s = (
    '''
    <ul>
        <li>something</li>
        <li>something else</li>
        <li>and more</li>
        <li>even more</li>
    </ul>
    '''
)
p = re.compile(r'<li>.*?</li>')
print p.findall(s)
p = re.compile(r'<li>(.*?)</li>')
print p.findall(s)
