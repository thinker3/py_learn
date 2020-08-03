#!/usr/bin/env python
# -*- coding: utf-8 -*-

sample = [3, 5, 2, 6, 9, 0, 1, 2, 5, 3]


def quick_sort(array):
    if len(array) <= 1:
        return array
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


print(quick_sort(sample))


class QuickSort(object):
    def __init__(self, array):
        self.array = array

    def sort(self, start, end):
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
            self.unsorted.append((start, pos - 1))
        if len(greater) > 1:
            pos = start + len(lesser) + len(eqal)
            self.unsorted.append((pos, end))

    def run(self):
        length = len(self.array)
        partitions = [(0, length - 1)]
        while partitions:
            self.unsorted = []
            for one in partitions:
                self.sort(*one)
            partitions = self.unsorted


sorter = QuickSort(sample)
sorter.run()
print(sorter.array)
