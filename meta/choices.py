#!/usr/bin/env python
# -*- coding: utf-8 -*-


class ChoiceItem(object):
    def __init__(self, value, label=None):
        self.value = value
        self.label = label


class ChoiceMeta(type):
    def __new__(meta, name, bases, attrs):
        choices = []
        for key, value in attrs.items():
            if isinstance(value, tuple):
                value = ChoiceItem(*value)
            if isinstance(value, ChoiceItem):
                if value.label is None:
                    value.label = key.capitalize()
                choices.append((value.value, value.label))
                attrs[key] = value.value
        attrs['choices'] = choices
        attrs['help_text'] = str(choices)
        return super().__new__(meta, name, bases, attrs)


class Choices(metaclass=ChoiceMeta):
    pass


class SexChoice(Choices):
    female = ChoiceItem(0)
    male = ChoiceItem(1)
    unknown = (2, 'Guess')


class BareChoiceMeta(type):
    def __new__(meta, name, bases, attrs):
        choices = []
        for key, value in attrs.items():
            if isinstance(value, tuple) and len(value) == 2:
                choices.append(value)
                attrs[key] = value[0]
        attrs['choices'] = choices
        attrs['help_text'] = str(choices)
        return super().__new__(meta, name, bases, attrs)


class BareSexChoice(metaclass=BareChoiceMeta):
    female = (0, '女')
    male = (1, '男')
    unknown = (2, '未知')


if __name__ == '__main__':
    print(SexChoice.help_text)
    assert SexChoice.choices == [(0, 'Female'), (1, 'Male'), (2, 'Guess')]
    assert SexChoice.female == 0
    assert SexChoice.unknown == 2

    print(BareSexChoice.help_text)
    assert BareSexChoice.choices == [(0, '女'), (1, '男'), (2, '未知')]
    assert BareSexChoice.female == 0
    assert BareSexChoice.unknown == 2
