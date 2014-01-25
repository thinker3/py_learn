from sys import argv

f = open(argv[1], 'r')
matrix = []
for one in f:
    if one != '\n':
        matrix.append(map(int, one.split(' ')))
f.close()

n = len(matrix)

def get_all_max():
    ans = None
    for i in range(1,n+1):
        for j in range(1,n+1):
            one_max = get_one_max(i,j)
            if ans is None or one_max > ans:
                ans = one_max
    print ans

def sub_sum(a,b, c,d):
    total = 0
    for i in range(c):
        for j in range(d):
            total += matrix[a+i][b+j]
    return total

def get_one_max(x, y):
    ans = None
    for i in range(n+1-x):
        for j in range(n+1-y):
            total = sub_sum(i,j, x,y)
            if ans is None or total > ans:
                ans = total
    return ans

get_all_max()




