from sys import argv
f = open(argv[1], 'r')
for one in f.readlines():
    if one not in ['\n']:
        print ' '.join(one.split()[::-1])
f.close()
