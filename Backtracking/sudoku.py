"""

"""
class Sudoku:

    def __init__(self, board) -> None:
        assert len(board) ==9, "Invalid Board"
        for i in board:
            assert len(i) == 9, "Invalid Board"
        self.board = board
        self.unfilled =[(r,c) for r in range(9) for c in range(9) if self.board[r][c] == 0]


    def isValid(self, r,c,num):
        for i in range(9): # check row
            if self.board[r][i] ==num and i != c: # if there is a different position in our current row that has the same number
                return False # we don't have a valid board state

        for i in range(9): # check column
            if self.board[i][c] == num and i != r:
                return False
        # check for the 3 * 3 square
        r_corner, c_corner = r -(r % 3), c -(c %3)
        for tR in range(r_corner, r_corner +3):
            for tC in range(c_corner, c_corner +3):
                # if we found the num & it is not the location we gave
                # means there was a different location in the box with same number
                if self.board[tR][tC] == num and (r, c) != (tR, tC): 
                    return False            
        return True

    def solve(self):
         return self._solve(0) if self._solve(0) else "Impossible Board"
        # assert self._solve(0), "Impossible Board"

    def _solve(self, idx):
        # return True because there are no more positions to fill -board is solved
        if idx >= len(self.unfilled): 
            return True
        r,c = self.unfilled[idx]
        for num in range(1,10):
            self.board[r][c] =num
            if not self.isValid(r,c, num): continue
            if self._solve(idx+1):
                return True
        self.board[r][c] =0
        return False

puzzle = [
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

if __name__=="__main__":
    
    sd =Sudoku(puzzle)
    print(sd.solve())

	# import SudokuSolver_Checker
	# SudokuSolver_Checker.validate()