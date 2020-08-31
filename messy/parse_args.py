#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse


def test():
    parser = argparse.ArgumentParser()
    # parser.add_argument('-h', '--host', default="localhost")  # -h, --help is reserved
    parser.add_argument('-c', '--count', type=int, help='count', default=1)  # default is None if not specified
    parser.add_argument('-d', '--debug', action='store_true', help='debug or not')
    parser.add_argument('-f', '--filename')
    parser.add_argument('-u', '--username', help='username to login', default='admin')

    actions = parser._actions[1:]
    options = parser.parse_args()
    added_args = [getattr(options, action.dest) for action in actions]
    assert added_args == [
        options.count,
        options.debug,
        options.filename,
        options.username,
    ]
    for index, action in enumerate(actions):
        print(f'{action.dest}: {added_args[index]}')


if __name__ == '__main__':
    test()
