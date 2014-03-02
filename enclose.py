def digits_sum(i):
    return sum(map(int, list(str(i))))

def connectable(a, b):
    pass


total = 0
for i in xrange(1, 299):
    for j in xrange(1, 299):
        if i + j > 298:
            continue
        s = digits_sum(i) + digits_sum(j)
        if s <= 19:
            total += 1
        else:
            print i, j

print total
