#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scrapy.selector import XmlXPathSelector

xml = (
    """
    <root>
        <foos>
            <foo>the quick <bar>brown </bar>fox</foo>
        </foos>
    </root>
    """
)


xxs = XmlXPathSelector(text=xml)
foos = xxs.select('//foos')
for one in foos:
    text = one.select('./foo//text()').extract()
    text = ''.join(text)
    print(text)

xml = (
    """
    <content type="text/xml">
      <s:dict>
        <s:key name="group_id">MAC</s:key>
        <s:key name="label">NOT FOR RESALE</s:key>
        <s:key name="max_violations">5</s:key>
        <s:key name="quota">1000000000</s:key>
        <s:key name="relative_expiration_interval">0</s:key>
        <s:key name="relative_expiration_start">0</s:key>
        <s:key name="sourcetypes"><s:list/></s:key>
        <s:key name="stack_id">mac</s:key>
        <s:key name="status">VALID</s:key>
        <s:key name="type">mac</s:key>
        <s:key name="window_period">30</s:key>
      </s:dict>
    </content>
    """
)

xxs = XmlXPathSelector(text=xml)
quota = xxs.select('//*[@name="quota"]/text()').extract()[0]
print(quota)
