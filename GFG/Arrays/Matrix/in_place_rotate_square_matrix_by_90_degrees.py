"""
Inplace rotate square matrix by 90 degrees | set 1

Given a square matrix turn it by 90 degrees in anti-clockwise direction without using an extra 
space.

Examples : 

Input:
Matrix:
 1  2  3
 4  5  6
 7  8  9
Output:
 3  6  9 
 2  5  8 
 1  4  7 
The given matrix is rotated by 90 degree 
in anti-clockwise direction.

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
The given matrix is rotated by 90 degree 
in anti-clockwise direction.

Approach

- To solve the question without an extra space, rotate the array in form of squares, dividig the
matrix into squares or cycles. For example, A 4 * 4 matrix will have 2 cycles. The first cycle is 
formed by its 1st row, last column, last row and 1st column. The second cycle is formed by 2nd row,
second-last column, second-last row and 2nd column. The idea is for each square cycle, swap the 
elements involved with the corresponding cell in the matrix in anit-clockwise direction i.e. from
top to left, left to bottom, bottom to right and from right to top once at a time using nothing 
but a temporary variable to achieve this.


First Cycle (Involves Red Elements)
 1  2  3 4 
 5  6  7 8 
 9 10 11 12 
 13 14 15 16 

Moving first group of four elements (First
elements of 1st row, last row, 1st column 
and last column) of first cycle in counter
clockwise. 
 4  2  3 16
 5  6  7 8 
 9 10 11 12 
 1 14  15 13 
 
Moving next group of four elements of 
first cycle in counter clockwise 
 4  8  3 16 
 5  6  7  15  
 2  10 11 12 
 1  14  9 13 

Moving final group of four elements of 
first cycle in counter clockwise 
 4  8 12 16 
 3  6  7 15 
 2 10 11 14 
 1  5  9 13 


Second Cycle (Involves Blue Elements)
 4  8 12 16 
 3  6 7  15 
 2  10 11 14 
 1  5  9 13 

Fixing second cycle
 4  8 12 16 
 3  7 11 15 
 2  6 10 14 
 1  5  9 13

Algorithm: 

- There is N/2 squares or cycles in a matrix of side N. Process a square one at a time. Run a loop 
to traverse the matrix a cycle at a time, i.e loop from 0 to N/2 – 1, loop counter is i
Consider elements in group of 4 in current square, rotate the 4 elements at a time. So the number 
of such groups in a cycle is N – 2*i.
So run a loop in each cycle from x to N – x – 1, loop counter is y

The elements in the current group is (x, y), (y, N-1-x), (N-1-x, N-1-y), (N-1-y, x), now rotate 
the these 4 elements, i.e (x, y) <- (y, N-1-x), (y, N-1-x)<- (N-1-x, N-1-y), (N-1-x, 
N-1-y)<- (N-1-y, x), (N-1-y, x)<- (x, y)

Print the matrix.


Complexity Analysis: 

    Time Complexity: O(n2), where n is side of array. 
    A single traversal of the matrix is needed.
    Space Complexity: O(1). 
    As a constant space is needed
    Since no extra space has been taken.

"""
# program to rotate a matrix by 90 degrees
N = 4

# An inplace function to rotate N * N matrix by 90 degrees in anti-clockwise direction
def rotate_matrix(mat):

    # consider all squares one by one
    for x in range(0, int(N/2)):

        # consider elements in group of 4 in current square
        for y in range(x, N-x-1):

            # store current cell in temp variable
            temp = mat[x][y]

            # move values from right to top
            mat[x][y] = mat[y][N-1-x]

            # move values from bottom to right
            mat[y][N-1-x] = mat[N-1-x][N-1-y]

            # move values from left to bottom
            mat[N-1-x][N-1-y] = mat[N-1-y][x]

            # assign temp to left
            mat[N-1-y][x] = temp

# Function to print the matrix
def display_matrix(mat):
    for i in range(0, N):
        for j in range(0, N):
            print(mat[i][j], end=' ')
        print("")

mat =[[0 for x in range(N)] for y in range(N)]



# Test case 1
mat = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]


'''
# Test case 2
mat = [ [1, 2, 3 ],
        [4, 5, 6 ],
        [7, 8, 9 ] ]
 
# Test case 3
mat = [ [1, 2 ],
        [4, 5 ] ]
         
'''

rotate_matrix(mat)
 
# Print rotated matrix
display_matrix(mat)
 

""" 

Another Approach:

    - Reverse every individual  row
    - Perform Transpose

Complexity Analysis:  

    Time Complexity: O(n2) + O(n2)   where n is size of array.
    Auxiliary Space: O(1). As a constant space is needed


"""
# program to rotate a matrix by 90 degrees
def rotate_matrix_two(mat):
    # reversing the matrix
    for i in range(len(mat)):
        mat[i].reverse()

    for i in range(len(mat)):
        for j in range(i, len(mat)):
            # swapping mat[i][j] and mat[j][i]
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]


# function to print the matrix
def display_matrix_two(mat):
    for i in range(0, len(mat)):
        for j in range(0, len(mat)):
            print(mat[i][j], end=' ')
        print()
 

mat_val = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]
 
rotate_matrix_two(mat_val)
 
# Print rotated matrix
display_matrix_two(mat_val)

