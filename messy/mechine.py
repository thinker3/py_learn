#!/usr/bin/env python
# -*- coding: utf-8 -*-

from transitions import Machine


class Matter(object):
    pass

states = ['solid', 'liquid', 'gas', 'plasma']

transitions = [
    {
        'trigger': 'melt',
        'source': 'solid',
        'dest': 'liquid',
    },
    {
        'trigger': 'evaporate',
        'source': 'liquid',
        'dest': 'gas',
    },
    {
        'trigger': 'sublimate',
        'source': 'solid',
        'dest': 'gas',
    },
    {
        'trigger': 'ionize',
        'source': 'gas',
        'dest': 'plasma',
    },
]

lump = Matter()
machine = Machine(lump, states=states, transitions=transitions, initial='liquid')
