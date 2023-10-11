"""
Longest Palindromic Substring

Given a string s, find the longest palindromic substring in s. You may assume that the
maximum length of s is 1000.

Example 1:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer

Example 2:
Input: "cbbd"
Output: "bb"
"""

def is_palindrome(s):
    start =0
    end =len(s)-1

    while start <=end:
        if s[start] == s[end]:
            start +=1
            end -=1
        else:
            return False
    return True

def longest_palindromic_substring(s):
    count =0
    res =""
    for i in range(len(s)):
        start =i
        end =i

        if is_palindrome(s[start: end+1]) and (start >=0 and end < len(s)):
            if len(s[start: end+1]) > count:
                count= len(s[start: end+1])
                res = s[start: end+1]
                start -=1
                end +=1

        start =i
        end =i +1
        if is_palindrome(s[start: end+1]) and (start >=0 and end < len(s)):
            if len(s[start: end+1]) > count:
                count= len(s[start: end+1])
                res = s[start: end+1]
                start -=1
                end +=1

    return count, res


print(longest_palindromic_substring("cbbd"))
print(longest_palindromic_substring("babad"))