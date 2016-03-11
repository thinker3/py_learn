#!/usr/bin/env python
#coding: utf8

# http://strftime.org/

import time
import datetime as dt


def parse_format():
    now = dt.datetime.now()
    s = dt.datetime.strftime(now, '%Y_%m_%d__%H_%M_%S__%f')
    print s
    print

    s = '20130824 09:32:12'
    time = dt.datetime.strptime(s, '%Y%m%d %H:%M:%S')
    print time
    print type(time)  # <type 'datetime.datetime'>
    print

    s = dt.datetime.strftime(time, '%Y/%m/%d %H:%M:%S')
    print s
    print type(s)  # <type 'str'>
    print

    some_day = dt.datetime.strptime('07/13/2007', '%m/%d/%Y')
    some_day = some_day.strftime('%m %B %Y')
    print some_day


def total_seconds():
    before = dt.datetime.now()
    time.sleep(1)
    now = dt.datetime.now()
    delta = now - before
    seconds = delta.total_seconds()
    print type(seconds)  # <type 'float'>
    print '%s seconds' % seconds
    print '%f seconds' % seconds


def how_many_days_past_in_a_year():
    some_day = dt.datetime.strptime('May 5 2007', '%B %d %Y').date()
    assert isinstance(some_day, dt.date)
    year = some_day.year
    print type(year)  # <type 'int'>
    first_day_of_a_year = '%s/01/01' % year
    first_day_of_a_year = dt.datetime.strptime(first_day_of_a_year, '%Y/%m/%d').date()
    day_delta = (some_day - first_day_of_a_year).days + 1
    print some_day, first_day_of_a_year
    print day_delta


def to_timestamp(t=None):
    if not t:
        t = dt.datetime.now()
    delta = t - dt.datetime(1970, 1, 1)
    print delta.total_seconds()

#parse_format()
#total_seconds()
#how_many_days_past_in_a_year()
to_timestamp()
