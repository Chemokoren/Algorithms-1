"""
Perfect Squares

Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the
product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 
3 and 11 are not.

Input: n = 12
Output: 3
Explanation: 12 = 4+4+4

Example 2:

Input: n = 13
Output: 2
Explanation: 13 =4 + 9

"""
import unittest

class Solution:

    # time complexity: O(n * n^1/2)
    def num_squares(self, n: int)->int:
        dp =[n] * (n + 1)
        dp[0] = 0

        for target in range(1, n+1):
            for s in range(1, target + 1):
                square = s * s

                if target - square < 0:
                    break
                dp[target] = min(dp[target], 1 + dp[target -square])
        return dp[n]

class TestPerfectSquare(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.sol =Solution()

    def test_perfect_squares(self):
        self.assertEqual(3, self.sol.num_squares(12))

if __name__=="__main__":
    unittest.main()