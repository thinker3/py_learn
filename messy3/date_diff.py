#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import date
from dateutil.relativedelta import relativedelta  # pip install python-dateutil


def add_months(the_day, months):
    return the_day + relativedelta(months=months)


if __name__ == '__main__':
    the_day = date(2019, 8, 31)
    assert add_months(the_day, 1) == date(2019, 9, 30)
    assert add_months(the_day, 2) == date(2019, 10, 31)
