#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

utils_path = os.path.dirname(os.path.abspath(__file__))
py_learn_path = os.path.join(utils_path, '..')


def get_abs_path(seq):
    return os.path.join(py_learn_path, *seq)
