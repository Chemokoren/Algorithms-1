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

in 23, 2: abc, 3:def
                                    /    |    \
                                   a     b     c
                                  /|\   /|\   /|\
                                 d e f d e f d e f 

"""
from typing import List
class Solution:
    """Letter combinations of a phone number implementation"""

    # O(n*4^n) -worst case time complexity where n is length of input string
    def letterCombinations(self, digits: str)->List[str]:
        """
        Letter combinations.
            Parameters:
                digits(str): string containing the input string
            Returns:
                res(List[str]): resultant letter combinations
        
        """

        res =[]
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        # i - what index we are at in the digits string
        # curStr that we are building
        def dfs(i, curStr): 
            if(len(curStr) == len(digits)):
                res.append(curStr)
                return
            for c in digitToChar[digits[i]]:
                dfs(i + 1, curStr + c)
        
        # put this condition coz the expected result is [] if digits is ""
        if digits:
            dfs(0, "")
        return res

digits ="23"
sol = Solution()
print(sol.letterCombinations(digits))