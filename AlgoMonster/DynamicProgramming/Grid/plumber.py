"""
Plumber

Our favourite plumber is on his way to save the princess located in the castle. The castle is represented by a 2-D grid that contains obstacles(denoted by a -1) and coins(denoted by a 1). Empty squares in the castle will be denote by a 0. Our plumber will always start at first row in the grid and the princess will always be at last row in the grid. Whilst on his way to save the princess(reach any position of the last row) what is the maximal number of coins that can be obtained?

Restriction:

    The plumber can only move down, right, and left. But never up.
    The plumber cannot cross through the obstacles.

If the plumber cannot reach the last row, return -1.
Input

    grid: Grid containing the castle layout

Output

Integer representing the maximal number of coins that can be obtained, return -1 if the 
plumber cannot reach the last level.

Examples
Example 1:

Input:

grid = [[0, 0], [1, 1]]

Output: 2

Explanation:

Both of the coins can be collected on the way to the princess
Example 2:

Input:

grid = [[0, 0, 1], [0, 0, -1], [0, 0, 0]]

Output: 1

Explanation:

After getting the coin in the first row, the plumber can move to the left and down to avoid the obstacle.
Example 3:

Input:

grid = [[1,0,-1,1,0,1],[1,-1,1,-1,1,-1],[0,0,-1,-1,1,1]]

Output: 5

Explanation:

See solution.
Constraints

    2 <= rows, columns <= 2000


"""