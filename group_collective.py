import re

p = r"Feb(ruary)? 2011"

s = "February 2011"
ss = "Feb 2011"
sss = "Febr 2011"

m = re.match(p, ss)
print m
print m.group()
print m.groups()


s_list = [
    'something{now I am wrapped {I should {not{} cause} splitting} I am still wrapped} something else',
    'something{now I am wrapped {I should {not{} cause} splitting} I am still wrapped}',
    '{now I am wrapped {I should {not{} cause} splitting} I am still wrapped} something else',
    '{now I am wrapped {I should {not{} cause} splitting} I am still wrapped}',
    'now I am wrapped {I should {not{} cause} splitting} I am still wrapped}',
    '{now I am wrapped {I should {not{} cause} splitting} I am still wrapped',
    'now I am wrapped {I should {not{} cause} splitting} I am still wrapped',
    ]
for one in s_list:
    m = re.search(r'([^{]*)({)(.*)(})([^}]*)', one)
    print m.groups()
