from datetime import date, timedelta
day = date.today()
#year = day.year()

print 'hello (%s) world' % day

import sqlite3 as lite

conn = lite.connect('lite.db')
cur = conn.cursor()
cur.execute('''create table if not exists days(day)''')
sql = '''insert into days values(%s)''' % day
print sql
sql = '''insert into days values('%s')''' % day
print sql
cur.execute(sql)
conn.commit()
cur.execute('''select day from days''')
day = cur.fetchone()
print day
conn.close()

