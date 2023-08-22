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




# Write a function, `count`
# that returns the units of time
# where each print statement is one unit of time
# and each evaluation of range also takes one unit of time

def count(n):
    # Your code here to count the units of time
    # it takes to execute clique
    return 0

def clique(n):
    print "in a clique..."
    for j in range(n):
        for i in range(j):
            print i, "is friends with", j



