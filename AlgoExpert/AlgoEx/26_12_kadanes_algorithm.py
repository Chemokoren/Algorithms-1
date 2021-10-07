
def kadanesAlgorithm(array):
    maxSofar = array[0]
    maxEndingHere = array[0]

    for i in range(1,len(array)):
        maxEndingHere =max(array[i],maxEndingHere+array[i])
        maxSofar =max(maxSofar,maxEndingHere)
    return maxSofar



my_array = [3, 5, -9, 1,3,-2,3,4,7,2,-9,6,3,1,-5,4]

print(kadanesAlgorithm(my_array))