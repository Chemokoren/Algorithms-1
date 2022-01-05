"""
Edit Distance

Given two strings word1 and word2, return the minimum number of operations required to convert word1
to word2.
You have the following three operations permitted on a word:
- insert a character
- delete a character
- replace a character

Example 1:
Input: word1 ="horse", word2="ros"
Output: 3
Explanation:
horse->rorse(replace 'h' with 'r')
rorse->rose(remove 'r')
rose ->ros (remove 'e')
"""

class Solution:
    def minDistance(self, word1: str, word2:str)->int:
        cache =[[float("inf")] * (len(word2)+1) for i in range(len(word1)+1)]

        for j in range(len(word2)+1):
            cache[len(word1)][j] =len(word2) - j
        for i in range(len(word1)+1):
            cache[i][len(word2)] = len(word1) - i

        for i in range(len(word1)-1, -1, -1):
            for j in range(len(word2) -1, -1, -1):
                if word1[i] == word2[j]:
                    cache[i][j] = cache[i + j][j + 1]
                else:
                    cache[i][j] =1 + min(cache[i+1][j], cache[i][j+1], cache[i+1][j+1])
        return cache[0][0]

word1 ="horse"
word2 ="ros"

sol = Solution()
print(sol.minDistance(word1, word2))