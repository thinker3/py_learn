from datetime import datetime

s = '20130824 09:32:12'
time = datetime.strptime(s, '%Y%m%d %H:%M:%S')
print time
print type(time)

s = datetime.strftime(time, '%Y/%m/%d %H:%M:%S')
print s
print type(s)
