#!/usr/bin/env python
#coding=utf8
import psycopg2
import sys

sql = '''
alter table sample_form_type_mapping add column categoryindex INTEGER;
alter table sample_stock add column index INTEGER;
alter table sample_stock add column report_name Text;
'''
print sql


designer_x_category = [
    u'Design',
    u'Artwork',
    u'Solidworks',
    u'Sampling',
    u'PrintOut',
    u'File',
]
conn_string = "host='192.168.21.157' port='5433' dbname='tribal_live_20140328' user='postgres' password='admin'"
conn = psycopg2.connect(conn_string)
cursor = conn.cursor()
cursor.execute("SELECT id, category FROM sample_form_type_mapping order by id")
records = cursor.fetchall()

print
for id, category in records:
    sql = '''update sample_form_type_mapping set categoryindex=%d where id=%d;''' % (designer_x_category.index(category), id)
    print sql


name__report_name = [
    (u'CCNB ', u'CCNB'),
    (u'C1S ', u'C1S'),
    (u'C2S ', u'C2S'),
    (u'FMW ', u'FMW'),
    (u'EMW ', u'EMW'),
    (u'EK ', u'EK'),
    (u'BMW ', u'BMW'),
    (u'BK ', u'BK'),
    (u'CMW ', u'CMW'),
    (u'CK ', u'CK'),
    (u'BCK ', u'BCK'),
    (u'BE-MW ', u'BEMW'),
    (u'Target E ', u'Target E'),
    (u'Target B ', u'Target B'),
    (u'Epson - Semi Gloss Paper (44" x 40")', u'Semi Gloss Paper'),
    (u'Epson - Woodfree Paper (42" x 40")', u'Woodfree Paper'),
    (u'Epson - Label (36" x 40")', u'Epson Label'),
]
cursor.execute("SELECT id, name FROM sample_stock")
records = cursor.fetchall()
d = {}
for id, name in records:
    d[name] = id

print
for i, (name, report_name) in enumerate(name__report_name):
    sql = '''update sample_stock set index=%d, report_name='%s' where id=%d;''' % (i, report_name, d[name])
    print sql

print
sql = '''update sample_stock set active=1 where id=33;'''
print sql
