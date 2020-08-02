import copy


def arrange(n):
    if n <= 0:
        return
    result = [[]]
    for i in range(n):
        temp = []
        for each in result:
            for j in range(i + 1):
                t = copy.copy(each)
                t.insert(j, i)
                temp.append(t)
        result = copy.deepcopy(temp)
    return result


def arrangestr(s):
    n = len(s)
    list_n = arrange(n)
    list_s = s[:]
    temp = []
    for L in list_n:
        temp = []
        for j in range(n):
            temp.append(list_s[L[j]])
        print("".join(temp))
    print(len(list_n))


arrangestr('abcdefg')
