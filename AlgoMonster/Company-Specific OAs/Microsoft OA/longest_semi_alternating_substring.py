"""
(OA) - Longest Semi-Alternating Substring

Given a string S containing only characters a and b. A substring (contiguous fragment) of S is 
called a semi-alternating substring if it does not contain three identical consecutive characters. 
In other words, it does not contain either 'aaa' or 'bbb' substrings. Note that the whole S is its
own substring.

Example 1:
Input: baaabbabbb
Output: 7
Explanation:

the longest semi-alternating substring is aabbabb
Example 2:
Input: babba
Output: 5
Explanation:

Whole S is semi-alternating.
Example 3:
Input: abaaaa
Output: 4
Explanation:

The first four letters of S create a semi-alternating substring.

Implementation
"""
def semi_substring(s: str) -> int:
    max_len = 0
    left = 0
    for right in range(len(s)):
        if right - left + 1 >= 3 and s[right] == s[right -1] ==s[right -2]:
            left = right -1
        max_len=max(max_len, right -left + 1)
    return max_len

if __name__ =='__main__':
    s = input()
    res = semi_substring(s)
    print(res)
