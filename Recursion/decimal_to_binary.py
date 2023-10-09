"""
20 // 2   10 rem = 0
10 // 2    5 rem = 0
5 // 2     2 rem = 1
2 // 2     1 rem = 0
1 // 2     0 rem = 1

"""
import unittest

class Solution:
    res =[]

    def decimal_to_binary(self, num):
        
        if num == 0:
            sol =Solution.res[::-1]
            second =''.join(str(item) for item in sol)
            return second
        
        Solution.res.append(num % 2)
        return self.decimal_to_binary(num//2)

class TestDecimalToBinary(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.sol= Solution()

    def test_decimal_to_binary(self):
        self.assertEqual("10100", self.sol.decimal_to_binary(20))
if __name__=="__main__":
    unittest.main()