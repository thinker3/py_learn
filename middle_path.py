from sys import argv

def get_right_down(a, b):
    temp = []
    if b+1 < n:
        temp.append((a, b+1))
    if a+1 < n:
        temp.append((a+1, b))
    return temp

def get_left_up(a, b):
    temp = []
    if 0 <= a-1:
        temp.append((a-1, b))
    if 0 <= b-1:
        temp.append((a, b-1))
    return temp

def get_one_min(a, b):
    paths = [[(a, b)]]
    ans = []
    j = n-2
    for i in range(j):
        for one in paths:
            right_down = get_right_down(*one[-1])
            left_up = get_left_up(*one[0])
            for c in left_up:
                for d in right_down:
                    ans.append([c] + one + [d])
        paths = ans
        ans = []
    return get_min_of_paths(paths)

def get_min_of_paths(paths):
    ans = None
    for i in paths:
        total = 0
        for j in i:
            a, b = j
            total += matrix[a][b]
        if ans is None or total < ans:
            ans = total 
    return ans

def get_min():
    ans = None
    for i in range(n):
        one_min = get_one_min(i, n-1-i)
        if ans is None or one_min < ans:
            ans = one_min
    print ans + matrix[n-1][n-1] + matrix[0][0]

f = open(argv[1], 'r')
n = i = 0 
matrix = []
for one in f:
    if one != '\n':
        if i == 0:
            n = i = int(one)
        elif i == 1:
            matrix.append(map(int, one.split(',')))
            get_min()
            i = 0
            matrix = []
        else:
            matrix.append(map(int, one.split(',')))
            i -= 1
f.close()

