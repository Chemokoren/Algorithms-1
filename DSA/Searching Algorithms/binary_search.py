"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search_iterative(input_array, value):
    """ Binary Search"""
    low = 0
    high = len(input_array) - 1
    while (low <= high):
        mid = (low + high) // 2
        if (input_array[mid] == value):
            return mid
        elif (input_array[mid] < value):
            low = mid + 1
        else:
            high = mid - 1
    return -1

print("Iterative:: ", binary_search_iterative([1,3,9,11,15,19,29], 15))

def binary_search_recursive(A, key, low, high):
    if low > high:
        return False
    else:
        mid = (low + high ) // 2
        if key == A[mid]:
            return True
        elif key < A[mid]:
            return binary_search_recursive(A, key,low,mid-1)
        else:
            return binary_search_recursive(A, key,mid+1,high)

A = [15, 21, 47,84,96]
low =0
high =len(A) -1
found =binary_search_recursive(A ,84, low,high)
print("recursive:: The element recursively 46: ",found)
