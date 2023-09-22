"""
Combination Sum IV

Given an array of distinct integers nums and a target integer target, return the number of
possible combinations that add up to the target.

The answer is guaranteed to fit in a 32-bit integer.

Example 1:

Input: nums =[1,2,3], target = 4
Output: 7
Explanation:
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

"""
from typing import List
import unittest

class Solution:

    def combination_sum_4(self, nums: List[int], target: int)-> int:

        dp ={0: 1}

        for total in range(1, target + 1):
            dp[total] = 0
            for n in nums:
                dp[total] +=dp.get(total -n, 0)
        return dp[target]
    
class TestCombinationSumIV(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.sol = Solution()

    def test_combination_sum_iv(self):
        self.assertEqual(7, self.sol.combination_sum_4([1,2,3], 4))

if __name__=="__main__":
    unittest.main()
