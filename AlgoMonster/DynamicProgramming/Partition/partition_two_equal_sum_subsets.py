"""
Partiti
on to Two Equal Sum Subsets
Input

    nums: the array

Output

if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal
Examples
Example 1:

Input:

nums = [3, 4, 7]

Output: true

Explanation:

The array can be partitioned as [3,4] and [7].
Example 2:

Input:

nums = [1, 5, 11, 5]

Output: true

Explanation:

The array can be partitioned as [1, 5, 5] and [11].

"""

from typing import List

def can_partition(nums: List[int]) -> bool:
    return False

if __name__ == '__main__':
    nums = [int(x) for x in input().split()]
    res = can_partition(nums)
    print('true' if res else 'false')