"""
(OA) - Longest Substring Without Two Contiguous Occurrences of Letter

Given a string str containing only a and b, find the longest substring of str such that str does not
contain more than two contiguous occurrences of a and b.

Example 1:
Input: aabbaaaaabb
Output: aabbaa
Example 2:
Input: aabbaabbaabbaaa
Output: aabbaabbaabbaa

"""
from itertools import groupby
def longestValidString(str) -> str:
    loc, ans ='', ''

    for c, g in groupby(str):
        glen =len(list(g))
        ans = max([ans, loc + c * min(glen, 2)], key=len)
        if glen > 2:
            loc = c * 2
        else :
            loc += c * glen
    return ans

if __name__ == '__main__':
    print(longestValidString(input()))