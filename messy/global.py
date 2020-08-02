num = 100


def func():
    print(num)  # global 'num' used
func()


def foo():
    num = 1  # local 'num' defined
    print(num)
foo()


'''
def bar():
    # UnboundLocalError: local variable 'num' referenced before assignment
    num = num + 1
    num += 1
    print num
bar()
'''

total = 0


def add(n):
    global total
    for i in range(n):
        total += (i + 1)  # global 'total' changed
    print(total)
add(100)
print('-' * 20)
print(num)


'''
def test(num):
    global num  # SyntaxError: name 'num' is local and global
'''


def outer(num):
    def inner():
        global num
        num = 2  # global 'num' changed
        print(num, 'inner')
    # swap the following two lines
    print(num, 'outer')  # local 'num' used
    inner()

outer(1)
print(num + 1)
