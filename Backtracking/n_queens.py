"""
Place N Queens on an NxN chessboard, in such a manner that no two queens attack each other. 
A queen can move horizontally, vertically, and diagonally.

   - Start in the leftmost column.
   - If all the queens are placed
        return true
   - Try all rows in the current column. Do the following for every tried row.
        - If the queen can be placed safely in this row, then mark this [row, column] as part of the
          solution and recursively check if placing the queen here leads to a solution.
        - If placing the queen in [row, column] leads to a solution, return true.
        - If placing the queen in [row, column] doesn’t lead to a solution, then unmark this [row, column] 
        and go to the first step to try other rows.
   - If all rows have been tried and nothing worked, return false to trigger backtracking.



"""

class NQueens:

    def __init__(self, n) -> None:
        self.n = n
        self.chess_table =[[0 for i in range(n)] for j in range(n)]

    def print_queens(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.chess_table[i][j] == 1:
                    print(" Q ", end=' ')
                else:
                    print(" - ", end=' ')
            print("\n")

    def is_place_safe(self, row_index, col_index):
        for i in range(self.n):
            if self.chess_table[row_index][i] ==1:
                return False

        j = col_index
        for i in range(row_index, -1, -1):
            if i < 0:
                break
            if self.chess_table[i][j] ==1:
                return False
            j = j -1
        
        j = col_index
        for i in range(row_index, self.n):
            if i < 0:
                break
            if self.chess_table[i][j] == 1:
                return False

            j = j -1

            return True

    def solve(self, col_index):
        if col_index == self.n:
            return True

        for row_index in range(self.n):
            if self.is_place_safe(row_index, col_index):
                self.chess_table[row_index][col_index] =1
                if self.solve(col_index+1):
                    return True
                self.chess_table[row_index][col_index] = 0
        return False

    def solve_NQueens(self):
        if self.solve(0):
            self.print_queens()
        else:
            print("No solution exists for the problem")


queens = NQueens(2)
queens.solve_NQueens()



# q =NQueens(8)
# print(q.chess_table)
# print("gggggggggggggggggggg")
# q.print_queens()