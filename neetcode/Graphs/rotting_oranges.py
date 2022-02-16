from collections import deque
from typing import List
"""
Rotting Oranges

You are given an m*n grid where each cell can have one of three values:

- 0 representing an empty cell,
- 1 representing a fresh orange, or
- 2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes
rotten.
Return the minumum number of minutes that must elapse until no cell has a fresh orange. If
this is impossible, return -1.

Minute 0    Minute 1    Minute 2    Minute 3    Minute 4

[2,1,1],    [2,2,1],    [2,2,2],    [2,2,2],    [2,2,2],
[1,1,0],    [2,1,0],    [2,2,0],    [2,2,0],    [2,2,0],
[0,1,1]     [0,1,1]     [0,1,1]     [0,2,1]     [0,2,2]

input:  grid =[[2,1,1],[1,1,0],[0,1,1]]
Output: 4
"""

class Solution:
    def orangesRotting(self, grid: List[List[int]])->int:
        q = deque()
        time, fresh = 0, 0

        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1: # fresh oranges
                    fresh  += 1
                if grid[c][c] == 2: # rotting oranges
                    q.append([r, c])
        
        directions =[[0,1],[0, -1], [1,0],[-1, 0]]
        while q and fresh > 0:

            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    row, col = dr + r, dc+c
                    # if in bounds and fresh, make rotten
                    if(row < 0 or row == len(grid) or col < 0 or col == len(grid[0]) or grid[row][col] != 1):
                        continue
                    grid[row][col] = 2
                    q.append([row, col])
                    fresh -= 1
            time += 1
        return time if fresh == 0 else -1

grid =[[2,1,1],[1,1,0],[0,1,1]]

sol = Solution()
print(sol.orangesRotting(grid))