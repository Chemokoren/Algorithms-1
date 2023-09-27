"""
Counting Bits

Given an integer n, return an array ans of length n + 1 such that for each i(0 <= i <=n),
ans[i] is the number of 1's in the binary representation of i.

Example 1:

Input: n = 2
Output: [0, 1, 1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
"""
from typing import List
import unittest

class Solution:

    def countBits(self, n: int)-> List[int]:
        dp =[0] * (n + 1)
        offset =1 

        for i in range(1, n + 1):
            if offset *2 ==i:
                offset =i
            dp[i] = 1 + dp[i -offset]
        return dp
    

class TestCountingBits(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.sol = Solution()

    def test_counting_bits(self):
        self.assertEqual([0, 1, 1], self.sol.countBits(2))

if __name__=="__main__":
    unittest.main()