def make_adder_and_setter(x):
    x = x
    def setter(n):
        x = n # defining
    return (lambda y: x + y, setter)

adder, setter = make_adder_and_setter(10)
print adder(5)
setter(1)
print adder(5)



def make_adder_and_setter(x):
    x = [x]
    def setter(n):
        x[0] = n # not defining, but using
    return (lambda y: x[0] + y, setter)

adder, setter = make_adder_and_setter(10)
print adder(5)
setter(1)
print adder(5)
