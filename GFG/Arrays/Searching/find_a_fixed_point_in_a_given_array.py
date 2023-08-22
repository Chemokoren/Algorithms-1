"""
Find a Fixed Point (Value equal to index) in a given array

Given an array of n distinct integers sorted in ascending order, write a function that returns a
Fixed Point in the array, if there is any Fixed Point present in array, else returns -1. Fixed 
Point in an array is an index i such that arr[i] is equal to i. Note that integers in array can 
negative.

Examples:

  Input: arr[] = {-10, -5, 0, 3, 7}
  Output: 3  // arr[3] == 3 

  Input: arr[] = {0, 2, 5, 8, 17}
  Output: 0  // arr[0] == 0 


  Input: arr[] = {-10, -5, 3, 4, 7, 9}
  Output: -1  // No Fixed Point

Method 1: Linear Search

Linearly search for an index i such that arr[i] == i. Return the first such index found.

Time Complexity: O(n) 
Auxiliary Space: O(1)

"""
def linear_search(arr):
    n = len(arr)
    for i in range(n):
        if arr[i] is i:
            return i
    return -1
 
print("Expected:3, Actual: ", linear_search([-10, -1, 0, 3, 10, 11, 30, 50, 100]))



"""

Method 2: Binary Search

First check whether middle element is Fixed Point or not. If it is, then return it; otherwise if
 the index of middle + 1 element is less than or equal to the value at the high index, then Fixed 
 Point(s) might lie on the right side of the middle point (obviously only if there is a 
 Fixed Point). Similarly, check if the index of middle – 1 element is greater than or equal to 
 the value at the low index, then Fixed Point(s) might lie on the left side of the middle point. 

Time Complexity: O(log n)

Auxiliary Space: O(log n) (As implicit stack is used for recursive calls)

"""

# check the fixed point in an array using binary search
def binarySearch(arr, low, high):
    if high >= low :
         
        mid = low + (high - low)//2
        if mid == arr[mid]:
            return mid
        res = -1
        if mid + 1 <= arr[high]:
            res = binarySearch(arr, (mid + 1), high)
        if res !=-1:
            return res
        if mid-1 >= arr[low]:
            return binarySearch(arr, low, (mid -1))

    return -1
 
print("BS Expected:3, Actual: ", binarySearch([-10, -5, 0, 3, 7], 0, len([-10, -5, 0, 3, 7])-1))
print("BS Expected:0, Actual: ", binarySearch([0, 2, 5, 8, 17], 0, len([0, 2, 5, 8, 17])-1))
print("BS Expected:-1, Actual: ", binarySearch([-10, -5, 3, 4, 7, 9],0, len([-10, -5, 3, 4, 7, 9])-1))

'''
my tests
'''
# Time complexity: O(n) | Space complexity: O(1)
def my_tests(arr):

    for i in range(len(arr)):
        if i ==arr[i]:
            return i
    return -1

print("Expected:3, Actual: ", my_tests([-10, -5, 0, 3, 7]))
print("Expected:0, Actual: ", my_tests([0, 2, 5, 8, 17]))
print("Expected:-1, Actual: ", my_tests([-10, -5, 3, 4, 7, 9]))


