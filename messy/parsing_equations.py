equ = [
        '3x1 + 2x2 = 7',
        '2x2 + -3x1 = 8',
        '-4x3 + 1x1 = 9',
        '-7x4 + 5x1 - 2x3 = -1',
        ]

import re

B = []
p_right = re.compile(r'= ([-]?\d+$)')
for one in equ:
    m = p_right.findall(one)
    B.append(float(m[0]))

p_var = re.compile(r'x\d')
vars = set([])
for one in equ:
    m = p_var.findall(one)
    vars |= set(m)
vars = sorted(list(vars))

p_ef = re.compile(r'([+-]* *\d*)(x\d)')
effs = []
for one in equ:
    m = p_ef.findall(one)
    temp = [0] * len(vars)
    for num, var in m:
        try:
            temp[vars.index(var)] = float(num.replace(' ', ''))
        except:
            pass
    effs.append(tuple(temp))

for one in effs:
    print(one)

import numpy as np
A = np.array(effs)
x = np.linalg.lstsq(A,B)
print(vars)
print(x[0])



