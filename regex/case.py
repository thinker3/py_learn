#!/usr/bin/env python
# encoding: utf-8

import re

print re.IGNORECASE  # 2
print re.search('abc', 'OABCD')  # None
# case sensitive
print re.search('abc', 'OABCD', 0)  # None
# case insensitive
print re.search('abc', 'OABCD', re.I)  # <_sre.SRE_Match object at 0x7f4629aa6308>
