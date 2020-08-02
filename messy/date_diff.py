#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import sleep
from datetime import date, timedelta, datetime

from utils.decorators import isolate
from utils.functions import divide


@isolate
def test():
    today = date.today()
    yesterday = today - timedelta(days=1)
    print('yesterday is %s' % yesterday)
    print(yesterday.year)
    print(yesterday.month)
    print(yesterday.day)
    print(today - yesterday > timedelta(days=1))

    divide(length=10)
    other_day = datetime.strptime('2013-08-15', '%Y-%m-%d').date()
    day_delta = today - other_day
    print('today > %s is %s' % (other_day, today > other_day))
    print(day_delta, type(day_delta))
    # ## TypeError: can't compare datetime.timedelta to int
    # print 'day_delta > 1 is %s' % (day_delta > 1)
    print('day_delta > 1 is %s' % (day_delta > timedelta(days=1)))
    days = day_delta.days
    print(days, type(days))

    divide(length=10)
    first = datetime.strptime('2014-04-08', '%Y-%m-%d').date()
    second = datetime.strptime('2014-10-31', '%Y-%m-%d').date()
    days_of_a_year = 365.0
    leave_days = 10.0
    print((second - first).days * leave_days / days_of_a_year)
    third = datetime.strptime('2015-02-15', '%Y-%m-%d').date()
    print((third - first).days * leave_days / days_of_a_year)
    divide(length=10)

test()


@isolate
def delta_test():
    before = datetime.now()  # fit for django datetime field
    print(before)
    sleep(2)
    now = datetime.now()
    print((datetime.today() - before))
    print((datetime.today() - before).days)
    yesterday = datetime.strptime('2015-08-19 16:30:09', '%Y-%m-%d %H:%M:%S')
    print((date.today() - yesterday))
    delta = now - before
    print(now, type(now))
    print(delta, type(delta))
    print(dir(delta))
    # AttributeError: 'datetime.timedelta' object has no attribute 'total_seconds'
    # print delta.total_seconds(), type(delta.total_seconds())
    print(delta.days, type(delta.days))
    print(delta.seconds, type(delta.seconds))
    print(delta.microseconds, type(delta.microseconds))

delta_test()


@isolate
def compare_test():
    before = datetime.utcnow()
    sleep(2)
    now = datetime.utcnow()
    delta = timedelta(seconds=1)
    print('now - before > delta is %s' % (now - before > delta))
    print('before < now - delta is %s' % (before < now - delta))

compare_test()
