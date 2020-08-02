#!/usr/bin/env python
# encoding: utf-8

from io import BytesIO
bio = BytesIO()
bio.write(b"some initial binary data")
bio.write(b', abc')
print(bio.read(10))
print(bio.getvalue())
