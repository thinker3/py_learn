#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rsa
from . import keys

secret = 'hello'
pubkey = open('./pubkey.pem', 'rb').read()
pubkey = rsa.PublicKey.load_pkcs1(pubkey)
privkey = open('./privkey.pem', 'rb').read()
privkey = rsa.PrivateKey.load_pkcs1(privkey)

encrypted = rsa.encrypt(secret, pubkey)
decrypted = rsa.decrypt(encrypted, privkey)
print(decrypted, decrypted == secret)

secret = 'world'
pubkey = rsa.PublicKey.load_pkcs1(keys.pubkey)
encrypted = rsa.encrypt(secret, pubkey)
privkey = rsa.PrivateKey.load_pkcs1(keys.privkey)
decrypted = rsa.decrypt(encrypted, privkey)
print(decrypted, decrypted == secret)
