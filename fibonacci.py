def fibonacci(n):
	a=b=1
	yield a
	yield b
	i=1
	while i<=n-2:
		a,b = b,a+b
		i += 1
		yield b

t = fibonacci(9)
for one in t:
	print one


def fibonacci_(n):
	a=b=1
	print a
	print b
	i=1
	while i<=n-2:
		a,b = b,a+b
		i += 1
		print b

fibonacci_(9)

m = map(lambda x:2*x,fibonacci(9))
print type(m)
print m

