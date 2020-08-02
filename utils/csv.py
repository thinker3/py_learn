#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unicodecsv import reader
UnicodeReader = reader


class UnicodeGBKReader(UnicodeReader):

    def _unicode(self, value, encoding_errors):
        try:
            return str(value, 'gbk', encoding_errors)
        except UnicodeDecodeError:
            return str(value, 'utf-8', encoding_errors)

    def __next__(self):
        row = next(self.reader)
        encoding_errors = self.encoding_errors
        if self._parse_numerics:
            return [(value if isinstance(value, float) else
                    self._unicode(value, encoding_errors))
                    for value in row]
        else:
            return [self._unicode(value, encoding_errors)
                    for value in row]
