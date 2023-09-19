"""
Unique Paths

A robot is located at the top-left corner of a m*n grid(marked 'Start' in the diagram 
below.)
The robot can only move either down or right at any point in time. The robot is trying
to reach the bottom-right corner of the grid(marked 'Finish' in the diagram below).

How many possible unique paths are there?

[ S |   |   |   |   |   |   |

|   |   |   |   |   |   |   |

|   |   |   |   |   |   | F ]
"""
import unittest
class Solution:

    # time complexity: O(n * m) | space complexity: O(n)
    def unique_paths(self, m:int, n: int)-> int:
        row =[1] * n

        for i in range(m-1):
            newRow =[1] * n
            for j in range(n-2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]
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