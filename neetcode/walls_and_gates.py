from collections import deque
from typing import List
"""
You are given an m*n grid rooms initialized with these three possible values.

* -1 A wall or an obstacle.
* 0 A gate
* INF Infinity means an empty room. We use the value 2^31 - 1 = 2147483647 to represent INF
as you may assume that the distance to a gate is less than 2147483647.

Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate,
it should be filled with INF.

task                                                        solution

[2147483647,    -1,     0,  2147483647]             [3,   -1,   0,   1]
[2147483647,    2147483647,2147483647,-1]           [2,    2,   1,  -1]    
[2147483647,    -1,2147483647,  -1]                 [1,    -1,  2,  -1]
[0, -1, 2147483647,       2147483647]               [0,    -1,  3,   4]

Input: rooms =[[2147483647, -1, 0,2147483647],[2147483647,2147483647,2147483647,-1],
[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
Output: [[3,-1,0,1],[2,2,1,-1],[1,-1, 2,-1],[0,-1,3,4]]

BFS - time O(m*n) | memory O(m*n)

"""
class Solution:

    def wallsAndGates(self, rooms: List[List[int]])->None:
        ROWS, COLS = len(rooms), len(rooms[0])
        visit = set()
        q = deque()

        def addRoom(r, c):
            if(r < 0 or r == ROWS or c < 0 or c == COLS or 
            (r, c) in visit or rooms[r][c] == -1):
                return
            visit.add((r, c))
            q.append([r, c])

        # add gates first(start at the gates)
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))
        
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                rooms[r][c] =dist

                addRoom(r + 1, c)
                addRoom(r - 1, c)
                addRoom(r, c + 1)
                addRoom(r, c - 1)

            dist += 1
