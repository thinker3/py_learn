class A(object):

    def __eq__(self, other):
        return '%s == %s' % (self.__class__.__name__, other)


a = A()
print(a == 0)
print(a == '')
print(a == True)
print(a == None)
print(a == 'Hello!')
print('*' * 50)


class In(object):
    def __init__(self, a=0, b=1):
        self.a = a
        self.b = b

    def __repr__(self):  # not __str__
        return "(%s, %s)" % (self.a, self.b)

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b

ex = [In(), In(1, 2), In(2, 3), In('', None)]
print(In() in ex)
print(In(1, 2) in ex)
print(In(2, 3) in ex)
print(In("", None) in ex)
print(In(None, "") in ex)
print(In(1, 3) in ex)
instances = [In(), In(1, 2), In(2, 4), In('', None)]
to_insert = [x for x in instances if x in ex]
print(to_insert)


class Base:
    # old, new style classes, assignment overloading, replace method at runtime
    def __setattr__(self, attr, value):
        self.__dict__[attr] = 'base'


class Extend(Base):
    pass

_setattr_ = Base.__setattr__
#_setattr_ = Extend.__setattr__


def my_setattr_(self, attr, value):
    print('called')
    _setattr_(self, attr, value)
    self.__dict__[attr*2] = value

e = Extend()
b = Base()
e.foo = 'foo'
print(e.__dict__)
Base.__setattr__ = my_setattr_
#Extend.__setattr__ = my_setattr_
e.foo = 'foo'
print(e.__dict__)
b.bar = 'bar'
print(b.__dict__)
print('*' * 50)


class Base(object):
    def __setattr__(self, attr, value):
        object.__setattr__(self, attr, 'base')


class Extend(Base):
    pass

_setattr_ = Base.__setattr__
#_setattr_ = Extend.__setattr__


def my_setattr_(self, attr, value):
    print('called')
    _setattr_(self, attr, value)
    object.__setattr__(self, attr*2, value)

e = Extend()
b = Base()
e.foo = 'foo'
print(e.__dict__)
Base.__setattr__ = my_setattr_
#Extend.__setattr__ = my_setattr_
e.foo = 'foo'
print(e.__dict__)
b.bar = 'bar'
print(b.__dict__)
