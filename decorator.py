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


