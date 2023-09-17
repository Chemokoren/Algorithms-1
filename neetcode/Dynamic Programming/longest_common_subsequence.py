"""
Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some
characters(can be none) deleted without changing the relative order of the remaining 
characters. (e.g. "ace" is a subsequence of "abcde" while "aec" is not). A common 
subsequence of two strings is a subsequence that is common to both strings.

if there is no common subsequence, return 0.

Example 1:

Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.
"""
import unittest

class Solution:

    def dp_longest_common_subsequence(self, text1: str, text2: str) ->int:

        dp =[[0 for j in range(len(text2) +1 )] for i in range(len(text1) + 1)]

        for i in range(len(text1) -1, -1, -1):

            for j in range(len(text2) -1, -1, -1):

                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] =max(dp[i][j +1], dp[i +1][j])
        return dp[0][0]
    
class TestLongestCommonSubsequence(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.sol =Solution()

    def test_longest_common_subsequence(self):
        self.assertEqual(3, self.sol.dp_longest_common_subsequence("abcde", "ace"))

if __name__=="__main__":
    unittest.main()



