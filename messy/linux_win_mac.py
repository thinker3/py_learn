import sys, os

print(type(sys.platform))
print(sys.platform)

import platform
print(platform.system())

print(os.name)
if sys.platform != 'win32':
    print(os.uname())
