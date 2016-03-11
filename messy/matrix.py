B = [5,-4,5,-6]
y = [
        [0,1,0,1],
        [0,0,0,0],
        [0,0,0,1],
        [0,0,0,0],
    ]
x = []
for i, row in enumerate(y):
    temp = []
    for j, col in enumerate(row):
        if col != 0:
            temp.append(str(col) + '*x' + str(i) + str(j))
        else:
            temp.append(col)
    x.append(temp)

#for one in x:
#    print one


equ = []
for i in xrange(4):
    temp1 = []
    temp2 = []
    for j in xrange(4):
        temp1.append(x[i][j])
        temp2.append(x[j][i])
    temp2.append(B[i])
    equ.append(tuple(temp1 + temp2))

equtions = []
for one in equ:
    s = '%s + %s + %s + %s - %s - %s - %s - %s = %s' % one
    equtions.append(s)

for one in equtions:
    print one

def solve(eq, var='x'):
    c = eval(eq.replace("=", "-(") + ")", {var: 1j})
    return -c.real/c.imag

import re
from time import sleep
from copy import deepcopy

equ_bak = deepcopy(equtions)

ans = {}
while(len(equtions) != 0):
    for i, one in enumerate(equtions):
        for k, v in ans.items():
            one = one.replace(k, str(v))
        try:
            var = re.search(r'x\d\d', one).group()
        except:
            equtions.pop(i)
        try:
            ans[var] = solve(one, var)
            equtions.pop(i)
        except:
            pass
    print equtions
    print ans
    sleep(1)



import re

p_var = re.compile(r'x\d\d')
vars = set([])
for one in equ_bak:
    m = p_var.findall(one)
    vars |= set(m)
vars = sorted(list(vars))

p_ef = re.compile(r'([+-]* *\d*)\*(x\d\d)')
effs = []
for one in equ_bak:
    m = p_ef.findall(one)
    #print m
    temp = [0] * len(vars)
    for num, var in m:
        try:
            temp[vars.index(var)] = float(num.replace(' ', ''))
        except:
            pass
    effs.append(tuple(temp))

#for one in effs:
#    print one

import numpy as np
A = np.array(effs)
x = np.linalg.lstsq(A,B)
print vars
print x[0]



