"""
Distinct Subsequences

Given two strings s and t, return the number of distinct subsequences of s which equals t.

A string's subsequence is a new string formed from the original string by deleting some
(can be none) of the characters without disturbing the remaining character's relative
positions. (i.e., "ACE" is a subsequence of "ABCDE" while "AEC" is not).

It is guaranteed the answer fits on a 32-bit signed integer.

Example 1:

Input: s ="rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from s.
rabbbit
    -
rabbbit
  -
rabbbit
   -
"""
import unittest

class Solution:

    def num_distinct(self, s: str, t: str)-> int:

        cache ={}

        def dfs(i, j):
            # if we are at the end of string t
            if j == len(t):
                return 1
            # if we are at the end of string s
            if i == len(s):
                return 0
            if (i, j) in cache:
                return cache[(i, j)]
            
            if s[i] == t[j]:
                cache[(i, j)] = dfs(i +1, j+1) + dfs(i + 1, j)
            else:
                cache[(i, j)] = dfs(i +1, j)
            return cache[(i, j)]
        
        return dfs(0, 0)
    
class TestDistinctSubsequences(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.sol = Solution()

    def test_distinct_subsequences(self):
        self.assertEqual(3, self.sol.num_distinct("rabbbit", "rabbit"))

if __name__=="__main__":
    unittest.main()