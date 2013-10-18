class Callable(object):
    def __init__(self, a):
        self.a = a

    def __call__(self):
        print self.a

c = Callable(1)
print c.a
c()


class Foo(object):
    def __call__(self):
        pass

foo = Foo()
foo()


class Bar(object):
    pass

bar = Bar()
bar()
