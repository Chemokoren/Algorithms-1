"""
Decode Ways

A message containing letters from A-Z can be encoded into numbers using the following 
mapping:
'A' -> "1"
'B' -> "2"

...

'Z' -> "26"

To decode an encoded message, all the digits must be grouped then mapped back into letters
using the reverse of the mapping above(there may be multiple ways). For example, "11106"
can be mapped into:
- "AAJF" with the grouping (1  1  10  6)
- "KJF" with the grouping (11  10  6)

Note that the grouping (1  11  06) is invalid because "06" cannot be mapped into 'F' since
"6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The answer is guaranteed to fit in a 32-bit integer.

Example 1:

Input: s ="12"
Output: 2
Explanation: "12" could be decoded as "AB" (1  2) or "L" (12)
"""

# map={
#     "A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,
#     "O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26,
#     }
import unittest

class Solution:

    # bottom-up dp
    def dp_num_decodings(self, s: str)-> int:
        dp ={len(s) : 1}
        
        for i in range(len(s)-1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i+1]
            if (i +1 < len(s) and (s[i] == "1" or 
                    s[i] =="2" and s[i + 1] in "0123456" )):
                dp[i] += dp[i + 2]
        return dp[0]


    # memoization
    def numDecodings(self, s:str)-> int:

        dp ={len(s) : 1}

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] =="0":
                return 0
            
            res = dfs(i + 1)
            if(i + 1 < len(s) and (s[i] =="1" or
                s[i] == "2" and s[i + 1] in "0123456")):
                res += dfs(i +2)
            dp[i] = res
            return res
        return dfs(0)
    
# print(Solution().numDecodings("12"))

class TestDecodeWays(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.sol =Solution()

    def test_decode_ways(self):
        self.assertEqual(2, self.sol.numDecodings("12"))
        # bottom up dp
        self.assertEqual(2, self.sol.dp_num_decodings("12"))


if __name__=="__main__":
    unittest.main()