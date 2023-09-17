"""
Interleaving String

Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.
An interleaving of two strings s and t is a configuration where they are divided into 
non-empty substrings such that:
- s = s1 + s2 + ... + sn
- t = t1 + t2 + ... + tm
- |n - m| <=1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 +s2 +t3 + s3 + ...

Note: a + b is the concatenation of strings a and b.

Example 1:

a a b c c                                d b b c a


                a a d b b c b c a c 

s1 = "aabcc", s2 ="dbbca", s3 = "aadbbcbcac"
Output = True
"""
import unittest

class Solution:

    def memoization_is_interleave(self, s1: str, s2: str, s3: str) -> bool:

        dp = {}

        # k = i + j
        def dfs(i, j):
            if i == len(s1) and j == len(s2):
                return True
            if (i, j)  in dp:
                return dp[(i, j)]
            if i < len(s1) and s1[i] == s3[i + j] and dfs(i + 1, j):
                return True
            if j < len(s2) and s2[j] == s3[i + j] and dfs(i, j + 1):
                return True
            dp[(i, j)] = False
        return dfs(0, 0)
    
    def dp_is_interleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        dp =[[False] * (len(s2) +  1) for i in range(len(s1) + 1)]
        dp[len(s1)][len(s2)] = True

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True
                if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True
        return dp[0][0]
    
class TestInterleavingString(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.sol = Solution()

    def test_interleaving_string_dp(self):
        self.assertEqual(True, self.sol.dp_is_interleave("aabcc", "dbbca", "aadbbcbcac"))

    def test_interleaving_string_memoization(self):
        self.assertEqual(True, self.sol.memoization_is_interleave("aabcc", "dbbca", "aadbbcbcac"))


if __name__=="__main__":
    unittest.main()