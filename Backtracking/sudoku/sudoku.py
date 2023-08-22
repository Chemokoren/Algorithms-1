def find_next_empty(puzzle):
    """
    Finds the next row, col on the puzzle that's not filled yet--> rep with -1.
    
        Parameters:
            puzzle(List[List[str]]): sudoku board to be solved
        
        Return:
            (r,c): return row, col tuple or (None, None) if there is None
    """
    
    # keep in mind that we are using 0-8 for our indices
    for r in range(9):
        for c in range(9): 
            # check if (r,c) is empty
            if puzzle[r][c] == -1:
                return r, c
            
    # if no spaces in the puzzle are empty
    return None, None 

def is_valid(puzzle, guess, row, col):
    """
    Figures out whether the guess at the row/col of the puzzle is a valid guess.
    
        Parameters:
            puzzle(List[List[str]]): sudoku puzzle to solve
            guess(str): represents the number to solve the board in that (r,c) cell
            row(int): integer representing the row in the board
            col(int): integer representing the column in the board
            
        Returns:
            bool: returns True if is valid, False otherwise
    
    """

    # row
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    
    # columns
    
    # col_vals =[]
    # for i in range(9):
    #     col_vals.append(puzzle[i][col])
        
    col_vals =[puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False
    
    # the square
    
    #get where the 3*3 square starts and iterate over the 3 values in the row/column
    row_start =(row // 3) * 3 
    col_start =(col // 3) * 3
    
    for r in range(row_start, row_start+3):
        for c in range(col_start, col_start+3):
            if puzzle[r][c] == guess:
                return False
            
    # if we get here, these checks pass
    return True

def solve_sudoku(puzzle):
    """
    return whether a solution exists to the puzzle 
    
        Parameters: 
            puzzle(List[List[str]]):list of lists, where @ inner list is a row in the 
                                    sudoku puzzle)
        Return:
            bool: mutates puzzle to be the solution(if solution exists)
    
    """
    # step 1: choose somewhere on the puzzle to make a guess
    row, col = find_next_empty(puzzle)
    
    # step 1.1 if there's nowhere left, then we're done because we only allowed valid inputs
    if row is None and col is None:
        return True
    
    # step 2: if there is a place to put a number, then make a guess between 1 and 9
    for guess in range(1, 10):
        # step 3: check if this is valid guess
        if is_valid(puzzle, guess, row, col):
            # step 3.1: if this is valid, then place that guess on the puzzle
            puzzle[row][col] = guess
            # now recurse using this puzzle!
            # step 4: recursively call our function
            if solve_sudoku(puzzle):
                return True
            
        # step 5: if not valid OR if our guess does not solve the puzzle, then we need to
        # backtrack and try a new number
        puzzle[row][col] = -1 # reset the guess
        
    # step 6: if none of the numbers that we try work, then this puzzle is UNSOLVABLE!!
    return False 

def print_board(bo):
    
    for i in range(len(bo)):
        if i % 3== 0 and i != 0:
            print("-------------------")
    
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print("|", end="")
                
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j])+" ", end="")
            
if __name__=="__main__":
    example_board =[
        [3, 9, -1,  -1,5,-1,    -1,-1,-1],
        [-1,-1,-1,  2,-1,-1,    -1,-1, 5],
        [-1,-1,-1,  7, 1, 9,    -1, 8,-1],
        
        [-1, 5,-1,  -1,6,8,     -1,-1,-1],
        [2, -1, 6,  -1,-1,3,    -1,-1,-1],
        [-1,-1,-1,  -1,-1,-1,   -1,-1, 4],
        
        [5, -1,-1,  -1,-1,-1,   -1,-1,-1],
        [6, 7, -1,  1, -1, 5,   -1, 4, -1],
        [1, -1, 9,  -1, -1, -1,  2, -1,-1]
    ]
    print(solve_sudoku(example_board))
    print_board(example_board)