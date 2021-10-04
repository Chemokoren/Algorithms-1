# O(n) time | O(1) space
def findThreeLargestNumbers(array):
    three_largest_numbers =[None,None,None]
    for num in array:
        updateLargest(three_largest_numbers,num)
    return three_largest_numbers

def updateLargest(array,num):
    """
    updates the largest value in array

    parameters:
        array: holds the three largest numbers
        num : value to update if its the largest
    Outputs:
        call a helper function shiftAndUpdate to update the largest value
    """
    if array[2] is None or num > array[2]:
        shiftAndUpdate(array,num,2)
    elif array[1] is None or num > array[1]:
        shiftAndUpdate(array,num,1)
    elif array[0] is None or num > array[0]:
        shiftAndUpdate(array,num,0)

def shiftAndUpdate(array,num,idx):
    """
    function to shift and update the largest value in and index

    parameters:
        array: holds the three largest values
        num: value from the original array whose value is being evaluated as one of 
        the three largest
        idx: index of the three largest numbers

    ouput:
        update the index with the largest value
    """
    for i in range(idx+1):
        if i == idx:
            array[i] = num
        else:
            array[i] = array[i+1]


array_vals = [141,1,17,-7,-17,-27,18,541,8,7,7]

print(findThreeLargestNumbers(array_vals))




