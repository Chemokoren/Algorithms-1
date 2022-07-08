"""
Queries for counts of array elements with values in given range

Given an unsorted array of size n, find no of elements between two elements i and j
(both inclusive)

Input :  arr = [1 3 3 9 10 4] 
         i1 = 1, j1 = 4
         i2 = 9, j2 = 12
Output : 4
         2
The numbers are: 1 3 3 4 for first query
The numbers are: 9 10 for second query

A simple approach will be to run a for loop to check if each element is in the given range
and maintain their count. Time complexity for running each query will be O(n).

Time Complexity: O(n),
Auxiliary Space: O(1)

"""
# function to count elements within given range
def countInRange(arr, x, y):

    # Initialize result
    count = 0

    for i in range(len(arr)):
        # check if element is in range
        if(arr[i] >= x and arr[i] <=y):
            count +=1
    return count

print("Expected: 4, actual: ", countInRange([1, 3, 4, 9, 10, 3], 1, 4))
print("Expected: 2, actual: ", countInRange([1, 3, 4, 9, 10, 3], 9, 12))

"""
An Efficient Approach will be to first sort the array and then using a modified binary 
search functionfind two indices, one of first element greater than or equal to lower bound
of range and the other of the last element less than or equal to upperbound.
Time for running each query will be O(logn) and for sorting the array oonce will be 
O(nlogn).

Time Complexity: O(n log n),
Auxiliary Space: O(1)

"""
# function to find first index >= x
def lowerIndex(arr, key):
    l = 0
    h = len(arr)-1
    while(l <= h):
        mid = int((l+h)//2)
        if(arr[mid] >= key):
            h = mid-1
        else:
            l =mid +1
    return l

# function to find last index <= x
def upperIndex(arr, key):
    l = 0
    h = len(arr)-1
    while( l <=h):
        mid = int((l + h) //2)
        if (arr[mid] <= key):
            l = mid +1
        else:
            h = mid-1
    return h

# function to count elements within given range
def countInRange(arr, l, h):
    # Preprocess array
    arr.sort()
    # initialize result
    count = 0
    count = upperIndex(arr,h) - lowerIndex(arr,l) + 1
    return count

print("expected: 4, actual: ", countInRange([1, 3, 4, 9, 10, 3], 1, 4))
print("expected: 2, actual:", countInRange([1, 3, 4, 9, 10, 3], 9, 12))

