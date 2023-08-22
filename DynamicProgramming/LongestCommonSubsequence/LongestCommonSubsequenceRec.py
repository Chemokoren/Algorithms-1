"""
Given two sequences X[1..m] and Y[1..n], find the longest common subsequence 
between them

Example:

X: ABACBDAB
Y: BDCABA
Longest Common Subsequence:BCBA

Has several applications in Genetics

Pseudocode:

let c[0..m,0..n] be a new 2D array of all 0
for i=1 to m
	for j =1 to n
		if(x[i]=y[j])
			c[i][j] =c[i-1][j-1]+1
		else
			c[i][j]=max(c[i-1][j],c[i][j-1])
			
return c[m][n]
"""

def LongestCommonSubsequenceRec(s, t):
    m = len(s)
    n = len(t)

    C = [[0] * (n+1) for _ in range(m+1)]

    for i in range(1,m+1):
        for j in range(1,n+1):
            if(s[i-1]== t[j-1]):
                C[i][j] =C[i-1][j-1]+1
            else:
                C[i][j]=max(C[i-1][j],C[i][j-1])
    return C[m][n]

s ="ABACBDAB"
t ="BDCABA"

print(LongestCommonSubsequenceRec(s,t))
print("first::", LongestCommonSubsequenceRec("abcde","ace"))

"""
given two strings text1 and text2, return the length of their longest common
subsequence.

A subsequence of a string is a new string generated from the original string
with some characters(can be none) deleted without changing the relative order
of the remaining characters. (e.g, "ace" is a seubsequence of "abcde" while
"aec is not"). A common subsequence of two strings is a subsequence that is
common to both strings.

If there is no common subsequence, return 0.

Example 1:

Input: text1 ="abcde", text2="ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.

"""
class Solution:
    
    # bottom-up solution
    def longestCommonSubsequence(self, text1: str, text2: str)-> int:
        
        dp =[[0 for j in range(len(text2)+1)] for i in range(len(text1)+ 1)]
        
        for i in range(len(text1)-1, -1, -1):
            for j in range(len(text2)-1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])
        return dp[0][0]
sol = Solution()
print(sol.longestCommonSubsequence("abcde","ace"))
print(sol.longestCommonSubsequence("ABACBDAB","BDCABA"))
print(sol.longestCommonSubsequence("DEADBEEF","EATBEEF"))