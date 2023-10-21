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
class Solution:

    def word_break(self, s: str, dp: List[str])->bool:

        for w in dp:
            if w in s:
                return True
        return False
    
sol = Solution()
print(sol.word_break("leetcode", ["leet", "code"]))