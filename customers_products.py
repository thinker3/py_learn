from sys import argv


def prepare(one):
    customers, products = one.split(';')
    customers = customers.split(',')
    products = products.split(',')
    return customers, products 

def get_letters(name):
    global cache
    if cache.has_key(name+'_l'):
        return cache[name+'_l']
    num = 0
    for i in name:
        if i.isalpha():
            num += 1
    cache[name+'_l'] = num
    return num

def get_vowels(name):
    global cache
    if cache.has_key(name+'_v'):
        return cache[name+'_v']
    vowels = 'aeiouy'
    vowels += vowels.upper()
    num = 0
    for i in name:
        if i in vowels:
            num += 1
    cache[name+'_v'] = num
    return num
    

def get_ss(product, customer):
    if get_letters(product) % 2 == 0: # even
        ss = get_vowels(customer) * 1.5
    else: # odd
        ss = get_letters(customer) - get_vowels(customer)
    if has_common_factor(get_letters(customer), get_letters(product)):
        ss *= 1.5
    return ss

def has_common_factor(less, more):
    if less>more:
        less, more = more, less
    global cache
    if cache.has_key('%s_%s' % (less, more)):
        return cache['%s_%s' % (less, more)]
    for i in range(2, less/2+1):
        if less%i == more%i == 0:
            cache['%s_%s' % (less, more)] = True
            return True
    if less>1 and more%less == 0:
        cache['%s_%s' % (less, more)] = True
        return True
    else:
        cache['%s_%s' % (less, more)] = False
        return False

import itertools
def get_max_ss(customers, products):
    max_ss = 0
    if len(customers) <= len(products):
        for some_products in itertools.combinations(products, len(customers)):
            for one in itertools.permutations(some_products):
                option = zip(one, customers) 
                ss = 0
                for product, customer in option:
                    ss += get_ss(product, customer)
                max_ss = ss if ss > max_ss else max_ss
    else:
        for some_customers in itertools.combinations(customers, len(products)):
            for one in itertools.permutations(some_customers):
                option = zip(products, one) 
                ss = 0
                for product, customer in option:
                    ss += get_ss(product, customer)
                max_ss = ss if ss > max_ss else max_ss
    return max_ss

cache = {'a': 1}
def main():
    f = open(argv[1], 'r')
    for one in f:
        if one.strip():
            global cache
            cache = {}
            customers, products = prepare(one)
            max_ss = get_max_ss(customers, products)
            print '%.2f' % max_ss
    f.close()

def test():
    print has_common_factor(1, 15)

main()











