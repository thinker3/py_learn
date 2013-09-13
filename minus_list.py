import re
from time import sleep

p = re.compile(r'\s+')

data = '''1  0   937 306 97  3
2  164472  75  17  81  3
3  197154  35268   306 97  3
4  310448  29493   64  38  1
5  310541  29063   64  38  1
6  310684  33707   64  38  1
7  319091  47451   16  41  1
8  319101  49724   16  41  1
9  324746  61578   1   5   1
10  324939  54611   1   5   1\n''' * 5000

data = data.split('\n')[0:-1]
data = [p.split(one) for one in data]
data = [map(int, one) for one in data]


def list_diff(a, b):
    temp = a[:]
    temp[1] = a[1] - b[1]
    return temp

result = [
        data[0],
    ]

for i, _ in enumerate(data):
    if i < len(data) - 1:
        result.append(list_diff(data[i+1], data[i]))

for i, one in enumerate(result):
    one[0] = i+1
    print one
    sleep(0.001)

