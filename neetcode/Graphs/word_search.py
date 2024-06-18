"""

Given an m*n grid of characters board and a string word, return true if word exists in the
grid.

The word can be constructed from letters of sequentially djacent cells, where adjacent cells
are horiontally or vertically neighboring. The same letter cell may not be used more than once.


Input: board =[["A","B","C","E"],["S", "F","C","S"],["A","D","E","E"]],
word = "ABCCED"
Output: True


This code implements a solution to the classic "Word Search" problem. 
It takes a board (represented as a 2D list of characters) and a word as input and determines 
if the word can be formed by connecting characters on the board.

The code systematically explores all possible paths on the board using depth-first search (dfs).
It keeps track of visited cells to avoid redundant exploration and ensures that the word is 
formed by connecting consecutive characters on the board.

Here's a breakdown of the code:

Class and Function:

Inside the Solution class, there's a function called exist that returns a boolean value 
indicating whether the word can be formed on the board (True) or not (False).

Time and Space Complexity:

Time Complexity:

In the worst case scenario, the time complexity can be exponential, reaching O(n * m * 4^w), 
where:
    n: Number of rows in the board.
    m: Number of columns in the board.
    w: Length of the word being searched for.

The nested loops iterate through all cells (O(n * m)).
For each cell, the dfs function explores all possible paths in the worst case, leading to a 
branching factor of 4 and a depth of exploration up to w.
Combining these factors, the worst-case time complexity becomes O(n * m * 4^w).

This exponential complexity occurs only in the worst-case scenario where the word perfectly fits
on the board and the search needs to explore all possible paths. In many practical cases,
the actual time complexity might be much lower, especially if the word doesn't fit easily on 
the board or is not present at all.

Space Complexity:

    The space complexity of the code is primarily due to the recursive calls in the dfs function.
    In the worst case, the depth of the recursion can be as high as the length of the word (w).
    Each recursive call adds a frame to the call stack, which requires additional memory.

Therefore, the space complexity can be considered O(w) in the worst case, proportional to the
depth of the recursion.


Codewalkthrough

Base Case:

    If i (character index) reaches the length of the word (len(word)), it means the entire word
    has been found on the board, so the function returns True.

Recursive Checks:

The function checks various conditions before proceeding with the search:
    - If the current position is out of bounds of the board (less than 0 or greater than 
    dimensions), it returns False.
    -If the character at the current position on the board doesn't match the character being 
    searched for (word[i]), it returns False.
    -If the current position has already been visited in the current path (checked using
    the path set), it returns False to avoid revisiting the same cell.

Recursive Calls:

    If the checks pass, the function adds the current position to the path set to mark it as
    visited.
    It then performs four recursive calls, exploring possibilities in all four directions
    (up, down, left, right) by incrementing/decrementing the row (r) and column (c) indices and
    incrementing the character index (i).
    The or operator ensures that the function returns True as soon as the word is found in 
    any of the explored directions.

Backtracking and Removing Visited Cell:

After the recursive calls, the current position is removed from the path set using 
path.remove((r, c)) to allow backtracking if none of the directions lead to the complete word.
Finally, the function returns the combined result of the recursive calls (res).

Main Loop:

    The code iterates through each cell of the board using nested loops for rows (r) and
    columns (c).
    If the dfs function starting from the current cell (r, c) returns True, it means the
    word has been found, and the function returns True.



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

"""

These tests cover various scenarios:

    Existing word on the board.
    Non-existent word.
    Word length exceeding board dimensions.
    Word formed diagonally.
    Testing edge cases, like empty boards, single-letter words, or repeated characters in
     the word.

By implementing these unit tests, you can ensure that the code functions as expected and 
identify potential issues with accuracy or unexpected behavior. 

Remember that unit tests primarily focus on the correctness of the implemented logic, 
and a separate analysis might be needed for in-depth performance evaluation.

"""
import unittest
class TestWordSearch(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_empty_board(self):
        board = []
        word = "ABCCED"
        assert self.solution.exist(board, word) == False  # Empty board cannot contain any word

    def test_single_letter_word(self):
        board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
        ]
        word = "A"
        assert self.solution.exist(board, word) == True  # Single letter word can be found

    def test_repeated_characters(self):
        board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'A', 'E', 'E']
        ]
        word = "AA"
        solution = Solution()
        assert solution.exist(board, word) == True  # Repeated characters allowed

    def test_word_with_same_character(self):
        board = [
        ['A', 'A', 'A', 'A'],
        ['A', 'A', 'A', 'A'],
        ['A', 'A', 'A', 'A']
        ]
        word = "AAAA"
        solution = Solution()
        assert solution.exist(board, word) == True  # Word formed from same character

    def test_word_not_formed_by_consecutive_chars(self):
        board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
        ]
        word = "ABCE"  # Characters not consecutive on board
        solution = Solution()
        assert solution.exist(board, word) == False


    def test_sample_word_search(self):
        board =[["A","B","C","E"],["S", "F","C","S"],["A","D","E","E"]]
        word = "ABCCED"
        self.assertEqual(self.solution.exist(board, word), True)

    def test_existing_word(self):
        board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
        ]
        word = "ABCCED"
        solution = Solution()
        assert solution.exist(board, word) == True  # Word exists

    def test_non_existing_word(self):
        board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
        ]
        word = "QWERTY"
        print(f":: {self.solution.exist(board, word)}")
        self.assertFalse(self.solution.exist(board, word), False)
        # assert self.solution.exist(board, word) == False  # Word doesn't exist

    def test_word_out_of_bounds(self):
        board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
        ]
        word = "ABCDEF"
        assert self.solution.exist(board, word) == False  # Word too long for board

    def test_diagonal_word(self):
        board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
        ]
        word = "SEE"
        assert self.solution.exist(board, word) == True  # Test diagonal search

if __name__=="__main__":
    unittest.main()