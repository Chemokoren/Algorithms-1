"""
Burst Balloons

You are given n balloons, indexed from 0 to n-1. Each balloon is  painted with a number on
it represented by an array nums. You are asked to burst all the balloons.

If you burst the ith balloon, you will get nums[i-1] * nums[i] * nums[i+1] coins. If i - 1
or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1
painted on it.

Return the maximum coins you can collect by bursting the balloons wisely.

Example 1:

Input: nums =[3, 1, 5, 8]
Output: 167
Explanation:
nums =[3, 1, 5, 8] --> [3, 5, 8] -->[3, 8]-->[8] -->[]
coins =3*1*5 + 3*5*8 + 1*3*8 + 1*8*1 = 167
"""
from typing import List
import unittest

class Solution:

    def max_coins(self, nums: List[int])-> int:
        nums =[1] + nums + [1]
        dp = {}

        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]
            dp[(l, r)] = 0

            for i in range(l, r + 1):
                coins =nums[l -1] * nums[i] * nums[r + 1]
                coins += dfs(l, i-1) + dfs(i + 1, r)
                dp[(l, r)] = max(dp[(l, r)], coins)
            return dp[(l, r)]
        return dfs(1, len(nums) -2)
    
class TestBurstBalloons(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.sol = Solution()

    def test_burst_balloons(self):
        self.assertEqual(167, self.sol.max_coins([3, 1, 5, 8]))

if __name__=="__main__":
    unittest.main()