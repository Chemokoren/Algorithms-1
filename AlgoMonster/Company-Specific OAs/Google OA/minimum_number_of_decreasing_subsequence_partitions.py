"""
(OA) - Minimum Number of Decreasing Subsequence Partitions

Given an integer array, split it into strictly decreasing subarrays. Return the minimum number of 
decreasing subarrays you can get from splitting the array.

Examples
Example 1:
Input:

[5, 2, 4, 3, 1, 7]
Output: 3
Explanation:

The array can be split into [5, 2, 1], [4, 3], [7] to get 3 decreasing subarrays. Or it can be split 
into [5, 4, 3], [2, 1], [7] to also get 3 decreasing subarrays.

The partition of [5, 4, 3, 2, 1], [7] is not valid because [5, 4, 3, 2, 1] is not a subarray of the 
original array.

Example 2:
Input:

[2, 9, 13, 14, 4, 8, 7, 6, 10]
Output: 4
Explanation:

[2], [9, 4], [13, 10], [14, 8, 7, 6]
Example 3:
Input:

[6, 6, 6]
Output: 3
Explanation:

[6], [6], [6]
"""

from typing import List

def min_decreasing_partitions(arr: List[int]) -> int:
    return 0

if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    res = min_decreasing_partitions(arr)
    print(res)