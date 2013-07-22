import binascii
a = binascii.b2a_hex('123abc')
print a
b = binascii.a2b_hex(a)
print b
