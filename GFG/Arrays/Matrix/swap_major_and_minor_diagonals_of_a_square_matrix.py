"""
Swap major and minor diagonals of a square matrix

Given a square matrix, swap the element of major and minor diagonals

Major Diagonal Elements of a Matrix:
- The Major Diagonal elements are the ones that occur from Top Left of Matrix down to bottom right
corner. The major diagonal is also known as main diagonal or primary diagonal.

Minor Diagonal Elements of a Matrix:
- The minor diagonal elements are the ones that occur from top right of matrix down to bottom
left corner - also known as the secondary diagonal.

Input : 0 1 2
        3 4 5
        6 7 8

Output : 2 1 0
         3 4 5
         8 7 6

Aproach 
- The indexes of Primary or Major diagonal are same i.e. Lets say A is a matrix then A[1][1] will
be a major diagonal element and sum of indexes of minor diagonal is equal to size of matrix.
Lets say A is a matrix of size 3 then A[1][2] will be minor diagonal element.

Time Complexity: O(N*N), as we are using nested loops to traverse N*N times.
Auxiliary Space: O(1), as we are not using any extra space.

"""
# size of square matrix
N = 3
# Function to swap diagonal of matrix
def swap_diagonal(matrix):

    for i in range(N):
        matrix[i][i], matrix[i][N-i-1] = matrix[i][N-i-1], matrix[i][i]


matrix = [[0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]]
 
swap_diagonal(matrix)

for i in range(N):   
    for j in range(N):       
        print(matrix[i][j], end = ' ')       
    print()
