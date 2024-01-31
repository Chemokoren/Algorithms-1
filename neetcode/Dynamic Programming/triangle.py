"""
Triangle

Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number on the row below.

Example 1:

Input: triangle =[[2],[3, 4], [6, 5, 7], [4, 1, 8, 3]]
Output: 11
Explanation: The minimum path sum from top to bottom is 11(i.e., 2 + 3 + 5 + 1 ==11)

Example 2:

Input: triangle =[[-10]]
Output: -10

"""
from typing import List
import unittest

class Solution:

    def test_triangle(self, nums: List[List[int]])-> int:
        res =0
        for i in range(len(nums)):
            res +=min(nums[i])
        return res
    
    # time complexity: O(n^2) | space complexity: O(n)
    def minimum_total(self, triangle: List[List[int]])->int:
        dp =[0] * (len(triangle) + 1)

        for row in triangle[::-1]:
            for i, n in enumerate(row):
                dp[i] = n + min(dp[i], dp[i+1])

        return dp[0]



class TestTriangle(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.sol = Solution()

    def test_triangle(self):
        self.assertEqual(11, self.sol.minimum_total([[2],[3, 4], [6, 5, 7], [4, 1, 8, 3]]))

    def test_negative_triangle(self):
        self.assertEqual(-10, self.sol.minimum_total([[-10]]))

if __name__=="__main__":
    unittest.main()
