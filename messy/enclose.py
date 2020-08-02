max_sum = 19

def digits_sum(i):
    return sum(map(int, list(str(i))))

middle = 0
axis = 0
def go_to(point, a, b):
    a = point[0]+a
    b = point[1]+b
    if a >= b > -1:
        s = digits_sum(a) + digits_sum(b)
        if s <= max_sum:
            p = (a, b)
            if p not in last:
                if a == b:
                    global middle
                    middle += 1
                if b == 0:
                    global axis
                    axis += 1
                return p

four = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def go_next(point):
    for one in four:
        p = go_to(point, *one)
        if p:
            that.add(p)

total = 0
last = set([])
this = set([(0, 0)])
while this:
    that = set([])
    for one in this:
        go_next(one)
    total += len(that)
    last = this
    this = that

total = ((total - middle - axis) * 2 + middle + axis) * 4 + 1 
print(total)



total = 0
for i in range(1, 299):
    for j in range(299):
        if i + j > 298:
            continue
        s = digits_sum(i) + digits_sum(j)
        if s <= 19:
            total += 1

print(total * 4 + 1)
