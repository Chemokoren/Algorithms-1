import unittest

class Solution:


    def fib(self, num):
        if num == 0 or num == 1:
            return num
        return self.fib(num -1) + self.fib(num -2)
    
    def fib_top_down(self, num):
        dp={0:0,1:1}
        if num in dp:
            return dp[num]
        res = self.fib(num -1) + self.fib(num -2)
        dp[num] =res
        return dp[num]

    def fib_bottom_up(self, num):
        dp={0:0,1:1}
        if num in dp:
            return dp[num]
        
        for i in range(2, num+1):
            res = dp[i-1] + dp[i-2]
            dp[i] =res
        return dp[num]

class TestFibonacci(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.sol  = Solution()

    def test_fib(self):
        self.assertEqual(8, self.sol.fib(6))

    def test_fib_top_down(self):
        self.assertEqual(8, self.sol.fib_top_down(6))

    def test_fib_bottom_up(self):
        self.assertEqual(8, self.sol.fib_bottom_up(6))

if __name__=="__main__":
    unittest.main()