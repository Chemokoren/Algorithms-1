from typing import List
"""
surrounded Regions

Given an m * n matrix board containing 'x' and 'o', capture all regions that are 
4-directionally surrounded by 'x'.

A region is captured by flipping all 'o' s into 'x' s in that surrounded region

Example 1
x   x   x   x               x   x   x   x
x   o   o   x               x   x   x   x
x   x   o   x               x   x   x   x
x   o   x   x               x   o   x   x

Input: board =[["x","x","x","x"],["x","o","o","x"],["x","x","o","x"],["x","o","x","x"]]
Output: [["x","x","x","x"],["x","x","x","x"],["x","x","x","x"],["x","o","x","x"]]

Explanation: Surrounded regions should not be on the border, which means that any 'o' on the
border of the board are not flipped to 'x'. Any 'o'  that is not on the border and it is not 
connected to an 'o' on the border will be flipped to 'x'. Two cells are connected if they
are adjacent cells connected horizontally or vertically.

Solution: Reverse thinking
phrase: capture surrounded regions
Rephrase: capture everything except unsurrounded regions

time: O(n.m)

"""
class Solution:

    def solve(self, board: List[List[str]])->None:
        """
        Do not return anything, modify board in-place instead
        """

        ROWS, COLS = len(board), len(board[0])

        def capture(r, c):
            if(r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != "o"):
                return
            board[r][c] ="T"
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        # 1. (DFS) Capture unsurrounded regions (o -> T)
        for r in range(ROWS):
            for c in range(COLS):
                if(board[r][c] =="o" and 
                (r in [0, ROWS-1] or c in [0, COLS -1])):
                    capture(r,c)

        # 2. Capture surrounded regions (o -> x)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "o":
                    board[r][c] = "x"
        # 3. Uncapture unsurrounded regions(T -> o)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "o"
