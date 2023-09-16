"""
House Robber

You are a professional robber planning to rob houses along a street. Each house has a 
certain amount of money stashed, the only constraint stopping you from robbing each of 
them is that adjacent houses have security system connected and it will automatically
contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, 
determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: nums =[1,2 3, 1]
Output: 4
Explanation: Rob house 1(money =1) ad then rob house 3(money =3)
Total amount you can rob = 1+3 =4
"""
from typing import List
import unittest

class Solution:

    def rob(self, nums: List[int])->int:
        rob1, rob2 =0, 0

        # [rob1, rob2, n, n+1, ...]
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
    
class TestHouseRobber(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.sol = Solution() 

    def test_house_robber(self):
        list_ints =[1, 2, 3, 1]
        self.assertEqual(4, self.sol.rob(list_ints))

if __name__=="__main__":
    unittest.main()