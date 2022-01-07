"""
we are given n different types of stickers. Each sticker has a lowercase English word on it.

You would like to spell out the given string target by cutting individual letters from your
collection of stickers and rearranging them. You can use each sticker more than once if
you want, and you have infinite quantities of each sticker.

Return the minimum number of stickers that you need to spell out target. If the task is
impossible, return -1.
Note: In all test cases, all words were chosen randomly from the 1000 most common US English
words, and target was chosen as a concatenation of two random words.

Example 1:

Input: stickers =["with","example", "science"], target ="thehat"
Output: 3
Explanation:
We can use 2 "with" stickers, and 1 "example" sticker.
After cutting and rearrange the letters of those stickers, we can form the target "thehat".
Also, this is the minimum number of stickers necessary to form the target string.

Similar to : Word Break (but this is like word break on steroids)

This solution is exponential
"""
from typing import List
class Solution:

    def minStickers(self, stickers: List[str], target: str)->int:
        stickCount =[]
        for i, s in enumerate(stickers):
            stickCount.append({})
            for c in s:
                stickCount[i][c] = 1 + stickCount[i].get(c, 0)
        dp ={} # key =subseq of target | val = min num of stickers

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
                    used = min(used, dfs(remainT, s.copy()))
                dp[remainT] = used
                res += used
            return res

        res = dfs(target, {})
        return res if res != float("inf") else -1

stickers, target =["with","example", "science"], "thehat"
sol = Solution()
print(sol.minStickers(stickers, target))