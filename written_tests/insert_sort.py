#!/usr/bin/env python
# encoding: utf-8


import random
import datetime as dt


def insert_sort(array):
    temp = [array[0]]
    for i in array[1:]:
        if i <= temp[0]:
            temp.insert(0, i)
            continue
        elif i >= temp[-1]:
            temp.append(i)
            continue
        else:
            for j in xrange(1, len(temp)):
                if temp[j -1] <= i <= temp[j]:
                    temp.insert(j, i)
                    break
    return temp

a = 5
sample = random.sample(xrange(10 ** a), 10 ** (a - 1))
#print sample
before = dt.datetime.now()
result = insert_sort(sample)
delta = (dt.datetime.now() - before)
print delta.total_seconds()
#print result
