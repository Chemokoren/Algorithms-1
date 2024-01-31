"""
Paint House

There is a row of n houses, where each house can be painted one of three colors: red, blue
or green. The cost of painting each house with a certain color is different. You have to
paint all the houses such that no two adjacent houses have the same color.

The costs of painting each house with a certain color is represented by an n * 3 cost
matrix costs.

- For example, costs[0][0] is the cost of painting house 0 with color red; costs[1][2] is
the cost of painting house 1 with color green, and so on ...

Return the minimum cost to paint all houses.

Example 1:

Input: costs =[[17, 2, 17], [16, 16, 5], [14, 3, 19]]
Output: 10
Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue.
Minimum cost: 2 + 5 + 3 = 10
"""
from typing import List
import unittest

class Solution:

    def min_cost(self, costs: List[List[int]])->int:

        # costs[i][j] i is house, j is color
        dp =[0, 0, 0]

        for i in range(len(costs)):
            dp0 = costs[i][0] + min(dp[1], dp[2])
            dp1 = costs[i][1] + min(dp[0], dp[2])
            dp2 = costs[i][2] + min(dp[0], dp[1])
            dp =[dp0, dp1, dp2]
        return min(dp)
    
class TestPainHouse(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.sol = Solution()

    def test_paint_house(self):
        self.assertEqual(10, self.sol.min_cost([[17, 2, 17], [16, 16, 5], [14, 3, 19]]))
         
if __name__=="__main__":
    unittest.main()