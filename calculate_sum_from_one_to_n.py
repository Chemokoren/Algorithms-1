"""
suppose we want to write a function that calculates the sum of all numbers from 1 up to(and including) some number n.
"""
def addUpTo(n):
    total = 0
    for i in range(n):
        total +=i
    return total

def addUpTo1(n):
    return n*(n+1)/2

print(addUpTo1(10))
