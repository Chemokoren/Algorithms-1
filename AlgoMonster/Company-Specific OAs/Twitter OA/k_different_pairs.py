"""
(OA) - K-different Pairs in an Array

Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the 
array. A k-diff pair is an integer pair (nums[i], nums[j]), where both of the following are true:

    0 <= i < j < nums.length
    |nums[i] - nums[j]| == k

Note: |x| is the absolute value of x.

Examples

Example 1:

Input: nums = [3,1,4,1,5], k = 2

Output: 2

"""
from typing import List

def k_difference(nums: List[int], k: int) -> int:
    return 0

if __name__ == '__main__':
    nums = [int(x) for x in input().split()]
    k = int(input())
    res = k_difference(nums, k)
    print(res)