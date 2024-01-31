"""
Pascal's Triangle

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of two numbers directly above it as shown.

                                1
                            1       1
                        1       2       1
                    1       3       3       1
                1       4       6       4       1

Example 1:

Input: numRows = 5
Output: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]




"""
from typing import List
import unittest

class Solution:

    def generate(self, numRows: int) -> List[List[int]]:
        res =[[1]]

        for i in range(numRows-1): # we have built the first 1 above
            temp = [0] + res[-1] + [0]
            row =[]
            for j in range(len(res[-1]) + 1): # len of previous row +1
                row.append(temp[j] + temp[j +1])
            res.append(row)
        return res


class TestPascalsTriangle(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.sol = Solution()
        self.output =[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

    def test_pascals_triangle(self):
        self.assertEqual(self.output, self.sol.generate(5))

if __name__=="__main__":
    unittest.main()