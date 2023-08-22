"""
Program to print Lower triangular and Upper triangular matrix of an array

Given a two dimensional array, write a program to print lower triangular matrix and upper 
triangular matrix.
- Lower triangular matrix is a matrix which contains elements below principle diagonal including
principle diagonal elements and rest of the elements are 0.
- Upper triangular matrix is a matrix which contains elements above principle diagonal
including principle diagonal elements and rest of the elements are 0.

Input : matrix[3][3] = {1 2 3
                       4 5 6
                       7 8 9}
Output :
Lower : 1 0 0        Upper : 1 2 3
        4 5 0                0 5 6
        7 8 9                0 0 9

Input : matrix[3][3] = {7 8 9
                        3 2 1
                        6 5 4}
Output :
Lower : 7 0 0       Upper : 7 8 9
        3 2 0               0 2 1
        6 5 4               0 0 4

Steps:
1. For lower triangular matrix, we check the index position i and j i.e. row and column
respectively. If column position is greater than row position we simply make that position 0.
2. For upper triangular matrix, we check the index position i and j i.e. row and column 
respectively. If Column position is smaller than row position, we simply make that position 0.

Time Complexity: O(row x col)
Auxiliary Space: O(1), since no extra space has been taken.

"""
# Program to print lower triangular and upper triangular matrix of an array
# Function to form lower triangular matrix
def lower(matrix):
    row = len(matrix)
    col = len(matrix[0])
    for i in range(0, row):
        for j in range(0, col):
            if(i < j):
                print("0", end=" ")
            else:
                print(matrix[i][j], end=" ")
        print(" ")

# Function to form upper triangular matrix
def upper(matrix):
    row = len(matrix)
    col = len(matrix[0])
    for i in range(0, row):
        for j in range(0, col):
            if (i > j):
                print("0", end=" ")
            else:
                print(matrix[i][j], end=" ")
        print(" ")

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]


matrix =[[1,4],
         [5,9]
         ]
     
print("Lower triangular matrix: ")
lower(matrix)
     
print("Upper triangular matrix: ")
upper(matrix)