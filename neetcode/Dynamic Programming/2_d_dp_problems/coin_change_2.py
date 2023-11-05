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

"""
This code is a dynamic programming solution to the coin change problem. It aims to find the number of different ways to make a specific amount of money using a given set of coin denominations.

Here's a step-by-step explanation of the code:

The coin_change_test function takes two parameters:

amount: The target amount of money you want to make.
coins: A list of coin denominations available to use.
Inside the function, a dictionary dp is used to memoize the results of subproblems. This helps avoid redundant calculations, which is a common optimization technique in dynamic programming.

The core of the solution is the dfs (depth-first search) recursive function. It explores different possibilities to make the target amount.

i: It represents the current index in the coins list.
a: It represents the current sum of coin values considered.
The function follows these conditions:

If a is equal to the amount, it means we've successfully reached the target amount. In this case, it returns 1 to indicate that one way to reach the target amount has been found.
If a exceeds the amount, it's not a valid way, so it returns 0.
If we've exhausted all available coin denominations (i.e., i is equal to the length of coins), we cannot proceed further, so it returns 0.
Before making a recursive call, the function checks whether it has already computed the result for the same parameters (i, a) in the dp dictionary. If it has, it simply returns the previously computed result, avoiding redundant work.

If the result is not found in the dp dictionary, the function calculates it using recursive calls:

dfs(i, a + coins[i]): It represents the scenario where the current coin at index i is selected, and its value is added to the current sum a.
dfs(i + 1, a): It represents the scenario where the current coin is not selected, and we move on to the next coin in the list.
The result of the recursive calls is summed up, and the result is stored in the dp dictionary to avoid recomputation.

Finally, the dfs(0, 0) call is made, starting with the first coin (index 0) and a current sum of 0. The function returns the total number of ways to make the target amount using the given coin denominations.

The code prints the result, indicating the number of ways to make the amount 5 using the coin denominations [1, 2, 5].

In this specific example, the output would be:

arduino
Copy code
manenos:: 4

Time Complexity:
-----------------

This means there are four different ways to make 5 units of currency using the provided coin denominations.


The time complexity of this solution is influenced by the memoization technique used to avoid redundant calculations. Let's analyze the time complexity:

The dfs function is a recursive function, and for each distinct pair of parameters (i, a), it computes the result exactly once and stores it in the dp dictionary.

Since each pair (i, a) is computed only once, and the function explores all possible combinations of i and a, the total number of unique pairs is bounded by the number of unique combinations of i and a, which is O(len(coins) * amount). This is because i can take on values from 0 to len(coins) - 1, and a can take on values from 0 to amount.

The time complexity of the dfs function is therefore O(len(coins) * amount).

The top-level call to dfs(0, 0) represents the starting point of the recursion, and it triggers the computation of all possible pairs (i, a) within the limits mentioned above.

Thus, the overall time complexity of the coin_change_test function, which includes the initial function call and the recursive computation, is also O(len(coins) * amount).

The time complexity is primarily determined by the number of unique pairs of (i, a) that need to be computed and stored in the dp dictionary. This dynamic programming approach significantly reduces redundant calculations and results in a time complexity that is proportional to the product of the number of coins and the target amount.

"""
def coin_change_test(amount, coins):
    
    dp ={}
    def dfs(i, a):
        if a == amount:
            return 1
        
        if a > amount:
                return 0
        
        if i == len(coins):
            return 0
        
        if (i, a) in dp:
            return dp[(i, a)]
        
        dp[(i, a)] = dfs(i, a + coins[i]) + dfs(i + 1, a) 

        return dp[(i, a)]

    return dfs(0,0)

print("manenos::", coin_change_test(5, [1,2,5]))

""" the code here returns the actual combinations instead of the number of combinations"""
def coin_change_combinations(amount, coins):
    
    def dfs(i, a, current_combination):
        if a == amount:
            result.append(current_combination[:])
            return
        
        if a > amount or i == len(coins):
            return
        
        # Use the current coin and add it to the combination
        current_combination.append(coins[i])
        dfs(i, a + coins[i], current_combination)
        current_combination.pop()  # Backtrack by removing the last added coin
        
        # Skip the current coin
        dfs(i + 1, a, current_combination)

    result = []  # List to store the combinations
    dfs(0, 0, [])
    
    return result

combinations = coin_change_combinations(5, [1, 2, 5])
print(combinations)



# computes the minimum number of coins that can make up the full amount
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

print("--- coin change 2 ---")
print(coin_change_two(5, [1,2,5]))
print(coin_change_two(7, [3,5]))
print("----------------------actual solutions ----------------------")

class Solution:

    # time complexity: O(m*n) | space complexity: O(m*n) where m is the len of coins array
    def change_top_down(self, amount: int, coins:List[int])->int:

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
    def change_bottom_up(self, amount: int, coins: List[int])-> int:
        dp =[[0] * (len(coins) + 1) for i in range(amount + 1)]
        dp[0] = [1] * (len(coins) + 1)

        for a in range(1, amount +1):
            for i in range(len(coins)-1, -1, -1):
                dp[a][i] = dp[a][i + 1]
                if a - coins[i] >=0:
                    dp[a][i] += dp[a- coins[i]][i]
        return dp[amount][0]
    
#     # O(n*m) time complexity | O(n) memory complexity
#     def change3(self, amount: int, coins: List[int])-> int:

#         dp =[0] * (amount + 1)
#         dp[0] =1

#         for i in range(len(coins) -1, -1, -1):
#             nextDP =[0] * (amount + 1)
#             nextDP[0] = 1

#             for a in range(1, amount + 1):
#                 nextDP[a] = dp[a]
#                 if a - coins[i] >= 0:
#                     nextDP[a] += nextDP[a - coins[i]]

#             dp = nextDP

#         return dp[amount]

# print("anii ")
# sol = Solution()
# print(sol.change(5, [1,2,5]))
# print('---')
# print(sol.change2(5, [1,2,5]))

# print('---')
# print(sol.change3(5, [1,2,5]))

