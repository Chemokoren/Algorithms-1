# numbers in pi -you are given a string representation of the first n digits
# of pi e.g. 3141592
# you are also given a list of your favorite numbers
# find the minimum number of spaces you can add in the digits of pi such that
# all the remaining numbers will be found in your list of favourites
# my_favorites =[3141, 5, 31, 2,4159, 9, 42]
# e.g. (31 | 4159 | 2 ) OR (3141| 5 | 9 | 2)
# O(n ^ 3 +m) time | O(n + m) space
def numbersInPi(pi, numbers):
    numbersTable ={number: True for number in numbers}
    minSpaces =getMinSpaces(pi,numbersTable, {}, 0)
    return -1 if minSpaces == float("inf") else minSpaces

def getMinSpaces(pi, numbersTable, cache, idx):
    if idx ==len(pi):
        return -1
    if idx in cache:
        return cache[idx]
    minSpaces =float("inf")
    for i in range(idx, len(pi)):
        prefix =pi[idx:i + 1]
        if prefix in numbersTable:
            minSpacesInSuffix = getMinSpaces(pi,numbersTable, cache, i+1)
            minSpaces =min(minSpaces, minSpacesInSuffix +1)
    cache[idx] = minSpaces
    return cache[idx]

# O(n^3 + m) time | O(n + m) space
def numbersInPi1(pi, numbers):
    numbersTable ={number: True for number in numbers}
    cache ={}
    for i in reversed(range(len(pi))):
        getMinSpaces(pi, numbersTable,cache, i)
    return -1 if cache[0] ==float("inf") else cache[0]

my_string ="3141592"
my_favorites =[3141, 5, 31, 2,4159, 9, 42]
print(numbersInPi1(my_string,my_favorites))


