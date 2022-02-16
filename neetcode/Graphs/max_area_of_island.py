from typing import List
"""
Max area of island

You are given an m*n binary matrix grid. An island is a group of 1's (representing land)
connected 4-directionally (horizontal or vertical). You may assume all four edges of the grid
are surrounded by water. The area of an island is the number of cells with a value 1 in the
island.
Return the maximum area of an island in grid. If there is no island, return 0.

grid =[[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
[0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
[0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

time : O(m*n) | space: O(m*n) because we have a hashset which could contain every single cell
in the grid in the worst case
"""
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]])->int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):
            if(r < 0 or r == ROWS or c < 0 or c == COLS or grid[r][c] == 0 or (r, c) in visit):
                return 0
            visit.add((r, c))
            return ( 1 + dfs(r+1, c)+
                    dfs(r -1, c)+
                    dfs(r, c+1)+
                    dfs(r, c-1))

        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                area = max(area, dfs(r,c))
           
        return area

grid =[[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
[0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
[0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
sol = Solution()
print(sol.maxAreaOfIsland(grid))