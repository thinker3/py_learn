import os

# run in this floder and another folder respectively
print __file__, type(__file__)
filepath = os.path.abspath(__file__)
print filepath
print os.path.dirname(filepath)
print os.path.dirname(__file__)

print '-' * 100
print __name__, type(__name__)

