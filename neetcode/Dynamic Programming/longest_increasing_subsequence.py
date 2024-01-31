"""
Given an integer array nums, return the length of the longest strictly increasing 
subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no 
elements without changing the order of the remaining elements. For example, [3, 6, 2, 7]
is a subsequence of the array [0, 3, 1, 6, 2, 2, 7]

Example 1:

Input: nums =[10, 9, 2, 5, 3, 7, 101, 18]
Explanation: The longest increasing subsequence is [2,3,7,101], thererfore the length is 4.

Example 2:

Input: nums =[0, 1, 0, 3, 2, 3]
Output: 4
"""
from typing import List
import unittest
class Solution:

    # O(n^2)
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS =[1] * len(nums)

        for i in range(len(nums)-1, -1, -1):

            for j in range(i +1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)
    # O(nlogn)

class TestLongestIncreasingSubsequence(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.sol = Solution()

    def test_longest_increasing_subsequence(self):
        self.assertEqual(4, self.sol.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))


if __name__=="__main__":
    unittest.main()