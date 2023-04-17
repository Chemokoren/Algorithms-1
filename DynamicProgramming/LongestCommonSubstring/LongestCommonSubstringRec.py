"""
given two strings X[1..m] and Y[1..n], we want to find the longest common substring 
between the two.

Example:

X: DEADBEEF
Y: EATBEEF

Two common substrings are EA and BEEF, the longest is BEEF with length 4. so return 4.

Recursive solution

let d[i][j] be the length of the longest common substring of X[1..i] and Y[1..j] that 
ends at X[i] and Y[j]

are we changing the problem?

Yes, but the the optimal solution is max(d[i][j]) for all i, j!
Two cases:
1) X[i] = Y[j]
2) X[i] != Y[j]

For 1), then the LCS of X[1..i] and Y[1..j] is just LCS of X[1..i-1] and Y[1..j-1], 
plus X[i] =Y[j]

for 2), then there can't be a common substring ending at X[i] and Y[j]! so the answer,
is 0!

d[i,j]= d[i-1,j-1]+1 if x[i] == y[j]
or
d[i,j] = 0 if x[i] != y[j]


Pseudocode:

Let d[0..m, 0..n] be a 2D array of all 0
max_value =-1
for i=1 to m:
	for j=1 to n:
		if (x[i] ==y[j]):
			d[i][j] =1+ d[i-1][j-1]
			
		else:
			d[i][j] = 0
			
	max_value =max(max_value, d[i][j])
return max_value

"""

def LongestCommonSubstringRec(s, t):
    m = len(s)
    n = len(t)

    max_val = -1

    d =[[0 for i in range(m+1)] for j in range(n+1)]
 
    for i in range(1,m+1):
        for j in range(1,n+1):
            if(s[i-1]==t[j-1]):
                d[i][j] =d[i-1][j-1]+1
                max_val =max(max_val, d[i][j])
            else:
                d[i][j] = 0
    return max_val

s = "DEADBEEF"
t = "EATBEEF"

# print(LongestCommonSubstringRec(s,t))
# print(LongestCommonSubstringRec("abcjklp","acjkp"))

def LongestCommonSubstringRec(s, t):
    m = len(s)
    n = len(t)

    max_val = -1

    d = [[0 for i in range(m+1)] for j in range(n+1)]
 
    for i in range(m):
        for j in range(n):
            if(s[i]==t[j]):
                d[i+1][j+1] = d[i][j]+1
                max_val = max(max_val, d[i+1][j+1])
            else:
                d[i+1][j+1] = 0

    return max_val

print(LongestCommonSubstringRec("abcjklp","acjkp"))
