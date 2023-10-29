"""
Longest Common Subsequence

Given two strings text1 and text2, return the length of their longest commmon subsequence.

A subsequence of a string is a new string generated from the original string with some
characters(can be none) deleted without changing the relative order of the remaining
characters. (e.g., "ace" is a subsequence of "abcde" while "aec" is not).

A common subsequence of two strings is a subsequence that is common to both strings.

If there is no common subsequence, return 0.

Example 1:

Input text1 = "abcde", text="ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.

"""

class Solution:

    # time complexity: O(n * m) | sapce complexity : O(n * m)
    def lcs(self, s1, s2):
        ROW, COL = len(s1), len(s2)
        g =[[0 for x in range(COL+1)] for y in range(ROW+1)]
        
        for i in range(ROW-1, -1, -1):
            for j in range(COL-1, -1, -1):
                if s2[j] == s1[i]:
                    g[i][j] =1 + g[i+1][j+1]
                else:
                    g[i][j] =max(g[i+1][j], g[i][j+1])

        return g[0][0]

sol = Solution()
print(sol.lcs("abcde", "ace"))

print("-------")


def longest_common_subsequence(s1, s2)->int:
    i,j=0,0
    count= 0
    lcs=""

    while i <len(s1) and j < len(s2):
        if s1[i] == s2[j]:
            lcs +=str(s1[i])
            i +=1
            j +=1
            count +=1
            
        else:
            if len(s1[i:]) < len(s2[j:]):
                j +=1
            else:
                i +=1
    return count, lcs

print(longest_common_subsequence("abcde", "ace"))
