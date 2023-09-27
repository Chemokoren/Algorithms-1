"""
Maximum Alternating Subsequence Sum

The alternating sum of a 0-indexed array is defined as the sum of elements at  even indices
minus the sum of the elements at odd indices.

- For example, the alternating sum of [4, 2, 5,3 ] is (4 + 5) -(2 + 3) = 4.

Given an array nums, return the maximum alternating sum of any subsequence of nums(after)
reindexing the elements of the subsequence).

A subsequence of an array is a new array generated from the original array by deleting some
elements(possibly none) without changing the remaining element's relative order. For example,
[2, 7, 4] is a subsequence of [4,2,3,7,2,1,4] (the underlined elements), while [2, 4, 2] is
not.

Example 1:

Input: nums =[4, 2, 5, 3]
Output: 7
Explanation: It is optimal to choose the subsequence [4, 2, 5] with alternating sum
(4 + 5) - 2 =7


**** first check:: Longest Increasing Subsequence
"""
from typing import List
import unittest

class Solution:

    # time complexity: O(n) | space complexity: O(n)
    def max_alternating_sum(self, nums: List[int])-> int:

        dp ={}
        # i = index, even = true/false

        def dfs(i, even):

            if i == len(nums):
                return 0
            if (i, even) in dp:
                return dp[(i, even)]
            
            total = nums[i]  if even else (-1 * nums[i])
            dp[(i, even)] = max(total + dfs(i + 1, not even), dfs(i + 1, even))
            return dp[(i, even)]
        return dfs(0, True)
    
    # time complexity: O(n) | space complexity: O(1)
    def max_alternating_sum_dp(self, nums: List[int])-> int:
        sumEven, sumOdd = 0, 0

        for i in range(len(nums) -1, -1, -1):
            tmpEven =max(sumOdd + nums[i], sumEven)
            tmpOdd = max(sumEven - nums[i], sumOdd)
            sumEven, sumOdd = tmpEven, tmpOdd
        return sumEven
    
class TestMaximumAlternatingSubsequenceSum(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.sol =Solution()

    def test_maximum_alternating_subsequence_sum(self):
        self.assertEqual(7, self.sol.max_alternating_sum([4, 2, 5, 3]))

    def test_maximum_alternating_subsequence_sum_dp(self):
        self.assertEqual(7, self.sol.max_alternating_sum([4, 2, 5, 3]))

if __name__=="__main__":
    unittest.main()
