import unittest
from typing import List

"""
Island Perimeter

You are given row * col grid representing a map where grid[i][j] =1
represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely 
surrounded by water, and there is exactly one island(i.e, one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water 
around the island. One cell is a square with side length 1. The grid is rectangular, width
and height don't exceed 100. Determine the perimeter of the island.

Input: grid =[
            [0,1,0,0],
            [1,1,1,0],
            [0,1,0,0],
            [1,1,0,0]
            ]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above

It is a linear time algorithm  -meaning that we are visiting every cell in the grid only once.
Time complexity: O(n*m)
"""

class Solution:
    """
    This class provides a solution to find the perimeter of an island in a grid.

    The problem considers a grid where each cell represents land (1) or water (0). The function calculates the
    total perimeter of the connected land (island) in the grid.
    """

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """
        Calculates the perimeter of the island in a 2D grid.

        Args:
            grid (List[List[int]]): A 2D list representing the grid, where grid[i][j] is 1 for land and 0 for water.

        Returns:
            int: The total perimeter length of the island in the grid.
        """

        visited = set()  # Set to keep track of visited cells

        def dfs(row: int, col: int) -> int:
            """
            Performs a Depth-First Search (DFS) traversal to explore the island and calculate its perimeter.

            Args:
                row (int): The row index of the current cell.
                col (int): The column index of the current cell.

            Returns:
                int: The perimeter contribution of the current cell (1 if on the edge, 0 otherwise).
            """

            if (row >= len(grid) or col >= len(grid[0]) or  # Check for out-of-bounds
                row < 0 or col < 0 or
                grid[row][col] == 0):  # Check for water cell
                return 1

            if (row, col) in visited:  # Skip already visited cell
                return 0

            visited.add((row, col))  # Mark cell as visited

            perimeter = dfs(row, col + 1)   # Explore right neighbor
            perimeter += dfs(row, col - 1)  # Explore left neighbor
            perimeter += dfs(row + 1, col)  # Explore down neighbor
            perimeter += dfs(row - 1, col)  # Explore up neighbor

            return perimeter

        # Start DFS from any land cell to find the island
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    return dfs(row, col)

        # If no land is found, the perimeter is 0
        return 0



class TestislandPerimeter(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_islandPerimeter(self):
        grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
        self.assertEqual(self.sol.islandPerimeter(grid), 16)

    def test_empty_grid(self):
        """Tests the function with an empty grid."""
        solution = Solution()
        grid = []
        result = solution.islandPerimeter(grid)
        self.assertEqual(result, 0)

    def test_single_cell_island(self):
        """Tests the function with a grid containing a single land cell."""
        solution = Solution()
        grid = [[1]]
        result = solution.islandPerimeter(grid)
        self.assertEqual(result, 4)  # Perimeter of a single cell

    def test_horizontal_island(self):
        """Tests the function with a horizontal island of connected land cells."""
        solution = Solution()
        grid = [[1, 1, 1, 1]]
        result = solution.islandPerimeter(grid)
        self.assertEqual(result, 10)  # 3 edges shared internally

    def test_vertical_island(self):
        """Tests the function with a vertical island of connected land cells."""
        solution = Solution()
        grid = [[1],
                [1],
                [1]]
        result = solution.islandPerimeter(grid)
        self.assertEqual(result, 8)  #

    def test_complex_island(self):
        """Tests the function with a complex island with various shapes."""
        solution = Solution()
        grid = [[0, 1, 0, 0],
                [1, 1, 1, 0],
                [0, 1, 0, 1],
                [0, 0, 0, 0]]
        result = solution.islandPerimeter(grid)
        # todo
        # one island is 12 while another is 4
        self.assertEqual(result, 16)

    def test_no_island(self):
        """Tests the function with a grid containing only water cells."""
        solution = Solution()
        grid = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]
        result = solution.islandPerimeter(grid)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
        


