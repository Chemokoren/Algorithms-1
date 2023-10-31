"""
Coin Change 2

You are given an integer array coins representing coins of different denominations and an
integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot
be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.

Example 1:

Input: amount =5, coins =[1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
"""
from typing import List
def coin_change(amount, coins):
    coins.sort()

    count = 0
    for c in coins:
        if c== amount:
            count +=1
        else:
            while amount > c:
                amount = amount-c
                count +=1
    return count

print(coin_change(5, [1,2,5]))
print(coin_change(7, [3,5]))
print("---")

def coin_change_two(amount, coins):
    coins.sort()

    # Create a list to store the minimum number of coins needed for each amount from 0 to 
    # 'amount'.
    # Initialize with a value greater than 'amount' to ensure we can find a smaller value.
    dp = [amount + 1] * (amount + 1)

    # 0 coins are needed to make an amount of 0.
    dp[0] = 0

    for i in range(1, amount + 1):
        for c in coins:
            if i >= c:
                dp[i] = min(dp[i], dp[i - c] + 1)

    return dp[amount] if dp[amount] <= amount else 0

print("---")
print(coin_change_two(5, [1,2,5]))
print(coin_change_two(7, [3,5]))
print("---")

class Solution:

    def change(self, amount: int, coins:List[int])->int:

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
    
    # O(n*m) time complexity | # O(n*m) memory complexity
    def change2(self, amount: int, coins: List[int])-> int:
        dp =[[0] * (len(coins) + 1) for i in range(amount + 1)]
        dp[0] = [1] * (len(coins) + 1)

        for a in range(1, amount +1):
            for i in range(len(coins)-1, -1, -1):
                dp[a][i] = dp[a][i + 1]
                if a - coins[i] >=0:
                    dp[a][i] += dp[a- coins[i]][i]
        return dp[amount][0]
    
    # O(n*m) time complexity | O(n) memory complexity
    def change3(self, amount: int, coins: List[int])-> int:

        dp =[0] * (amount + 1)
        dp[0] =1

        for i in range(len(coins) -1, -1, -1):
            nextDP =[0] * (amount + 1)
            nextDP[0] = 1

            for a in range(1, amount + 1):
                nextDP[a] = dp[a]
                if a - coins[i] >= 0:
                    nextDP[a] += nextDP[a - coins[i]]

            dp = nextDP

        return dp[amount]
    
sol = Solution()
print(sol.change(5, [1,2,5]))
print('---')
print(sol.change2(5, [1,2,5]))

print('---')
print(sol.change3(5, [1,2,5]))

