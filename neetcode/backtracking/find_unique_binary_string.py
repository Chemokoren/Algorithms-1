from typing import List
"""
Find Unique Binary String

Given an array of strings nums containing n unique binary strings each of length n, return a
binary string of length n that does not appear in nums. If there are multiple answers, you
may return any of them.

Example 1:
Input: nums =["01","10"]
Output: "11"
Explanation: "11" does not appear in nums. "00" would also be correct.

Example 2:
Input: nums =["00","01"]
Output: "11"
Explnation: "11" does not appear in nums. "10" would also be correct.

Example 3:
Input: nums =["111", "011", "001"]
Output: "101"
Explanation: "101" does not appear in nums. "000", "010", and "110" would also be correct.

*** there are 2^n possibilities
Time complexity is n^2 because as soon as we get an answer, we return instead of trying all
possibilities.
"""

class Solution:

    def findDifferentBinaryString(self, nums: List[str])->str:

        strSet = {s for s in nums}

        def backtrack(i, cur):
            if i == len(nums):
                res ="".join(cur)
                return None if res in strSet else res

            res = backtrack(i + 1, cur)
            if res: return res

            cur[i] ="1"
            res = backtrack(i + 1, cur)
            if res: return res

        return backtrack(0,["0" for s in nums])

nums =["111", "011", "001"]
nums =["00","01"]
sol = Solution()
print(sol.findDifferentBinaryString(nums))