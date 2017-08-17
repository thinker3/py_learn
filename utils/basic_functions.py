# coding=utf8

import os
import time
import codecs
import string
import urllib2
import socket
from datetime import (
    date,
    datetime,
)

lower_letters_digits = string.letters[:26] + string.digits


def all(*cons):  # shortcircuiting
    result = True
    for con in cons:
        result = result and con
        if result is False:
            return result
    return True


def get_html(url, callback=None, headers=None):
    _headers = {
        'User-Agent': 'Mozilla/5.0',
        'Referer': 'http://www.baidu.com',
        'X-Forwarded-For': '220.181.111.148',
    }
    if headers and isinstance(headers, dict):
        _headers.update(headers)
    req = urllib2.Request(url, None, _headers)
    try:
        html = urllib2.urlopen(req, timeout=8).read()
    except urllib2.URLError:
        try:
            html = urllib2.urlopen(url, timeout=8).read()
        except urllib2.URLError:
            html = None
            print url + ' error...'
            if callback:
                callback()
    except socket.timeout:
        print url + ' socket timeout...'
        time.sleep(5)
        html = None
    return html


def read_id(filepath):
    f = None
    try:
        f = open(filepath, 'r')
        id = f.readline()
        id = int(id)
        f.close()
        return id
    except:
        raise
    finally:
        if f:
            f.close()


def read_file(filepath):
    f = None
    try:
        f = open(filepath, 'r')
        _file_str = f.read()
        f.close()
        return _file_str
    except:
        raise
    finally:
        if f:
            f.close()


def read_file_codecs(filepath, encoding='utf-8'):
    f = None
    try:
        f = codecs.open(filepath, encoding=encoding, mode='r')
        _file_str = f.read()
        f.close()
        return _file_str
    except:
        raise
    finally:
        if f:
            f.close()


def write_id(filepath, id):
    f = None
    try:
        f = open(filepath, 'w')
        f.write(str(id))
        f.close()
    except:
        raise
    finally:
        if f:
            f.close()


def check_file_exists(filepath):
    if filepath:
        return os.path.exists(filepath)
    else:
        return False


def check_file_size(filepath, size):
    if check_file_exists(filepath):
        return os.path.getsize(filepath) > size
    else:
        return False


def check_html_length(html, length_needed):
    if html is None:
        return False
    length = len(html)
    return length > length_needed


def sleeping(seconds):
    print 'sleeping %d seconds' % seconds
    time.sleep(seconds)


def date_str_to_date(s):
    return datetime.strptime(s, '%Y-%m-%d').date()


def date_diff(s):
    today = date.today()
    other_day = date_str_to_date(s)
    return abs((today - other_day).days)


def wrap_by_len(text, length):
    while text:
        print text[:length]
        text = text[length:]
