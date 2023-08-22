"""
Regular Expression Matching - Top-Down Memoization Dynamic Programming

Given an input string (s) and a pattern (p), implement regular expression matching with 
support for '.' and '*' where:

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string(not partial).

Example 1:

Input s = "aa", p ="a"
Output = false
Explanation: "a" does not match the entire string "aa".

Example 2:

Input: s = "aa", p ="a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'.
Therefore, by repreating 'a' once, it becomes "aa".

Example 3:

Input s = "ab", p =".*"
Output: true


"""

# Brute force approach
class Solution:
    def isMatch(self, s: str, p:str)-> bool:
        def dfs(i, j):
            if i >=len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False

            match =i< len(s) and (s[j] == p[j] or p[j] == ".")
            if(j+1) < len(p) and p[j+1] == "*":
                return(dfs(i,j + 2) or  # dont use *
                      (match and dfs(i + 1, j))) # use *

            if match:
                return dfs(i + 1, j+1)
            return False
        return dfs(0,0)

# s = "ab"
# p =".*"
# s = "aa"
# p = "a"
s= "aa"
p ="a*"
sol = Solution()
print(sol.isMatch(s,p))

"""
Top-Down approach

"""

class SolutionTopDown:
    def isMatch(self, s: str, p:str)-> bool:

        # Top-Down Memoization

        cache ={}

        def dfs(i, j):
            if(i,j) in cache:
                return cache[(i, j)]
            if i >=len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False

            match =i< len(s) and (s[j] == p[j] or p[j] == ".")
            if(j+1) < len(p) and p[j+1] == "*":
                cache[(i, j)]=(dfs(i,j + 2) or  # dont use *
                      (match and dfs(i + 1, j))) # use *
                return cache[(i, j)]

            if match:
                cache[(i, j)]= dfs(i + 1, j+1)
                return cache[(i, j)]
                
            return False
        return dfs(0,0)