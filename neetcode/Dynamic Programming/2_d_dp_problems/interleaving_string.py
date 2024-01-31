"""
Interleaving string

Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.
An interleaving of two strings s and t is a configuration where they are divided into
non-empty substrings such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n- m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 ... or t1 + s1 + t2 + s2 + t3 + s3 +...

Note: a + b is the concatenation of strings a and b.

Example 1:

a a b c c                           d b b c a

                a a d b b c b c a c
Input: s1 = "aabcc", s2 ="dbbca", s3 ="aadbbcbcac"
Output: True
"""
class Solution:

    def is_interleave_top_down(self, s1: str, s2: str, s3: str)-> bool:
        dp ={}

        # k = i + j
        def dfs(i, j):
            if i ==len(s1) and j == len(s2):
                return True
            if (i, j) in dp:
                return dp[(i, j)]
            if i < len(s1) and s1[i] == s3[i + j] and dfs(i + 1, j):
                return True
            if j < len(s2) and s2[j] == s3[i + j] and dfs (i, j + 1):
                return True
            dp[(i, j)]= False
            return False
        return dfs(0, 0)
    
    def is_interleave_bottom_up(self, s1: str, s2: str, s3: str)->bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        # create a 2d grid with an extra row & column
        # dp =[[False for i in range(len(s1) + 1)] for j in range(len(s2) + 1)]
        dp =[[False] * (len(s1) + 1) for j in range(len(s2) + 1)]
        # initialize the bottom right item to True
        dp[len(s1)][len(s2)] =True
        for row in dp:
            print(row)

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] =True
                if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] =True
        print('----------------')
        for row in dp:
            print(row)

        return dp[0][0]




        # for row in dp:
        #     print(row)

    
sol = Solution()
print(sol.is_interleave_top_down(s1 = "aabcc", s2 ="dbbca", s3 ="aadbbcbcac"))

print("------")
print(sol.is_interleave_bottom_up(s1 = "aabcc", s2 ="dbbca", s3 ="aadbbcbcac"))