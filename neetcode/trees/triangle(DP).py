from typing import List
"""
Given a triangle array, return the minimum path sum from top to bottom. For each step, 
you may move to an adjacent number on the row below.

Example 1:

Input: triangle =[[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
                       2
                      /  \
                    3      4
                  /  \   /   \
                6      5      4
               /  \   /  \  /   \
              4     1     8      3    

Explanation: The minimum path sum from top to bottom is 11 (i.e., 2+3+5+1 = 11).

Example 2:
Input: triangle =[[-10]]
Output: -10

Memory complexity is O(n) where n is the number of rows we have
Time complexity =O(n^2) where n is the number of elements we have
"""

class solution:
    """
    Bottom-up dynamic programming approach to efficiently calculate the minimum path sum
    by iteratively updating the optimal substructure.
    
    """

    def minimum_total(self, triangle: List[List[int]])->int:
        """
        Method returns the minimum path sum from top to bottom for a given triangle.
        
        Args:
            triangle(List[List[int]]): triangle array
        Returns:
            int:  minimum path sum from top to bottom
        
        """
        if len(triangle)==0:
            raise ValueError(" triangle is empty")
        # initialize dp array with the length of the triangle plus 1
        dp =[0] * (len(triangle)+ 1)

        # iterates over the rows of the triangle in reverse order
        for row in triangle[::-1]: 
            for i, n in enumerate(row):
                # The minimum path sum to reach the current element n is calculated by 
                # adding n to the minimum of the adjacent elements in the next row, 
                # dp[i] and dp[i+1].
                dp[i] =n + min(dp[i], dp[i+1])
        # after the loop completes, the minimum path sum from the top to the bottom of the 
        # triangle is stored in dp[0]
        return dp[0]


        
        
import unittest

class TestMinimumTotal(unittest.TestCase):

    def setUp(self):
        self.sol = solution()

    def test_initial_sample_triangle(self):
        triangle =[[2],[3,4],[6,5,7],[4,1,8,3]]
        self.assertEqual(self.sol.minimum_total(triangle), 11)

    def test_empty_triangle(self):
        """Tests an empty triangle."""
        triangle = []
        
        self.assertRaises(ValueError, self.sol.minimum_total, triangle)

    def test_single_element_triangle(self):
        """Tests a triangle with a single element."""
        triangle = [[2]]
        self.assertEqual(self.sol.minimum_total(triangle), 2)

    def test_balanced_triangle(self):
        """Tests a balanced triangle."""
        triangle = [
            [2],
            [3, 4],
            [6, 5, 7]
        ]
        actual=self.sol.minimum_total(triangle)
        self.assertEqual(10, actual)  # 2 + min(3, 4) + 5

    def test_unbalanced_triangle(self):
        """Tests an unbalanced triangle."""
        triangle = [
            [2],
            [3, 1],
            [4, 6, 8]
        ]
        self.assertEqual(self.sol.minimum_total(triangle), 9)  # 2 + 1 + 5

    def test_negative_values(self):
        """Tests a triangle with negative values."""
        triangle = [
            [2],
            [-3, 4],
            [6, -5, 7]
        ]
        self.assertEqual(self.sol.minimum_total(triangle), -6)  # 2 + (-3) + 5

    def test_large_values(self):
        """Tests a triangle with large values."""
        triangle = [
            [100],
            [200, 300],
            [400, 500, 600]
        ]
        self.assertEqual(self.sol.minimum_total(triangle), 700)  # 100 + min(200, 300) + 500

if __name__ == '__main__':
    unittest.main()
