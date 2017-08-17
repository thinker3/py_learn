#!/usr/bin/env python
# encoding: utf-8

import random
from utils.decorators import show_time_interval


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
    eqal = [pivot]
    lesser = []
    greater = []
    for i in array[1:]:
        if i < pivot:
            lesser.append(i)
        elif i == pivot:
            eqal.append(i)
        else:
            greater.append(i)
    lesser = quick_sort(lesser)
    greater = quick_sort(greater)
    return lesser + eqal + greater


class QuickSortNoRecursion(object):
    def __init__(self, array):
        self.array = array

    def seek(self, start, end):
        pivot = self.array[start]
        eqal = [pivot]
        lesser = []
        greater = []
        for i in self.array[start + 1: end + 1]:
            if i < pivot:
                lesser.append(i)
            elif i == pivot:
                eqal.append(i)
            else:
                greater.append(i)
        self.array[start: end + 1] = lesser + eqal + greater
        if len(lesser) > 1:
            pos = start + len(lesser)
            self.temp.append((start, pos - 1))
        if len(greater) > 1:
            pos = start + len(lesser) + len(eqal)
            self.temp.append((pos, end))

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


a = 6
b = 5
sample = random.sample(xrange(10 ** a), 10 ** b)
print type(sample)
# print sample
show_length = 20


@show_time_interval
def test_quick_sort():
    sorted_list = quick_sort(sample)
    print sorted_list[:show_length]


@show_time_interval
def test_quick_sort_no_recursion():
    sorting = QuickSortNoRecursion(sample)
    sorting.run()
    print sorting.array[:show_length]


if __name__ == '__main__':
    test_quick_sort()
    test_quick_sort_no_recursion()
