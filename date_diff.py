from datetime import date, timedelta, datetime
from time import sleep

the_last_day = date.today() + timedelta(days=19)
print the_last_day
print the_last_day.year
print the_last_day.month
print the_last_day.day



today = date.today()
other_day = datetime.strptime('2013-08-15', '%Y-%m-%d').date()

day_delta = (today - other_day).days

print abs(day_delta)

print type(today.year)

before = datetime.now() # fit for django datetime field
sleep(2)
now = datetime.now()
delta = now - before
print now, type(now)
print delta, type(delta)
print dir(delta)
print delta.total_seconds(), type(delta.total_seconds())
print delta.days, type(delta.days)
print delta.seconds, type(delta.seconds)
print delta.microseconds, type(delta.microseconds)

