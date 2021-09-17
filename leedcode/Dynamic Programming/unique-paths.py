"""
Unique paths

A robot is located at the top-left corner of a m*n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to 
reach the bottom-right corner of the grid (marked 'Finish' in the diagram below.)

How many possible unique paths are there?

Example 1:

Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
Example 3:

Input: m = 7, n = 3
Output: 28
Example 4:

Input: m = 3, n = 3
Output: 6
 

Constraints:

1 <= m, n <= 100
It's guaranteed that the answer will be less than or equal to 2 * 109.


"""

class Solution:

    def uniquePaths(self, m:int, n: int)->int:

        dp =[[0 for x in range(m) for y in range(n)]]

        # first column elements
        for i in range(m):
            dp[0][i] = 1

        # first row elements
        for i in range(n):
            dp[i][0] = 1

        # for each current element, we will have its value equal to the number of ways we
        # can reach the element above it and the number of ways we can reach the element
        # from its left
        for i in range(1, n):
            for j in range(1,m):
                dp[i][j] = dp[i-1][j]+ dp[i][j-1]

        return (dp[-1][-1])

m , n = 7, 3
sol = Solution()
print(sol.uniquePaths(m,n))