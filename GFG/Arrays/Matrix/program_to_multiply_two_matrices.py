"""
Program to multiply two matrices

Given two matrices, the task to is to multiply them. Matrices can either be square or 
rectangular.

(Square Matrix Multiplication)
Input : mat1[m][n] = {
             {1, 1},
            {2, 2}
        }
        mat2[n][p] = {
            {1, 1},
            {2, 2}
        }
Output : result[m][p] = {
             {3, 3},
            {6, 6}
         }

(Rectangular Matrix Multiplication)
Input : mat1[3][2] = {
             {1, 1},
            {2, 2},
            {3, 3}
        }
        mat2[2][3] = {
            {1, 1, 1},
            {2, 2, 2}
        }
Output : result[3][3] = {
             {3, 3, 3},
            {6, 6, 6},
            {9, 9, 9}
         }

Multiplication of two Square or Rectangular Matrices:

This program can multiply any two square or rectangular matrices.

The below program multiplies two square matrices of size 4 * 4.

There is also an example of a rectangular matrix for the same code (commented below).

We can change the Matrix value with the number of rows and columns (from MACROs) for Matrix-1 and Matrix-2 for different dimensions.

Note:  i-  The number of columns in Matrix-1 must be equal to the number of rows in Matrix-2.

           ii-  Output of multiplication of Matrix-1 and Matrix-2, results with equal to the number of rows of Matrix-1 and 

                 the number of columns of Matrix-2 i.e. rslt[R1][C2].

"""
# 4 * 4 matrix multiplication


def mulMat(mat1, mat2, R1, R2, C1, C2):
    # List to store matrix multiplicaiton result
    rslt = [[0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]]

    for i in range(0, R1):
        for j in range(0, C2):
            for k in range(0, R2):
                rslt[i][j] += mat1[i][k] * mat2[k][j]
    
    for i in range(0, R1):
        for j in range(0, C2):
            print(rslt[i][j], end=" ")
        print("\n", end="")

R1 = 4
R2 = 4
C1 = 4
C2 = 4

# First matrix. M is a list
mat1 = [[1, 1, 1, 1],
        [2, 2, 2, 2],
        [3, 3, 3, 3],
        [4, 4, 4, 4]]
 
# Second matrix. N is a list
mat2 = [[1, 1, 1, 1],
        [2, 2, 2, 2],
        [3, 3, 3, 3],
        [4, 4, 4, 4]]
 
if C1 != R2:
    print("The number of columns in Matrix-1  must be equal to the number of rows in " + "Matrix-2", end='')
    print("\n", end='')
    print("Please update MACROs according to your array dimension in #define section", end='')
    print("\n", end='')
else:
    # Call matrix_multiplication function
    mulMat(mat1, mat2, R1, R2, C1, C2)

"""

Multiplication of Square Matrices : 

The below program multiplies two square matrices of size 4*4, we can change N for different 
dimensions. 

Time complexity: O(n3). It can be optimized using Strassen’s Matrix Multiplication

Auxiliary Space: O(n2)

"""
# 4 * 4 matrix multiplication
def matrix_multiplication(M, N):
    # List to store matrix multiplication result

    R = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]

    for i in range(0, 4):
        for j in range(0, 4):
            for k in range(0, 4):
                R[i][j] += M[i][k] * N[k][j]

    for i in range(0, 4):
        for j in range(0, 4):
            # if we use print(), by default cursor moves to next line each time,
            # Now we can explicitly define ending character or sequence passing
            # second parameter as end ="<character or string>"
            # syntax: print(<variable or value to print>, end ="<ending with>")
            # Here space (" ") is used to print a gap after printing
            # each element of R
            print(R[i][j], end=" ")
        print("\n", end="")

# First matrix. M is a list
M = [[1, 1, 1, 1],
    [2, 2, 2, 2],
    [3, 3, 3, 3],
    [4, 4, 4, 4]]
 
# Second matrix. N is a list
N = [[1, 1, 1, 1],
    [2, 2, 2, 2],
    [3, 3, 3, 3],
    [4, 4, 4, 4]]


matrix_multiplication(M, N)

"""

Multiplication of Rectangular Matrices : 

We use pointers in C to multiply to matrices. Please refer to the following post as a 
prerequisite of the code.

Time complexity: O(n3). It can be optimized using Strassen’s Matrix Multiplication

Auxiliary Space: O(m1 * n2)

"""
# program to multiply two rectangular matrices
# (m1) x (m2) and (n1) x (n2) are
# dimensions of given matrices.
def multiply(m1, m2, mat1, n1, n2, mat2):
    res =[[0 for x in range(n2)]for y in range(m1)]

    for i in range(m1):
        for j in range(n2):
            res[i][j] = 0
            for x in range(m2):
                res[i][j] += (mat1[i][x] *mat2[x][j])

    for i in range(m1):
        for j in range(n2):
            print(res[i][j], end=" ")
        print()
    print("aaa", res)

mat1 = [[2, 4], [3, 4]]
mat2 = [[1, 2], [1, 3]]
m1, m2, n1, n2 = 2, 2, 2, 2
   
multiply(m1, m2, mat1, n1, n2, mat2)
     

