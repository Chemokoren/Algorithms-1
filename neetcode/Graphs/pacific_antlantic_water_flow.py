from typing import List
"""
You are given an m*n integer matrix heights representing the height of each unit cell
in a continent. The Pacific ocean touches the continent left and top edge and the Atlantic 
ocean touches the continent's right and bottom edges.
Water can only flow in four directions:up, down, left, and right. Water flows from a cell to
an adjacent one with an equal or lower height.

Return a list of grid coordinates where water can flow to both Pacific and Atlantic oceans

                Pacific ocean
                1   2   2   3   5

Pacific         3   2   3   4   4       Atlantic

ocean           6   7   1   4   5       ocean

                5   1   1   2   4

                Atlantic ocean

Input: heights =[[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]

Time: O(N.M)^2 


"""
class Solution:

    def pacificAtlantic(self, heights: List[List[int]])-> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r,c, visit, prevHeight):
            if((r, c) in visit or 
             r<0 or c < 0 or r == ROWS or r == COLS or
             heights[r][c] < prevHeight):
             return
            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

            for c in range(COLS):
                dfs(0,  c, pac, heights[0][c])
                dfs(ROWS-1, c, atl, heights[ROWS - 1][c])

            for r in range(ROWS):
                dfs(r, 0, pac, heights[r][0])
                dfs(r, COLS -1, atl, heights[r][COLS -1])

            res =[]
            for r in range(ROWS):
                for c in range(COLS):
                    if(r,c) in pac and (r,c) in atl:
                        res.append([r,c])
            return res
