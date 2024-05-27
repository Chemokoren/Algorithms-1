from typing import List
import collections
"""
Number of Islands

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island
is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
"""
from typing import List
import collections

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Given a 2D grid of '1's (land) and '0's (water), count the number of islands.
        An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
        You may assume all four edges of the grid are all surrounded by water.

        :param grid: List of List of str, representing the 2D grid map
        :return: Integer, the number of islands in the grid
        """
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def bfs(r, c):
            """
            Perform Breadth-First Search to visit all parts of the island starting from (r, c).
            """
            q = collections.deque()
            visit.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()  # Remove the oldest item from the queue (BFS)
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]  # right, left, above, below

                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc
                    if (new_row in range(rows) and
                        new_col in range(cols) and
                        grid[new_row][new_col] == "1" and
                        (new_row, new_col) not in visit):
                        q.append((new_row, new_col))
                        visit.add((new_row, new_col))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1

        return islands
    
import unittest
class TestNumIslands(unittest.TestCase):
    """
    test_empty_grid: Tests the function with an empty grid.
    test_single_element_grid_water: Tests the function with a grid containing a single water element.
    test_single_element_grid_land: Tests the function with a grid containing a single land element.
    test_no_islands: Tests the function with a grid with no islands (all water).
    test_one_island: Tests the function with a grid containing one island.
    test_multiple_islands: Tests the function with a grid containing multiple islands.
    test_large_grid: Tests the function with a larger grid containing multiple islands.
    test_complex_island_shapes: Tests the function with a grid containing complex island shapes.
    """

    def setUp(self):
        """This method initializes a Solution instance before each test method is run."""
        self.solution = Solution()

    def test_sample(self):
        grid = [
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"],
        ]
        self.assertEqual(self.solution.numIslands(grid), 1)

    def test_empty_grid(self):
        grid = []
        self.assertEqual(self.solution.numIslands(grid), 0)

    def test_single_element_grid_water(self):
        grid = [["0"]]
        self.assertEqual(self.solution.numIslands(grid), 0)

    def test_single_element_grid_land(self):
        grid = [["1"]]
        self.assertEqual(self.solution.numIslands(grid), 1)

    def test_no_islands(self):
        grid = [
            ["0", "0", "0"],
            ["0", "0", "0"],
            ["0", "0", "0"]
        ]
        self.assertEqual(self.solution.numIslands(grid), 0)

    def test_one_island(self):
        grid = [
            ["1", "1", "0"],
            ["1", "1", "0"],
            ["0", "0", "0"]
        ]
        self.assertEqual(self.solution.numIslands(grid), 1)

    def test_multiple_islands(self):
        grid = [
            ["1", "0", "0", "1", "0"],
            ["1", "0", "0", "1", "0"],
            ["0", "0", "0", "0", "1"],
            ["0", "1", "1", "0", "0"]
        ]
        self.assertEqual(self.solution.numIslands(grid), 4)

    def test_large_grid(self):
        grid = [
            ["1", "1", "1", "0", "0", "0", "1", "1", "1"],
            ["1", "1", "0", "0", "0", "0", "1", "1", "1"],
            ["1", "1", "0", "0", "1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "1", "1", "0", "0", "0"]
        ]
        self.assertEqual(self.solution.numIslands(grid), 3)

    def test_complex_island_shapes(self):
        grid = [
            ["1", "0", "1", "0"],
            ["1", "1", "0", "1"],
            ["0", "1", "1", "0"],
            ["0", "0", "1", "1"]
        ]
        self.assertEqual(self.solution.numIslands(grid), 3)

if __name__ == "__main__":
    unittest.main()