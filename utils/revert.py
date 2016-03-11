import subprocess
import re, os


p = subprocess.Popen("svn st", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
files = p.stdout.read()

files = [one for one in files.split('\n')]
modified = [one for one in files if one.startswith('M')]
new = [one for one in files if one.startswith('?')]

modified = [re.split(r'\s+', one)[-1] for one in modified]
for one in modified:
    print one
    os.system('svn revert %s' % one)

