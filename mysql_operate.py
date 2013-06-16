#!/usr/bin/env python
#coding=utf-8

import MySQLdb as mysql

DB_HOST = '192.168.0.6'
DB_NAME = 'test'
DB_USER = 'chenkun'
DB_PASSWORD = 'ck1234'

conn = mysql.connect(host=DB_HOST, db=DB_NAME, user=DB_USER, passwd=DB_PASSWORD,charset='utf8')
cur = conn.cursor()
#sql = 'alter table words add example varchar(255)'
#sql = 'alter table words drop analysed_flag'
#sql = "insert into words(id,name,phonetic,meaning,example) values(2,'world','wd','','hello world')"
#sql = "insert into words(name,phonetic,meaning,example) values('world','wd','世界','hello world')"
#sql = "update words set meaning='世界'"
#sql = "update words set meaning='哈罗' where id<2"
sql = "delete from words where id>2"
r = cur.execute(sql)
conn.commit()
cur.close()
conn.close()
print r

