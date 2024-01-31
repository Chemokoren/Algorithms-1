"""
You are given an integer array coins representing coins of different denominations and an 
integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money 
cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin. #(hints at unbounded knapsack problem)

The answer is guaranteed to fit into a signed 32-bit integer.

Example 1:

Input: amount =5, coins=[1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

"""
from typing import List
import unittest
class Solution:

    # memoization
    def change(self, amount:int, coins: List[int])-> int:
        cache ={}

        def dfs(i, a):
            if a == amount:
                return 1
            if a > amount:
                return 0
            if i == len(coins):
                return 0
            if (i, a) in cache:
                return cache[(i, a)]
            
            cache[(i, a)] = dfs(i, a + coins[i]) + dfs(i + 1, a)
            return cache[(i, a)]
        
        return dfs(0, 0)
    
    # bottom-up dp
    # time complexity: O(n*m)
    def dp_change(self, amount: int, coins: List[int])-> int:
        dp =[[0] * (len(coins)+1) for i in range(amount+1)]
        dp[0] =[1] * (len(coins) + 1)

        for a in range(1, amount + 1):
            for i in range(len(coins) -1, -1, -1):
                dp[a][i] = dp[a][i+1]
                if a - coins[i] >= 0:
                    dp[a][i] += dp[a - coins[i]][i]
        return dp[amount][0]
    
    # time complexity: O(n*m)
    # space complexity: O(n)
    def optimized_dp_change(self, amount: int, coins: List[int])-> int:
        dp = [0] * (amount +1)
        dp[0] = 1

        for i in range(len(coins) -1, -1, -1):
            nextDP =[0] * (amount + 1)
            nextDP[0] = 1

            for a in range(1, amount + 1):
                nextDP[a] = dp[a]
                if a - coins[i] >= 0:
                    nextDP[a] += nextDP[a - coins[i]]

            dp = nextDP
        return dp[amount]



class TestCoinChange(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.sol = Solution()

    def test_coin_change(self):
        self.assertEqual(4, self.sol.change(5, [1, 2, 5]))

    def test_dp_coin_change(self):
        self.assertEqual(4, self.sol.dp_change(5, [1, 2, 5]))

    def test_optimized_dp_coin_change(self):
        self.assertEqual(4, self.sol.optimized_dp_change(5, [1, 2, 5]))


if __name__ =='__main__':
    unittest.main()