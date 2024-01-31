"""
Longest Increasing Path in a Matrix

Given an m*n integers matrix, return the length of the longest increasing path 
in a matrix.

From each cell, you can either move in four directions: left, right, up or down. 
You may not move diagonally or move outside the boundary (i.e. wrap-around is not allowed)

Example 1:

9       9       4
^
|
6       6       8
^
|
2  <-   1       1

"""
from typing import List
import unittest

class Solution:

    def longestIncreasingPath(self, matrix: List[List[int]])-> int:

        ROWS, COLS = len(matrix), len(matrix[0])
        dp ={} # (r, c) -> LIP

        def dfs(r, c, prevVal):
            if(r < 0 or r == ROWS or
               c < 0 or c == COLS or
               matrix[r][c] <= prevVal):
                return 0
            if(r, c) in dp:
                return dp[(r, c)]
            
            res = 1
            res = max(res, 1 + dfs(r +1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r -1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c + 1, matrix[r][c]))
            res = max(res, 1 + dfs(r , c - 1, matrix[r][c]))
            dp[(r, c)] = res
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, -1)
        return max(dp.values())

class TestLongestIncreasingPathMatrix(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.sol = Solution()
        self.matrix =[[9, 9, 4], [6, 6, 8], [2, 1, 1]]

    def test_longest_increasing_path_matrix(self):
        self.assertEqual(4, self.sol.longestIncreasingPath(self.matrix))


if __name__=="__main__":
    unittest.main()
