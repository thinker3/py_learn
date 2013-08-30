from scrapy.selector import XmlXPathSelector

xml = \
"""
<root>
    <foos>
        <foo>the quick <bar>brown </bar>fox</foo>
    </foos>
</root>
"""


xxs =XmlXPathSelector(text=xml)
foos = xxs.select('//foos')
for one in foos:
    text = one.select('./foo//text()').extract()
    text = ''.join(text)
    print text


