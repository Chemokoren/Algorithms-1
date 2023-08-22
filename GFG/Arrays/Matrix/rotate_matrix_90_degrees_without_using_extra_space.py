"""
Rotate a matrix by 90 degree without using any extra space | Set 2

Given a square matrix, turn it by 90 degrees in anti-clockwise direction without using any
extra space.


Examples: 

Input:
 1  2  3
 4  5  6
 7  8  9
Output:
 3  6  9 
 2  5  8 
 1  4  7 
Rotated the input matrix by
90 degrees in anti-clockwise direction.

Input:
 1  2  3  4 
 5  6  7  8 
 9 10 11 12 
13 14 15 16 
Output:
 4  8 12 16 
 3  7 11 15 
 2  6 10 14 
 1  5  9 13
Rotated the input matrix by
90 degrees in anti-clockwise direction.

Approach
- The idea is to find the transpose of the matrix and then reverse the columns of the transposed
matrix.
Example:

1   2   3   4               1   5   9   13                  4   8   12  16
5   6   7   8               2   6   10  14                  3   7   11  15
9   10  11  12              3   7   11  15                  2   6   10  14
13  14  15  16              4   8   12  16                  1   5   9   13

Original matrix             Transpose matrix                columns reversed of the Transpose matrix


Algorithm
- To solve the given problem, there are two tasks. 1st is finding the transpose and the second
is reversing the columns without using an extra space
- A transpose of a matrix is when the matrix is flipped over its diagonal, i.e. the row index of 
an element becomes the column index and vice versa. So to find the transpose interchange the 
elements at position  (i, j) with (j, i). Run two loops, the outer loop from 0 to row count and
the inner loop from 0 to the index of the outer loop.
- To reverse the column of the transposed matrix, run two nested loops, the outer loop from 0 to
column count and the inner loop from 0 to row count/2, interchange elements at (i, j) with
(i, row[count-1-j]), where i and j are indices of inner and outer loop respectively.

Complexity Analysis: 

    Time complexity :O(R*C). 
    The matrix is traversed twice, so the complexity is O(R*C).
    Space complexity :O(1). 
    The space complexity is constant as no extra space is required.

"""
# program for left rotation of matrix by 90 degrees without using extra space
R = 4
C = 4

# After transpose, we swap elements of column one by one for finding left rotation of matrix
# by 90 degree
def reverse_columns(arr):
    for i in range(C):
        j = 0
        k = C-1

        while j < k:
            t = arr[j][i]
            arr[j][i] =arr[k][i]
            arr[k][i] = t
            j += 1
            k -= 1

# function for transposing a matrix

def transpose(arr):
    for i in range(R):
        for j in range(i, C):
            t = arr[i][j]
            arr[i][j] = arr[j][i]
            arr[j][i] = t

# Function for printing the matrix
def print_matrix(arr):
    for i in range(R):
        for j in range(C):
            print(str(arr[i][j]), end=" ")
        print()

# Function to anticlockwise rotate matric by 90 degree
def rotate_90(arr):
    transpose(arr)
    reverse_columns(arr)


arr = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]
       ]
rotate_90(arr)
print_matrix(arr)

