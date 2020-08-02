if 1:
    a = 'hello'
print(a)

for i in range(10):
    b = i*3
print(b, i)

t = 0
for i in range(10):
    t = t + i
print(t)
print('*' * 50)


class A(object):
    def __init__(self, num):
        self.num = num


class B(object):
    def func(self):
        a = A(0)
        b = 1
        print(locals())
        for k, v in list(locals().items()):
            if isinstance(v, A):
                print(v.num)

        def inner():
            a = A(10)
            b = 20
            print(locals())
            for k, v in list(locals().items()):
                if isinstance(v, A):
                    print(v.num)
                    print(locals())
        inner()

b = B()
b.func()
