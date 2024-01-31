"""
Palindromic Substrings

Given a string s, return the number of palindromic substrings in it. A string is a 
palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

Example 1:

Input: s="abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c"

Example 2:

Input: s ="aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "aa", "aa", "aaa"
"""

def is_palindrome(s: str)->int:
    start =0
    end =len(s) -1 

    while start <= end:
        if s[start] == s[end]:
            start +=1
            end -=1
        else:
            return False
    return True

class Solution:

    def palindromic_substrings(self, s):

        count = 0
        palindromes =[]
        for i in range(len(s)):
            # odd palindrome
            start, end = i, i

            while start >=0 and end <= len(s)-1 and is_palindrome(s[start: end +1]):
                count +=1
                palindromes.append(s[start: end +1])
                start -=1
                end +=1


            # even palindrome
            start, end = i, i + 1

            while start >=0 and end <= len(s)-1 and is_palindrome(s[start: end +1]):
                count +=1
                palindromes.append(s[start: end +1])
                start -=1
                end +=1
        return count, palindromes
    
    def countySubstrings(self, s: str)-> int:
        res = 0

        for i in range(len(s)):
            res += self.countPali(s, i, i)
            res += self.countPali(s, i, i + 1)
        return res
    
    def countPali(self, s, l, r):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -=1
            r += 1
        return res

sol =Solution()
print(sol.palindromic_substrings("abc"))
print(sol.palindromic_substrings("aaa"))
print(sol.palindromic_substrings("aaab"))

print("---------------")

print(sol.countySubstrings("abc"))
print(sol.countySubstrings("aaa"))
print(sol.countySubstrings("aaab"))
