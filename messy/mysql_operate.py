#!/usr/bin/env python
#coding=utf8

import MySQLdb as mysql

DB_HOST = '192.168.0.6'
DB_NAME = 'test'
DB_USER = 'chenkun'
DB_PASSWORD = 'ck1234'

conn = mysql.connect(host=DB_HOST, db=DB_NAME, user=DB_USER, passwd=DB_PASSWORD, charset='') # charset is the key of messed encoding
cur = conn.cursor()
#sql = 'alter table words add example varchar(255)'
#sql = 'alter table words drop analysed_flag'
#sql = "insert into words(id,name,phonetic,meaning,example) values(2,'world','wd','','hello world')"
#sql = "insert into words(name,phonetic,meaning,example) values('world','wd','世界','hello world')"
#sql = "update words set meaning='世界'"
meaning = '哈哈3'
example = '哈哈4'
meaning = meaning.encode('utf8')
example = example.encode('utf8')
sql = "update words set meaning=%s, example=%s where id=%d"
#sql = "delete from words where id>2"
try:
    r = cur.execute(sql, [meaning, example, 2])
except:
    r = 0
conn.commit()
cur.close()
conn.close()
print(r)

