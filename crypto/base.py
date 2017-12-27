#!/usr/bin/env python
# encoding: utf-8

import base64
import simplecrypt

text = 'hello world'
coded = base64.b64encode(text)
print type(coded)  # <type 'str'>
print coded
text = coded.decode('base64')
print text
text = base64.b64decode(coded)
print text

crypted = simplecrypt.encrypt('test', text)
print crypted
coded = base64.b64encode(crypted)
print coded
crypted = coded.decode('base64')
print crypted
text = simplecrypt.decrypt('test', crypted)
print text
