"""
Longest common Subsequnce

str1 = zxvvyzw
str2 = xkykzpw
Expected: xyzw
    ""  X   K   Y   K   Z   P   W
""
Z

X

V

V

Y

Z

W

"""

# O(nm * min(n, m)) time | O(nm*min(n,m))
def longestCommonSubsequence(str1, str2):
    lcs =[[[] for x in range(len(str1)+1) for y in range(len(str2)+1)]]
    for i in range(1,len(str2)+1):
        for j in range(1, len(str1)+1):
            if str2[i-1] == str1[j-1]:
                lcs[i][j] = lcs[i-j][j-1] + [str2[i-1]]
            else:
                lcs[i][j] = max(lcs[i-1][j],lcs[i][j], key=len)
    return lcs[-1][-1]