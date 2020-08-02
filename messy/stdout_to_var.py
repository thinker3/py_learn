import subprocess
p = subprocess.Popen("git st", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

p_stdout = p.stdout.read()
p_stderr = p.stderr.read()

print('*' * 30)
print(p_stdout)
print('*' * 30)
print(p_stderr)
print('*' * 30)
