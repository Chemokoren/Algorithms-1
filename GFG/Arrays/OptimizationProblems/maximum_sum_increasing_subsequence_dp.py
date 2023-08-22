"""

Maximum sum Increasing subsequence - DP

Given an array of n positive integers. Write a program to find the sum of maximum sum 
subsequence of the given array such that the integers in the subsequence are sorted in 
increasing order. For example, if input is {1, 101, 2,3, 100, 4,5}, then output should be
106(1+2+3+100), if the input array is{3,4,5,10}, then output should be 22(3+4+5+10) and 
if the input is {10,5,4,3}, then output should be 10.

Solution
- This problem is a variation of the standard Longest Increasing Subsequence(LIS) 
problem. We need a slight change in the Dynamic Programming Solution of LIS problem.
All we need to change is to use sum as a criteria instead of a length of increasing
subsequence.

Time Complexity: O(n^2) 
Space Complexity O(n) 

"""

# implementation of Maximum Sum Increasing subsequence(MSIS) problem
# maxSumIS() returns the maximum sum of increasing subsequence in arr[] of size n
def maxSumIS(arr):
    n = len(arr)
    max= 0 
    # msis =[0 for x in range(n)]
    # Initialize msis values for all indexes
    # for i in range(n):
    #     msis[i] = arr[i]

    msis =arr.copy()


    # Compute maximum sum values in bottom up manner
    for i in range(1, n):
        for j in range(i):
            if(arr[i] > arr[j] and msis[i] < msis[j]+arr[i]):
                msis[i] = msis[j]+arr[i]

    # pick maximum of all msis values
    for i in range(n):
        if max < msis[i]:
            max = msis[i]
    return max

arr = [1, 101, 2, 3, 100, 4, 5]

print("expected:, actual:", str(maxSumIS(arr)))
