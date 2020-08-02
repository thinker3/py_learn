#!/usr/bin/env python
# encoding: utf-8

matrix = [
        ['y', 'C', 'i'],
        ['a', 'r', 't'],
        ['i', '!', 'l'],
        ]

s = """
z p t m k
p b b v j
s f k l a
i z e w x
o n a o z
"""

matrix = [_f for _f in s.split('\n') if _f]
matrix = [row.split() for row in matrix]
dim = len(matrix)
wanted = []


def move_up_right(here):
    x, y = here
    x = (x - 1) % dim
    y = (y + 1) % dim
    return x, y


def move_down(here):
    x, y = here
    x = (x + 2) % dim
    y = (y - 1) % dim
    return x, y


def main():
    start = (0, dim / 2)
    num = 0
    while num < dim * dim:
        a, b = start
        if matrix[a][b] is None:
            start = move_down(start)
        else:
            wanted.append(matrix[a][b])
            num += 1
            matrix[a][b] = None
            start = move_up_right(start)
    print(''.join(wanted))


main()
