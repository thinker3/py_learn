#coding=utf8

class Person(object):
    country = 'cn'
    def __getattr__(self, name):
        return object.__getattribute__(self, name)

    def show(self):
        print 'hello'
        return self.country

p = Person()

attr = getattr(p, 'show')()
print attr


attr = getattr(p, 'country')
print attr


