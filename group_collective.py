import re

p = r"Feb(ruary)? 2011"

s = "February 2011"
ss = "Feb 2011"
sss = "Febr 2011"

m = re.match(p,sss)
s
print m
print m.group()
print m.groups()