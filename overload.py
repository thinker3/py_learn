class A(object):

    def __eq__(self, other):
        return '%s == %s' % (self.__class__.__name__, other)


a = A()
print a == 0
print a == ''
print a == True
print a == None
print a == 'Hello!'
