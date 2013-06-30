class Person():
    country='USA'
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def show(cls):
        print cls.country

    @staticmethod
    def say_hello():
        print 'hello'

class Student(Person):
    country = 'CN'

s = Student('Chen', 2)
s.say_hello()
s.show()

p = Person('Tom', 1)
p.show()
Person.show()
p.say_hello()
Person.say_hello()
