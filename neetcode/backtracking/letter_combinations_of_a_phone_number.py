"""
Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations
that the number could represent. Return the answer in any order.

A mapping of digit to letters(just like on the telephone buttons) is given below.
Note that 1 does not map to any letters

1[]         2[a,b,c]        3[d,e,f]

4[g,h,i]    5[j,k,l]        6[m,n,o]

7[p,q,r,s]  8[t,u,v]        9[w,x,y,z]
*[+]        0[ ]            🔝[#]
Example 1:
Input: digits ="23"
Output: ["ad","ae", "af", "bd","be","bf","cd", "ce","cf"]
"""
from typing import List
class Solution:

    def letterCombinations(self, digits: str)->List[str]:

        res =[]
        digitToChar ={
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtrack(i, curStr):
            if(len(curStr) == len(digits)):
                res.append(curStr)
                return
            for c in digitToChar[digits[i]]:
                backtrack(i + 1, curStr + c)
        if digits:
            backtrack(0, "")
        return res

digits ="23"
sol = Solution()
print(sol.letterCombinations(digits))