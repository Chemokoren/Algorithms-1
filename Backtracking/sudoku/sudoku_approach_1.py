"""
notes::

1) The Dancing Links algorithm, by Knuth, is one of the most beautiful algos I have ever seen.
It works by abstracting away from the sudoku itself, and translating all the constraints into 
a matrix form, on witch you can apply a backtracking algorithm,
in order to find a subset of lines with exactly one non-zero value in each column. 
The advantage is that it treats all constraints as equal. 

You should absolutely do a video on solving Sudoku with Dancing Links. 
Moreover, you can show that by generalizing a problem, you can use exactly the same algorithm
for Sudoku, Pentominos, Soma cube and many others.

2) For those who wanted to learn more about this. The problem of solving sudoku can be 
generalized to a problem called Constraint Satisfaction Problem (CSP), 
CSP includes things from puzzle solving to real world problem like planning and scheduling.

3) Worth mentioning is that sudoku is part of a family of problems called 'exact cover' 
problems which are NP hard. 
In the family are problems such as nonograms and the eight queens problem. 
Would be cool to see sudoku generalized as an exact cover problem and solved that way.

4) Like other puzzle solvers though, Sokoban requires you to avoid repeated positions in your
recursion, much like repeated positions in chess.  
I think a very scaled-down chess solver, like an end-game solver, would be a fun thing to write.

4) For anyone interested: If you want an easy way to go the constraint solving route, 
for example because you want to solve this for larger N where the running time becomes 
restrictive, you can model your sudoku problem in a constraint programming language such as 
MiniZinc and solve it using a constraint solver. 
Sudoku is actually part of the MiniZinc tutorial
5)  Conceptual Programming with Python.

"""

grid =[
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
       ]

# Initialize the Sudoku grid (global variable)
# grid = [
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0]
# ]

import numpy as np
print("---------------------------------------------------------------------------")
print(np.matrix(grid))
print("---------------------------------------------------------------------------")




def possible(y, x, n):
    """
    Check if it's possible to place the number 'n' at position '(y, x)' in the Sudoku grid 
    without violating the rules.

    Parameters:
        y (int): Row index.
        x (int): Column index.
        n (int): Number to be placed.

    Returns:
        bool: True if it's possible to place 'n' at position '(y, x)', False otherwise.
    """
    global grid

    # Check if 'n' is already present in the same row or column
    for i in range(9):
        if grid[y][i] == n:
            return False
        if grid[i][x] == n:
            return False
    
    # Calculate the top-left corner coordinates of the 3x3 subgrid
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3

    # Check if 'n' is already present in the 3x3 subgrid
    for i in range(3):
        for j in range(3):
            if grid[y0 + i][x0 + j] == n:
                return False
    return True

def solve():
    """
    Solve the Sudoku puzzle using a backtracking algorithm.

    Prints the solved Sudoku grid and prompts the user if they want to find more solutions.
    """
    global grid

    # Iterate over each cell in the Sudoku grid
    for y in range(9):
        for x in range(9):
            # Check if the cell is empty (contains 0)
            if grid[y][x] == 0:
                # Try placing numbers from 1 to 9
                for n in range(1, 10):
                    # Check if it's possible to place 'n' at the current position
                    if possible(y, x, n):
                        # Place 'n' at the current position
                        grid[y][x] = n
                        # Recursively call solve() to continue solving the puzzle
                        solve()
                        # Reset the cell value to 0 (backtrack) and try other numbers
                        grid[y][x] = 0
                return 

    # Print the solved Sudoku grid using np.matrix() and prompt the user for more solutions
    print(np.matrix(grid))
    input("More?")



# Start solving the Sudoku puzzle
solve()
