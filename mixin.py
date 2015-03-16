class Mixin(object):
    def add(self, value):
        self.number += value

    def sub(self, value):
        self.number -= value


class Number(object):
    def __init__(self, number):
        self.number = number

    def show_me(self):
        print self.number


class SuperNumber(Mixin, Number): # SuperNumber => Mixin => Number
    def __init__(self, number):
        super(SuperNumber, self).__init__(number)
        self.name = 'SuperNumber'


class MightyNumber(Number, Mixin):
    def __init__(self, number):
        super(MightyNumber, self).__init__(number)
        self.name = 'MightyNumber'

s = SuperNumber(0)
s.show_me()
s.add(10)
s.show_me()
s.sub(1)
s.show_me()
print s.name

m = MightyNumber(0)
m.show_me()
m.add(10)
m.show_me()
m.sub(1)
m.show_me()
print m.name
