from typing import List
"""
Count Sub Islands

You are given two m*n binary matrixes grid1 and grid2 containing only o's(representing water)
and 1's (representing land). An island is a group of 1's connected 4-directionally(horizontal
or vertical). Any cells outside of the grid are considered water cells.

An island in grid2 is considered a sub-island if there is an island in grid1 that contains all
the cells that make up this island in grid2. Return the number of islands in grid2 that are
considered sub-islands.

Example 1:

            grid 1                              grid2
    [1, 1,  1,  0,  0]                    [1,   1,  1,  0,  0]
    [0, 1,  1,  1,  1]                    [0,   0,  1,  1,  1]
    [0, 0,  0,  0,  0]                    [0,   1,  0,  0,  0]
    [1, 0,  0,  0,  0]                    [1,   0,  1,  1,  0]
    [1, 1,  0,  1,  1]                    [0,   1,  0,  1,  0]

Input: grid1 =[[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]]
       grid2 =[[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]

Output: 3
Explanation: In the picture above, the grid on the left is grid1 and the grid on the right
is grid2. The 1s colored red in grid2 are those considered to be part of a sub-island. There 
are three sub-islands.
"""
class Solution:
    """
    This class provides a solution to count sub-islands in a grid.

    The problem considers two grids (`grid1` and `grid2`). A sub-island in `grid2` refers to a connected land area
    (value 1) that is entirely contained within a land area (value 1) in `grid1`. The function calculates the number
    of such sub-islands present in `grid2`.
    """

    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        """
        Counts the number of sub-islands in a grid `grid2` that are entirely contained within land areas of `grid1`.

        Args:
            grid1 (List[List[int]]): A 2D list representing the reference grid `grid1`.
            grid2 (List[List[int]]): A 2D list representing the target grid `grid2` where sub-islands are counted.

        Returns:
            int: The total number of sub-islands in `grid2` that are entirely within land areas of `grid1`.
        """

        rows = len(grid1)
        cols = len(grid1[0])
        visited = set()  # Set to keep track of visited cells in `grid2`

        def dfs(row: int, col: int) -> bool:
            """
            Performs a Depth-First Search (DFS) traversal on `grid2` to explore connected land areas and
            check if they are sub-islands (entirely within land of `grid1`).

            Args:
                row (int): The row index of the current cell in `grid2`.
                col (int): The column index of the current cell in `grid2`.

            Returns:
                bool: True if the explored area is a sub-island, False otherwise.
            """

            if (row < 0 or col < 0 or row >= rows or col >= cols or  # Check for out-of-bounds
                grid2[row][col] == 0 or (row, col) in visited):
                return True  # Not a sub-island if out-of-bounds, water (0), or visited

            visited.add((row, col))  # Mark cell as visited

            # Not a sub-island if the corresponding cell in grid1 is water (0)
            if grid1[row][col] == 0:
                return False

            # Recursively explore neighbors and combine results using short-circuiting
            return (dfs(row - 1, col) and  # Up neighbor
                    dfs(row + 1, col) and  # Down neighbor
                    dfs(row, col - 1) and  # Left neighbor
                    dfs(row, col + 1))  # Right neighbor

        sub_island_count = 0
        for row in range(rows):
            for col in range(cols):
                if grid2[row][col] == 1 and (row, col) not in visited and dfs(row, col):
                    sub_island_count += 1

        return sub_island_count

import unittest

class TestCountSubIslands(unittest.TestCase):
    """
    test_empty_grids: Checks the behavior with empty grids (no cells).
    test_single_cell_grids: Tests scenarios with single-cell grids to verify sub-island identification based on both grids.
    test_horizontal_islands: Evaluates the function with horizontal islands to ensure it considers land overlap between grid1 and grid2.
    test_vertical_islands: Tests vertical islands to handle sub-islands that fit entirely within grid1.
    test_complex_grids: Uses complex grids with various shapes to test the function's robustness for different island configurations.
    """

    def setUp(self):
        self.solution = Solution()
        
    def test_empty_grids(self):
        grid1 = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        grid2 = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        self.assertEqual(0, self.solution.countSubIslands(grid1, grid2))

    def test_empty_grids(self):
        """Tests the function with empty grids."""
        solution = Solution()
        grid1 = []
        grid2 = []
        result = solution.countSubIslands(grid1, grid2)
        self.assertEqual(result, 0)

    def test_single_cell_grids(self):
        """Tests the function with grids containing a single cell."""
        solution = Solution()
        grid1 = [[1]]
        grid2 = [[1]]
        result = solution.countSubIslands(grid1, grid2)
        self.assertEqual(result, 1)  # Sub-island if both grids have land

        grid1 = [[0]]
        grid2 = [[1]]
        result = solution.countSubIslands(grid1, grid2)
        self.assertEqual(result, 0)  # Not a sub-island if grid1 has water

    def test_horizontal_islands(self):
        """Tests the function with horizontal islands."""
        solution = Solution()
        grid1 = [[1, 1, 1]]
        grid2 = [[1, 0, 1]]
        result = solution.countSubIslands(grid1, grid2)
        self.assertEqual(result, 0)  # Not a sub-island if part is missing in grid1

        grid1 = [[1, 1, 1]]
        grid2 = [[1, 1, 1]]
        result = solution.countSubIslands(grid1, grid2)
        self.assertEqual(result, 1)  # Sub-island if fully contained

    def test_vertical_islands(self):
        """Tests the function with vertical islands."""
        solution = Solution()
        grid1 = [[1], [1], [1]]
        grid2 = [[1], [0], [1]]
        result = solution.countSubIslands(grid1, grid2)
        self.assertEqual(result, 0)  # Not a sub-island if part is missing in grid1

        grid1 = [[1], [1], [1]]
        grid2 = [[1], [1], [1]]
        result = solution.countSubIslands(grid1, grid2)
        self.assertEqual(result, 1)  # Sub-island if fully contained

    def test_complex_grids(self):
        """Tests the function with complex grids with various shapes."""
        solution = Solution()
        grid1 = [[1, 0, 1], [0, 1, 1], [1, 0, 1]]
        grid2 = [[0, 0, 1], [1, 0, 1], [0, 1, 1]]
        result = solution.countSubIslands(grid1, grid2)
        self.assertEqual(result, 1)  # Only the center island is a sub-island

        grid1 = [[1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1]]
        grid2 = [[1, 1, 1, 1], [0, 1, 0, 1], [1, 1, 0, 1]]
        result = solution.countSubIslands(grid1, grid2)
        self.assertEqual(result, 2)  # Two sub-islands in the top and bottom rows

if __name__ == '__main__':
    unittest.main()

