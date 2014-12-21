#coding=utf8

import os
import json
import requests

home = os.path.expanduser('~')


def separate(num=80):
    print '*' * num


def test_get():
    separate()
    url = 'http://www.baidu.com'
    r = requests.get(url)
    assert isinstance(r, requests.Response)
    #print dir(r)
    print r.url
    print r.headers
    print r.cookies
    print type(r.status_code)  # <type 'int'>
    print r.status_code  # 200
    print type(r.text)  # <type 'unicode'>
    print len(r.text)  # 85994
    print type(r.content)  # <type 'str'>
    print len(r.content)  # 86207
    with open(os.path.join(home, 'requests_content'), 'w') as f:
        f.write(r.content)
    #print type(r.json())  # ValueError: No JSON object could be decoded
    #print r.json()
    print type(r.links)  # <type 'dict'>
    print r.links  # {}
    print type(r.raw)  # <class 'urllib3.response.HTTPResponse'>
    print r.raw  # <requests.packages.urllib3.response.HTTPResponse object at 0x1cd0990>


def test_post():
    separate()
    url = 'http://httpbin.org/post'
    payload = {'key1': 'value1', 'key2': 'value2'}
    r = requests.post(url, data=payload)
    assert isinstance(r, requests.Response)
    print r.text
    separate(30)
    print r.content
    separate(30)
    print type(r.json())  # <type 'dict'>
    print r.json()


def test_post_json():
    separate()
    url = 'http://httpbin.org/post'
    payload = {'key1': 'value1', 'key2': 'value2'}
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    assert isinstance(r, requests.Response)
    print r.text
    separate(30)
    print r.content
    separate(30)
    print type(r.json())  # <type 'dict'>
    print r.json()

#test_get()
#test_post()
test_post_json()

separate()
