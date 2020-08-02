def show(dt):
    for i in dt:
        print(i)
    print(dt)
    print('a=%d,b=%d,c=%d' % dt)

show((1,3,5))


print()
def abc(a=None, b=None, c=None):
    print(a, c)

abc('a', 'b')
abc('a', c='c')
