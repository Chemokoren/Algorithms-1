"""
Longest Increasing Path in Matrix

Given an m*n integers matrix, return the length of the longst increasing path in a matrix.
From each cell, you can either move in four directions; left, right, up, or down. You may 
not move diagonally or move outside the bounday(i.e. wrap-around is not allowed).

Example 1:
9   9   4

6   6   8

2   1   1

Input: matrix =[[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: longest increasing path is [1,2,6,9]

O(n*m) time complexity
"""
from typing import List
class Solution:

    def longestIncreasingPath(self, matrix: List[List[int]]) ->int:
        ROWS, COLS =len(matrix), len(matrix[0])
        dp ={} # (r, c)->LIP

        def dfs(r, c, prevVal):
            if (r < 0 or r == ROWS or c < 0 or c== COLS or matrix[r][c] <=prevVal):
                return 0

            if (r, c) in dp:
                return dp[r, c]

            res =1
            res = max(res, 1 + dfs(r + 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r - 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c + 1, matrix[r][c]))
            res = max(res, 1 + dfs(r, c - 1, matrix[r][c]))
            dp[(r, c)] = res
            return res

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c)
        return max(dp.values())