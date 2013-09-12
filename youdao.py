#!/usr/bin/env python
#coding=utf8

import urllib2 as u
import re
from scrapy.selector import HtmlXPathSelector
while True:
    query = raw_input('q to quit, input the word: ')
    if query.lower() == 'q': break
    url = "http://dict.youdao.com/search?tab=\
    chn&keyfrom=dict.top&q=" + query
    html = u.urlopen(url).read()
    hxs = HtmlXPathSelector(text = html)
    phonetics = hxs.select('//div[@id="phrsListTab"]/h2[1]/div[1]/span')
    for ph in phonetics:
        ph = ph.select('./span/text()').extract()
        if len(ph) > 0: print ph[0],
    print
    lis = hxs.select('//div[@id="phrsListTab"]/div[@class="trans-container"]/ul/li')
    for li in lis:
        try:
            print li.select('./text()').extract()[0]
        except:
            pass
    examples = hxs.select('//div[@id="bilingual"]/ul/li')
    for li in examples:
        spans = li.select('./p[1]/span')
        example_en = []
        for span in spans:
            one = span.select('./text()').extract()
            if len(one) == 0:
                one = span.select('./b/text()').extract()
            example_en.extend(one)

        example_cn = li.select('./p[2]/span/text()').extract()

        print ''.join(example_en)
        print ''.join(example_cn)
        print






