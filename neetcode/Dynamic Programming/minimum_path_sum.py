"""
Maximum Path Sum

Given a m*n grid filled with non-negative numbers, find a path from top left to bottom 
right, which minimizes the sum of all numbers along its path.

Note: you can only move eiher down or right at any point in time.

Example 1:


1   3   1

1   5   1

4   2   1

Input: grid =[[1, 2, 1], [1, 5, 1], [4, 2, 1]]
Output: 7
Explanation: Bexause the path 1->3->1->1->1 minimizes the sum
"""
from typing import List
import unittest

class Solution:

    def minimum_path_sum(self, grid: List[List[int]])->int:
        ROW, COL =len(grid), len(grid[0])

        res =[[ float("inf") for i in range(COL +1)] for i in range(ROW +1)]
        res[ROW-1][COL] =0
       

        for i in range(ROW-1 , -1, -1):
            for j in range(COL-1, -1, -1):
                res[i][j] =grid[i][j]+ min(res[i][j+1], res[i+1][j])
        
        return res[0][0]
    

    def minPathSum(self, grid: List[List[int]])-> int:

        ROWS, COLS = len(grid), len(grid[0])

        res =[[float("inf")] *(COLS +1) for r in range(ROWS +1)]
        res[ROWS -1][COLS] = 1

        for r in range(ROWS-1, -1, -1):
            for c in range(COLS-1, -1, -1):
                res[r][c] = grid[r][c] + min(res[r+1][c],  res[r][c+1])
        return res[0][0]
    



class TestMinimumPathSum(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.sol = Solution()
        self.grid =[[1, 2, 1], [1, 5, 1], [4, 2, 1]]

    def test_minimum_path_sum(self):
        self.assertEqual(5, self.sol.minimum_path_sum(self.grid))

if __name__=="__name__":
    unittest.main()