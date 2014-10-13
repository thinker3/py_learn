#coding=utf8

import requests
import json

url = 'http://www.baidu.com'
r = requests.get(url)
print dir(r)
#print r.text # html
print r.url
print r.links
print r.raw # <requests.packages.urllib3.response.HTTPResponse object at 0x1cd0990>

print '*' * 80
print
url = 'http://httpbin.org/post'
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post(url, data=payload)
print r.text
print r.json()

print '*' * 80
print
url = 'http://httpbin.org/post'
payload = {'key1': 'value1', 'key2': 'value2'}
headers = {'content-type': 'application/json'}
r = requests.post(url, data=json.dumps(payload), headers=headers)
print r.text
print r.json()
