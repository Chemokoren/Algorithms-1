"""
(OA) - Largest Subarray

An array A is greater than an array B if the first non-matching item in both arrays has a greater 
value in A than in B. For example,

    A = [3, 4, 9, 6, 8]
    B = [3, 4, 8, 6, 7]

A is bigger than B because the first non-matching element is larger in A (A[2] > B[2]).

A contiguous subarray is a subarray that has consecutive indexes.

Given an array arr consisting of n integers and an integer k, return the largest contiguous subarray 
of length k from all the possible contiguous subarrays of length k.

Constraints

    1 <= k <= n <= 100
    1 <= arr[i] <= 1000

Examples
Example 1:
Input:

arr = [1, 4, 3, 2, 5]

k = 4
Output: [4, 3, 2, 5]
Explanation:

There are 2 possible subarrays of size 4: [1, 4, 3, 2] and [4, 3, 2, 5], and the largest subarray is
[4, 3, 2, 5].

"""