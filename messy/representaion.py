class Foo(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

foo = Foo('Jim')
print foo
print [foo]
print

class Bar(object):
    def __init__(self, name):
        self.name = name

bar = Bar('Jim')
print bar 
print

class Bar(object):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

bar = Bar('Jim')
print bar 
print [bar]
print


class Foobar(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'hello'

    def __repr__(self):
        return self.name

foobar = Foobar('Jim')
print foobar 
print [foobar]
print
