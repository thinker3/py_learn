#!/usr/bin/env python
# encoding: utf-8


import random
import datetime as dt


def half(n):
    while n > 1:
        n = n / 2
        yield n


def shell_sort(array):
    for i in half(len(array)):
        sub_sort(array, i)
    return array


def sub_sort(array, k):
    for i in xrange(k, len(array)):
        temp = array[i]
        j = i - k
        while j > -1 and array[j] > temp:
            array[j + k] = array[j]
            j -= k
        array[j + k] = temp


a = 7
sample = random.sample(xrange(10 ** a), 10 ** (a - 1))
#print sample
before = dt.datetime.now()
result = shell_sort(sample)
delta = (dt.datetime.now() - before)
print delta.total_seconds()
#print result
