def makebold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped

def makeitalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped

@makebold
@makeitalic
def hello():
    return "hello world"

print hello()

@makeitalic
@makebold
def hello():
    return "hello world"

print hello()

def hello():
    return "hello world"

hello = makeitalic(makebold(hello))
print hello()


class Tag(object):
    def __init__(self, tag):
        self.tag = tag

    def __call__(self, f):
        def newf():
            return "<{tag}>{res}</{tag}>".format(res=f(), tag=self.tag)
        return newf


@Tag('b')
@Tag('i')
def sayhi():
    return 'hi'

print sayhi()

def sayhi():
    return 'hi'
tag_i = Tag('i')
tag_b = Tag('b')
sayhi = tag_i(tag_b(sayhi))
print sayhi()


def table(name):
    def _table(cls):
        cls.__table__ = name
        return cls
    return _table

@table('u')
class User(object): pass

print User
abc = User()
print abc.__table__

class User(object): pass
User = table('v')(User)
abc = User()
print abc.__table__


def tag(name):
    def _tag(f):
        def newf():
            return "<{tag}>{res}</{tag}>".format(res=f(), tag=name)
        return newf
    return _tag


@tag('b')
@tag('i')
def sayhi():
    return 'hi'

print sayhi()


def tag(name):
    '''
    tag is a function which need an argument
    and return _tag, which is a decorator
    '''
    def _tag(f):
        def newf(*args):
            return "<{tag}>{res}</{tag}>".format(res=f(*args), tag=name)
        return newf
    return _tag


@tag('b')
@tag('i')
def sayhi(person, time):
    return 'hi %s, good %s.' % (person, time)

print sayhi('tom', 'night')


def sayhi(person, time):
    return 'hi %s, good %s.' % (person, time)

print tag('b')(tag('i')(sayhi))('tom', 'night')


def tags(*names):
    '''
    tags is a function which can take many arguments and return _tags,
    which is a decorator that can decorate a function,
    which can take many arguments.
    '''
    def _tags(f):
        def newf(*args):
            res = f(*args)
            for name in names:
                res = "<{tag}>{res}</{tag}>".format(res=res, tag=name)
            return res
        return newf
    return _tags


@tags('span', 'div', 'body')
def sayhi(person, time):
    return 'Hi %s, good %s.' % (person, time)

print sayhi('Tom', 'morning')
