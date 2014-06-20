import random

n=0
while n<10:
    r = random.randint(0,10) # integers in [0, 10]
    print r,
    n += 1

print
numbers = range(0, 20)
some_numbers= random.sample(numbers, 5)
print numbers
print some_numbers

print random.choice(numbers)

random.seed(0)
print random.random()
random.seed(0)
print random.random()
print random.random()
