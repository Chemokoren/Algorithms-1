"""
Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you 
climb to the top?

Example 1: Input: n =2
Output: 2
Explanation: there are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

"""



"""

Let's break down the solution step by step:

Defining the Problem: The problem statement asks us to find the number of distinct ways to
climb a staircase with n steps. You can either climb 1 or 2 steps at a time.

Base Cases: We start by defining the base cases:

If n is 0, there's only one way to climb the stairs (no steps).
If n is negative, there's no way to climb the stairs.
Using Recursion: The problem has overlapping subproblems. To find the total number of 
ways to climb n stairs, we can consider two possibilities for the last step:

If you take 1 step, then there are n-1 stairs left to climb.
If you take 2 steps, then there are n-2 stairs left to climb.
Recursion with Memoization: To avoid redundant calculations, we use memoization. Memoization 
involves storing the results of expensive function calls and reusing them when the
same inputs occur again. In this case, we use a dictionary (dp) to store the number of ways to climb n stairs.

Recursive Function: The climbStairs function takes two arguments: n (the number of stairs left to climb) and memo (the memoization dictionary). Here's the breakdown of the function:

First, it checks if n is already in the dp dictionary. If it is, it returns the precomputed
result.
Then, it checks the base cases. If n is 0, it returns 1 (there's only one way, no steps). 
If n is negative, it returns 0 (no way to climb).
If n is not in the dp dictionary, it calculates the number of ways to climb the stairs by
recursively calling climbStairs for n-1 and n-2. It adds these two values together because
those are the two possible ways to climb the stairs.
Finally, it stores the result in the dp dictionary for future use and returns the result.

Example Usage: The last part of the code demonstrates how to use the climbStairs function
 with example inputs and prints the results.

By using memoization, this solution efficiently calculates the number of ways to climb the
stairs for any value of n without recomputing the same subproblems, 
making it much faster than a simple recursive approach without memoization.
"""
class Solution:


    """
    In this function, we use memoization to store the number of ways to climb n stairs,
    which avoids redundant calculations. We check if we've already computed the result 
    for n, and if so, we return it from the dp dictionary. 
    Otherwise, we calculate it by recursively considering the two possible ways to climb 
    the stairs (either taking 1 step or 2 steps at a time) and store the result in the 
    dp dictionary.
    This approach ensures that each subproblem is solved only once, improving the efficiency 
    of the algorithm.
    """
    def climbStairs(self, n: int) -> int:
        dp = {}
        
        def dfs(n):
            if n < 0:
                return 0
            if n <= 3:
                dp[n] = n
                return n
            elif n in dp:
                return dp[n]
            else:
                rs = dfs(n-1) + dfs(n-2)
                dp[n] = rs
                
            return rs
            
        return dfs(n)
    
    """
    We create an array dp of size n + 1 to store the number of ways to climb each step. dp[i] will represent the number of ways to reach the i-th step.

We initialize the base cases:

dp[0] is set to 0 because there are no steps to climb.
dp[1] is set to 1 because there is only one way to climb 1 step (take one 1-step).
dp[2] is set to 2 because there are two ways to climb 2 steps (take two 1-steps or one 2-step).
We use a loop to iteratively calculate the number of ways to climb each step from the 3rd step up to the n-th step. The formula dp[i] = dp[i - 1] + dp[i - 2] represents that the number of ways to reach the i-th step is the sum of the number of ways to reach the previous step (i - 1) and the step before that (i - 2).

Finally, we return dp[n], which represents the number of ways to climb n steps.

This bottom-up approach avoids recursion and calculates the number of ways in an efficient manner, making it more space and time efficient than the recursive approach.
    """
    def climb_stairs_bottom_up(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2

        # Initialize an array to store the number of ways to climb each step
        dp = [0] * (n + 1)

        # Base cases
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2

        # Calculate the number of ways to climb each step from bottom to top
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]

    
    # optimized bottom up approach
    def climb_stairs_optimized_bottom_up(self, n: int) -> int:
        one, two =1, 1

        # for i in range(n-1, 0, -1):
        for i in range(n-1):    
            temp = one
            one = one + two
            two = temp
        return one

    
print("top down approach:", Solution().climbStairs(5))
print("bottom up approach:", Solution().climb_stairs_bottom_up(5))
print("optimized bottom up approach:", Solution().climb_stairs_optimized_bottom_up(5))

print("#################### solution 2 ####################")
