"""
Word Break

Given a string s and a dictionary of strings wordDict, return True if s can be segmented
into a space-seperated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:

Input: s ="leetcode", wordDict =["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segemented as "leetcode"
"""
from typing import List
import unittest
class Solution:

    def word_break(self, s: str, wordDict: List[str])->bool:

        dp =[False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) -1, -1, -1):

            for w in wordDict:
                if(i + len(w)) <= len(s) and s[i: i+ len(w)] == w:
                    dp[i] = dp[i + len(w)]
                
                if dp[i]:
                    break
        return dp[0]
    
class TestWordBreak(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.sol = Solution()
        

    def test_word_break(self):
        self.assertEqual(True, self.sol.word_break("leetcode", ["leet", "code"]))


if __name__=="__main__":
    unittest.main()