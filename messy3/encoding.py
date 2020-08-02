#!/usr/bin/env python
# -*- coding: utf-8 -*-

s = '中文'
gbk = s.encode('gbk')
utf = s.encode('utf-8')

with open('encoding.bak', 'wb') as f:
    f.write(gbk)
    f.write(utf)

with open('encoding.bak', 'rb') as f:
    content = f.readline()
    assert content == b'\xd6\xd0\xce\xc4' + b'\xe4\xb8\xad\xe6\x96\x87'

with open('encoding.bak', 'wb') as f:
    f.write(utf)
    f.write(gbk)

with open('encoding.bak', 'rb') as f:
    content = f.readline()
    assert content == b'\xe4\xb8\xad\xe6\x96\x87' + b'\xd6\xd0\xce\xc4'

with open('encoding.bak', 'r') as f:
    try:
        content = f.readline()
    except UnicodeDecodeError as e:
        print(e)

with open('encoding.bak', 'r') as f:
    content = f.buffer.read()
    assert content == b'\xe4\xb8\xad\xe6\x96\x87' + b'\xd6\xd0\xce\xc4'
