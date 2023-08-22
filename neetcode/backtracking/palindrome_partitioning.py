from typing import List
"""
Given a string s, partition s such that every substring of the partition is a palindrome.
Return all possible palindrome partitioning  of s.

A palindrome string is a string that reads the same backward as forward.

Example 1:
Input s ="aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:
Input s ="a"
Output: [["a"]]


                            [a,a,b]
                            /  |    \
                        [a]   [a,a]  [a,a,b]X
                       / \      |
                    [a]  [a,b]X [b]
                   /
                 [b]    
"""
class Solution:
    """palindrome partitioning implementation"""

    def partition(self, s:str)->List[List[str]]:
        """ 
        Return all possible palindrome partitioning  of s
        
            Parameters:
                s(str): string to be partitioned
            
            Returns:
                res(List[List[str]]) : List of lists containing strings 
        """
        res =   []
        part =  []

        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return
            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    part.append(s[i:j+1])
                    dfs(j + 1) # the next character
                    part.pop()
                    

        dfs(0)
        return res

    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
        
s ="aab"
sol = Solution()
print(sol.partition(s))



print("\n my tests \n")
'''
my tests
'''
def palindrome_substrings(s):
	res =[]

	for i in range(len(s)):
	
		# even 
		l, r = i, i
		while l>=0 and r<len(s) and s[l] == s[r]:
			res.append([s[l:r+1]])
			l -=1
			r +=1
		# odd
		l, r, = i, i+1
		
		while l>=0 and r<len(s) and s[l] == s[r]:
			res.append([s[l:r+1]])
			l -=1
			r +=1
	return res
	
print(palindrome_substrings("babad"))
print(palindrome_substrings("aab"))
print(palindrome_substrings("a"))
