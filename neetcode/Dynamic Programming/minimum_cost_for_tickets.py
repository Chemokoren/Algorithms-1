"""
Minimum Cost for Tickets

You have planned some train traveling one year in advance. The days of the year in which
you travel are given as an integer array days. Each day is an integer from 1 to 365.

Train tickets are sold in three different ways:
- a 1-day pass is sold for costs[0] dollars,
- a 7-day pass is sold for costs[1] dollars, and
- a 30-day pass is sold for costs[2] dollars.

The passes allow that many days of consecutive travel.

For example, if we get a 7-day pass on day 2, then we can travel for 7 days: 2, 3, 4, 5, 
6, 7, and 8.

Return the minimum number of dollars you need to travel every day in the given list of days.

Example 1:

Input: days =[1, 4, 6, 7, 8, 20], costs =[2, 7, 15]
Output: 11
Explanation: For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
In total, you spent $11 and covered all the days of your travel.
"""
from typing import List
class Solution:

    def mincostTickets(self, days: List[int], costs: List[int])-> int:
        dp ={}

        def dfs(i):
            if i == len(days):
                return 0
            if i in dp:
                return dp[i]
            dp[i] = float("inf")
            for d, c in zip([1, 7, 30], costs):
                j = i
                while j < len(days) and days[j] < days[i] + d:
                    j += 1
                dp[i] = min(dp[i], c + dfs(j))
            return dp[i]
        return dfs(0)
    
    def mincostTickets2(self, days: List[int], costs: List[int])-> int:

        dp ={}
        for i in range(len(days)-1, -1, -1):
            dp[i] = float("inf")
            for d, c in zip([1, 7, 30], costs):
                j = i
                while j < len(days) and days[j] < days[i] + d:
                    j +=1
                dp[i] = min(dp[i], c + dp.get(j, 0))
        return dp[0]
    
sol = Solution()
print("sol 1::", sol.mincostTickets([1, 4, 6, 7, 8, 20], [2, 7, 15]))
print("sol 2::", sol.mincostTickets2([1, 4, 6, 7, 8, 20], [2, 7, 15]))