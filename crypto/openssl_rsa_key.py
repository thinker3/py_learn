#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rsa

pub = open('./pub.pem', 'rb').read()

pubkey = rsa.PublicKey.load_pkcs1(pub)
__import__('ipdb').set_trace()
print(pubkey)
