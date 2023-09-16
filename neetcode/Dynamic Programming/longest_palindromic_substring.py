"""
Longest Palindromic Substring

Given a string s, find the longest palindromic substring in s. You may assume that the 
maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:

Input: "cbbd"
Output: "bb"
"""
import unittest

def check_is_palindrome(s):
    start =0
    end =len(s)-1

    while start < end:
        if s[start] == s[end]:
            start +=1
            end -=1
        else:
            return False
    return True

# print(check_is_palindrome("b"))

class Solution:

    def longest_pandromic_substring(self, s: str)-> str:

        longest_pal =""

        for i in range(len(s)):
          
            # odd
            start, end= i, i
            new_str = s[start: end+1]
                
            if start >=0 and end < len(s) and check_is_palindrome(new_str):
                if len(new_str)> len(longest_pal):
                    longest_pal =new_str
                    start = start - 1
                    end = end + 1

            # even
            start, end = i,  i + 1
            new_str = s[start: end+1]

            if start >=0 and end < len(s) and check_is_palindrome(new_str):
                if len(new_str)> len(longest_pal):
                    longest_pal =new_str
                    start = start - 1
                    end = end + 1
            
        return longest_pal
    
    def longestPalindrome(self, s: str) -> str:
        res =""
        resLen =0

        for i in range(len(s)):

            # odd length
            l, r = i, i

            while l >=0 and r < len(s) and s[l] == s[r]:
                if (r -l + 1) > resLen:
                    res = s[l: r+1]
                    resLen = r - l +1
                l -=1
                r +=1

            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r -l + 1) > resLen:
                    res = s[l: r + 1]
                    resLen = r -1 +1
                l -=1
                r +=1
        return res
    
# def check_edge_cases(l, r, s, res, resLen):

#     while l >= 0 and r < len(s) and s[l] == s[r]:
#                 if (r -l + 1) > resLen:
#                     res = s[l: r + 1]
#                     resLen = r -1 +1
#                 l -=1
#                 r +=1
print("mine::", Solution().longest_pandromic_substring("cbbd"))

class TestLongestPalindromicSubstring(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.sol = Solution()

    def test_longest_palindromic_substring(self):
        self.assertEqual("bb", self.sol.longestPalindrome("cbbd"))
        self.assertEqual("bab", self.sol.longestPalindrome("babad"))

if __name__=="__main__":
    unittest.main()

            



