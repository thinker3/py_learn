from sys import argv

nums = [1, 2, 3]
def how_many_steps(n):
    while n > len(nums):
        nums.append(nums[-2]+nums[-1])
    return nums[n-1]

f = open(argv[1], 'r')
for one in f:
    if one != '\n':
        print how_many_steps(int(one))
f.close()
