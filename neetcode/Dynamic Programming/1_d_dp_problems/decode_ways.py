"""
A message containing letters from A-Z can be encoded into numbers using the following 
mapping:

'A' -> '1'
'B' -> '2'

...
'z' -> '26'

To decode an encoded message, all the digits must be grouped then mapped back into letters
using the reverse of the mapping above(there may be multiple ways). For example, "11106"
can be mapped into:
"AAJF" with the grouping (1    1    10      6)
"KJF" with the grouping  (11     10      6)

Note that the grouping (1       11      06) is invalid because "06" cannot be mapped into 
'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The answer is guaranteed to fit in a 32-bit integer.

Example 1:

Input: s ="12"
Output: 2
Explanation: "12" could be decoded as "AB" (1       2)  or "L"  (12)

{
"1":"A",
"2":"B",
"3":"C",
"4":"D",
"5":"E",
"6":"F",
"7":"G",
"8":"H",
"9":"I",
"10":"J",
"11":"K",
"12":"L",
"13":"M",
"14":"N",
"15":"O",
"16":"P",
"17":"Q",
"18":"R",
"19":"S",
"20":"T",
"21":"U",
"22":"V",
"23":"W",
"24":"X",
"25":"Y",
"26":"Z",
}

            12                          121                             12131
            / \                         /  \                            /      \
           1   12                      1    12                         1        12
          /                           / \     \                       / \       /  \
         2                           2   21     1                    2   21    1    13 
                                    /                               / \   /   /      \
                                   1                               1   13 3    3       1
                                                                  / \  |  |    |
                                                                 3     1  1    1 
                                                                / \
                                                               1  
"""
class Solution:

    def numDecodings(self, s: str)-> int:

        dp ={len(s) : 1}

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] =="0":
                return 0
            
            res = dfs(i + 1)
            if(i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456"))):
                res += dfs(i + 2)
            dp[i] = res
            return res
        return dfs(0)
    
    def num_decodings_dp(self, s: str)->int:
        dp ={len(s): 1}

        for i in range(len(s) -1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i +1]

            if(i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456"))):
                dp[i] += dp[i + 2]
        return dp[0]

        
sol = Solution()
print(sol.numDecodings("12"))
print(sol.numDecodings("12131"))

print("----------")

print(sol.num_decodings_dp("12"))
print(sol.num_decodings_dp("12131"))

print("----------")

print(sol.num_decodings_dp("11106"))
print(sol.numDecodings("11106"))



