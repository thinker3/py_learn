#!/usr/bin/env python
# encoding: utf-8

import functools
import operator


def add(a, b):
    print a + b

add_1 = functools.partial(add, 1)
add_1(5)


def say_hello(name, default="Good morning"):
    print "Hello %s, %s!" % (name, default)

say_hello('Ken')
welcome = functools.partial(say_hello, default='Welcome')
welcome('Ken')
welcome_jerry = functools.partial(welcome, 'Jerry')
welcome_jerry()


def run_callback(callback):
    callback()

run_callback(welcome_jerry)
#run_callback(welcome)  # TypeError
run_callback(functools.partial(welcome, 'Benny'))
run_callback(functools.partial(say_hello, 'Benny', 'Nice to meet you'))


def add(n):
    print functools.reduce(lambda x, y: x + y, xrange(n + 1))
    print functools.reduce(lambda x, y: x + y, xrange(n + 1), 0)
    print functools.reduce(lambda x, y: x + y, xrange(n + 1), 1)
    # TypeError: reduce() of empty sequence with no initial value
    #print functools.reduce(lambda x, y: x + y, [])
    print functools.reduce(lambda x, y: x + y, [], 0)
    print functools.reduce(lambda x, y: x + y, [], 1)
    print functools.reduce(operator.add, xrange(n + 1))


def multiply(n):
    print functools.reduce(lambda x, y: x * y, xrange(1, n + 1))
    print functools.reduce(lambda x, y: x * y, xrange(1, n + 1), 0)
    print functools.reduce(lambda x, y: x * y, xrange(1, n + 1), 1)
    #print functools.reduce(lambda x, y: x * y, [])
    print functools.reduce(lambda x, y: x * y, [], 0)
    print functools.reduce(lambda x, y: x * y, [], 1)
    print functools.reduce(operator.mul, xrange(1, n + 1))

add(100)
print '*' * 20
multiply(4)


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


def lgcd(*args):
    return reduce(gcd, args)


def llcm(*args):
    return reduce(lcm, args)

print '*' * 20
print lgcd(100, 80, 36)
print llcm(100, 80, 36)

deep = {
    'he': {
        'she': {
            'you': {
                'they': 'here'
            }
        }
    }
}
print '*' * 20
print functools.reduce(dict.__getitem__, 'he.she.you.they'.split('.'), deep)


def dot(d, path):
    print functools.reduce(dict.__getitem__, path.split('.'), d)

dot(deep, 'he.she.you')


class Dict(object):

    def __init__(self, d):
        self.d = d

    def dot(self, path):
        return functools.reduce(dict.__getitem__, path.split('.'), self.d)

deep = Dict(deep)
print deep.dot('he.she')


def tags(*names):
    '''
    tags is a function which can take many arguments and return _tags,
    which is a decorator that can decorate a function,
    which can take many arguments.
    '''
    def _tags(f):
        @functools.wraps(f)  # dd to see diff
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

print '*' * 20
print sayhi('Tom', 'morning')
print sayhi.__name__


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
        #return newf
        #return functools.wraps(f)(newf)
        return functools.update_wrapper(newf, f)
    return _tags


@tags('span', 'div', 'body')
def sayhi(person, time):
    return 'Hi %s, good %s.' % (person, time)

print sayhi('Tom', 'morning')
print sayhi.__name__


class SomeClass(object):

    @tags('span', 'div', 'body')
    def sayhi(self, person, time):
        return 'Hi %s, good %s.' % (person, time)

a = SomeClass()
print a.sayhi('Tom', 'morning')
print a.sayhi.__name__
