#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_PKCS1_v1_5
from base64 import b64decode, b64encode

pubkey = 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQChixw4y0BDtlufNiwby9UTpampVdduYgBmCRdwJKfY/SPe/jGIdbmq1FONZiVBYArcfkVt4sDZpQ4Qh8nmNhU1kwOXYnehmPUVaWLo5lhd+OsGHbE+P6ZzvSG8f8R/BNK5uHSucC2mwsqG5nmfCwTLLaCnr4uu+EahTvDqW6AhMQIDAQAB'
msg = "test" * 1000
keyDER = b64decode(pubkey)
keyPub = RSA.importKey(keyDER)
cipher = Cipher_PKCS1_v1_5.new(keyPub)
cipher_text = cipher.encrypt(msg.encode())  # ValueError: Plaintext is too long
emsg = b64encode(cipher_text)
print emsg

# ValueError: RSA modulus length must be a multiple of 256 and >= 1024
key = RSA.generate(1024)
binPrivKey = key.exportKey('DER')
binPubKey = key.publickey().exportKey('DER')
print repr(binPubKey)
print b64encode(binPubKey)
privKeyObj = RSA.importKey(binPrivKey)
pubKeyObj = RSA.importKey(binPubKey)
msg = "attack at dawn"
emsg = pubKeyObj.encrypt(msg, 'x')[0]
dmsg = privKeyObj.decrypt(emsg)
assert(msg == dmsg)
