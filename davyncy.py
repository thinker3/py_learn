src = \
'''
O draconia;conian devil! Oh la;h lame sa;saint!

m quaerat voluptatem.;pora incidunt ut labore et d;, consectetur, adipisci velit;olore magnam aliqua;idunt ut labore et dolore magn;uptatem.;i dolorem ipsum qu;iquam quaerat vol;psum quia dolor sit amet, consectetur, a;ia dolor sit amet, conse;squam est, qui do;Neque porro quisquam est, qu;aerat voluptatem.;m eius modi tem;Neque porro qui;, sed quia non numquam ei;lorem ipsum quia dolor sit amet;ctetur, adipisci velit, sed quia non numq;unt ut labore et dolore magnam aliquam qu;dipisci velit, sed quia non numqua;us modi tempora incid;Neque porro quisquam est, qui dolorem i;uam eius modi tem;pora inc;am al
'''

'''
O draconian devil! Oh lame saint!

Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem.
'''

def get_overlap_number_sub(a, b):
    len_a, len_b = map(len, (a, b))
    b0 = b[0]
    try:
        j = a.index(b0)
        le_a = len_a-j
        if le_a == 1:
            return 1
        for i in xrange(1, min(le_a, len_b)):
            if a[i+j] != b[i]:
                return 0
        else:
            return i + 1
    except:
        return 0

def get_overlap_number(a, b):
    #m = max(get_overlap_number_sub(a, b), get_overlap_number_sub(b, a))
    i = get_overlap_number_sub(a, b)
    j = get_overlap_number_sub(b, a)
    if i>j:
        return i
    elif i<j:
        return j
    else:
        return 0

def merge(a, b):
    i = get_overlap_number_sub(a, b)
    j = get_overlap_number_sub(b, a)
    if i>j:
        return a + b[i:]
    else:
        return b + a[j:]


from time import sleep
for one in src.split('\n'):
    if one:
        fragments = one.split(';')
        temp = []
        while len(fragments) + len(temp)>1:
            n = len(fragments)
            if n <= 1:
                fragments = fragments + temp
                temp = []
                continue
            sleep(0.1)
            the_max = 0
            index = 0
            for i in xrange(1, n):
                m = get_overlap_number(fragments[0], fragments[i])
                if m > the_max:
                    the_max = m
                    index = i
            if index:
                merged = merge(fragments[0], fragments[index])
                fragments.pop(index)
                fragments.pop(0)
                temp.append(merged)
            else:
                s0 = fragments.pop(0)
                temp.append(s0)
            print fragments, temp








