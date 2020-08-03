#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils.common import (
    deep_update,
)


source = {
    'pk': 1,
    'profile': {
        'pk': 1,
        'gender': 0,
        'nick_name': 'Lily',
    }
}
override = {
    'pk': 1,
    'profile': {
        'gender': 2,
        'address': 'there',
    }
}
deep_update(source, override)
assert source == {
    'pk': 1,
    'profile': {
        'pk': 1,
        'gender': 2,
        'address': 'there',
        'nick_name': 'Lily',
    }
}


source = {
    'pk': 1,
    'profile': 1,
    'username': 'admin',
}
override = {
    'pk': 2,
    'profile': {
        'pk': 1,
        'gender': 1,
    }
}
deep_update(source, override)
assert source == {
    'pk': 2,
    'profile': {
        'pk': 1,
        'gender': 1,
    },
    'username': 'admin',
}


source = {
    'pk': 1,
    'profile': {
        'pk': 1,
        'gender': 1,
    },
    'username': 'admin',
}
override = {
    'pk': 2,
    'profile': None,
}
deep_update(source, override)
assert source == {
    'pk': 2,
    'profile': None,
    'username': 'admin',
}
