import inspect
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.spiders import CrawlSpider as c

print inspect.getsource(c)
