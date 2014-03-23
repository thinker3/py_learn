import inspect
#from scrapy.selector import HtmlXPathSelector
#from scrapy.contrib.spiders import CrawlSpider as c

#print inspect.getsource(c)


class A(object):

    @property
    def instance_names(self):
        self.__instance_names = []
        frame = inspect.currentframe().f_back
        tmp = dict(frame.f_globals.items() + frame.f_locals.items())
        for k, var in tmp.items():
            if isinstance(var, self.__class__):
                if hash(self) == hash(var):
                    self.__instance_names.append(k)
        return self.__instance_names

    @classmethod
    def class_instance_names(cls):
        cls.__class_instance_names = []
        frame = inspect.currentframe().f_back
        tmp = dict(frame.f_globals.items() + frame.f_locals.items())
        for k, var in tmp.items():
            if isinstance(var, cls):
                cls.__class_instance_names.append(k)
        return cls.__class_instance_names

abc = A()
efg = abc
xyz = A()
print A.class_instance_names()
print abc.instance_names
