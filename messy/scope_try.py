try:
    a = 1 # a must be defined before possible exception
    a = 30/0
except:
    if a:
        print(a)
