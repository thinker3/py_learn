#!/usr/bin/env python
# encoding: utf-8

# sudo pip install simple-crypt

from simplecrypt import encrypt, decrypt


def right():
    plaintext = 'hello world'

    key = 'python'
    ciphertext = encrypt(key, plaintext)
    print ciphertext

    key = 'password'
    ciphertext = encrypt(key, plaintext)
    print ciphertext

    plaintext = decrypt(key, ciphertext)
    print plaintext


def wrong():
    plaintext = 'hello world'

    key = 'password'
    ciphertext = encrypt(key, plaintext)
    print ciphertext

    key = 'python'
    plaintext = decrypt(key, ciphertext)
    print plaintext

right()
print
wrong()
