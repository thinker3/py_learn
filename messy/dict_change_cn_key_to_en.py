#coding=utf8
d1 = {
        u'姓名': 'chenkun',
        u'性别': 1,
        }

d2 = {
        u'': '',
        u'姓名': 'name',
        u'性别': 'sex',
        }

n_d = {}
for k, v in d1.items():
    n_key = d2[k]
    n_value = v
    n_d[n_key] = n_value

for k, v in n_d.items():
    print k, v
