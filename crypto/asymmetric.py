#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rsa
from base64 import b64encode

secret = 'hello' * 1000
pubkey, privkey = rsa.newkeys(512)
print(pubkey)
print(pubkey.save_pkcs1())
print(repr(pubkey.save_pkcs1('DER')))
print(b64encode(pubkey.save_pkcs1('DER')))
print(privkey)
print(privkey.save_pkcs1())

pubkey = rsa.PublicKey(
    7415502624357151701843602000555318455948573542840931625729150638611638251360782052774127447815979830851875097447216767147242437831115031378524678172264921,
    65537,
)
privkey = rsa.PrivateKey(
    7415502624357151701843602000555318455948573542840931625729150638611638251360782052774127447815979830851875097447216767147242437831115031378524678172264921,
    65537,
    5677294416545159019180046849533288120103448090575457288569207215654347148007043218092439893759997074589438975571531525440203012025002055883676278902503473,
    4446231151572194572272541834440666920306217930405766286220328832524851462544515341,
    1667817612616703003339597571420391729959720600059564280837759069331120381,
)
print(pubkey)
print(pubkey.save_pkcs1())
print(privkey)
print(privkey.save_pkcs1())

print()
crypto = rsa.encrypt(secret, pubkey)  # OverflowError, if secret is too long
print('encrypted msg:', repr(crypto))
msg = rsa.decrypt(crypto, privkey)
print(msg)

token = 'Doo4Laijooveibodee5aV6co8eeL3eeb'
signature = rsa.sign(token, privkey, 'SHA-256')
print('signature:', repr(signature))
is_valid = rsa.verify(token, signature, pubkey)
print(is_valid)
