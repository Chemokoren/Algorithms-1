"""
Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s 

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
Example 3:

Input: s = "a"
Output: "a"
Example 4:

Input: s = "ac"
Output: "a"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.

"""

class Solution:

    def longestPalindrome(self, s: str)->str:

        n = len(s)
        if(n < 2):
            return s

        left = 0
        right = 0

        palindrome =[[0] *n for _ in range(n)]

        for j in range(1, n):
            for i in range(0, j):
                innerIsPalindrome = palindrome[i+1][j-1] or j-i <= 2
                if(s[i] == s[j] and innerIsPalindrome):
                    palindrome[i][j] = True
                    if(j-i > right-left):
                        left = i
                        right = j

            return s[left:right+1]

# s = "cbbd"
s = "babad"
sol = Solution()
print(sol.longestPalindrome(s))