"""
Search, insert and delete in a sorted array

Searching - binary search

Time Complexity of Search Operation: O(log(n))
Auxiliary Space: O(log(n)) due to recursive calls

"""

def binary_search(arr, key):
    return bin_s(arr, 0, len(arr)-1, key)
    

def bin_s(arr, start, end, key):

    while start <= end:
        mid = (start + end)//2

        if arr[mid] < key:
            return bin_s(arr, mid+1, end, key)
        elif arr[mid] > key:
            return bin_s(arr, start, mid-1, key)
        else:
            return mid
        

print("Expected:, Actual:", binary_search([5, 6, 7, 8, 9, 10], 10))
# print("Expected:, Actual:", bin_s([5, 6, 7, 8, 9, 10],0,6, 10))

"""
Insert Operation

In a sorted array, a search operation is performed for the possible position of the given element 
by using Binary Search, and then an insert operation is performed followed by shifting the 
elements. And in an unsorted array, the insert operation is faster as compared to the sorted array 
because we don't have to care about the position at which the element is placed.

Time Complexity of Insert Operation: O(n) [In the worst case all elements may have to be moved] 
Auxiliary Space: O(1)
"""
# inserts a key in arr[] of given capacity. n is current size of arr[]. This function returns
# n+1 if insertion is successful, else n
def insertSorted(arr, key):
    capacity = len(arr)
    n = 6
    # cannot insert more elements if n is already more than or equal to capacity
    if(n >= capacity):
        return n

    i = n-1
    while i >= 0 and arr[i] > key:
        arr[i + 1] = arr[i]
        i -= 1
    arr[i + 1] = key

    return arr[:(n+1)]


arr = [12, 16, 20, 40, 50, 70]

arr.append(0)
     
# Inserting key
print("Expected, Actual:", insertSorted(arr, 26))

"""
Delete Operation
----------------

In the delete operation, the element to be deleted is searched using binary search, and then 
the delete operation is performed followed by shifting the elements.

Time Complexity of Delete Operation: O(n) [In the worst case all elements may have to be moved]
Auxiliary Space: O(log n) (As implicit stack will be used )

"""
def deleteElement(arr, key):
    n =len(arr)
    pos = binary_search(arr,key)
    for i in range(pos, len(arr)-1):
        arr[i] =arr[i+1]
    return arr[:n-1]

print("Expected:[10, 20, 40, 50], Actual: ", deleteElement([10, 20, 30, 40, 50 ], 30))


