#!/usr/bin/env python
# -*- coding: utf-8 -*-

import decimal
from decimal import (
    Decimal,
    # getcontext,
    localcontext,
)


def test():
    a = Decimal(1.50)
    print a
    b = Decimal(3.00)
    print b

    print a + b
    print a - b
    print a * b
    print a / b

    print 2 + a
    print 2 - a
    print 2 * a
    print 2 / a
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


# https://docs.python.org/2/library/decimal.html#decimal.Decimal.quantize
TWO_PLACES = Decimal("0.01")


def test_quantize():
    x = Decimal('1.125')
    print x
    print x.quantize(TWO_PLACES)
    print x.quantize(TWO_PLACES, decimal.ROUND_HALF_DOWN)


def test_ROUND_CEILING():
    x = Decimal('1.120')
    print x.quantize(TWO_PLACES, decimal.ROUND_CEILING)
    x = Decimal('1.121')
    print x.quantize(TWO_PLACES, decimal.ROUND_CEILING)


def test_ROUND_FLOOR():
    x = Decimal('1.129')
    print x.quantize(TWO_PLACES, decimal.ROUND_FLOOR)
    x = Decimal('1.120')
    print x.quantize(TWO_PLACES, decimal.ROUND_FLOOR)


def test_ROUND_UP():
    x = Decimal('1.120')
    print x.quantize(TWO_PLACES, decimal.ROUND_UP)
    x = Decimal('1.121')
    print x.quantize(TWO_PLACES, decimal.ROUND_UP)
    x = Decimal('-1.121')
    print x.quantize(TWO_PLACES, decimal.ROUND_UP)
    x = Decimal('-1.121')
    print x.quantize(TWO_PLACES, decimal.ROUND_CEILING)


def test_ROUND_DOWN():  # truncate
    x = Decimal('1.1')
    print x.quantize(TWO_PLACES, decimal.ROUND_DOWN)
    x = Decimal('1.120')
    print x.quantize(TWO_PLACES, decimal.ROUND_DOWN)
    x = Decimal('1.129')
    print x.quantize(TWO_PLACES, decimal.ROUND_DOWN)
    x = Decimal('-1.129')
    print x.quantize(TWO_PLACES, decimal.ROUND_DOWN)
    x = Decimal('-1.129')
    print x.quantize(TWO_PLACES, decimal.ROUND_FLOOR)


def test_ROUND_HALF_UP():
    x = Decimal('1.124')
    print x.quantize(TWO_PLACES, decimal.ROUND_HALF_UP)
    x = Decimal('1.125')
    print x.quantize(TWO_PLACES, decimal.ROUND_HALF_UP)
    x = Decimal('1.126')
    print x.quantize(TWO_PLACES, decimal.ROUND_HALF_UP)


def test_ROUND_HALF_DOWN():
    x = Decimal('1.124')
    print x.quantize(TWO_PLACES, decimal.ROUND_HALF_DOWN)
    x = Decimal('1.125')
    print x.quantize(TWO_PLACES, decimal.ROUND_HALF_DOWN)
    x = Decimal('1.126')
    print x.quantize(TWO_PLACES, decimal.ROUND_HALF_DOWN)


def test_ROUND_HALF_EVEN():
    '''
    If the value to be rounded is 5 then the preceding digit is examined.
    Even values cause the result to be rounded down and odd digits cause the result to be rounded up.
    '''
    x = Decimal('1.124')
    print x.quantize(TWO_PLACES, decimal.ROUND_HALF_EVEN)
    x = Decimal('1.125')
    print x.quantize(TWO_PLACES, decimal.ROUND_HALF_EVEN)
    x = Decimal('1.126')
    print x.quantize(TWO_PLACES, decimal.ROUND_HALF_EVEN)
    x = Decimal('1.134')
    print x.quantize(TWO_PLACES, decimal.ROUND_HALF_EVEN)
    x = Decimal('1.135')
    print x.quantize(TWO_PLACES, decimal.ROUND_HALF_EVEN)
    x = Decimal('1.136')
    print x.quantize(TWO_PLACES, decimal.ROUND_HALF_EVEN)


def test_ROUND_05UP():
    # away from zero if last digit after rounding towards zero would have been 0 or 5; otherwise towards zero
    x = Decimal('1.101')
    print x.quantize(TWO_PLACES, decimal.ROUND_05UP)
    x = Decimal('1.151')
    print x.quantize(TWO_PLACES, decimal.ROUND_05UP)
    x = Decimal('1.185')
    print x.quantize(TWO_PLACES, decimal.ROUND_05UP)
    x = Decimal('1.186')
    print x.quantize(TWO_PLACES, decimal.ROUND_05UP)


def test_localcontext():
    with localcontext() as ctx:
        for precision in range(3, 6):
            ctx.prec = precision
            x = decimal.Decimal(78.96) + decimal.Decimal(90.99)
            print x


# test_ROUND_CEILING()
# test_ROUND_FLOOR()
# test_ROUND_UP()
# test_ROUND_DOWN()
# test_ROUND_HALF_UP()
# test_ROUND_HALF_DOWN()
# test_ROUND_HALF_EVEN()
# test_ROUND_05UP()
# test_localcontext()
