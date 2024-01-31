"""
Jump Game

Given an array of non-negative integers nums, you are initially positioned at the first
index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: nums =[2, 3, 1, 1, 4]
Output: True
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
"""
from typing import List
import unittest

class Solution:
    
    def can_jump(self, nums: List[int])-> bool:
        goal = len(nums) -1

        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return True if goal == 0 else False
    
class TestGame(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.sol = Solution()

    def test_jump_game_true(self):
        self.assertEqual(True, self.sol.can_jump([2, 3, 1, 1, 4]))

    def test_jump_game_false(self):
        self.assertEqual(False, self.sol.can_jump([3, 2, 1, 0, 4]))

if __name__=="__main__":
    unittest.main()
