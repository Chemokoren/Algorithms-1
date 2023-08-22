from typing import List
from collections import deque
"""
Snakes and Ladders

You are given an n * n integer matrix board where the cells are labeled from 1 to n^2 in a 
Boustrophedon style starting from the bottom left of the board(i.e. board[n-1][0]) and 
alternating direction each row.

You start on square 1 of the board. In each move, starting from square curr, do the following:
- Choose a destination square next with a label in the range[curr + 1, min(curr + 6, n^2)]
    - This choice simulates the result of a standard 6-sided die roll: i.e., there are always 
    at most 6 destinations, regardless of the size of the board.
- If next has a snake or ladder, you must move to the destination of that snake or ladder.
Otherwise, you move to next .
-The game ends when you reach the square n^2.

A board square on row r and column c has a snake or ladder if board[r][c] != -1. The 
destination of that snake or ladder is board[r][c]. Squares 1 and n^2 do not have a snake or 
ladder.

Note that you only take a snake or ladder at most once per move. If the destination to a 
snake or ladder is the start of another snake or ladder, you do not follow the subsequent snake 
or ladder.

- For example suppose the board is [[-1, 4], [-1,3]], and on the first move, your destination
square is 2. You follow the ladder to square 3, but do not follow the subsequent ladder to 4.

Return the least number of moves required to reach the square n^2. If it is not possible to
reach the square return -1.

Example 1:

[36, 35, 34, 33, 32, 31],
[25, 26, 27, 28, 29, 30],
[24, -1, 22, 21, 20, 19],
[13, 14, 15, 16, 17, 18],
[12, 11, 10,  9,  8, -7],
[1,  2,  3,   4,  5,  6]


Input: board [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],
[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,15,-1,-1,-1]]
Output: 4

Explanation:
In the beginning, you start at square 1 (at row 5, column 0).
You decide to move to square 2 and must take the ladder to square 15.
You then decide to move to square 17 and must take the snake to square 13.
You then decide to move to square 14 and must take the ladder to square 35.
You then decide to move to square 36, ending the game.
This is the lowest possible number of moves to reach the last square, so return 4.

"""

class Solution:

    def snakesAndLadders(self, board: List[List[int]])->int:
        length = len(board)
        board.reverse()

        def intToPos(square):
            r =(square -1) // length
            c =(square -1) % length
            if r % 2:
                c = length -1-c
            return [r, c]

        q = deque()

        q.append([1,0]) # [square, moves]
        visit =set()
        while q:
            square, moves = q.popleft()
            for i in range(1,7):
                nextSquare = square + i
                r, c = intToPos(nextSquare)
                if board[r][c] != -1:
                    nextSquare = board[r][c]
                
                if nextSquare == length * length:
                    return moves + 1

                if nextSquare not in visit:
                    visit.add(nextSquare)
                    q.append([nextSquare, moves+1])

        return -1

board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],
[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,15,-1,-1,-1]]

sol = Solution()
print(sol.snakesAndLadders(board))
