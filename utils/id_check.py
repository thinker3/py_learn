#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from datetime import date, datetime, timedelta

RE_IDNUM = re.compile(r'^[1-9]\d{5}[1-9]\d{3}((0\d)|(1[0-2]))(([0|1|2]\d)|3[0-1])(\d{3})(\d|x|X)$')
WEIGHT = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
ID_CHECK = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
area_code_list = [
    ("11", u"北京"),
    ("12", u"天津"),
    ("13", u"河北"),
    ("14", u"山西"),
    ("15", u"内蒙古"),
    ("21", u"辽宁"),
    ("22", u"吉林"),
    ("23", u"黑龙江"),
    ("31", u"上海"),
    ("32", u"江苏"),
    ("33", u"浙江"),
    ("34", u"安徽"),
    ("35", u"福建"),
    ("36", u"江西"),
    ("37", u"山东"),
    ("41", u"河南"),
    ("42", u"湖北"),
    ("43", u"湖南"),
    ("44", u"广东"),
    ("45", u"广西"),
    ("46", u"海南"),
    ("50", u"重庆"),
    ("51", u"四川"),
    ("52", u"贵州"),
    ("53", u"云南"),
    ("54", u"西藏"),
    ("61", u"陕西"),
    ("62", u"甘肃"),
    ("63", u"青海"),
    ("64", u"宁夏"),
    ("65", u"新疆"),
    ("71", u"台湾"),
    ("81", u"香港"),
    ("82", u"澳门"),
    ("91", u"国外"),
]
area_codes = [one[0] for one in area_code_list]


def to_date(date_string):
    return datetime.strptime(date_string, '%Y%m%d').date()


def id_num_validate(id_num):
    if not RE_IDNUM.match(id_num):
        return False
    if id_num[:2] not in area_codes:
        return False
    birthday = id_num[6:14]
    try:
        birthday = to_date(birthday)
    except ValueError:
        return False
    today = date.today()
    if birthday > today:
        return False
    if today.year - birthday.year > 150:
        return False
    check_sum = 0
    for i in range(17):
        check_sum = check_sum + int(id_num[i]) * WEIGHT[i]
    check_bit = check_sum % 11
    if id_num[-1].upper() != ID_CHECK[check_bit]:
        return False
    return True

if __name__=='__main__':
    __import__('ipdb').set_trace()
