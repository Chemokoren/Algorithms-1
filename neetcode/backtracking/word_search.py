from typing import List
"""
Word Search

Given an m*n grid of characters board and a string word, return true if word exists in the
grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent 
cells are horizontally or vertically neighboring.

The same letter cell may not be used more than once.

Example 1:

A   B   C   E

S   F   C   S

A   D   E   E



Input: board =[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
Output: true

Use recursive backtracking (DFS)

Timing for running through the entire board is O(n*m)

time complexity is O(n*m*dfs) because we are calling the dfs function every single time for
every position in the board
time complexity of dfs' callstack is len(word)
because we are calling dfs 4 times
O(n*m*dfs) 4^len(word) is equivalent to O(n*m*4^n)

"""
# O(n*m*4^word(len)) time 
class Solution:
    """ word search implementation """

    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Check if word exists in the given board.
        
            Parameters:
                board(List[List[str]]): 2D board with a List of string Lists
                word(str) : string word to be searched
            
            Return:
                bool : True or False if it does not exist
        
        """
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, i): 
            """ 
            Returns True if current character is in the board.
            
                Parameters:
                    r(int): integer representing the rows
                    c(int): integer representing the columns
                    i(int): current character within our target word
                    
                Returns:
                    res(Bool): True or False if the character does not exist in the board
            """
            # if we ever find the word, return true
            if i == len(word):
                return True
            
            # check the boundaries
            if(r< 0 or c < 0 or 
               r >= ROWS or 
               c >= COLS or 
               word[i] != board[r][c] or 
               (r, c) in path):
                return False
            
            path.add((r, c))
            res =(dfs(r + 1, c, i + 1) or 
                  dfs(r - 1, c, i + 1) or
                  dfs(r, c + 1, i + 1) or
                  dfs(r, c -1, i + 1))
            
            # backtrack
            path.remove((r, c)) 
   
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0): return True
        return False
        
board =[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]

sol = Solution()
print("ABCCED ::",sol.exist(board, "ABCCED"))
print("SCEDA ::", sol.exist(board, "SCEDA"))
print("ANII ::", sol.exist(board, "ANII"))
