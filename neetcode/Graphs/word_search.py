"""

Given an m*n grid of characters board and a string word, return true if word exists in the
grid.

The word can be constructed from letters of sequentially djacent cells, where adjacent cells
are horiontally or vertically neighboring. The same letter cell may not be used more than once.


Input: board =[["A","B","C","E"],["S", "F","C","S"],["A","D","E","E"]],
word = "ABCCED"
Output: True
"""

from typing import List
class Solution:

    # O(n * m * dfs) where dfs =4^(len(word))
    def exist(self, board: List[List[str]], word:str)->bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            if(r < 0 or c < 0 or r >= ROWS or c >= COLS or
               word[i] != board[r][c] or
               (r, c) in path):
                return False
            path.add((r, c))
            res =(dfs(r+1, c, i+1) or \
                 dfs(r-1, c, i +1) or \
                 dfs(r, c + 1, i + 1) or\
                    dfs(r, c -1, i + 1)
                )
            path.remove((r, c))
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0): return True
        return False

import unittest
class TestWordSearch(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_sample_word_search(self):
        board =[["A","B","C","E"],["S", "F","C","S"],["A","D","E","E"]]
        word = "ABCCED"
        self.assertEqual(self.solution.exist(board, word), True)

if __name__=="__main__":
    unittest.main()