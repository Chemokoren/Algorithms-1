from typing import List
from collections import Counter
"""
Given an array of strings arr. String s is a concatenation of a sub-sequence of arr
which have unique characters.

Return the maximum possible length of s.

Example 1:

Input: arr =["un","iq","ue"]
Output: 4
Explanation: All possible concatenations are "", "un", "iq","ue", "uniq" and "ique"
Maximum length is 4.

Example 2:
Input: arr =["cha","r","act","ers"]
Output: 6
Explanation: Possible solutions are "chaers" and "acters"

"""

class Solution:

    def maxLength(self, arr: List[str])->int:
        charSet =set()

        def overlap(charSet, s):
            c = Counter(charSet) + Counter(s)
            return max(c.values()) > 1

            # prev = set()
            # for c in s:
            #   if c in charSet or c in prev:
            #       return True
            #   prev.add(c)
            # return False

        def backtrack(i):
            if i == len(arr):
                return len(charSet)

            res = 0
            if not overlap(charSet, arr[i]):
                for c in arr[i]:
                    charSet.add(c)
                res = backtrack(i + 1)
                for c in arr[i]:
                    charSet.remove(c)
            return max(res, backtrack(i+1)) # don't concatenate arr[i]
        return backtrack(0)

arr =["un","iq","ue"]
sol =Solution()
print(sol.maxLength(arr))