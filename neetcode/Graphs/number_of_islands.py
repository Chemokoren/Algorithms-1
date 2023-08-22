from typing import List
import collections
"""
Number of Islands

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island
is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
"""
def numIslands(self, grid: List[List[str]])->int:
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    visit =set()
    islands = 0

    
    def bfs(r, c):
        q = collections.deque()
        visit.add((r,c))
        q.append((r,c))

        while q:
            row, col = q.popleft() # if you just pop then the most recent item is removed -dfs
            directions =[[1,0],[-1,0],[0,1],[0,-1]]

            for dr, dc in directions:
                r, c = row + dr, col + dc
                if(r in range(rows) and
                  c in range(cols) and
                  grid[r][c]== "1" and
                  (r,c) not in visit):
                  q.append((r,c))
                  visit.add((r,c))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "a" and (r, c) not in visit:
                bfs(r, c)
                islands += 1
    return islands