import os

print os.getcwd()
print os.walk(os.getcwd())
for one in os.walk(os.getcwd()):
    print one

dirname = os.path.dirname(__file__)
test = os.path.join(dirname, 'test/')
if not os.path.exists(test):
    os.makedirs(test)

print
for one in os.listdir(os.getcwd()):
    if one.endswith('~'):
        print one
    #if os.path.isdir((os.path.join(os.getcwd(), one))):
    if os.path.isdir(one):
        print one

print
print __file__
print type(__file__)
print os.path.abspath(__file__)
print os.path.dirname(__file__)
print os.path.dirname(os.path.abspath(__file__))
print os.path.basename(__file__)
