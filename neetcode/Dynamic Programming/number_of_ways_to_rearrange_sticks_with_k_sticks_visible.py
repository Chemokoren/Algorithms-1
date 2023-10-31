"""
Number of ways to Rearrange Sticks with K Sticks visible

There are n uniquely-sized sticks whose lengths are integers from 1 to n. You want to 
arrange the sticks such that exactly k sticks are visible from the left. A stick is visible
from the left if there are no longer sticks to the left of it.

For example, if the sticks are arranged [1,3,2,5,4], then the sticks with lengths 1, 3, and
5 are visible from the left.

Given n and k, return the number of such arrangements. Since the answer may be large, 
return it modulo 10^9 + 7.

Example 1:
Input: n=3, k =2
Output: 3
Explanation: [1,3,2], [2,3, 1], and [2,1,3] are the only arrangements such that exactly 2
sticks are visible.
The visible sticks are underlined.

"""

class Solution:

    def rearrange_sticks(self, n: int, k:int) -> int:

        dp ={}

        def dfs(N, K):

            if N == K:
                return 1
            if N == 0 or K == 0:
                return 0
            if (N, K) in dp:
                return dp[(N, K)]
            
            dp[(N, K)] = (dfs(N-1, K-1) +
                          (N-1) * dfs(N-1, K))
            return dp[(N, K)]
        return dfs(n, k) % (10 ** 9 + 7)
    
    def rearrange_dp(self, n: int, k:int) -> int:

        dp ={(1, 1) : 1}

        for N in range(2, n + 1):
            for K in range(1, k + 1):
                dp[(N, K)] = (dp.get((N-1, K-1), 0) +
                              (N -1) * dp.get((N-1, K), 0))
        return dp[(n, k)] % (10**9 + 7)

        