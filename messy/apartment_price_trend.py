#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import requests
from munch import Munch

cities = [
    ("510100", "成都市"),
    ("500000", "重庆市"),
    ("610100", "西安市"),
]


def print_price_data(city_code):
    # 参考均价 < 挂牌均价
    url = 'https://cd.lianjia.com/fangjia/priceTrend/?region=city&region_id=%s' % city_code
    response = requests.get(url)
    try:
        data = response.json()['currentLevel']
    except Exception:
        __import__('ipdb').set_trace()
        return
    data = Munch(data)
    deal_price = Munch(data.dealPrice)
    list_price = Munch(data.listPrice)
    datas = [
        data.month,
        deal_price.total,
        list_price.total,
    ]
    for li in datas:
        content = '\t'.join([str(one) for one in li])
        print(content)


for code, name in cities:
    print(name)
    print_price_data(code)
    time.sleep(1)
