#student = object()
#student.name = 'Jack'
#print student.name



class Person(object):
    pass
class Address(object):
    pass
person = Person()
person.name = 'Tom'
person.address = Address()
person.address.zip = '40015'

print(person.name)
print(person.address.zip)
