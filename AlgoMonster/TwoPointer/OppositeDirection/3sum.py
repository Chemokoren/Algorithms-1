"""
3Sum

Given a list of integers, return a list containing all unique triplets in the list such that the
sum of the triplet is zero. Each triplet must be sorted in ascending order, and the resulting 
list must be sorted lexicographically.

Parameter

    nums: a list of integers

Result

    A list of triplets containing all unique triplets that sums up to zero, sorted.

Examples
Example 1

Input: nums = [-1, 0, 1, 2, -1, -4]

Output: [[-1, -1, 2], [-1, 0, 1]]
Example 2

Input: nums = [1, -1, 2, -2, 3, -3, 4, -4]

Output: [[-4, 1, 3], [-3, -1, 4], [-3, 1, 2], [-2, -1, 3]]

"""

from typing import List

def triplets_with_sum_0(nums: List[int]) -> List[List[int]]:
    # WRITE YOUR BRILLIANT CODE HERE
    return []

if __name__ == '__main__':
    nums = [int(x) for x in input().split()]
    res = triplets_with_sum_0(nums)
    for row in res:
        print(' '.join(map(str, row)))