#coding=utf8
from decimal import Decimal
a = Decimal(1.50)
print a
b = Decimal(3.00)
print b

print a+b
print a-b
print a*b
print a/b

print 2+a
print 2-a
print 2*a
print 2/a
# print 2.+a # TypeError: unsupported operand type(s) for +: 'float' and 'Decimal'

print
c = 0.123
d = Decimal(c)
print c
print d
d = Decimal(str(c))
print d

print
e = Decimal(0.123)
f = float(e)
print e
print f

