#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Crypto.Cipher import AES


class AesEcb(object):
    def __init__(self, key="abcdefgh12345678", padding=b' '):
        self.aes = AES.new(key, AES.MODE_ECB)
        self.padding = padding

    def encrypt(self, data):
        length = len(data)
        number = AES.block_size - length % AES.block_size
        data += self.padding * number
        return self.aes.encrypt(data)

    def decrypt(self, data):
        return self.aes.decrypt(data).rstrip(self.padding)

if __name__ == '__main__':
    data = b'hello '
    encrypted_data = AesEcb().encrypt(data)
    print(encrypted_data)
    decrypted_data = AesEcb().decrypt(encrypted_data)
    print(decrypted_data)
