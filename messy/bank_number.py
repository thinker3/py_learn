def new_number(a):
    for i, l in enumerate(a, start=1):
        if i%4 == 0:
            yield l
            if i != len(a):
                yield ' '
        else:
            yield l

a = '983497829489328492'
a = list(new_number(a))
print a
print ''.join(a)

a = '98349782948932849229'
a = list(new_number(a))
print a
print ''.join(a)

a = '98349782948932849229'
print ''.join(new_number(a))
