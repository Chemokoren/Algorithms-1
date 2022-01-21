"""
Splitting a string into descending consecutive values

You are given a string s that consists of only digits.

Check if we can split s into two or more non-empty substrings such that the numerical values
of the substrings are in descending order and the difference between numerical values of
every two adjacent substrings is equal to 1.

For example, the string s ="0090089" can be split into ["0090","089"] with numerical values
[90,89]. The values are in descending order and adjacent values differ by 1, so this way is 
valid.

Another example, the string s="001" can be split into ["0","01"], ["00","1"] or ["0","0","1"]
However, all the ways are invalid because they have numerical values [0,1], [0,1] and
[0,0,1] respectively, all of which are not in descending order.

Return true if it is possible to split  s as described abov, or false otherwise.

A substring is a contiguous sequence of characters in a string.

"""

class Solution:

    def splitString(self, s:str)->bool:

        def dfs(index, prev):
            if index == len(s):
                return True
            for j in range(index, len(s)):
                val =int(s[index:j+1])
                if val + 1 == prev and dfs(j + 1, val): #  if part 1 of and is true then execute the second part
                    return True
            return False

        for i in range(len(s) -1):
            val = int(s[:i+1])
            if dfs(i+1, val): return True
        return False

s = "0090089"
# s = "001"
sol = Solution()
print(sol.splitString(s))