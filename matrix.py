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
            temp.append('x' + str(i) + str(j))
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





















