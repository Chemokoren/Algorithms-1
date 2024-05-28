from typing import List
import unittest
"""
You are given an m*n integer matrix heights representing the height of each unit cell
in a continent. The Pacific ocean touches the continent left and top edge and the Atlantic 
ocean touches the continent's right and bottom edges.
Water can only flow in four directions:up, down, left, and right. Water flows from a cell to
an adjacent one with an equal or lower height.

Return a list of grid coordinates where water can flow to both Pacific and Atlantic oceans

                Pacific ocean
                1   2   2   3   5

Pacific         3   2   3   4   4       Atlantic

ocean           6   7   1   4   5       ocean

                5   1   1   2   4

                Atlantic ocean

Input: heights =[[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]

Time: O(N.M)^2 


"""
class Solution:
    """
    This class provides a solution to find cells that can flow water to both the Pacific Ocean and the Atlantic Ocean.

    The problem considers a height map where water can only flow from a cell to a neighboring cell with a non-negative
    height difference (i.e., water flows from higher to lower ground). The function identifies cells that can drain
    water to both the Pacific Ocean (left and top borders) and the Atlantic Ocean (right and bottom borders).
    """

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        Finds all cells that can flow water to both the Pacific Ocean and the Atlantic Ocean.

        Args:
            heights (List[List[int]]): A 2D list representing the height map, where heights[r][c] represents the height
                                       of cell (row r, column c).

        Returns:
            List[List[int]]: A list of lists containing the coordinates (row, column) of cells that can flow water
                             to both the Pacific and Atlantic Oceans.
        """

        num_rows, num_cols = len(heights), len(heights[0])
        pacific_reachable = set()  # Cells reachable from the Pacific Ocean
        atlantic_reachable = set()  # Cells reachable from the Atlantic Ocean

        def dfs(row, col, visited, prev_height):
            """
            Performs a Depth-First Search (DFS) traversal to explore reachable cells from a given starting point.

            Args:
                row (int): The row index of the current cell.
                col (int): The column index of the current cell.
                visited (set): A set of visited cells to avoid revisiting.
                prev_height (int): The height of the previous cell to ensure water can flow downwards.
            """

            if (row, col) in visited or \
               row < 0 or col < 0 or row >= num_rows or col >= num_cols or \
               heights[row][col] < prev_height:
                return

            visited.add((row, col))
            dfs(row + 1, col, visited, heights[row][col])  # Explore down
            dfs(row - 1, col, visited, heights[row][col])  # Explore up
            dfs(row, col + 1, visited, heights[row][col])  # Explore right
            dfs(row, col - 1, visited, heights[row][col])  # Explore left

        # Start DFS from all cells on the borders (Pacific and Atlantic)
        for col in range(num_cols):
            dfs(0, col, pacific_reachable, heights[0][col])  # Pacific Ocean (top border)
            dfs(num_rows - 1, col, atlantic_reachable, heights[num_rows - 1][col])  # Atlantic Ocean (bottom border)

        for row in range(num_rows):
            dfs(row, 0, pacific_reachable, heights[row][0])  # Pacific Ocean (left border)
            dfs(row, num_cols - 1, atlantic_reachable, heights[row][num_cols - 1])  # Atlantic Ocean (right border)

        # Find cells reachable from both oceans
        result = []
        for row in range(num_rows):
            for col in range(num_cols):
                if (row, col) in pacific_reachable and (row, col) in atlantic_reachable:
                    result.append([row, col])

        return result


class TestPacificAtlantic(unittest.TestCase):
    """
    test_empty_grid: Checks the behavior with an empty grid (no cells).
    test_single_cell: Tests the case with a single cell, where no cell can flow to both oceans.
    test_all_reachable: Ensures the function identifies all reachable cells in a grid with a simple height map.
    test_no_pacific_flow: Verifies that the function returns an empty list if no cell can flow to the Pacific Ocean.
    test_no_atlantic_flow: Tests the scenario where no cell can flow to the Atlantic Ocean.
    test_complex_grid: Evaluates the function with a more complex grid and varying heights to ensure it handles different cases.

    """

    def setUp(self):
        self.solution = Solution()

    def test_empty_grid(self):
        """Tests the function with an empty grid."""
        heights = []
        result = self.solution.pacificAtlantic(heights)
        self.assertEqual(result, [])

    def test_single_cell(self):
        """Tests the function with a grid containing a single cell."""
        heights = [[1]]
        result = self.solution.pacificAtlantic(heights)
        self.assertEqual(result, [])  # No cell can flow to both oceans

    def test_all_reachable(self):
        """Tests the function with a grid where all cells are reachable from both oceans."""
        heights = [[1, 2, 2, 3, 5],
                   [3, 2, 3, 4, 4],
                   [2, 4, 5, 3, 1],
                   [3, 1, 2, 3, 4]]
        result = self.solution.pacificAtlantic(heights)
        expected_result = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4),
                           (1, 0), (1, 1), (1, 2), (1, 3), (1, 4),
                           (2, 0), (2, 1), (2, 2), (2, 3), (2, 4),
                           (3, 0), (3, 1), (3, 2), (3, 3), (3, 4)]
        self.assertEqual(set(result), set(expected_result))

    def test_no_pacific_flow(self):
        """Tests the case where no cell can flow water to the Pacific Ocean."""
        heights = [[10, 10, 10],
                   [10, 10, 10],
                   [10, 10, 10]]
        result = self.solution.pacificAtlantic(heights)
        self.assertEqual(result, [])

    def test_no_atlantic_flow(self):
        """Tests the case where no cell can flow water to the Atlantic Ocean."""
        heights = [[1, 2, 3],
                   [3, 2, 1],
                   [2, 1, 0]]
        result = self.solution.pacificAtlantic(heights)
        self.assertEqual(result, [])

    def test_complex_grid(self):
        """Tests the function with a complex grid with varying heights."""
        heights = [[1, 2, 2, 3, 5],
                   [3, 2, 3, 4, 4],
                   [2, 4, 5, 3, 1],
                   [2, 1, 2, 5, 1]]
        result = self.solution.pacificAtlantic(heights)
        expected_result = [(0, 3), (1, 2), (2, 0), (2, 1), (2, 2), (2, 3), (3, 0)]
        self.assertEqual(set(result), set(expected_result))

if __name__ == '__main__':
    unittest.main()
