# O(n ^ 2) time | O(n ^ 2) space
def sameBsts(arrayOne, arrayTwo):
    if len(arrayOne) != len(arrayTwo):
        return False
    if len(arrayOne) == 0 and len(arrayTwo) ==0:
        return True
    if arrayOne[0] != arrayTwo[0]:
        return False

    leftOne =getSmaller(arrayOne)
    leftTwo =getSmaller(arrayTwo)
    rightOne =getBiggerOneorEqual(arrayOne)
    rightTwo =getBiggerOneorEqual(arrayTwo)

    return sameBsts(leftOne,leftTwo) and sameBsts(rightOne, rightTwo)

def getSmaller(array):
    smaller =[]
    for i in range(1, len(array)):
        if array[i] < array[0]:
            smaller.append(array[i])
    return smaller
def getBiggerOneorEqual(array):
    biggerOrEqual =[]
    for i in range(1,len(array)):
        if array[i] >= array[0]:
            biggerOrEqual.append(array[i])
    return biggerOrEqual



"""
approach 2 minimizes the space complexity
"""
# O(n ^ 2) time | O(d) space
def sameBsts1(arrayOne, arrayTwo):
    return areSameBsts(arrayOne, arrayTwo, 0, 0, float("-inf"), float("inf"))

def areSameBsts(arrayOne, arrayTwo, rootIdxOne, rootIdxTwo, minVal, maxVal):
    if rootIdxOne == -1 or rootIdxTwo == -1:
        return  rootIdxOne == rootIdxTwo

    if arrayOne[rootIdxOne] != arrayTwo[rootIdxTwo]:
        return False

    leftRootIdxOne =getIdxOfFirstSmaller(arrayOne, rootIdxOne, minVal)
    leftRootIdxTwo =getIdxOfFirstSmaller(arrayTwo, rootIdxTwo, minVal)
    rigtRootIdxOne =getIdxOfFirstBiggerOrEqual(arrayOne, rootIdxOne, maxVal)
    rigtRootIdxTwo =getIdxOfFirstBiggerOrEqual(arrayTwo, rootIdxTwo, maxVal)


    currentValue =arrayOne[rootIdxOne]
    leftAreSame =areSameBsts(arrayOne, arrayTwo, leftRootIdxOne, leftRootIdxTwo, minVal, currentValue)
    rightAreSame =areSameBsts(arrayOne, arrayTwo, leftRootIdxOne, leftRootIdxTwo, currentValue, maxVal)

    return leftAreSame and rightAreSame

def getIdxOfFirstSmaller(array, startingIdx, minVal):
    for i in range(startingIdx + 1, len(array)):
        if array[i] < array[startingIdx] and array[i] >=minVal:
            return i
    return -1

def getIdxOfFirstBiggerOrEqual(array, startingIdx, maxVal):
    for i in range(startingIdx + 1, len(array)):
        if array[i] >= array[startingIdx] and array[i] < maxVal:
            return i
    return -1

array_one =[10,15,8,12,94,81,5,2,11]
array_two =[10,8,5,15,2,12,11,94,81]

print(sameBsts1(array_one,array_two))
