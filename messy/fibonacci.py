def fibonacci_generator(n):
    a=b=1
    yield a
    yield b
    i=1
    while i<=n-2:
        a,b = b,a+b
        i += 1
        yield b

t = fibonacci_generator(9)
print type(t)
for one in t:
    print one


def fibonacci_list(n):
    temp = []
    a=b=1
    temp.append(a)
    temp.append(b)
    i=1
    while i<=n-2:
        a,b = b,a+b
        i += 1
        temp.append(b)
    return temp

print
t = fibonacci_list(9)
print type(t)
for one in t:
    print one


def fibonacci(n):
    temp = [1,1]
    i=1
    while i<=n-2:
        temp.append(temp[i-1]+temp[i])
        i += 1
    return temp

print
t = fibonacci(9)
for one in t:
    print one
