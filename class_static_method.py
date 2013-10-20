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

class Teacher():
    def say_hello():
        print 'Teacher'

print Teacher.say_hello
# unbound method say_hello() must be called with Teacher instance as first argument (got nothing instead)
#Teacher.say_hello()
print Teacher().say_hello
# say_hello() takes no arguments (1 given)
#Teacher().say_hello()

class Teacher():
    @staticmethod
    def say_hello():
        print 'Teacher'

print Teacher.say_hello
Teacher.say_hello()
print Teacher().say_hello
Teacher().say_hello()

class Pro(Teacher):
    pass

print Pro.say_hello
Pro.say_hello()
print Pro().say_hello
Pro().say_hello()

class Pro(Teacher):
    @staticmethod
    def say_hello():
        print 'Pro'

print Pro.say_hello
Pro.say_hello()
print Pro().say_hello
Pro().say_hello()

class Teacher():
    @staticmethod
    def say_hello(what):
        print 'Teacher'

print Teacher.say_hello
# say_hello() takes exactly 1 argument (0 given)
#Teacher.say_hello()
print Teacher().say_hello
# say_hello() takes exactly 1 argument (0 given)
#Teacher().say_hello()

class Teacher():
    @classmethod
    def say_hello():
        print 'Teacher'

print Teacher.say_hello
# say_hello() takes no arguments (1 given)
#Teacher.say_hello()
print Teacher().say_hello
# say_hello() takes no arguments (1 given)
#Teacher().say_hello()

class Teacher():
    @classmethod
    def say_hello(what):
        print 'Teacher'

print Teacher.say_hello
Teacher.say_hello()
print Teacher().say_hello
Teacher().say_hello()

class Pro(Teacher):
    pass

print Pro.say_hello
Pro.say_hello()
print Pro().say_hello
Pro().say_hello()

