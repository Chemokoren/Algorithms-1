"""
You are given coins of different denominations and a total amount of money amount. Write
a function to compute the fewest number of coins that you need to make up that amount if
that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:

Input: coins =[1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:

Input: coins =[2], amount = 3
Output: -1

"""
import unittest

from typing import List
# time complexity: O(amount * len(coins))
# space complexity: O(amount)
class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:

        dp =[amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a -c  >= 0:
                    dp[a] = min(dp[a], 1 + dp[a-c])

        return dp[amount] if dp[amount] != amount + 1 else -1
    
sol = Solution()

class TestCoinChange(unittest.TestCase):

    def test_true_coin_change(self):
        coins=[1,2,5]
        amount= 11
        self.assertEqual(3, sol.coinChange(coins,amount))

    def test_false_coin_change(self):
        coins=[2]
        amount= 3
        self.assertEqual(-1, sol.coinChange(coins,amount))


if __name__=="__main__":
    unittest.main()