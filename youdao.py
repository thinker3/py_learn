#!/usr/bin/env python
#coding: utf8

import urllib2 as u
import re
from scrapy.selector import Selector
while True:
    query = raw_input('q to quit, input the word: ')
    if query.lower() == 'q': break
    url = "http://dict.youdao.com/search?tab=chn&keyfrom=dict.top&q=" + query
    html = u.urlopen(url).read()
    hxs = Selector(text = html)
    phonetics = hxs.xpath('//div[@id="phrsListTab"]/h2[1]/div[1]/span')
    for ph in phonetics:
        ph = ph.xpath('./span/text()').extract()
        #if len(ph) > 0: print ph[0]  # UnicodeEncodeError on windows
        if len(ph) > 0: print ph[0].encode('utf8')
    print
    xpath = '//div[@id="phrsListTab"]/div[@class="trans-container"]/ul/li'
    lis = hxs.xpath(xpath)
    for li in lis:
        try:
            print li.xpath('./text()').extract()[0]
        except:
            pass
    examples = hxs.xpath('//div[@id="bilingual"]/ul/li')
    for li in examples:
        example_en = li.xpath('./p[1]/span//text()').extract()
        example_cn = li.xpath('./p[2]/span//text()').extract()

        # UnicodeEncodeError on mac
        #print ''.join(example_en)
        #print ''.join(example_cn)

        print ''.join(example_en).encode('utf8')
        print ''.join(example_cn).encode('utf8')
    print
    print
