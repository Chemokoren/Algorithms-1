"""
How many units of time does it take to execute clique(4)?
Count each print statement as one unit and count each time range is evaluated as one unit

print
range 4 (0,1,2,3)
range 0
range 1
print
range 2
print
print
range 3
print
print
print

Answer is 12
"""

def clique(n):
	print ("in a clique ...")
	for j in range(n):
		for i in range(j):
			print (i, "is friends with", j)

clique(4)
