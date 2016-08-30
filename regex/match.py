#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

samples = [
    " 0 M - 12 M ",
    " 0 - 12 M ",
]
for sample in samples:
    result = re.match("\s*(\d+)\s*(\w*)\s*-\s*(\d+)\s*(\w+)\s*", sample)
    if result:
        print result.group()
        print result.groups()
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


def process_match(m):
    return '<li></li>'

p = re.compile(r'<li>(.*?)</li>')
print p.sub(process_match, s, re.S)
