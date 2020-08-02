#coding=utf8

import os
import json
import urllib.request, urllib.parse, urllib.error
import requests

home = os.path.expanduser('~')


def separate(num=80):
    print('*' * num)


def test_get():
    separate()
    url = 'http://www.baidu.com'
    params = dict(
        x=1,
        y=[2, 3],
    )
    r = requests.get(url, params=params)  # doseq is True
    assert isinstance(r, requests.Response)
    #print dir(r)
    print(r.url)
    print(r.headers)
    print(r.cookies)
    print(type(r.status_code))  # <type 'int'>
    print(r.status_code)  # 200
    print(type(r.text))  # <type 'unicode'>
    print(len(r.text))  # 85994
    print(type(r.content))  # <type 'str'>
    print(len(r.content))  # 86207
    with open(os.path.join(home, 'requests_content'), 'w') as f:
        f.write(r.content)
    #print type(r.json())  # ValueError: No JSON object could be decoded
    #print r.json()
    print(type(r.links))  # <type 'dict'>
    print(r.links)  # {}
    print(type(r.raw))  # <class 'urllib3.response.HTTPResponse'>
    print(r.raw)  # <requests.packages.urllib3.response.HTTPResponse object at 0x1cd0990>


def test_post():
    separate()
    url = 'http://httpbin.org/post'
    payload = {'key1': 'value1', 'key2': 'value2'}
    r = requests.post(url, data=payload)
    assert isinstance(r, requests.Response)
    print(r.text)
    separate(30)
    print(r.content)
    separate(30)
    print(type(r.json()))  # <type 'dict'>
    print(r.json())


def test_post_json():
    separate()
    url = 'http://httpbin.org/post'
    payload = {'key1': 'value1', 'key2': 'value2'}
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    assert isinstance(r, requests.Response)
    print(r.text)
    separate(30)
    print(r.content)
    separate(30)
    print(type(r.json()))  # <type 'dict'>
    print(r.json())


def post_with_session():
    client = requests.session()
    url = 'http://127.0.0.1:8800/partner_dash/staff/login/'
    client.get(url)
    csrftoken = client.cookies['csrftoken']
    data = dict(
        csrfmiddlewaretoken=csrftoken,
        username='18030703819',
        password='18030703819',
    )
    client.post(url, data=data)


def construct_query_string():
    params = dict(
        x=1,
        y=[2, 3],
    )
    query_string = urllib.parse.urlencode(params, doseq=0)  # default is 0
    print(query_string)
    query_string = urllib.parse.urlencode(params, doseq=True)
    url = 'http://www.baidu.com'
    url = '%s?%s' % (url, query_string)
    print(url)


# test_get()
# test_post()
# test_post_json()
# post_with_session()
# construct_query_string()
