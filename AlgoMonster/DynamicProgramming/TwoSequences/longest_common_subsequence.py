"""
Longest Common Subsequence

Given two strings word1 and word2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some 
characters(can be none) deleted without changing the relative order of the remaining 
characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common 
subsequence of two strings is a subsequence that is common to both strings.

If there is no common subsequence, return 0.

Example 1:
Input:

word1 = "abcde"

word2 = "ace"

Output: 3
Explanation:

The longest common subsequence is ace and its length is 3.
Example 2:
Input:

word1 = "almost"

word2 = "algomonster"

Output: 6
Explanation:

The longest common subsequence is almost and its length is 6.
Example 3:
Input:

word1 = "abc"

word2 = "def"

Output: 0
Explanation:

There is no such common subsequence, so the result is 0.
"""

def longest_common_subsequence(word1: str, word2: str) -> int:
    return 0

if __name__ == '__main__':
    word1 = input()
    word2 = input()
    res = longest_common_subsequence(word1, word2)
    print(res)