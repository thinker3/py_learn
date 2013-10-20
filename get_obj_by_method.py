class Pizza(object):
    def __init__(self, size):
        self.size = size

    def get_size(self):
        return self.size

    def set_size(self, size):
        self.size = size

m = Pizza(1).get_size
obj = m.__self__
print m == Pizza.get_size

print m == obj.get_size
print m is obj.get_size

print obj.get_size()
obj.set_size(2)
print obj.get_size()


