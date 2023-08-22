"""
Rearrange positie & negative numbers with constant extra space

Given an array of positive and negative numbers, arrange them such that all 
negative integers appear before all the positive integers in the array without 
using any additional data structure like hash table, arrays, etc. 
The order of appearance should be maintained.

Examples:  

Input:  [12 11 -13 -5 6 -7 5 -3 -6]
Output: [-13 -5 -7 -3 -6 12 11 6 5]

A simple solution is to use another array. We copy all elements of original array to 
new array. We then traverse the new array and copy all negative and positive elements 
back in original array one by one. The problem with this approach is that it uses 
auxiliary array and we’reThe similar partition process is discussed here . not allowed to use any data structure to solve this problem.
One approach that does not use any data structure is to use use partition process of
QuickSort. The idea is to consider 0 as pivot and divide the array around it. 
The problem with this approach is that it changes relative order of elements. 

Approach 1: Modified Insertion Sort
We can modify insertion sort to solve this problem.
Algorithm –  

Loop from i = 1 to n - 1.
  a) If the current element is positive, do nothing.
  b) If the current element arr[i] is negative, we 
     insert it into sequence arr[0..i-1] such that 
     all positive elements in arr[0..i-1] are shifted 
     one position to their right and arr[i] is inserted
     at index of first positive element.

Time complexity of above solution is O(n2) and auxiliary space is O(1). 
We have maintained the order of appearance and have not used any other data structure.

"""

# program to rearrange positive and negative numbers in array

def printArray(arr, n):
    for i in range(n):
        print(arr[i], end=" ")
    print()

# Function to Rearrange positive and negative numbers in a array
def RearrangePosNeg(arr, n):
    for i in range(1,n):
        key = arr[i]

        # if current element is positive do nothing 
        if(key > 0):
            continue
        '''
        if current element is negative, shift psitive elemts of arr[0 ..i-1], to one 
        position to their right
        '''
        j = i - 1
        while(j >= 0 and arr[j] > 0):
            arr[j+1] = arr[j]
            j =j -1

        # put negative element at its right position
        arr[j + 1] = key

if __name__ == "__main__":
    arr = [ -12, 11, -13, -5, 6, -7, 5, -3, -6 ]
    n = len(arr)
 
    RearrangePosNeg(arr, n)
    printArray(arr, n)

print("\n Approach 2: Optimized Merge Sort: \n")
"""
Approach 2: Optimized Merge Sort 
Merge method of standard merge sort algorithm can be modified to solve this problem.
While merging two sorted halves say left and right, we need to merge in such a way 
that negative part of left and right sub-array is copied first followed by positive 
part of left and right sub-array.

The time complexity of above solution is O(n log n). The problem with this approach is
we are using auxiliary array for merging but we’re not allowed to use any data structure
to solve this problem. We can do merging in-place without using any data-structure.

"""

# program to rearrange positive and negative numbers in a array
def printArray(A, size):
    for i in range(size):
        print(A[i], end=" ")
    print()


# Merges two subarrays of arr[]
# First subarray is arr[l..m] & second subarray is arr[m+1..r]
def merge(arr, l, m, r):
    i, j, k= 0, 0, 0
    n1 = m - l + 1
    n2 = r -m

    # create temp arrays
    L = [arr[l + i] for i in range(n1)]
    R = [arr[m+1+j] for j in range(n2)]

    # Merge the temp arrays back into arr[l..r]
    i =0 # Initial index of first subarray
    j =0 # Initial index of second subarray
    k =l # Initial index of merged subarray

    # Note the order of appearance of elements should be maintained  - we copy elements
    # of left subarray first followed by that of right subarray
    
    # copy  negative element of left subarray
    while( i< n1 and L[i] < 0):
        arr[k] =L[i]
        k += 1
        i += 1

    # copy negative elements of right subarray
    while(j < n2 and R[j] < 0):
        arr[k] =R[j]
        k += 1
        j += 1

    # copy positive elements of left subarray
    while(i < n1):
        arr[k] = L[i]
        k += 1
        i += 1
    
    # copy positive elements of right subarray
    while( j < n2):
        arr[k] = R[j]
        k += 1
        j += 1

# function to rearrange positive and negative numbers in a array
def RearrangePosNeg(arr, l, r):
    if(l < r):
        # same as (l + r)/2, but avoids overflow for large l and h
        m = l + (r - l) // 2

        # Sort first and second halves
        RearrangePosNeg(arr, l, m)
        RearrangePosNeg(arr, m+1, r)

        merge(arr, l, m, r)

arr = [ -12, 11, -13, -5, 6, -7, 5, -3, -6 ]
arr_size = len(arr)
 
RearrangePosNeg(arr, 0, arr_size - 1)
 
printArray(arr, arr_size)


"""
Let Ln and Lp denotes the negative part and positive part of left sub-array respectively.
Similarly, Rn and Rp denote the negative and positive part of right sub-array respectively. 

Below are the steps to convert [Ln Lp Rn Rp] to [Ln Rn Lp Rp] without using extra space. 

1. Reverse Lp and Rn. We get [Lp] -> [Lp'] and [Rn] -> [Rn'] 
    [Ln Lp Rn Rp] -> [Ln Lp’ Rn’ Rp]

2. Reverse [Lp’ Rn’]. We get [Rn Lp].
    [Ln Lp’ Rn’ Rp] -> [Ln Rn Lp Rp]


The time complexity of above solution is O(n log n), O(Log n) space for recursive calls,
and no additional data structure.

"""

# program to rearrange positive and negative numbers in an array

def printArray(A, size):
    for i in range(size):
        print(A[i], end=" ")
    print()

# function to reverse an array. An array can be reversed in O(n) time and O(1) space
def reverse(arr, l, r):
    if l < r:
        arr[l],arr[r] = arr[r], arr[l]
        l, r = l + 1, r - 1
        reverse(arr, l, r)

# Merges two subarrays of arr[]. First subarray is arr[l..m] & second subarray is arr[m+1..r]
def merge(arr, l, m, r):
    i = l # initial index of 1st subarray
    j = m + 1 # initial index of 2nd subarray

    while i <= m and arr[i] < 0:
        i += 1

    # arr[i..m] is positive

    while j<= r and arr[j] < 0:
        j+= 1

    # arr[j..r] is positive

    # reverse positive part of left sub-array (arr[i..m])
    reverse(arr, i, m)

    # reverse negative part of right sub-array (arr[m + 1..j-1])
    reverse(arr, m+1, j-1)

    # reverse arr[i..j-1]
    reverse(arr, i, j -1)

# Function to rearrange positive and negative numbers in a array
def RearrangePosNeg(arr, l, r):
    if l < r:
        # same as (l + r)/2 but avoids overflow for large l and h
        m = l+ (r -l) //2

        # sort first and second halves
        RearrangePosNeg(arr, l, m)
        RearrangePosNeg(arr, m + 1, r)

        merge(arr, l, m, r)

if __name__ == "__main__":
 
    arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
    arr_size = len(arr)
 
    RearrangePosNeg(arr, 0, arr_size - 1)
 
    printArray(arr, arr_size)

print("\n Approach 4: Using Two Pointer Algorith: \n")

"""
Approach 4: Using Two Pointer Algorithm


"""

def RearrangePosNeg(arr, n):
    i = 0 
    j = n-1

    while(True):
        # Loop until arr[i] < 0 and still inside the array 
        while( i < n and arr[i] < 0):
            i += 1

        # Loop until arr[j] > 0 and still inside the array
        while(j >=0 and arr[j] > 0):
            j -= 1

        # if i is less than j
        if( i < j):
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break

arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
n = len(arr)
RearrangePosNeg(arr, n)
print(*arr)

