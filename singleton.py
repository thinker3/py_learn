class SingletonMetaClass(type):
    obj = None

    def __call__(cls, *args, **kwargs):
        if cls.obj is None:
            cls.obj = cls.__new__(cls, *args, **kwargs)
            cls.obj.__init__(*args, **kwargs)
        return cls.obj


class Foo(object):
    #pass
    __metaclass__ = SingletonMetaClass

    def __init__(self, a, b):
        self.a = a
        self.b = b

g = Foo(1, 2)
h = Foo(2, 3)
print g == h
print h.a, h.b


class Bar(object):
    __metaclass__ = SingletonMetaClass

    def __init__(self, a, b):
        self.a = a
        self.b = b

g = Bar(10, 20)
h = Bar(20, 30)
print g == h
print h.a, h.b


def singleton_decorator(cls):
    cls.instance = None

    def new_cls(*args, **kwargs):
        if cls.instance is None:
            cls.instance = cls(*args, **kwargs)
        return cls.instance
    return new_cls


@singleton_decorator
class Foo(object):

    def __init__(self, a, b):
        self.a = a
        self.b = b

g = Foo(1, 2)
h = Foo(2, 3)
print g == h
print h.a, h.b


@singleton_decorator
class Bar(object):

    def __init__(self, a, b):
        self.a = a
        self.b = b

g = Bar(10, 20)
h = Bar(20, 30)
print g == h
print h.a, h.b


class SingletonDecorator(object):

    def __call__(self, cls):
        cls.instance = None

        def new_cls(*args, **kwargs):
            if cls.instance is None:
                cls.instance = cls(*args, **kwargs)
            return cls.instance
        return new_cls


@SingletonDecorator
class Foo(object):

    def __init__(self, a, b):
        self.a = a
        self.b = b

g = Foo(1, 2)
h = Foo(2, 3)
print g == h
print h.a, h.b


@SingletonDecorator
class Bar(object):

    def __init__(self, a, b):
        self.a = a
        self.b = b

g = Bar(10, 20)
h = Bar(20, 30)
print g == h
print h.a, h.b
