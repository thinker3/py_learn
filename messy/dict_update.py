#!/usr/bin/env python
# encoding: utf-8

one = {
    1: 1,
    2: 2,
}

two = {
    2: 'b',
    3: 3,
}

three = dict(
    # 3='c',  # SyntaxError: keyword can't be an expression
    # 4=4,  # SyntaxError: keyword can't be an expression
    c=3,
    d=4,
)

# both ok
one.update(two)
one.update(**two)
one.update(three)

one.update(
    this='this'
)
print(one)

print(dict.fromkeys(['a', 'b', 'c'], 1))

data = [
    ('a', 1),
    ('b', 2),
    ('a', 3),
    ('b', 4),
    ('c', 5),
]
total = {}
for k, v in data:
    total.setdefault(k, []).append(v)
print(total)
total = {k: sum(v) for k, v in list(total.items())}
print(total)

a = {k: str(k) for k in range(4)}
print(a)
for k, v in list(a.items()):
    del a[k]
    a[v] = k
print(a)

# update reversed
defaults = dict(
    ip='127.0.0.1',
    port=4002,
)
params = dict(
    port=5002,
    debug=True,
)
params = dict(defaults, **params)
assert params == dict(
    ip='127.0.0.1',
    port=5002,
    debug=True,
)
