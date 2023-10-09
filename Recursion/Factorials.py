"""
what factorial(4) means
factorial(4) = 4 * factorial(3)
factorial(4) = 4 * 3 * factorial(2)
factorial(4) = 4 * 3 * 2 * factorial(1)  # we know factorial(1) is 1
factorial(4) = 4 * 3 * 2* 1 # replace factorial(1) with 1
factorial(4) = 4 * 3 * 2 # replace factorial(2) with 2
factorial(4) = 4 * 6  # replace factorial(3) with 6
factorial(4) = 24 # replace factorial(4) with 24
"""
import unittest

class Solution:

    def iterative_factorial(self,n: int)->int:
        result =1
        for i in range(1,n+1):
            result *= i
            print("aa:: {} {}".format(i, result))
        return result

    def recursive_factorial(self, n:int)->int:
        if n==1:
            return 1
        else:
            return n * self.recursive_factorial(n-1)

class TestFactorials(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.sol =Solution()

    def test_iterative_factorial(self):
        self.assertEqual(24, self.sol.iterative_factorial(4))

    def test_recursive_factorial(self):
        self.assertEqual(24, self.sol.recursive_factorial(4))

if __name__== "__main__":
    unittest.main()
