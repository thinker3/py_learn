#!/usr/bin/env python
#coding=utf8
import sqlite3 as lite
import MySQLdb as mysql
import MySQLdb.cursors as cursors

def init_conn(db=None, what='mysql'):
    if what == 'sqlite':
        if db:
            conn = lite.connect(db)
            return conn
        else:
            print 'db is None'
            return None
    HOST = '192.168.0.6'
    DB = 'chenkun_digikey' if db is None else db
    USER = 'chenkun'
    PASSWD = 'ck1234'
    conn = mysql.connect(host=HOST,port=3306,user=USER,passwd=PASSWD,\
            db=DB,use_unicode=1,charset='utf8')
    return conn

def get_cur_conn(db=None, return_dict=False, what='mysql'):
    conn = init_conn(db, what)
    if conn:
        if return_dict and what == 'mysql':
            cur = conn.cursor(cursors.DictCursor)
        else:
            cur = conn.cursor()
        return cur, conn
    else:
        return None, None


def close_cur_conn(cur, conn):
    try:
        if cur:
            cur.close()
        if conn:
            conn.close()
    except:
        print 'close cur, conn error'



def execute_sql(cur,conn,sql,one_many=False):
        cur.execute(sql)
        if one_many =='many':
            return cur.fetchall()
        elif one_many == 'one':
            one = cur.fetchone()
            if one:
                return one[0]
            else:
                return None
        conn.commit()

def test(db=None,table=None,id=1):
    sql = 'select * from %s where id=%d' % (table, id)
    cur, conn = get_cur_conn(db)
    cur.execute(sql)
    r = cur.fetchone()
    print r
    close_cur_conn(cur, conn)

if __name__ == '__main__':
    test(db='chenkun_hqew_new', table='t_html_partno', id=1747898)
