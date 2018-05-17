#!/usr/bin/env python
# -*- coding: utf-8 -*-

import operator

li = [1, 5, 3, 2, 7]
assert li.sort() is None
assert li == [1, 2, 3, 5, 7]

li = [(3, 'ab'), (2, 'ac'), (1, 'ad'), (2, 'aa')]
li.sort(key=lambda x: x[0])  # order_by
assert li == [(1, 'ad'), (2, 'ac'), (2, 'aa'), (3, 'ab')]
li.sort(key=lambda x: x[1])
assert li == [(2, 'aa'), (3, 'ab'), (2, 'ac'), (1, 'ad')]
li.sort(key=lambda x: x[1], reverse=True)  # order_by
assert li == [(1, 'ad'), (2, 'ac'), (3, 'ab'), (2, 'aa')]
li.sort(key=operator.itemgetter(0, 1))  # order_by
assert li == [(1, 'ad'), (2, 'aa'), (2, 'ac'), (3, 'ab')]


class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age


people = [
    Person('Jim', 5),
    Person('Tom', 3),
    Person('Bob', 9),
]
people.sort(key=operator.attrgetter('age'), reverse=True)  # order_by
ages = [person.age for person in people]
assert ages == [9, 5, 3]
