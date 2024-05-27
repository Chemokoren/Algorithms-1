from typing import List
"""
Count Sub Islands

You are given two m*n binary matrixes grid1 and grid2 containing only o's(representing water)
and 1's (representing land). An island is a group of 1's connected 4-directionally(horizontal
or vertical). Any cells outside of the grid are considered water cells.

An island in grid2 is considered a sub-island if there is an island in grid1 that contains all
the cells that make up this island in grid2. Return the number of islands in grid2 that are
considered sub-islands.

Example 1:

            grid 1                              grid2
    [1, 1,  1,  0,  0]                    [1,   1,  1,  0,  0]
    [0, 1,  1,  1,  1]                    [0,   0,  1,  1,  1]
    [0, 0,  0,  0,  0]                    [0,   1,  0,  0,  0]
    [1, 0,  0,  0,  0]                    [1,   0,  1,  1,  0]
    [1, 1,  0,  1,  1]                    [0,   1,  0,  1,  0]

Input: grid1 =[[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]]
       grid2 =[[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]

Output: 3
Explanation: In the picture above, the grid on the left is grid1 and the grid on the right
is grid2. The 1s colored red in grid2 are those considered to be part of a sub-island. There 
are three sub-islands.
"""
class Solution:

    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]])->int:
        ROWS, COLS = len(grid1), len(grid1[0])
        visit =set()

        def dfs(r,c):
            if(r < 0 or c< 0 or r== ROWS or c == COLS or 
            grid2[r][c] == 0 or (r,c) in visit):
                return True
            visit.add((r, c))
            res = True
            if grid1[r][c] == 0:
                res = False

            res = dfs(r -1, c) and res
            res = dfs(r + 1, c) and res
            res = dfs(r, c- 1) and res
            res = dfs(r, c + 1) and res

            return res

        count = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid2[r][c] and (r,c) not in visit and dfs(r,c):
                    count += 1
        return count