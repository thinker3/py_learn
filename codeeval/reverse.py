from sys import argv
f = open(argv[1], 'r')
for one in f:
    if one != '\n':
        print ' '.join(one.split()[::-1])
f.close()
