"""
Min Cost Climbing Stairs

You are given an integer array cost where cost[i] is the cost of ith step on a staircase.
Once you pay the cost, yu can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

Example 1:

Input: cost =[10, 15, 20]
Output: 15
Explanation: Cheapest is: start on cost[1], pay that cost, and go to the top.
The position after [20] is the top floor **** that's the trick

Example 2:Explanation

Input: cost =[1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is: start on cost[0], and only step on 1s, skipping cost[3].
"""

class Solution:

    def climbing_stairs(self, cost):
        cost.append(0)
        
        for i in range(len(cost)-3, -1, -1):
            cost[i] =min(cost[i] + cost[i+1], cost[i] + cost[i+2])
        return min(cost[0], cost[1])
        
sol = Solution()
print(sol.climbing_stairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
print(sol.climbing_stairs([10, 15, 20]))

