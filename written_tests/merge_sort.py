#!/usr/bin/env python
# encoding: utf-8


import random
import datetime as dt


def merge(left, right):
    temp = []
    left_i = right_i = 0
    while left_i < len(left) and right_i < len(right):
        if left[left_i] < right[right_i]:
            temp.append(left[left_i])
            left_i += 1
        else:
            temp.append(right[right_i])
            right_i += 1
    if left_i < len(left):
        temp.extend(left[left_i:])
    if right_i < len(right):
        temp.extend(right[right_i:])
    return temp


'''
def merge(left, right):
    temp = []
    while left and right:
        if left[0] < right[0]:
            temp.append(left.pop(0))
        else:
            temp.append(right.pop(0))
    if left:
        temp += left
    if right:
        temp += right
    return temp
'''


def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) / 2
    left = array[:mid]
    right = array[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

a = 6
sample = random.sample(xrange(10 ** a), 10 ** (a - 1))
#print sample
before = dt.datetime.now()
result = merge_sort(sample)
delta = (dt.datetime.now() - before)
print delta.total_seconds()
#print result
