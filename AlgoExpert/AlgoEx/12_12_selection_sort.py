
"""
Selection sort
"""

def selectionSort(array):
    """
    selection sort - maintain two lists, one sorted and another unsorted, loop through the 
    entire list, pick the smallest value and add to the sorted list & continuously do this
    until the entire list is sorted

    parameters:
        array:  accepts an array as the input

    Output:
        array: returns a sorted array as the output
    """
    currentIdx = 0
    while currentIdx < len(array)-1:
        smallestIdx = currentIdx
        for i in range(currentIdx+1,len(array)):
            if array[i] < array[smallestIdx]:
                smallestIdx = i
        swap(currentIdx, smallestIdx, array)
        currentIdx +=1
    return array

def swap(i, j, array):
    array[i],array[j] = array[j], array[i]


my_array =[8,5,2,9,5,6,3]

print("selection sort:", selectionSort(my_array))

