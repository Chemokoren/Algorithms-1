"""
Find all elements in array which have at-least two greater elements

Given an array of n distinct elements, the task is to find all elements in array which have at-least two greater elements than themselves.

Examples : 

Input : arr[] = {2, 8, 7, 1, 5};
Output : 2  1  5  
Explanation:
The output three elements have two or more greater elements

Explanation:
Input  : arr[] = {7, -2, 3, 4, 9, -1};
Output : -2  3  4 -1  

Method 1: Simple
The naive approach is to run two loops and check one by one element of array check that array
elements have at-least two elements greater than itself or not. If it's true then print 
array element.


Time Complexity: O(n2)

"""
def findElements(arr, n):
    # pick elements one by one and counter greater elements. If count is more than 2,
    # print that element.
    for i in range(n):
        count = 0
        for j in range(0, n):
            if arr[j] > arr[i]:
                count = count + 1

        if count >= 2:
            print(arr[i], end=" ")

arr = [ 2, -6 ,3 , 5, 1]
n = len(arr)
findElements(arr, n)

print("\n Method 2: Use Sorting :\n")
"""
We sort the array first in increasing order, then we print first n-2 elements where n is size
of array.

Time Complexity: O(n Log n)

"""

def findElements(arr, n):
    arr.sort()

    for i in range(0, n-2):
        print(arr[i], end=" ")

    
arr = [2, -6, 3, 5, 1]
n = len(arr)
findElements(arr, n)


print("\n Method 3: Efficient \n")
"""
Method 3 (Efficient) 

In the second method we simply calculate the second maximum element of the array
and print all element which is less than or equal to the second maximum. 

Time Complexity: O(n)

"""

import sys

def findElements(arr, n):

    first = -sys.maxsize
    second = -sys.maxsize

    for i in range(0, n):
        
        # If current element is smaller than first then update both first and second
        if(arr[i] > first):
            second = first
            first = arr[i]

        # If arr[i] is in between first and second then update second
        elif (arr[i] > second):
            second = arr[i]

    for i in range(0, n):
        if(arr[i] < second):
            print(arr[i], end=" ")

arr = [2, -6, 3, 5, 1]
n = len(arr)
findElements(arr, n)
