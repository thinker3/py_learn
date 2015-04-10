#!/usr/bin/env python
# encoding: utf-8

import random

sample = random.sample(xrange(100), 20)
print type(sample)
print sample


def qsort(array):
    if len(array) <= 1:
        return array
    elif len(array) == 2:
        a, b = array
        if a < b:
            return [a, b]
        else:
            return [b, a]
    pivot = array[0]
    lesser = []
    greater = []
    for i in array[1:]:
        if i < pivot:
            lesser.append(i)
        else:
            greater.append(i)
    lesser = qsort(lesser)
    greater = qsort(greater)
    return lesser + [pivot] + greater

print qsort(sample)


class QuickSortNoRecursion(object):
    def __init__(self, array):
        self.array = array
        self.max_sub = len(array)
        self.max_temp = 0

    def qsort_one(self, array):
        if len(array) <= 1:
            self.max_temp = max(self.max_temp, 0)
            return [array]
        elif len(array) == 2:
            self.max_temp = max(self.max_temp, 1)
            a, b = array
            if a < b:
                return [[a], [b]]
            else:
                return [[b], [a]]
        pivot = array[0]
        lesser = []
        greater = []
        for i in array[1:]:
            if i < pivot:
                lesser.append(i)
            else:
                greater.append(i)
        r = filter(None, [lesser, [pivot], greater])
        self.max_temp = max(self.max_temp, max(map(len, r)))
        return r

    def run(self):
        first = [self.array]
        while self.max_sub > 1:
            second = []
            self.max_temp = 0
            for sub in first:
                second += self.qsort_one(sub)
            first = second
            self.max_sub = self.max_temp
        self.result = [j for i in first for j in i]

sorting = QuickSortNoRecursion(sample)
sorting.run()
print sorting.result
