import MySQLdb as mysql

def get_cur_conn():
	conn = mysql.connect(host='localhost',user='root',db='youdao',\
	passwd='qweasd',charset='utf8')
	cur = conn.cursor()
	return cur, conn

def close_cur_conn(cur,conn):
	cur.close()
	conn.close()

def create_table_words():
	sql = '''create table if not exists words (
	name varchar(100) not null,
	phonetic varchar(100),
	meaning varchar(1000) not null,
	example varchar(10000),
	primary key(name)
	)default charset utf8;'''
	#default charset=utf8
	cur,conn = get_cur_conn()
	cur.execute(sql)
	conn.commit()
	close_cur_conn(cur,conn)

def execute_sql(sql):
	cur,conn = get_cur_conn()
	cur.execute(sql)
	conn.commit()
	close_cur_conn(cur,conn)


if __name__ == '__main__':
	sql = '''drop table if exists words;'''
	execute_sql(sql)
	create_table_words()



