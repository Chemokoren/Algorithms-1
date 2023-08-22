# Max Subset Sum No Adjacent- maximum of two numbers in an array without adding two numbers that
# are close (adjacent) to each other

# O(n) time | O(n) space
def maxSubsetSumNoAdjacent(array):
    if not len(array):
        return
    elif len(array) ==1:
        return array[0]
    maxSums =array[:]
    maxSums[1] =max(array[0], array[1])
    for i in range(2,len(array)):
        maxSums[i] =max(maxSums[i - 1], maxSums[i - 2] +array[i])
    return maxSums[-1]

# O(n) time | O(1) space
def maxSubsetSumNoAdjacent1(array):
    if not len(array):
        return
    elif len(array) ==1:
        return array[0]
    second =array[0]
    first =max(array[0],array[1])
    for i in range(2,len(array)):
        current =max(first, second + array[i])
        second =first
        first = current
    return first

my_array =[7,10,12,7,9,14]

print(maxSubsetSumNoAdjacent1(my_array))
