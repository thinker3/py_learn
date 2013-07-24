class add_sub_Mixin(object):
    def add(self, value):
        self.number += value

    def sub(self, value):
        self.number -= value


class myNumber(object):
    def __init__(self, number):
        self.number = number
    
    def show_me(self):
        print self.number

class mySuperNumber(add_sub_Mixin, myNumber): # mySuperNumber => add_sub_Mixin => myNumber
    pass

n = mySuperNumber(0)
n.show_me()
n.add(10)
n.show_me()
n.sub(1)
n.show_me()

