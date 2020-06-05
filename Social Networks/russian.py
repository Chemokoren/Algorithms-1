"""
Let's say we're computing russian(63,12) .At some point during the execution,
we have x =7 and z =84. What is y at this moment?

ab =xy +z
63.12 =7y+84
756-84 =7y
672/7 =y
96 =y

"""

def russian(a,b):
	x =a; y =b
	z = 0
	while x > 0:
		if x % 2 == 1:
			z = z + y
		y = y << 1
		x = x >> 1

	return z

print (russian(63,12))
