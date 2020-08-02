import os

print(os.getcwd())
print(os.walk(os.getcwd()))
#for one in os.walk(os.getcwd()): # too many
    #print one

#dirname = os.path.dirname(__file__)
dirname = os.path.dirname(os.path.abspath(__file__))
print(dirname)
test = os.path.join(dirname, 'test/')
print(test)
if not os.path.exists(test):
    os.makedirs(test)

print('-' * 50)
for one in os.listdir(os.getcwd()):
    if one.endswith('~'):
        print(one)
    #if os.path.isdir((os.path.join(os.getcwd(), one))):
    if os.path.isdir(one):
        print(one)

print('-' * 50)
print(__file__)
print(type(__file__))
print(os.path.abspath(__file__))
print(os.path.dirname(__file__)) # chenkun@chenkun-P43T-ES3G:~/git$ py py_learn/os_path.py
print(os.path.dirname(os.path.abspath(__file__))) # ends without '/' # /home/chenkun/git/py_learn
print(os.path.basename(__file__))

print('-' * 50)
print(os.path.join('/home', 'abc'))
print(os.path.join(['/home', 'abc'])) # ['/home', 'abc']
print('/'.join(['/home', 'abc']))
#print '/'.join('/home', 'abc') # TypeError: join() takes exactly one argument (2 given)
