"""
Regular Expression Matching

Given an input string(s) and a pattern (p), implement regular expression matching 
with support for '.' and '*' where:

- '.' Matches any single character.
- '*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

Example 1:

Input: s ="aa", p ="a"
Output: False
Explanation: "a" does not match the entire string "aa".

Example 2:

Input: s="aa", p="a*"
Output: True
Explanation: '*' means zero or more of the preceding element, 'a'.

Example 3:

Input s ="ab", p=".*"
output: True
"""
import unittest

class Solution:

    def is_match(self, s: str, p: str):
        # Top-Down Memoization
        cache ={}

        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")

            if (j + 1) < len(p) and p[j + 1] =="*":
                cache[(i, j)] =(dfs(i, j + 2) or (match and dfs(i +1, j)))
                return cache[(i, j)]
            if match:
                cache[(i, j)] = dfs(i +1, j + 1)
                return cache[(i, j)]
            cache[(i, j)] = False
            return cache[(i, j)]

        return dfs(0, 0)
        


class TestRegularExpressionMatching(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.sol = Solution()

    def test_regular_expression(self):
        self.assertEqual(False, self.sol.is_match("aa", "a"))
        self.assertEqual(True, self.sol.is_match("aa", "a*"))
        self.assertEqual(True, self.sol.is_match("ab", ".*"))


if __name__=="__main__":
    unittest.main()