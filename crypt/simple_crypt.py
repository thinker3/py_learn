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


def size(n):
    plaintext = 'a' * n
    key = 'python'
    ciphertext = encrypt(key, plaintext)
    print n, len(ciphertext)
    plaintext = decrypt(key, ciphertext)
    #print ciphertext
    print '[%s]' % plaintext


def test_size():
    size(0)
    size(1)
    size(2)
    size(8)
    size(9)
    size(10)
    size(16)
    size(17)
    size(18)

'''
right()
print
wrong()
'''
test_size()
