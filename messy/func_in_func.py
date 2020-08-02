def outer(a):
    def inner():
        print(a, b)
        #a = 0 # UnboundLocalError: local variable 'a' referenced before assignment
    b = 2
    inner()

outer(1)
print('-' * 20)


def outer(a):
    def inner():
        #print a, b # NameError: global name 'a' is not defined
        global a, b
        a = 'a'
        b = 'b'
    b = 2
    inner()
    print(a, b)

outer(1)
print(a, b)






