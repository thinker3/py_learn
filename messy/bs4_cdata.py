#coding=utf8
from bs4 import CData
from bs4 import BeautifulSoup
from bs4.builder import LXMLTreeBuilderForXML

xml = \
'''
<?xml version="1.0" ?>
<foo>
    <bar><![CDATA[!@#$%^&*()_+{}|:"<>?,./;'[]\-=]]></bar>
</foo>
'''
builder=LXMLTreeBuilderForXML()
soup = BeautifulSoup(xml, "xml") 
print((soup.new_string))
soup.foo.bar.string = CData(soup.foo.bar.string)
soup = soup.prettify(formatter="xml")
print(soup)

