from sys import argv

d = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10,
    'eleven': 11,
    'twelve': 12,
    'thirteen': 13,
    'fourteen': 14,
    'fifteen': 15,
    'sixteen': 16,
    'seventeen': 17,
    'eighteen': 18,
    'nineteen': 19,
    'twenty': 20,
    'thirty': 30,
    'forty': 40,
    'fifty': 50,
    'sixty': 60,
    'seventy': 70,
    'eighty': 80,
    'ninety': 90,
    'hundred': 100,
    'thousand': 1000,
    'million': 10 ** 6,
}

multipliers = [100, 1000, 10 ** 6]


def to_number(one):
    factor = 1
    if one[0] == 'negative':
        factor = -1
        one = one[1:]
    one = [d[i] for i in one]
    ans = 0
    sub_ans = 0
    temp = []
    last_multiplier = 1
    last_max_multipler = 1
    for i in one:
        if i in multipliers:
            if i > last_max_multipler:
                ans = (ans + sub_ans + sum(temp)) * i
                sub_ans = 0
                last_max_multipler = i
            elif i > last_multiplier:
                sub_ans = (sub_ans + sum(temp)) * i
            else:
                ans += sub_ans
                sub_ans = sum(temp) * i
            temp = []
            last_multiplier = i
        else:
            temp.append(i)
    ans += sum(temp) + sub_ans

    return ans * factor


f = open(argv[1], 'r')
for one in f:
    one = one.strip()
    if one:
        print(to_number(one.split()))
f.close()
