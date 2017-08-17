#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import time
import random
import requests
import datetime
import mongoengine as mongo
from mongoengine import connect

from utils import common
from utils.common import DictObject
from utils.lxml_selector import Selector


class Job(mongo.Document):
    position_id = mongo.StringField()
    url = mongo.URLField(
        verbose_name=u'职位详情链接',
    )
    description = mongo.StringField(
        verbose_name=u'职位描述',
    )
    create_time = mongo.DateTimeField(
        verbose_name=u'创建时间',
        default=datetime.datetime.now(),
    )
    create_time = mongo.DateTimeField(
        verbose_name=u'更新时间',
        default=datetime.datetime.now(),
    )

    meta = {
        'collection': 'job',
    }


connect(
    db='lagou',
    host='mongo',
    port=27017,
)

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36 OPR/46.0.2597.57'


class Lagou(object):
    def __init__(self, city, search_kw, jd_kw):
        self.total_page = None
        self.city = city
        self.search_kw = search_kw
        self.jd_kw = jd_kw
        self.jobs = []

    def get_job_detail_urls_per_page(self, page=1):
        city = self.city
        search_kw = self.search_kw
        base_url = 'https://www.lagou.com/jobs/positionAjax.json'
        get_params = dict(
            city=city,
            px='new',
            gx=u'全职',
            isSchoolJob=0,
            needAddtionalResult='false',
        )
        first = 'true'
        if page != 1:
            first = 'false'
        form_params = dict(
            kd=search_kw,
            pn=page,
            first=first,
        )

        def get_referer():
            base_url = u'https://www.lagou.com/jobs/list_%s' % search_kw
            params = dict(
                city=city,
                px='new',
                gx=u'全职',
            )
            referer = common.get_url(base_url, params)
            return referer

        headers = {
            'User-Agent': user_agent,
        }
        headers.update(
            Host='www.lagou.com',
            Origin='https://www.lagou.com',
            Referer=get_referer(),
        )
        response = requests.post(
            base_url,
            data=form_params,
            headers=headers,
            params=get_params,
        )
        json = response.json()
        json = DictObject(**json)
        try:
            result = json.content['positionResult']['result']
            if self.total_page is None:
                total_count = json.content['positionResult']['totalCount']
                page_size = json.content['pageSize']
                self.total_page = int(math.ceil(float(total_count) / page_size))
                print self.total_page
        except Exception as e:
            print e
            result = []
        for job in result:
            position_id = str(job['positionId'])
            url = 'https://www.lagou.com/jobs/%s.html' % position_id
            job = DictObject(
                position_id=position_id,
                url=url,
            )
            self.jobs.append(job)

    def get_job_detail_urls(self):
        while True:
            if self.total_page is None:
                self.get_job_detail_urls_per_page()
                time.sleep(1)
            else:
                for i in range(2, self.total_page + 1):
                    self.get_job_detail_urls_per_page(i)
                    time.sleep(random.randint(1, 3))
                break

    def check_description(self, job):
        headers = {
            'User-Agent': user_agent,
        }
        response = requests.get(job.url, headers=headers)
        html = response.text
        length = len(html)
        if length < 10 ** 4:
            self.jobs.append(job)
            return
        selector = Selector(html=html)
        desc = selector.xpath('//dd[@class="job_bt"]/div//text()').extract()
        desc = ''.join(desc)
        Job.objects.create(
            position_id=job.position_id,
            url=job.url,
            description=desc,
        )

    def filter(self):
        for job in Job.objects.filter(
            description__icontains=self.jd_kw,
            description__not__icontains='jquery',
        ):
            print job.url

    def run(self):
        self.get_job_detail_urls()
        while self.jobs:
            job = self.jobs.pop(0)
            if Job.objects.filter(
                position_id=job.position_id,
            ).first():
                continue
            self.check_description(job)
            time.sleep(1)


def test_lagou():
    city = u'重庆'
    search_kw = u'前端'
    jd_kw = 'react'
    lagou = Lagou(city, search_kw, jd_kw)
    # lagou.run()
    lagou.filter()


if __name__ == '__main__':
    test_lagou()
