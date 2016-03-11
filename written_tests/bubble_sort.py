#!/usr/bin/env python
# encoding: utf-8

import random
import datetime as dt


def bubble(array):
    '''
    length = len(array)
    for i in xrange(length - 1):
        for j in xrange(i + 1, length):
            if array[j] < array[i]:
                array[i], array[j] = array[j], array[i]
    '''
    end = len(array) - 1
    for i in xrange(end, 0, -1):
        for j in xrange(i - 1, -1, -1):
            if array[j] > array[i]:
                array[i], array[j] = array[j], array[i]

a = 5
sample = random.sample(xrange(10 ** a), 10 ** (a - 1))
#print sample
before = dt.datetime.now()
bubble(sample)
delta = (dt.datetime.now() - before)
print delta.total_seconds()
#print sample
