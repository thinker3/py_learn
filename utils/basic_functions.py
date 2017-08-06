# coding=utf8

import os
import time
import codecs
import string
import urllib
import urllib2
import socket
from xlwt import Workbook
from datetime import datetime, date
try:
    from django.http import HttpResponse
except:
    HttpResponse = None

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


def get_attrs(columns):
    attrs = []
    for inner_list in columns:
        attrs.append(inner_list[0])
    return attrs


def index_of(key, list_2d):
    for i, one in enumerate(list_2d):
        if key == one[0]:
            return i


def make_workbook(sheetname, filename, columns, objs):
    book = Workbook()
    sheet = book.add_sheet(sheetname)
    attrs = get_attrs(columns)
    for i in xrange(len(columns)):
        sheet.write(0, i, columns[i][1])
        sheet.col(i).width = columns[i][2] * 256
    for i, obj in enumerate(objs, start=1):
        for attr in attrs:
            if isinstance(obj, dict):
                sheet.write(i, index_of(attr, columns), obj[attr])
            else:
                sheet.write(i, index_of(attr, columns),
                            obj.__getattribute__(attr))
    if not filename:
        filename = '%s.xls' % datetime.now()
    return book, filename


def make_xls_file(sheetname='1', filename=None, columns=[], objs=[]):
    book, filename = make_workbook(sheetname, filename, columns, objs)
    book.save(filename)


def make_xls_response(sheetname='1', filename=None, columns=[], objs=[]):
    book, filename = make_workbook(sheetname, filename, columns, objs)
    response = HttpResponse(mimetype='application/vnd.ms-excel')
    # "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    response = HttpResponse(content_type='application/vnd.ms-excel')
    filename = urllib.quote(unicode(filename).encode('utf8'))
    response['Content-Disposition'] = 'attachment; filename=%s' % filename
    book.save(response)
    return response


def init_xls(sheetname='1'):
    book = Workbook()
    if sheetname:
        sheet = book.add_sheet(sheetname)
    else:
        sheet = book.add_sheet('1')
    return book, sheet


def save_xls(book, filename=None):
    if filename:
        book.save(filename)
    else:
        filename = '%s.xls' % datetime.now()
        book.save(filename)


def write_xls_1d(sheet, columns=[], objs=[]):
    attrs = get_attrs(columns)
    l = len(sheet.rows)
    for i in xrange(len(columns)):
        sheet.write(l, i, columns[i][1])
        sheet.col(i).width = columns[i][2] * 256
    for i, obj in enumerate(objs, start=l + 1):
        for attr in attrs:
            if isinstance(obj, dict):
                sheet.write(i, index_of(attr, columns), obj[attr])
            else:
                #sheet.write(i, index_of(attr, columns),
                #            obj.__getattribute__(attr))
                sheet.write(i, index_of(attr, columns), getattr(obj, attr))


def write_xls_2d(sheet, col_titles=[], row_titles=[], two_dim_obj=[]):
    l = len(sheet.rows)
    for i, one in enumerate(col_titles, start=0):
        sheet.write(l, i, one[0])
        sheet.col(i).width = one[1] * 256
    for i, one in enumerate(row_titles, start=l + 1):
        sheet.write(i, 0, one)
    for i, r in enumerate(two_dim_obj, start=l + 1):
        for j, c in enumerate(r, start=1):
            sheet.write(i, j, c)


def write_xls_empty_lines(sheet, num=0):
    l = len(sheet.rows)
    if num <= 0:
        return
    else:
        for i in range(l, num + l):
            sheet.write(i, 0, '')


def append_xls_with(sheet, something, col=0):
    row_num = len(sheet.rows)
    if col:
        sheet.write(row_num, col, something)
    else:
        sheet.write(row_num, 0, something)


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
