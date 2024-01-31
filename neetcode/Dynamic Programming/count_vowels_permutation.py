"""
Count Vowels Permutation

Given an integer n, your task is to count how many strings of length n can be formed
under the following rules:

- Each character is a lower case vowel('a','e','i','o','u')
- Each vowel 'a' may only be followed by an 'e'.
- Each vowel 'e' may only be followed by an 'a' or an 'i'.
- Each vowel 'i' may not be followed by another 'i'
- Each vowel 'o' may only be followed by an 'i' or a 'u'
- Each vowel 'u' may only be followed by an 'a'

Since the answer may be too large, return it modulo 10^9 + 7.

Example 1:

Input: n = 1
Output: 5
Explanation: All possible strings are : "a", "e", "i", "o" and "u".


"""

class Solution:

    def countVowelPermutation(self, n:int)-> int:
        # dp[j][c] = num of strs of len=j
        # where last char is c:
        dp =[[], [1, 1, 1, 1, 1]]

        a, e, i, o, u = 0, 1, 2, 3, 4
        mod = 10**9 + 7

        for j in range(2, n + 1):
            dp.append([0, 0, 0, 0, 0])

            dp[j][a] = (dp[j-1][e] + dp[j-1][i] + dp[j-1][u]) % mod
            dp[j][e] = (dp[j-1][a] + dp[j-1][i]) % mod
            dp[j][i] = (dp[j-1][e] + dp[j-1][o]) % mod
            dp[j][o] = (dp[j-1][i])
            dp[j][u] = (dp[j-1][i] + dp[j-1][o]) % mod
        return sum(dp[n]) % mod
    
sol =Solution()
print(sol.countVowelPermutation(1))