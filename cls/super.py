#!~/.pyenv/version
# -*- coding: utf-8 -*-


class A(object):
    def get(self):
        return 'A'

    def take(self):
        return 'AA'


class B(A):
    def get(self):
        return 'B'


class C(B):
    def test(self):
        assert super().get() == 'B'
        assert super(B, self).get() == 'A'
        assert super(C, self).get() == 'B'

        assert super().take() == 'AA'
        assert super(B, self).take() == 'AA'
        assert super(C, self).take() == 'AA'


if __name__ == '__main__':
    C().test()
