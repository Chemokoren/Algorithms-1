"""
Unique Paths

A robot is located at the top-left corner of a m*n grid(marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying
to reach the bottom-right corner of the grid(marked 'Finish' in the diagram below).

How many possible unique paths are there?

Example 1:

start   x       x       x       x       x       x

x       x       x       x       x       x       x

x       x       x       x       x       x   Finish

Input: m = 3, n = 7
Output: 28

"""
import unittest

class Solution:
      
    # o(n * m) time complexity | O(n * m) space complexity  
    def unique_paths(self, m, n):
        g = [[0 for c in range(n +1)] for r in range(m + 1)]
        g[m-1][n] =1

        
        for r in range(m-1, -1, -1):
                for c in range(n-1, -1, -1):
                    g[r][c] = g[r+1][c] + g[r][c+1]
        return g[0][0]
      
    # o(n * m) time complexity | O(n) space complexity where n is the lengthROW of a row
    def uniquePaths(self, m:int, n:int)-> int:
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
         self.assertEqual(28, self.sol.start_to_finish(3, 7))
         self.assertEqual(28, self.sol.uniquePaths(3, 7))


if __name__=="__main__":
     unittest.main()