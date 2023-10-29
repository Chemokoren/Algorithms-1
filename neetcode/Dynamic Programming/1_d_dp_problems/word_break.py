"""
Word Break

Given a string s and a dictionary of strings wordDict, return true if s can be segmented
into a space-seperated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the
segmentation.

Example 1:

Input: s ="leetcode", wordDict =["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet", "code".

"""
from typing import List
import unittest

class Solution:

    def word_break1(self, s: str, dp: List[str])->bool:
        res =[]
        for w in dp:
            if w in s:
                res.append(1)
        return True if len(res) == len(dp) else False
    
    def word_break(self, s: str, word_dict: List[str])->bool:

        dp =[False] * (len(s) + 1)
        dp[len(s)] = True # base case

        for i in range(len(s)-1, -1, -1):
            for w in word_dict:
                if(i + len(w)) <= len(s) and s[i: i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        return dp[0]
    
sol = Solution()
print("--------------------")
print(sol.word_break("leetcode", ["leet", "code"]))
# print(sol.wordBreak("neetcode", ["neet", "leet", "code"]))

class TestWordBreak(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.sol = Solution()

    def test_word_break(self):
        self.assertEqual(True, self.sol.word_break("leetcode", ["leet", "code"]))

    def test_word_break_two(self):
        self.assertEqual(True, self.sol.word_break1("leetcode", ["leet", "code"]))

if __name__=="__main__":
    unittest.main()