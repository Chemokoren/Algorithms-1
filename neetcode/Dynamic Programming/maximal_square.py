"""
Maximal Square

Given an m*n binary matrix filled with 0's and 1's, find the largest square containing 
only 1's and return its area.

Example 1:

1   0   1   0   0

1   0   1   1   1

1   1   1   1   1

1   0   0   1   0

Input: matrix =[["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"],
["1", "0", "0", "1", "0"]]
Output: 4
"""
from typing import List
import unittest

class Solution:

    # time complexity: O(m*n), space complexity: O(m*n)
    def maximal_square(self, matrix: List[List[str]])-> int:

        # dp : bottom up
        # recursive: top down

        ROWS, COLS = len(matrix), len(matrix[0])
        cache ={} # map each (r, c) -> maxLength of square

        def helper(r, c):
            if r >= ROWS or c >= COLS:
                return 0
            
            if (r, c)  not in cache:
                down = helper(r + 1, c)
                right = helper(r, c + 1)
                diag = helper(r + 1, c + 1)

                cache[(r, c)] = 0
                if matrix[r][c] =="1":
                    cache[(r, c)] = 1 + min(down, right, diag)

            return cache[(r, c)]
        helper(0, 0)
        return max(cache.values()) ** 2
    

matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"],
["1", "0", "0", "1", "0"]]

class TestMaximalSquare(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.sol = Solution()

    def test_maximal_square(self):
        self.assertEqual(4, self.sol.maximal_square(matrix))


if __name__=="__main__":
    unittest.main()