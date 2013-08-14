from datetime import date, timedelta, datetime




today = date.today()
other_day = datetime.strptime('2013-08-15', '%Y-%m-%d').date()

day_delta = (today - other_day).days

print abs(day_delta)

print type(today.year)

print datetime.now() # fit for django datetime field
