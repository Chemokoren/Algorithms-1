"""
Coin Change

You are given coins of different denominations and a total amount of money amount. Write
a function to compute the fewest number of coins that you need to make up that amount. If
that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

example 1:

Input: coins =[1,2,5], amount =11
Output: 3
Explanation: 11 = 5+5+1

Example 2:

Input: coins =[2], amount=3
Output: -1

"""
from typing import List
class Solution:

    # time complexity: O(amount * len(coins)) | space complexity: O(amount) of the dp
    def coinChange(self, coins: List[int], amount: int)->int:
        dp    = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a -c >= 0:
                    # coin =4, a=7
                    dp[a] = min(dp[a], 1 +dp[a -c]) #dp[7] =1 + dp[7-4]

        return dp[amount] if dp[amount] != amount + 1 else -1
    
sol = Solution()
print(sol.coinChange([2], 3))
print(sol.coinChange([1,2,5], 11))