from datetime import datetime
from time import sleep

s = '20130824 09:32:12'
time = datetime.strptime(s, '%Y%m%d %H:%M:%S')
print time
print type(time)

s = datetime.strftime(time, '%Y/%m/%d %H:%M:%S')
print s
print type(s)

before = datetime.now()
sleep(1)
now = datetime.now()
delta = now - before
print '%s seconds' % delta.total_seconds()
print '%f seconds' % delta.total_seconds()

print
some_day = datetime.strptime('07/13/2007', '%m/%d/%Y')
some_day = some_day.strftime('%m %B %Y')
print some_day

some_day = datetime.strptime('May 5 2007', '%B %d %Y').date()
first_day = datetime.strptime('01/01/2007', '%m/%d/%Y').date()
day_delta = (some_day - first_day).days + 1
print some_day, first_day
print day_delta
