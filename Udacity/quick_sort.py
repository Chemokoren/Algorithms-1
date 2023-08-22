"""

Quick Sort 

- not ideal for use with nearly sorted lists - O(n^2)

"""
def quicksort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return quicksort(less)+equal+quicksort(greater)  # Just use the + operator to join lists
    
    else:  # when you only have one element in your array, just return the array.
        return array



arr = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(arr))