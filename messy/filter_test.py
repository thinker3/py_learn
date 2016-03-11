li = [0, 1, 'a', '', ' ', None]
lit = filter(None, li)
print li
print lit

def my_filter(item):
    if isinstance(item, str):
        return True
    else:
        return False

print
li = [0, 1, 'a', '', ' ', None]
lit = filter(my_filter, li)
print li
print lit

