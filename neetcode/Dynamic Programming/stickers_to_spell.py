"""
Stickers to Spell Word

We are given n different types of stickers. Each sticker has a lowercase English word on it.
You would like to spell out the given string target by cutting individual letters from your
collection of stickers and rearranging them. You can use each sticker more than once if
you want, and you have infinite quantities of each sticker.

Return the minimum number of stickers that you need to spell out target. If the task is
impossible, return -1.

Note: In all test cases, all words were chosen randomly from the 1000 most common US
English words, and target was chosen as a concatenation of two random words.

Example 1:

Input: Stickers =["with", "example", "science"], target="thehat"
Output: 3
Explanation:
We can use 2 "with" stickers and 1 "example" sticker.
After cutting and rearranging the letters of those stickers, we can form the target "thehat"
Also, this is the minimum number of stickers necessary to form the target string.

"""
from typing import List
import unittest

class Solution:

    def min_stickers(self, stickers: List[str], target: str)->int:
        stickCount =[]
        for i, s in enumerate(stickers):
            stickCount.append({})
            for c in s:
                stickCount[i][c] = 1 + stickCount[i].get(c, 0)
        dp ={} # key = subsq of target | val = min num of stickers
        
        def dfs(t, stick):
            if t in dp:
                return dp[t]
            
            res = 1 if stick else 0
            remainT =""
            for c in t:
                if c in stick and stick[c] > 0:
                    stick[c] -=1
                else:
                    remainT += c
            if remainT:
                used = float("inf")

                for s in stickCount:
                    if remainT[0] not in s:
                        continue
                    used =min(used, dfs(remainT, s.copy()))
                dp[remainT] = used
                res += used
            return res
        res =dfs(target, {})
        return res if res != float("inf") else -1
    
class TestStickersToSpell(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.sol = Solution()

    def test_stickers_to_spell(self):
        self.assertEqual(3, self.sol.min_stickers(["with", "example", "science"], "thehat"))

if __name__=="__main__":
    unittest.main()

