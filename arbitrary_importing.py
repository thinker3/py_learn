import sys
p = sys.path
print p[0]
p[0] = '/'.join(p[0].split('/')[:-1])
print p[0]

from base.basic_functions import get_html
print get_html

p[0] = '/home/chenkun/work/'
print p[0]

from data_scrapy.mysql_tools import get_cur_conn
print get_cur_conn


#p.append('/home/chenkun/git/weight/')
p.insert(0, '/home/chenkun/git/weight/')
for one in p:
    if one.startswith('/h'):
        print one

from write import init_db
print init_db 
