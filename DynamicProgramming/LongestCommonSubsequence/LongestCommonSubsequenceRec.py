"""
Given two sequences X[1..m] and Y[1..n], find the longest common subsequence between them

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
    # C=[[m+1,n+1]] # create a two dimensional array
    # translate vector< vector<int>>C(m+1, vector<int>(n+1, 0))
    C=[[0]*int(m+1)]*int(n+1)

    for i in range(1,m):
        for j in range(1,m):
            if(s[i-1]==t[j-1]):
                C[i][j] =C[i-1][j-1]+1
            else:
                C[i][j]=max(C[i-1][j],C[i][j-1])

    return C[m][n]

s ="ABACBDAB"
t ="BDCABA"

print(LongestCommonSubsequenceRec(s,t))