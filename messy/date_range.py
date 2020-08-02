#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import (
    date,
    timedelta,
)


def date_range(start_date, end_date, with_end=False):
    for ordinal in range(start_date.toordinal(), end_date.toordinal()):
        yield date.fromordinal(ordinal)
    if with_end:
        yield end_date


def daterange(start_date, end_date, with_end=False):
    days = (end_date - start_date).days
    for n in range(days):
        yield start_date + timedelta(n)
    if with_end:
        yield end_date


if __name__ == '__main__':
    start_date = date(2010, 12, 29)
    end_date = date(2011, 1, 2)
    for one in date_range(start_date, end_date, True):
        print(one, one.strftime("%Y-%m-%d"))
    print()
    for one in daterange(start_date, end_date, True):
        print(one, one.strftime("%Y-%m-%d"))
