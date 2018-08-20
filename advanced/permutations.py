#!/usr/bin/env python
#coding=utf-8

import itertools
from permutation import Permutation


def test_permutations():
    t = itertools.permutations(range(1, 5))
    s = 0
    even = []
    odd = []
    for i in t:
        pm = Permutation(*i)
        if pm.is_even:
            even.append(i)
        else:
            odd.append(i)
        s += 1
    print('even:')
    for one in even:
        print(one)
    print('odd:')
    for one in odd:
        print(one)
    print(s)


def test_combinations():
    s = 0
    for one in itertools.combinations(range(4), 3):
        print(one)
        s += 1
    print(s)


def test_zip():
    print('*' * 20)
    more = ['a', 'b', 'c', 'd', 'e']
    less = [1, 2, 3]
    s = 0
    for one in itertools.combinations(more, len(less)):
        for two in itertools.permutations(one):
            for a, b in zip(two, less):
                print(a, b)
            print()
            s += 1
    print(s)


def my_permutations(n):
    ans = [[0]]
    if n <= 0:
        return ans
    i = 1
    temp = []
    while i < n + 1:
        for one in ans:
            for j in range(i + 1):
                two = one[:]
                two.insert(j, i)
                temp.append(two)
        ans = temp
        temp = []
        i += 1
    return ans


def test_my_permutations():
    print('*' * 20)
    ans = my_permutations(3)
    for one in ans:
        print(one)
    print(len(ans))


test_permutations()
