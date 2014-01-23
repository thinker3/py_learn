from sys import argv

def get_right(a, b):
    if b+1 < n:
        return [(a, b+1)]
    else:
        return []

def get_down(a, b):
    if a+1 < n:
        return [(a+1, b)]
    else:
        return []

def get_paths():
    paths = [[(0, 0)]]
    ans = []
    j = 2*n-2
    for i in range(j):
        for one in paths:
            temp = get_right(*one[-1])
            if temp:
                ans.append(get_num_list(one) + temp)
            temp = get_down(*one[-1])
            if temp:
                ans.append(get_num_list(one) + temp)
        paths = ans
        ans = []
    return paths

def get_num_list(one, flag=True):
    a, b = one[-1]
    total = matrix[a][b]
    if len(one)>1:
        total += one[0]
    if flag:
        return [total]
    else:
        return total

def get_min():
    ans = None
    for one in get_paths():
        total = get_num_list(one, False)
        if ans is None or ans > total:
            ans = total 
    print ans

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







