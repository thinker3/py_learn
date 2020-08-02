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
    assert a == Decimal('1.5')
    b = Decimal(3.00)
    assert b == Decimal('3')

    assert a + b == Decimal('4.5')
    assert a - b == Decimal('-1.5')
    assert a * b == Decimal('4.5')
    assert a / b == Decimal('0.5')

    assert 2 * a  == Decimal('3.0')
    print(2 / a)

    c = Decimal(0.123)
    print(c)
    assert c != Decimal('0.123')
    assert Decimal(str(0.123)) == Decimal('0.123')
    assert float(c) == 0.123


# https://docs.python.org/2/library/decimal.html#decimal.Decimal.quantize
TWO_PLACES = Decimal("0.01")


def test_quantize():  # default, ROUND_HALF_DOWN
    assert Decimal('1.124').quantize(TWO_PLACES) == Decimal('1.12')
    assert Decimal('1.125').quantize(TWO_PLACES) == Decimal('1.12')
    assert Decimal('1.126').quantize(TWO_PLACES) == Decimal('1.13')


def test_ROUND_CEILING():
    assert Decimal('1.120').quantize(TWO_PLACES, decimal.ROUND_CEILING) == Decimal('1.12')
    assert Decimal('1.121').quantize(TWO_PLACES, decimal.ROUND_CEILING) == Decimal('1.13')
    assert Decimal('1.129').quantize(TWO_PLACES, decimal.ROUND_CEILING) == Decimal('1.13')


def test_ROUND_FLOOR():
    assert Decimal('1.120').quantize(TWO_PLACES, decimal.ROUND_FLOOR) == Decimal('1.12')
    assert Decimal('1.129').quantize(TWO_PLACES, decimal.ROUND_FLOOR) == Decimal('1.12')

    assert Decimal('-1.120').quantize(TWO_PLACES, decimal.ROUND_FLOOR) == Decimal('-1.12')
    assert Decimal('-1.121').quantize(TWO_PLACES, decimal.ROUND_FLOOR) == Decimal('-1.13')
    assert Decimal('-1.129').quantize(TWO_PLACES, decimal.ROUND_FLOOR) == Decimal('-1.13')


def test_ROUND_UP():
    assert Decimal('1.120').quantize(TWO_PLACES, decimal.ROUND_UP) == Decimal('1.12')
    assert Decimal('1.121').quantize(TWO_PLACES, decimal.ROUND_UP) == Decimal('1.13')

    assert Decimal('-1.121').quantize(TWO_PLACES, decimal.ROUND_UP) == Decimal('-1.13')
    assert Decimal('-1.129').quantize(TWO_PLACES, decimal.ROUND_UP) == Decimal('-1.13')


def test_ROUND_DOWN():  # truncate
    assert Decimal('1.1').quantize(TWO_PLACES, decimal.ROUND_DOWN) == Decimal('1.10')
    assert Decimal('1.120').quantize(TWO_PLACES, decimal.ROUND_DOWN) == Decimal('1.12')
    assert Decimal('1.121').quantize(TWO_PLACES, decimal.ROUND_DOWN) == Decimal('1.12')
    assert Decimal('1.129').quantize(TWO_PLACES, decimal.ROUND_DOWN) == Decimal('1.12')

    assert Decimal('-1.129').quantize(TWO_PLACES, decimal.ROUND_DOWN) == Decimal('-1.12')



def test_ROUND_HALF_UP():
    assert Decimal('1.125').quantize(TWO_PLACES, decimal.ROUND_HALF_UP) == Decimal('1.13')


def test_ROUND_HALF_DOWN():
    assert Decimal('1.125').quantize(TWO_PLACES, decimal.ROUND_HALF_DOWN) == Decimal('1.12')


def test_ROUND_HALF_EVEN():
    '''
    If the value to be rounded is 5 then the preceding digit is examined.
    Even values cause the result to be rounded down and odd digits cause the result to be rounded up.
    '''
    assert Decimal('1.125').quantize(TWO_PLACES, decimal.ROUND_HALF_EVEN) == Decimal('1.12')
    assert Decimal('1.135').quantize(TWO_PLACES, decimal.ROUND_HALF_EVEN) == Decimal('1.14')

    assert Decimal('1.124').quantize(TWO_PLACES, decimal.ROUND_HALF_EVEN) == Decimal('1.12')
    assert Decimal('1.134').quantize(TWO_PLACES, decimal.ROUND_HALF_EVEN) == Decimal('1.13')

    assert Decimal('1.126').quantize(TWO_PLACES, decimal.ROUND_HALF_EVEN) == Decimal('1.13')
    assert Decimal('1.136').quantize(TWO_PLACES, decimal.ROUND_HALF_EVEN) == Decimal('1.14')

def test_ROUND_05UP():
    assert Decimal('1.100').quantize(TWO_PLACES, decimal.ROUND_05UP) == Decimal('1.10')
    assert Decimal('1.101').quantize(TWO_PLACES, decimal.ROUND_05UP) == Decimal('1.11')
    assert Decimal('1.109').quantize(TWO_PLACES, decimal.ROUND_05UP) == Decimal('1.11')

    assert Decimal('1.150').quantize(TWO_PLACES, decimal.ROUND_05UP) == Decimal('1.15')
    assert Decimal('1.151').quantize(TWO_PLACES, decimal.ROUND_05UP) == Decimal('1.16')
    assert Decimal('1.159').quantize(TWO_PLACES, decimal.ROUND_05UP) == Decimal('1.16')

    assert Decimal('1.120').quantize(TWO_PLACES, decimal.ROUND_05UP) == Decimal('1.12')
    assert Decimal('1.121').quantize(TWO_PLACES, decimal.ROUND_05UP) == Decimal('1.12')
    assert Decimal('1.129').quantize(TWO_PLACES, decimal.ROUND_05UP) == Decimal('1.12')

    assert Decimal('1.170').quantize(TWO_PLACES, decimal.ROUND_05UP) == Decimal('1.17')
    assert Decimal('1.171').quantize(TWO_PLACES, decimal.ROUND_05UP) == Decimal('1.17')
    assert Decimal('1.179').quantize(TWO_PLACES, decimal.ROUND_05UP) == Decimal('1.17')


def test_localcontext():
    values = []
    x = decimal.Decimal(169.95)
    print(x)
    with localcontext() as ctx:
        for precision in range(3, 7):
            ctx.prec = precision
            values.append(x + 0)
    assert values == [
        Decimal(170),
        Decimal('169.9'),
        Decimal('169.95'),
        Decimal('169.950'),
    ]


if __name__ == '__main__':
    test()
    test_quantize()
    test_ROUND_CEILING()
    test_ROUND_FLOOR()
    test_ROUND_UP()
    test_ROUND_DOWN()
    test_ROUND_HALF_UP()
    test_ROUND_HALF_DOWN()
    test_ROUND_HALF_EVEN()
    test_ROUND_05UP()
    test_localcontext()
