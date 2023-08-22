"""
Numbers in Pi
"""
# O(n^3 +m) time | O(n + m) space
def numbersInPi(pi, numbers):
    numbersTable ={number:True for number in numbers}
    minSpaces =getMinSpaces(pi, numbersTable, {}, 0)
    return -1 if minSpaces == float("inf") else minSpaces

def getMinSpaces(pi, numbersTable, cache, idx):
    if idx == len(pi):
        return -1
    if idx in cache:
        return cache[idx]

    minSpaces = float("inf")

    for i in range(idx,len(pi)):
        prefix = pi[idx:i+1]
        if prefix in numbersTable:
            minSpacesInSuffix = getMinSpaces(pi, numbersTable, cache, i+1)
            minSpaces = min(minSpaces,minSpacesInSuffix + 1)
    cache[idx] = minSpaces
    return cache[idx]

# approach 2 -reversed
# O(n^3 +m) time | O(n + m) space
def numbersInPiReversed(pi, numbers):
    numbersTable ={number: True for number in numbers}
    cache = {}
    for i in reversed(range(len(pi))):
        getMinSpaces(pi, numbersTable, cache, i)
    return -1 if cache[0] == float("inf") else cache[0]

my_pi ="3141592"
my_numbers =[3141,5,31,2,4159,9,42]

print(numbersInPi(my_pi,my_numbers))