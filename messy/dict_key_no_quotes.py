a = (1, 2, 3)
b = ('jack', 'tom')
d = {
    a: 'abc',
    b: 'edf',
}

for k, v in list(d.items()):
    print(k, v)


print()
d = {True: 'abc', False: '123'}
for k, v in list(d.items()):
    print(k, v)
print(d[True])
print(d[False])

li = [(k, v) for k, v in list(d.items())]
print(li)  # [(False, '123'), (True, 'abc')]

print(list(d.items()))  # [(False, '123'), (True, 'abc')]
print(iter(d.items()))  # <dictionary-itemiterator object at 0x7f9456456f18>
