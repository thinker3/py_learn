#!/usr/bin/env python
# -*- coding: utf-8 -*-


def test(a=1, b=2, **kwargs):
    print(a, b, kwargs)


test()
test(100)
test(100, 200)
test(100, b=200)
test(a=100, b=200)


def test_star(a=1, *, b=2, **kwargs):
    print(a, b, kwargs)


test_star()
test_star(100)
# test_star(100, 200)  # TypeError
test_star(100, b=200)
test_star(a=100, b=200)


def test_star_2(*, a=1, b=2):
    print(a, b)


test_star_2()
# test_star_2(100)  # TypeError
test_star_2(a=100)
test_star_2(b=200)
test_star_2(a=100, b=200)


def test_star_3(a=1, *args, b=2, **kwargs):
    print(args, a, b, kwargs)


test_star_3()
test_star_3(100)
test_star_3(b=200)
test_star_3('a', b=200)
test_star_3('a', 'b', b=200)
