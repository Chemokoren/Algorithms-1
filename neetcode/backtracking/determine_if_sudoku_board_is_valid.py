"""
Determine if a 9 * 9 sudoku board is valid

Only the filled cells need to be validated according to the following rules:
- Each row must contain the digits 1-9 without repetition
- Each column must contain the digits 1-9 without repetition
- Each of the nine 3 * 3 sub-boxes of the grid must contain the digits 1-9 without
repetition

Note: 
- A Sudoku board(partially filled) could be valid but is not necessarily solvable
- Only the filled cells to be validated according to the mentioned rules.

Example 1:

5   3   .   .   7   .   .   .   .

6   .   .   1   9   5   .   .   .

.   9   8   .   .   .   .   6   .

8   .   .   .   6   .   .   .   3

4   .   .   8   .   3   .   .   1

7   .   .   .   2   .   .   .   6

.   6   .   .   .   .   2   8   .

.   .   .   4   1   9   .   .   5

.   .   .   .   8   .   .   7   9


"""
import collections
from typing import List
class Solution:
    
    def isValidSudoku(self, board: List[List[str]])->bool:
        
        cols    = collections.defaultdict(set)
        rows    = collections.defaultdict(set)
        squares = collections.defaultdict(set) # key =(r/3, c/3)
        
        for r in range(0,9):
            for c in range(0,9):
                if r >= len(board) or c >= len(board[0]):
                    print(f"Index out of range: ({r}, {c})")
                    return False
                
                if board[r][c] == ".":
                    continue
                if(board[r][c] in rows[r] or 
                   board[r][c] in cols[c] or 
                   board[r][c] in squares[(r//3, c//3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        return True
        
board =[["5",  "3",   ".",   ".",   "7",   ".",   ".",   ".",   "."],
        ["6",   ".",   ".",   "1",   "9",   "5",   ".",   ".",   "."],
        [".",   "9",   "8",   ".",   ".",   ".",   ".",   "6",   "."],
        ["8",   ".",   ".",   ".",   "6",   ".",   ".",   ".",   "3"],
        ["4",   ".",   ".",   "8",   ".",   "3",   ".",   ".",   "1"],
        ["7",   ".",   ".",   ".",   "2",   ".",   ".",   ".",   "6"],
        [".",   "6",   ".",   ".",   ".",   ".",   "2",   "8",   "."],
        [".",   ".",   ".",   "4",   "1",   "9",   ".",   ".",   "5"],
        [".",   ".",   ".",   ".",   "8",   ".",   ".",   "7",   "9"]]

# board =[["5"   "3"   "."   "."   "7"   "."   "."   "."   "."],
#         ["6"   "."   "."   "1"   "9"   "5"   "."   "."   "."],
#         ["."   "9"   "8"   "."   "."   "."   "."   "6"   "."],
#         ["8"   "."   "."   "."   "6"   "."   "."   "."   "3"],
#         ["4"   "."   "."   "8"   "."   "3"   "."   "."   "1"],
#         ["7"   "."   "."   "."   "2"   "."   "."   "."   "6"],
#         ["."   "6"   "."   "."   "."   "."   "2"   "8"   "."],
#         ["."   "."   "."   "4"   "1"   "9"   "."   "."   "5"],
#         ["."   "."   "."   "."   "8"   "."   "."   "7"   "9"]]

sol =Solution()
print(sol.isValidSudoku(board))