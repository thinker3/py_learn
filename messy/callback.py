from sys import argv
def show(sth):
    print('simple callback function to show %s' % sth)

def main(num, callback=None, sth=None):
    if num:
        callback(sth)
    else:
        print('callback function not called')

if __name__ == '__main__':
    num = int(argv[1])
    main(num, show, 'abc')
