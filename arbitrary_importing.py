import sys
p = sys.path
print p[0]
p[0] = '/'.join(p[0].split('/')[:-1])
print p[0]

from base.basic_functions import get_html
print get_html

sys.path[0] = '/home/chenkun/work/'
print p[0]

from data_scrapy.mysql_tools import get_cur_conn
print get_cur_conn


