"""
Unique Paths

A robot is located at the top-left corner of a m*n grid(marked 'Start' in the diagram 
below.)
The robot can only move either down or right at any point in time. The robot is trying
to reach the bottom-right corner of the grid(marked 'Finish' in the diagram below).

How many possible unique paths are there?

Example 1:

[ S |   |   |   |   |   |   |

|   |   |   |   |   |   |   |

|   |   |   |   |   |   | F ]

sol

[ 28| 21|15 |10 | 6 | 3 | 1 |0

| 7 | 6 | 5 | 4 | 3 | 2 | 1 |0

| 1 | 1 | 1 | 1 | 1 | 1 | 1 ]0
  0   0   0   0   0   0   0

m =3, n=7
Output=28
"""
import unittest
class Solution:

    # time complexity: O(n * m) | space complexity: O(n) coz it is the length of the row
    def unique_paths(self, m:int, n: int)-> int:
        row =[1] * n  # bottom row (n is length of number of rows)

        for i in range(m-1): # go through all the other rows except for the last one
            newRow =[1] * n # new row is above the bottom(old) row
            # go through all columns except the rightmost column coz it is going to  be 1
            # coz all last values in every single row are 1
            for j in range(n-2, -1, -1): 
                newRow[j] = newRow[j + 1] + row[j] # row[j] is the value below in the old row
            row = newRow
        return row[0]
    
class TestUniquePaths(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.sol = Solution()

    def test_unique_paths(self):
        self.assertEqual(28, self.sol.unique_paths(7, 3))

if __name__=="__main__":
    unittest.main()