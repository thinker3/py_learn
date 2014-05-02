from sys import argv

operators = {
    '+': lambda a, b: a + b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b,
}


def evaluate(one):
    temp = []
    for i in reversed(one):
        if i in operators:
            a = temp.pop(0)
            b = temp.pop(0)
            temp.insert(0, operators[i](a, b))
        else:
            temp.insert(0, float(i))
    return int(temp[0])


f = open(argv[1], 'r')
for one in f:
    one = one.strip()
    if one:
        print evaluate(one.split())
f.close()
