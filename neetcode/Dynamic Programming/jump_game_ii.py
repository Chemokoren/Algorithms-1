"""
Jump Game II

Given an array of non-negative integers nums, you are initially positioned at the first 
index of the array.
Each element in the array represents your maximum jump at that position.
Your goal is to reach the last index in the minimum number of jumps.
You can assume that you can always reach the last index.

Example 1:

Input: nums =[2, 3, 1, 1, 4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from 
index 0 to 1, then 3 steps to the last index.
"""
from typing import List
import unittest
class Solution:

    def jump(self, nums: List[int])->int:
        res = 0
        l = r = 0

        while r < len(nums)-1:
            farthest = 0
            for i in range(l, r + 1):
                farthest =max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res +=1
        return res
    
class JumpGameII(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.sol = Solution()

    def test_jump_game_ii(self):
        self.assertEqual(2, self.sol.jump([2, 3, 1, 1, 4]))

if __name__=="__main__":
    unittest.main()
