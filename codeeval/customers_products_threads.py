from sys import argv
import itertools
import threading
from time import sleep


ans = []
class Dosomething(threading.Thread):
    def __init__(self, one, index):
        super(Dosomething, self).__init__()
        self.matrix = []
        self.one = one 
        self.index = index 

    def run(self):
        ss = self.done(self.one)
        while len(ans) <= self.index:
            ans.append(0)
        ans[self.index] = ss

    def done(self, one):
        customers, products = one.split(';')
        customers = customers.split(',')
        products = list(map(get_letters, products.split(',')))
        for customer in customers:
            row = []
            letters = get_letters(customer)
            vowels = get_vowels(customer)
            for product in products:
                row.append(get_ss(product, letters, vowels))
            self.matrix.append(row)
        row_num = len(self.matrix)
        col_num = len(row)
        max_ss = 0
        less = row_num
        if row_num > col_num:
            less = col_num 
            for one in itertools.combinations(list(range(row_num)), less):
                for two in itertools.permutations(list(range(col_num))):
                    total = self.get_total(one, two, less)
                    max_ss = total if max_ss < total else max_ss
        else:
            for one in itertools.combinations(list(range(col_num)), less):
                for two in itertools.permutations(list(range(row_num))):
                    total = self.get_total(two, one, less)
                    max_ss = total if max_ss < total else max_ss
        return max_ss

    def get_total(self, one, two, less):
        total = 0
        for i in range(less):
            total += self.matrix[one[i]][two[i]]
        return total

def get_ss(product, letters, vowels):
    if product % 2 == 0: # even
        ss = vowels * 1.5
    else: # odd
        ss = letters - vowels
    if has_common_factor(letters, product):
        ss *= 1.5
    return ss

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
    
def has_common_factor(less, more):
    if less>more:
        less, more = more, less
    if less <= 1:
        return False
    elif more%less == 0:
        return True
    for i in range(2, less/2+1):
        if less%i == more%i == 0:
            return True
    return False

index = 0
f = open(argv[1], 'r')
for one in f:
    if one.strip():
        doer = Dosomething(one, index)
        while threading.active_count() >= 2:
            sleep(0.001)
        doer.start() # threading does not help here!!!
        index += 1
f.close()
while threading.active_count() >= 2:
    sleep(0.001)
for one in ans:
    print('%.2f' % one)












