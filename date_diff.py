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

print '*' * 30
first = datetime.strptime('2014-04-08', '%Y-%m-%d').date()
second = datetime.strptime('2014-10-31', '%Y-%m-%d').date()
days_of_a_year = 365.0
leave_days = 10.0
print (second - first).days * leave_days / days_of_a_year
third = datetime.strptime('2015-02-15', '%Y-%m-%d').date()
print (third - first).days * leave_days / days_of_a_year
print '*' * 30

print type(today.year)

before = datetime.now() # fit for django datetime field
print before
sleep(2)
now = datetime.now()
delta = now - before
print now, type(now)
print delta, type(delta)
print dir(delta)
# AttributeError: 'datetime.timedelta' object has no attribute 'total_seconds'
#print delta.total_seconds(), type(delta.total_seconds())
print delta.days, type(delta.days)
print delta.seconds, type(delta.seconds)
print delta.microseconds, type(delta.microseconds)
