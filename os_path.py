import os

print __file__
print type(__file__)
print os.path.abspath(__file__)

print
print os.getcwd()
print os.walk(os.getcwd())
for one in os.walk(os.getcwd()):
    print one
