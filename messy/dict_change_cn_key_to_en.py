#coding=utf8
d1 = {
        '姓名': 'chenkun',
        '性别': 1,
        }

d2 = {
        '': '',
        '姓名': 'name',
        '性别': 'sex',
        }

n_d = {}
for k, v in list(d1.items()):
    n_key = d2[k]
    n_value = v
    n_d[n_key] = n_value

for k, v in list(n_d.items()):
    print(k, v)
