import re

s='<title></title>'
m=re.match('<.*?>',s)
print(m.group())


m=re.match('<.*>',s)
print(m.group())