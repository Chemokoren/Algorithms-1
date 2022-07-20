"""
Find the smallest positive integer value that cannot be represented as sum of any subset
of a given array

Given an array of positive numbers, find the smallest positive integer value that cannot
be represented as the sum of elements of any subset of a given set. The expected time
complexity is O(nlogn).

Examples: 

Input:  arr[] = {1, 10, 3, 11, 6, 15};
Output: 2

Input:  arr[] = {1, 1, 1, 1};
Output: 5

Input:  arr[] = {1, 1, 3, 4};
Output: 10

Input:  arr[] = {1, 2, 5, 10, 20, 40};
Output: 4

Input:  arr[] = {1, 2, 3, 4, 5, 6};
Output: 22

A simple solution is to start from value 1 and check all values one by one if they can sum
to values in the given array. This solution is very inefficient as it reduces to the subset 
sum problem which is a well-known NP-Complete Problem.

Using a simple loop, we can solve this problem in O(N log N) time. Let the input array
be arr[0..n-1]. We first sort the array in non-decreasing order. Let the smallest element 
that cannot be represented by elements at indexes from 0 to (i-1) be 'res'. We initialize
'res' as 1(smallest possible answer) and traverse the given array from i=0. There are
the following two possibilities when we consider element at index i:

1. We decide that 'res' is the final result. If arr[i] is greater than 'res', then we found 
the gap which is 'res' because the elements after arr[i] are also going to be greater than
'res'.
2. The value of 'res' is incremented after considering arr[i]: If arr[i] is not greater 
than 'res', the value of 'res' is incremented by arr[i] so 'res'='res'+arr[i](why? if 
elements from 0 to (i-1)) can represent 1 to 'res-1', then elements from 0 to i can 
represent from 1 to 'res + arr[i]-1' by adding arr[i] to all subsets that represent 1
to 'res-1' which we have already determined to be represented

The Time Complexity is O(nlogn). 

The Space Complexity is O(1) in best case for heap sort.  

"""

# Program to find the smallest positive value that cannot be reprsented as sum of 
# subsets of a given sorted array

# Returns the smallest number that cannot be represented as sum of subset of elements
# from set represented by sorted array arr[0..n-1]
def findSmallest(arr):

    n = len(arr)

    res = 1 # Initialize result

    # Traverse the array and increment 'res' if arr[i] is smaller than or equal to
    # 'res'
    for i in range(0, n):
        if arr[i]  <= res:
            res = res + arr[i]
        else:
            break
    return res

print("Expected:2, Actual",findSmallest([1, 3, 4, 5]))
print("Expected:4, Actual",findSmallest([1, 2, 6, 10, 11, 15]))
print("Expected:5, Actual",findSmallest([1, 1, 1, 1]))
print("Expected:10, Actual",findSmallest([1, 1, 3, 4]))
