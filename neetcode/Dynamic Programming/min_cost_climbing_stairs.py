"""
You are given an integer array cost where cost[i] is the cost of ith step on a staircase.
Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

Example 1:
Input: cost =[10, 15, 20]
Output: 15
Explanation: Cheapest is: start on cost[1], pay that cost and go to the top.

Example 2:
Input: cost =[1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is: start on cost[0], and only step on 1s, skipping cost[3].
"""

from typing import List
import unittest

class Solution:

    # time complexity: O(n) | memory complexity: O(1)
    def min_cost_climbing_stairs(self, cost: List[int])-> int:
        cost.append(0)

        for i in range(len(cost)-3, -1, -1):
            # cost[i] = min(cost[i] + cost[i +1], cost[i]+ cost[i + 2])
            cost[i] += min(cost[i +1], cost[i + 2])

        return min(cost[0], cost[1])
    
    def min_cost(self, cost: List[int]):
        for i in range(2, len(cost)):
            cost[i] += min(cost[i - 1], cost[i - 2])
        return min(cost[-2:])
    
    def min_cost_climbing_stairs_opt(self, cost: List[int]) -> int:
        one = two = 0
        for i in range(2, len(cost) + 1):
            temp = one
            one = min(one + cost[i - 1], two + cost[i - 2])
            two = temp
        return one
    
class TestMinCostClimbingStairs(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.sol =Solution()

    def test_min_cost_climbing_stair_1(self):
        self.assertEqual(15, self.sol.min_cost_climbing_stairs([10, 15, 20]))

    def test_min_cost_climbing_stair_2(self):
        self.assertEqual(6, self.sol.min_cost_climbing_stairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))

    def test_min_cost_1(self):
        self.assertEqual(15, self.sol.min_cost([10, 15, 20]))

    def test_min_cost_2(self):
        self.assertEqual(6, self.sol.min_cost([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))

    def test_min_cost_climbing_stairs_opt_1(self):
        self.assertEqual(15, self.sol.min_cost_climbing_stairs_opt([10, 15, 20]))

    def test_min_cost_climbing_stairs_opt_2(self):
        self.assertEqual(6, self.sol.min_cost_climbing_stairs_opt([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))




if __name__ =="__main__":
    unittest.main()
    
