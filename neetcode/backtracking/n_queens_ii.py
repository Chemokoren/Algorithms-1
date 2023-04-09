"""
The n-queens puzzle is the problem of placing n queens on an n*n chessboard such
that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens
puzzle.

Example 1:

.   Q   .   .               .   .   Q   .
.   .   .   Q               Q   .   .   .
Q   .   .   .               .   .   .   Q
.   .   Q   .               .   Q   .   .


Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.

"""

class Solution:
    
    def totalNQueens(self, n:int)->int:
        col = set()
        posDiag = set() # (r + c)
        negDiag = set() # (r - c)
        
        res = 0
        
        def backtrack(r):
            if r == n:
                nonlocal res
                res += 1
                return 
            for c in range(n):
                if c in col or (r+c) in posDiag or (r-c) in negDiag:
                    continue
                
                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                backtrack(r+1)
                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
            
        backtrack(0)
        return res
    
sol = Solution()
print("Expected::2, Actual::", sol.totalNQueens(4))