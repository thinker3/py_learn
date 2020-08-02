#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Celsius(object):
    def __init__(self, temperature=0):
        self.__temperature = temperature

    @property  # define property getter first, or else NameError: name 'temperature' is not defined
    def _temperature(self):
        return self.__temperature

    @_temperature.setter
    def temperature(self, value):  # method name must be temperature, or else AttributeError: can't set attribute
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible")
        self.__temperature = value

    def get_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    def set_fahrenheit(self, value):
        limit = -459.67
        if value < limit:
            raise ValueError(f"Fahrenheit below {limit} is not possible")
        self.__temperature = round((value - 32) / 1.8, 2)

    # fahrenheit = property(get_fahrenheit, set_fahrenheit)

    # fahrenheit = property()
    # fahrenheit.getter(get_fahrenheit)  # AttributeError: unreadable attribute
    # fahrenheit.setter(set_fahrenheit)

    # fahrenheit = property(get_fahrenheit)
    # fahrenheit.fset = set_fahrenheit  # AttributeError: readonly attribute
    # fahrenheit.setter(set_fahrenheit)  # AttributeError: can't set attribute

    # https://docs.python.org/3/howto/descriptor.html
    _fahrenheit = property(get_fahrenheit)
    fahrenheit = _fahrenheit.setter(set_fahrenheit)
    assert not (_fahrenheit is fahrenheit)


if __name__ == '__main__':
    t = Celsius()
    t.temperature = 1
    assert t.temperature == 1 == t._temperature
    assert t.fahrenheit == 33.8 == t._fahrenheit
    t.fahrenheit = 35.6
    t.fahrenheit == 35.6
    assert t.temperature == 2.0
