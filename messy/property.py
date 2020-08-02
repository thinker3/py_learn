class String2Int(object):
    def __init__(self, str_num):
        self.str_num = str_num

    def get_num(self):
        return int(self.str_num)

    def set_num(self, value):
        self.str_num = str(value)

    def show_int(self):
        print(self.num, type(self.num))

    def show_str(self):
        print(self.str_num, type(self.str_num))

    num = property(get_num, set_num)


n = String2Int('123')
n.show_int()
n.show_str()
n.num = 321
n.show_int()
n.show_str()
print('*' * 30)

class CallProperty(object):
    '''
        A property can not be called
    '''
    @property
    def name(self):
        return 'John'

    @property
    def full_name(self):
        #return self.name() + ' Kennedy'
        return self.name + ' Kennedy'

obj = CallProperty()
print(obj.name)
print(obj.full_name)
print('*' * 30)


def alias(key):
    return property(
        lambda self: getattr(self, key),
        lambda self, value: setattr(self, key, value),
        #lambda self: delattr(self, key),
        )


class Alias(object):
    x = 0
    y = alias('x')

    m = 'hello'

    @property
    def n(self):
        return self.m

    @n.setter
    def n(self, value):
        self.m = value

a = Alias()
print(a.x)
print(a.y)
a.y = 1
print(a.x)
print(a.y)

print(a.m)
print(a.n)
a.n = 'world'
print(a.m)
print(a.n)
