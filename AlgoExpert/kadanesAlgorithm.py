# O(n) time | O(1) space

def kadanesAlgorithm(array):
    maxEndingHere =array[0]
    maxSoFar =array[0]
    for num in array[1:]:
        maxEndingHere =max(num,maxEndingHere + num)
        maxSoFar =max(maxSoFar, maxEndingHere)
    return maxSoFar

my_array=[3,5,-9,1,3,-2,3,4,7,2,-9,6,3,1,-5,4]

print(kadanesAlgorithm(my_array))
