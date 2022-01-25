"""
solves the maximum subarray problem
"""
# O(n) time where n is the size of input array | O(1) space
def kadanesAlgorithm(array):
    maxSofar = array[0]
    maxEndingHere = array[0]

    # for i in range(1,len(array)):
    #     maxEndingHere =max(array[i],maxEndingHere+array[i])
    #     maxSofar =max(maxSofar,maxEndingHere)

    for num in array[1:]:
        maxEndingHere =max(num,maxEndingHere+ num)
        maxSofar =max(maxSofar,maxEndingHere)

    return maxSofar



my_array = [3, 5, -9, 1,3,-2,3,4,7,2,-9,6,3,1,-5,4]

print("solves maximum subarray problem: ", kadanesAlgorithm(my_array))