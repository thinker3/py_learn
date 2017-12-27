#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import rsa
import keys
import base64

encrypted = sys.argv[1]
encrypted = base64.b64decode(encrypted)

privkey = rsa.PrivateKey.load_pkcs1(keys.privkey)
decrypted = rsa.decrypt(encrypted, privkey)
print decrypted
