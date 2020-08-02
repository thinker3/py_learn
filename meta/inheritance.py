#!/usr/bin/env python
# -*- coding: utf-8 -*-

from meta.hello import (
    HelloType,
    Hello,
)
from meta.choices import BareChoiceMeta


class MixedMeta(HelloType, BareChoiceMeta):
    pass


class MixedHello(Hello, metaclass=MixedMeta):
    one = (1, 'One')
    two = (2, 'Two')


if __name__ == '__main__':
    print(MixedHello.choices)
    MixedHello.greet()
