class Pizza(object):
    def __init__(self, size):
        self.size = size

    def get_size(self):
        return self.size

    def set_size(self, size):
        self.size = size

    @staticmethod
    def mix(x, y):
        return x + y

print(Pizza.set_size == Pizza.set_size)
print(Pizza.set_size is Pizza.set_size)
print(Pizza(1) == Pizza(1))
obj = Pizza(1)
print(obj.set_size == obj.set_size)
print(obj.set_size is obj.set_size)

print('-' * 30)
m = Pizza(1).get_size
obj = m.__self__
print(m == Pizza.get_size)

print(m == obj.get_size)
print(m is obj.get_size)

print(obj.get_size())
obj.set_size(2)
print(obj.get_size())

print('-' * 30)
class Pizza(object):
    @staticmethod
    def mix(x, y):
        return x + y

print(Pizza.mix is Pizza.mix)
print(Pizza().mix is Pizza.mix)
print(Pizza().mix is Pizza().mix)

class NewPizza(Pizza):
    @staticmethod
    def mix(x, y):
        return 2*x + y

pizza = Pizza()
print(pizza.mix(2,1))

new_pizza = NewPizza()
print(new_pizza.mix(2,1))


print('-' * 30)
class Pizza(object):
    radius = 42
    @classmethod
    def get_radius(cls):
        return cls.radius

    def set_radius(self, radius):
        self.radius = radius

    def show(self):
        return self.radius

p = Pizza()
print(Pizza.get_radius())
print(Pizza.radius)
print(p.get_radius())
print(p.show())

p.set_radius(40)
print(Pizza.get_radius())
print(Pizza.radius)
print(p.get_radius())
print(p.show())

Pizza.radius = 30
print(Pizza.get_radius())
print(Pizza.radius)
print(p.get_radius())
print(p.show())

Pizza.size = 1
print(Pizza.size)
print(p.size)
p.weight = 22
print(p.weight)
print(Pizza.weight)



