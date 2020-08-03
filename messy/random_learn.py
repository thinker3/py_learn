#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

print('random float:')
print(random.uniform(1.2, 3.6))

print('*' * 30)
for i in range(10):
    print(random.randint(0, 3))  # integers in [0, 3]
print('*' * 30)
for i in range(10):
    print(random.randrange(0, 1), random.randint(0, 1))

print('*' * 30)
numbers = list(range(0, 20))
print(numbers)
some_numbers = random.sample(numbers, 5)
print(some_numbers)
print(random.choice(some_numbers))

print('*' * 30)
random.seed(0)
print(random.random())
random.seed(0)
print(random.random())
print(random.random())

a = list(range(10))
print(a)
random.shuffle(a)
print(a)
