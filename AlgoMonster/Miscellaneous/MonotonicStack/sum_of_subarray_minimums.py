"""
Sum of Subarray Minimums

Given an array of integers arr, find the sum of min(b), where b ranges over every(contiguos) subarray
of arr.

Input

    weights: an array of integers

Output

the sum of subarray minimums
Examples
Example 1:

Input:

weights = [1, 3, 2]

Output: 10

Explanation:

Subarray    Min Weight
1,3,2       1
1,3,2       3
1,3,2       2
1,3,2       1
1,3,2       2
1,3,2       1

The sum of subarray minimums is 1+3+2+1+2+1=10.
"""