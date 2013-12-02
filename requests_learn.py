#coding=utf8
import requests
url = 'http://www.baidu.com'
r = requests.get(url)
print dir(r)
#print r.text # html
print r.url
print r.links
print r.raw # <requests.packages.urllib3.response.HTTPResponse object at 0x1cd0990>
