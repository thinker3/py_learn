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
