#!/usr/bin/env python
# encoding: utf-8

import random
import datetime as dt

a = 7
b = 6
sample = random.sample(xrange(10 ** a), 10 ** b)
print type(sample)
#print sample


def quick_sort(array):
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
    lesser = quick_sort(lesser)
    greater = quick_sort(greater)
    return lesser + [pivot] + greater

before = dt.datetime.now()
#print quick_sort(sample)
quick_sort(sample)
delta = (dt.datetime.now() - before)
assert isinstance(delta, dt.timedelta)
print delta.total_seconds()


class QuickSortNoRecursion(object):
    def __init__(self, array):
        self.array = array
        self.max_sub = len(array)
        self.max_temp = 0

    def quick_sort_one(self, array):
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
                second += self.quick_sort_one(sub)
            first = second
            self.max_sub = self.max_temp
        self.result = [j for i in first for j in i]

a = 6
b = 5
sample = random.sample(xrange(10 ** a), 10 ** b)
before = dt.datetime.now()
sorting = QuickSortNoRecursion(sample)
sorting.run()
delta = (dt.datetime.now() - before)
print delta.total_seconds()
#print sorting.result


class QuickSortNoRecursion(object):
    def __init__(self, array):
        self.array = array

    def seek(self, start, end):
        pivot = self.array[start]
        hole = pos = start
        while pos < end:
            pos += 1
            if self.array[pos] < pivot:
                self.array[hole] = self.array[pos]
                self.shift(hole, pos)
                hole += 1
        self.array[hole] = pivot
        if start < hole - 1:
            self.temp.append((start, hole - 1))
        if hole + 1 < end:
            self.temp.append((hole + 1, end))

    def shift(self, hole, pos):
        self.array[hole] = self.array[pos]
        self.array[hole + 2: pos + 1] = self.array[hole + 1: pos]
        '''
        for i in xrange(pos, hole + 1, -1):  # reversed xrange
            self.array[i] = self.array[i - 1]
        '''

    def run(self):
        length = len(self.array)
        if length <= 1:
            return
        partitions = [(0, length - 1)]
        while partitions:
            self.temp = []
            for one in partitions:
                self.seek(*one)
            partitions = self.temp

a = 5
b = 4
sample = random.sample(xrange(10 ** a), 10 ** b)
#print sample
before = dt.datetime.now()
sorting = QuickSortNoRecursion(sample)
sorting.run()
delta = (dt.datetime.now() - before)
print delta.total_seconds()
#print sample


class QuickSortNoRecursion(object):
    def __init__(self, array):
        self.array = array

    def seek(self, start, end):
        pivot = self.array[start]
        lesser = []
        greater = []
        for i in self.array[start + 1: end + 1]:
            if i < pivot:
                lesser.append(i)
            else:
                greater.append(i)
        self.array[start: end + 1] = lesser + [pivot] + greater
        pos = start + len(lesser)
        if start < pos - 1:
            self.temp.append((start, pos - 1))
        if pos + 1 < end:
            self.temp.append((pos + 1, end))

    def run(self):
        length = len(self.array)
        if length <= 1:
            return
        partitions = [(0, length - 1)]
        while partitions:
            self.temp = []
            for one in partitions:
                self.seek(*one)
            partitions = self.temp

a = 7
b = 6
sample = random.sample(xrange(10 ** a), 10 ** b)
#print sample
before = dt.datetime.now()
sorting = QuickSortNoRecursion(sample)
sorting.run()
delta = (dt.datetime.now() - before)
print delta.total_seconds()
#print sample
