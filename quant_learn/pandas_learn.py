#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd

inp = [
    {'c1':10, 'c2':100},
    {'c1':11, 'c2':110},
    {'c1':12, 'c2':120},
]
df = pd.DataFrame(inp)
print(df)


def iteritems():
    for key, serie in df.iteritems():
        import ipdb; ipdb.set_trace()


def iterkv():
    for key, serie in df.iterkv():  # iteritems == iterkv
        import ipdb; ipdb.set_trace()


def iterrows():
    for key, serie in df.iterrows():
        import ipdb; ipdb.set_trace()


def itertuples():
    for one in df.itertuples():
        print(one)
        print([getattr(one, title) for title in df.columns])


def zipping():
    rows = zip(df['c1'], df['c2'])
    rows = zip(df.c1, df.c2)
    columns = df.columns.tolist()
    rows = zip(*[getattr(df, title) for title in df.columns])
    import ipdb; ipdb.set_trace()


def apply():
    print(df.sum(0))
    print(df.sum(1))
    def inner(x):
        return sum(x)
    ret = df.apply(inner, axis=0)  # x is a column
    print(ret)
    ret = df.apply(inner, axis=1)  # x is a row
    print(ret)


if __name__ == '__main__':
    apply()
