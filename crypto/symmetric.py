#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES


def unicode_to_utf8(s):
    if isinstance(s, unicode):
        s = s.encode("utf-8")
    return s


def digest(key):
    return hashlib.sha256(key).digest()


class AESCipher(object):
    def __init__(self, key):
        self.bs = 16
        self.key = key

    def encrypt(self, message):
        message = self._pad(unicode_to_utf8(message))
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(message))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:]))

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s) - 1:])]


def test_AESCipher(data):  # noqa
    key = 'mahxeecha4ipai2B'
    crypto = AESCipher(key)
    encrypted = crypto.encrypt(data)
    print repr(encrypted)
    decrypted = crypto.decrypt(encrypted)
    print decrypted


if __name__ == '__main__':
    data = 'hello'
    test_AESCipher(data)
    data = u'你好'
    test_AESCipher(data)
