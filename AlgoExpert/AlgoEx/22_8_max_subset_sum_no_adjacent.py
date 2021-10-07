"""
Max Subset Sum No Adjacent

[7,10,12,7,9,14]
"""
# O(n) time | O(n) space
def maxSubsetSumNoAdjacent(array):
    if not len(array):
        return
    if len(array) == 1:
        return array[0]

    maxSums =array[:]
    maxSums[0] =array[0]
    maxSums[1] =max(array[0], array[1])
    for i in range(2,len(array)):
        maxSums[i] = max(maxSums[i-1],maxSums[i-2]+array[i])
    return maxSums[-1]

# Bottom-up approach DP
# O(n) time | O(1) space
def maxSubsetSumNoAdjacentDP(array):
    if not len(array):
        return
    elif len(array) == 1:
        return array[0]

    second =array[0]
    first = max(array[0],array[1])
    for i in range(2,len(array)):
        current_val = max(first,second+array[i])
        second = first
        first = current_val
    return first


my_array = [7,10,12,7,9,14,16,17, 19, 20, 23, 25, 28, 29, 33, 37, 39, 40, 41, 43, 45,
 48, 49,51,53,54,57,63,64,67,69,73,79,80,82,83,85,88,89,91,93,95,97,100,
 107,110,112,117,119,114,116,127, 139, 120, 123, 225, 328, 229, 133, 337, 139, 240, 141, 443,
  145,348, 449,251,553,654,257,163,264,567,369,673,279,180,482,683,385,288,489,691,793,395,
  897,310]
# my_array = [7,10,12,7,9,14]
print(maxSubsetSumNoAdjacentDP(my_array))
