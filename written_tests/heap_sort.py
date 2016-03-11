#!/usr/bin/env python
# encoding: utf-8

import heapq
import random
import datetime as dt


def build(array):
    heapq.heapify(array)


def heap_sort(array):
    build(array)
    temp = []
    while array:
        smallest = heapq.heappop(array)
        temp.append(smallest)
    return temp


a = 7
sample = random.sample(xrange(10 ** a), 10 ** (a - 1))
#print sample
before = dt.datetime.now()
result = heap_sort(sample)
delta = (dt.datetime.now() - before)
print delta.total_seconds()
#print result
