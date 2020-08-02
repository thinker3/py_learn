import datetime
import itertools

num = 10
num = 9

def my_inductive_permutations_generator(n):
    ans = [[0]]
    if n <= 1:
        yield ans[0]
    temp = []
    for i in range(1, n):
        for one in ans:
            for j in range(i,-1,-1):
                two = one[:]
                two.insert(j, i)
                if i == n-1:
                    yield two
                else:
                    temp.append(two)
        ans = temp 
        temp = []

def my_permutations_generator_faster(n):
    l = list(range(n))
    yield l
    if n<=1:
        return
    while 1:
        for i in range(n-1, 0, -1):
            l[i], l[i-1] = l[i-1], l[i]
            yield l
        index = 0 
        for i in range(1, n):
            if not index and l[i] != n-i-1:
                index = i
                continue
            if index and l[i] == n-index-1:
                l[i], l[i-1] = l[i-1], l[i]
                left = l[:index]
                left.reverse()
                l = l[index:] + left
                yield l
                break
        else:
            return

def python_permutations(n):
    indices = list(range(n))
    cycles = list(range(n, 0, -1))
    yield indices
    while n:
        for i in reversed(list(range(n))):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield indices
                break
        else:
            return

def permute_in_place(n):
    a = list(range(n))
    yield a
    if n <= 1:
        return
    while 1:
        i = n - 1
        while 1:
            i = i - 1
            if a[i] < a[i+1]:
                j = n - 1
                while a[i] >= a[j]:
                    j = j - 1
                a[i], a[j] = a[j], a[i]
                r = a[i+1:n]
                r.reverse()
                a[i+1:n] = r
                yield a
                break
            if i == 0:
                return

def get_time_delta(f):
    now = datetime.datetime.now()
    s = 0
    for one in f:
        s += 1
    delta = (datetime.datetime.now() - now)
    return delta

def main():
    times = []
    times.append(get_time_delta(itertools.permutations(list(range(num)))))
    times.append(get_time_delta(my_permutations_generator_faster(num)))
    times.append(get_time_delta(my_inductive_permutations_generator(num)))
    times.append(get_time_delta(permute_in_place(num)))
    times.append(get_time_delta(python_permutations(num)))
    for one in times:
        print(one)

main()





