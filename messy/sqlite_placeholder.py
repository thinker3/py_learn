import sqlite3 as lite
from datetime import date
day = date.today()

conn = lite.connect('lite.db')
cur = conn.cursor()
cur.execute('''create table if not exists days(day)''')
cur.execute('''insert into days values('%s')''' % day)
#cur.execute('''insert into days values(%s)''' % day)
#cur.execute('''insert into days values(?)''', (day, ))
conn.commit()
cur.execute('''select day from days''')
day = cur.fetchone()
print(day)
conn.close()

