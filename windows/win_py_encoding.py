#coding: utf8

import sys
import locale

print sys.getfilesystemencoding()
print sys.getdefaultencoding()
# code page of the console
print sys.stdout.encoding
print locale.getdefaultlocale()
print locale.getpreferredencoding()

s = u'命令处理程序'
print s

