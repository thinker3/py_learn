from sys import argv
import itertools


def done(one):
    row_num, col_num = fill_matrix(one)
    if row_num < col_num:
        transpose(row_num, col_num)
        row_num, col_num = col_num, row_num
    row_num = remove_rows_if_possible(row_num, col_num)
    max_ss = 0
    for one in itertools.permutations(range(row_num), col_num):
        total = 0
        for i in range(col_num):
            total += matrix[one[i]][i]
        if max_ss < total:
            max_ss = total
    return max_ss


def transpose(row_num, col_num):
    temp = []
    for i in xrange(col_num):
        row = tuple(map(lambda j: matrix[j][i], range(row_num)))
        temp.append(row)
    global matrix
    matrix = temp


def remove_rows_if_possible(row_num, col_num):
    while row_num > col_num:
        s = set([])
        for i in range(3):
            matrix.sort(key=lambda x: x[i])
            s.add(matrix[0])
        if len(s) == 1:
            matrix.pop(0)
            row_num -= 1
        else:
            break
    return row_num


def fill_matrix(one):
    customers, products = one.split(';')
    customers = customers.split(',')
    products = map(get_letters, products.split(','))
    row_num = len(customers)
    col_num = len(products)
    for customer in customers:
        row = []
        letters = get_letters(customer)
        vowels = get_vowels(customer)
        for product in products:
            row.append(get_ss(product, letters, vowels))
        matrix.append(tuple(row))
    return row_num, col_num


def get_letters(name):
    num = 0
    for i in name:
        if i.isalpha():
            num += 1
    return num


def get_vowels(name):
    vowels = 'aeiouy'
    vowels += vowels.upper()
    num = 0
    for i in name:
        if i in vowels:
            num += 1
    return num


def get_ss(product, letters, vowels):
    if product % 2 == 0:  # even
        ss = vowels * 1.5
    else:  # odd
        ss = letters - vowels
    if has_common_factor(letters, product):
        ss *= 1.5
    return ss


def has_common_factor(less, more):
    if less > more:
        less, more = more, less
    if less <= 1:
        return False
    elif more % less == 0:
        return True
    for i in range(2, less / 2 + 1):
        if less % i == more % i == 0:
            return True
    return False


f = open(argv[1], 'r')
for one in f:
    if one.strip():
        matrix = []
        max_ss = done(one)
        print '%.2f' % max_ss
f.close()
