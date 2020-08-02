a = [[1,2],3,4,[[5,[6]],7,8]]

def flatten(nested):
	for sub in nested:
		if isinstance(sub,list):
			for e in flatten(sub):
				yield e
		else:yield sub

for i in flatten(a):
	print(i)

print()

def myprint(nested):
	for sub in nested:
		if not isinstance(sub,list):
			print(sub)
		else: myprint(sub)

myprint(a)
