#!/usr/bin/env python
# encoding: utf-8

import re
from PyQt4 import QtGui
from PyQt4 import QtCore


class MyHighlighter(QtGui.QTextEdit):
    def __init__(self, parent=None):
        super(MyHighlighter, self).__init__(parent)
        # Setup the text editor
        text = """
        In this Word WoRd text I want to highlight this word and only this word.
        Any other word shouldn't be highlighted
        """
        self.setText(text)
        cursor = self.textCursor()
        # Setup the desired format for matches
        format = QtGui.QTextCharFormat()
        format.setBackground(QtGui.QBrush(QtGui.QColor("red")))
        # Setup the regex engine
        pattern = "word"
        pattern = re.compile(pattern, re.IGNORECASE)
        print(pattern)
        regex = QtCore.QRegExp(pattern.sub)
        # Process the displayed document
        pos = 0
        index = regex.indexIn(self.toPlainText(), pos)
        while (index != -1):
            # Select the matched text and apply the desired format
            cursor.setPosition(index)
            cursor.movePosition(QtGui.QTextCursor.EndOfWord, 1)
            cursor.mergeCharFormat(format)
            # Move to the next match
            pos = index + regex.matchedLength()
            index = regex.indexIn(self.toPlainText(), pos)

if __name__ == "__main__":
    import sys
    a = QtGui.QApplication(sys.argv)
    t = MyHighlighter()
    t.show()
    sys.exit(a.exec_())
