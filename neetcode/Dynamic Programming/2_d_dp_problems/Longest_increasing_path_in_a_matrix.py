"""
Longest Increasing Path in a Matrix

Given an m*n integers matrix, return the length of the longest increasing path in 
matrix.
From each cell, you can either move in four directions: left, right, up, or down. You may
not move diagonally or move outside the boundary (i.e., wrap-around is not allowed)

Example 1:

9       9       4
^
|
6       6       8
^
|
2<----  1       0

"""
matrix =[[9, 9, 4], [6, 6, 8], [2, 1, 1]]
from typing import List
class Solution:
     
    def longest_increasing_path_in_a_matrix(self, matrix):
        if len(matrix) == 0:
                return 0
        
        ROW, COL = len(matrix), len(matrix[0])
        visited = {(i, j): False for i in range(ROW) for j in range(COL)}
        dp=[[1] * ROW for i in range(COL)]
        print(dp)
        
        

        def dfs(i, j):
            if i < ROW and j < COL and (i, j) not in visited and \
            (matrix[i][j] > matrix[i-1][j] or matrix[i][j] > matrix[i+1][j] or 
            matrix[i][j] > matrix[i][j-1] or matrix[i][j] > matrix[i][j+1]):
                dp[i][j] +=1
            visited[(i, j)] = True
            
            return 
    
    
        i, j =0,0
        dfs(i+1, j) 
        dfs(i-1, j) 
        dfs(i, j-1)
        dfs(i, j+1)

        lis = -float('inf')

        for i in range(ROW):
            for j in range(COL):
                if (dp[i][j]) > lis:
                    lis = dp[i][j]
            print(dp[i])
                

        return lis
    
    '''
    This code is an implementation of a solution to find the length of the longest increasing path in a 2D matrix using depth-first search (DFS) with memoization (dynamic programming).

Here's an explanation of what's happening in the code:

    The longest_increasing_path function takes a 2D matrix matrix as input and returns an integer representing the length of the longest increasing path (LIP) in the matrix.

    ROWS and COLS are calculated to determine the dimensions of the matrix.

    The dp dictionary is used to store the results of subproblems. It maps a tuple (r, c) (representing the current row and column) to the length of the longest increasing path starting from that cell. This dictionary is used for memoization to avoid redundant calculations.

    The dfs function is a recursive depth-first search function that explores paths starting from a given cell (r, c). It takes three parameters: r (current row), c (current column), and prevVal (the value of the previous cell in the path).

        The function checks if the current cell is out of bounds or if the value of the current cell is less than or equal to the prevVal. If either of these conditions is true, it returns 0, indicating that this is not a valid path.

        It also checks if the result for the current cell (r, c) is already in the dp dictionary. If it is, the function returns the memoized result to avoid re-computation.

        The function initializes res to 1, representing the length of the current cell's path.

        It then explores four possible directions: up, down, left, and right. For each direction, it recursively calls dfs with the updated position (r +/- 1, c) or (r, c +/- 1) and the current cell's value as prevVal. It increments the result res by 1 for each valid move.

        After exploring all valid directions, it updates the dp dictionary with the result for the current cell (r, c) and returns the result.

    The main part of the code iterates through each cell in the matrix using two nested loops. For each cell (r, c), it calls the dfs function, starting the search from that cell with a prevVal of -1 (indicating there's no previous value).

    Finally, the code returns the maximum value stored in the dp dictionary, which represents the length of the longest increasing path found in the matrix.

This code uses DFS with memoization to efficiently find the longest increasing path in the matrix, and it should work correctly for that purpose.

    '''
    def longest_increasing_path(self, matrix: List[List[int]])->int:
         
         ROWS, COLS = len(matrix), len(matrix[0])
         dp ={} # (r, c) -> LIP

         def dfs(r, c, prevVal):
              if(r < 0 or r == ROWS or
                 c < 0 or c == COLS or
                 matrix[r][c] <= prevVal):
                   return 0
              if (r, c) in dp:
                   return dp[(r, c)]
              
              res = 1
              res = max(res, 1 + dfs(r + 1, c, matrix[r][c]))
              res = max(res, 1 + dfs(r - 1, c, matrix[r][c]))
              res = max(res, 1 + dfs(r , c + 1, matrix[r][c]))
              res = max(res, 1 + dfs(r , c - 1, matrix[r][c]))
              dp[(r, c)] = res
              return dp[(r, c)]
         
         for r in range(ROWS):
            for c in range(COLS):
                 dfs(r, c, -1)
         return max(dp.values())


sol = Solution()
print(sol.longest_increasing_path(matrix))

print("--------")
print(sol.longest_increasing_path_in_a_matrix(matrix))



# matrix = [[9, 9, 4], [6, 6, 8], [6, 1, 1]]

# def longest_increasing_path_in_a_matrix(matrix):
#     if not matrix:
#         return 0
    
#     ROW, COL = len(matrix), len(matrix[0])
#     dp = [[1] * COL for i in range(ROW)]
#     visited = {(i, j): False for i in range(ROW) for j in range(COL)}  # Initialize visited for all cells
    
#     def dfs(i, j):
#         if i < 0 or i >= ROW or j < 0 or j >= COL:
#             return 0  # Out of bounds
#         if visited[(i, j)]:
#             return dp[i][j]
        
#         directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#         max_path = 1
#         for dx, dy in directions:
#             if 0 <= i + dx < ROW and 0 <= j + dy < COL and matrix[i][j] < matrix[i + dx][j + dy]:
#                 max_path = max(max_path, 1 + dfs(i + dx, j + dy))
        
#         dp[i][j] = max_path
#         visited[(i, j)] = True
#         return dp[i][j]

#     longest_path = 0
#     for i in range(ROW):
#         for j in range(COL):
#             longest_path = max(longest_path, dfs(i, j))
    
#     return longest_path

# print(longest_increasing_path_in_a_matrix(matrix))
