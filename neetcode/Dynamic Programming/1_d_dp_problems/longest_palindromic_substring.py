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

def longest_palindromic_substring_2(s):
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    longest = ""

    for i in range(len(s)):
        # Odd length palindrome
        palindrome1 = expand_around_center(i, i)
        if len(palindrome1) > len(longest):
            longest = palindrome1

        # Even length palindrome
        palindrome2 = expand_around_center(i, i + 1)
        if len(palindrome2) > len(longest):
            longest = palindrome2

    return longest

def longest_palindromic_substring_3(s: str)-> str:
    res =""
    resLen =0

    for i in range(len(s)):
        # odd length
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r -l + 1) > resLen:
                res = s[l: r + 1]
                resLen = r - l + 1
            l -= 1
            r += 1
        # even length
        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if(r -l + 1) > resLen:
                res = s[l: r+1]
                resLen = r - l + 1
            l -= 1
            r +=1
    return res


print(longest_palindromic_substring("cbbd"))
print(longest_palindromic_substring("babad"))

print("-------------")
print(longest_palindromic_substring_2("cbbd"))
print(longest_palindromic_substring_2("babad"))

print("-------------")
print(longest_palindromic_substring_3("cbbd"))
print(longest_palindromic_substring_3("babad"))