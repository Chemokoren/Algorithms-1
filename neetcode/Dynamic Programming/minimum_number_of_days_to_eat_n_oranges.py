"""
Minimum Number of Days to Eat N Oranges

There are n oranges in the kitchen and you decided to eat some of these oranges every day
as follows:

- Eat one orange
- if the number of remaining oranges (n) is divisible by 2 then you eat n/2 oranges.
- if the number of remaining oranges (n) is divisible by 3 then you can eat 2*(n/3) oranges

You can only choose one of the actions per day.

Return the minimum number of days to eat n oranges.

Example 1:

Input: n =10
Output: 4
Explanation: you have 10 oranges

Day 1: Eat 1 orange, 10-1 = 9
Day 2: Eat 6 oranges, 9 - 2 *(9/3) = 9-6 = 3 (since 9 is divisible by 3)
Day 3: Eat 2 oranges, 3 - 2 *(3/3) = 3 -2 = 1.
Day 4: Eat the last orange 1-1 = 0.
You need at least 4 days to eat the 10 oranges.

"""
import unittest

class Solution:

    # time complexity: log n
    def min_days(self, n: int) -> int:
        dp ={0: 0, 1: 1}

        def dfs(n):
            if n in dp:
                return dp[n]
            
            one = 1 + (n % 2) + dfs(n // 2)
            two = 1 + (n % 3) + dfs(n // 3)

            dp[n] = min(one, two)

            return dp[n]
        
        return dfs(n)
    
class TestMinimumNumberOfDaysToEatNOranges(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.sol = Solution()

    def test_minimum_number_of_days_to_eat_n_oranges(self):
        self.assertEqual(4, self.sol.min_days(10))

if __name__=="__main__":
    unittest.main()
