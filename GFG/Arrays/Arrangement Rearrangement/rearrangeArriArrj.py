"""
Rerrange array such that arr[i] >=arr[j] if i is even and arr[i]<=arr[j]
if i is odd and j<i

Given an array of n elements - write a program to rearrange the array such that the elements at
even positions are greater than all elements before it and elements at odd positions
are less than all elements before it.

Input : arr[] = {1, 2, 3, 4, 5, 6, 7}
Output : 4 5 3 6 2 7 1

Input : arr[] = {1, 2, 1, 4, 5, 6, 8, 8} 
Output : 4 5 2 6 1 8 1 8

The idea to solve this problem is to first create an auxiliary copy of the original array
and sort the copied array. Now total number of even position in array with n elements 
will be floor(n/2) and remaining number is the number of odd positions.
Now fill the odd and even positions in the original array using the sorted array as below:

1) Total odd positions will be n-floor(n/2). Start from(n-floor(n/2))th position in 
the sorted array and copy the element to 1st position of sorted array. Start traversing
the sorted array from this position towards left and keep filling the odd positions in
the original array towards the right.
2) Start traversing the sorted array starting from(n-floor(n/2)+1)th position towards right
and keep filling the original array starting from 2nd position.

Time Complexity: O( n logn ) 
Auxiliary Space: O(n)

"""

# code to rearrange the array as per the given condition
import array as a
import numpy as np

# function to rearrange the array
def rearrangeArr(arr,n):

    # total even positions
    evenPos =int(n/2)

    # total odd positions
    oddPos =n -evenPos

    # initializing empty array in Python
    tempArr =np.empty(n, dtype=object)

    # copy original array in an auxiliary array
    for i in range(0, n):
        tempArr[i] =arr[i]

    # sort the auxiliary array
    tempArr.sort()

    j =oddPos - 1

    # fill up odd position in original array
    for i in range(0, n, 2):
        arr[i] = tempArr[j]
        j =j-1

    j = oddPos

    # fill up even positions in original array
    for i in range(1, n, 2):
        arr[i] = tempArr[j]
        j = j + 1
    
    # display array
    for i in range(0, n):
        print(arr[i], end=' ')

arr = a.array('i', [ 1, 2, 3, 4, 5, 6, 7 ])
rearrangeArr(arr, 7)




