"""
work out how many units of time it takes to excute clique(n) asa function of n.
def count():
 #your code here to count the units of time it takes to execute clique(n)
 
"""

def clique(n):
	print ("in a clique ...")
	for j in range(n):
		for i in range(j):
			print (i, "is friends with", j)

clique(4)

