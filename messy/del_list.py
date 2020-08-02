l = [2,4,9]
a = l.remove(2) #remove obj, do not return it
print(a)
print(l)
#None
#[4, 9]

b = l.pop(0)    #pop obj at some index, and return it
print(b, l)
#4 [9]

l = [2,4,9]
index = l.index(9)
a = l.pop(index)
print(a, l)

l = [2,4,9]
del l[2]    #del
print(l)
