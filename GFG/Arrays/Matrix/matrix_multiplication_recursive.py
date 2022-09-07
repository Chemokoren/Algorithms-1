"""
Matrix Multiplication | Recursive

Given two matrices A and B. The task is to multiply matrix A and matrix B recursively. If matrix
A and matrix B are not multiplicative compatible, then generate output "Not possible"

Input: A = 12 56
           45 78

       B = 2 6
           5 8

Output: 304 520
        480 894

Input: A = 1 2 3
           4 5 6
           7 8 9
       B = 1 2 3
           4 5 6
           7 8 9

Output: 30  36  42  
        66  81  96  
       102 126 150  

First chek if multiplication between matrices is possible or not. For this, check if number of 
columns of first matrix is equal to number of rows of second matrix or not. If both are equal
then proceed further, otherwise generate output, "Not Possible".

In Recursive Matrix Multiplication, we implement three loops of iteration through 
recursive calls. The inner most Recursive call of muliplyMatrix is to iterate k(col1 or row2).
The second recursive call of multiplyMatrix() is to change the columns and the outermost 
recursive call is to change rows.

Time Complexity: O(row1 * col2)
Auxiliary Space: O(log (max(row1,col2)), As implicit stack is used due to recursion
"""
# Recursive code for Matrix Multiplication
MAX = 100
i = 0
j = 0
k = 0

def multiplyMatrixRec(row1, col1, A, row2, col2, B, C):
    # Note that below variables are static
    # i and j are used to know current cell of result matrix C[][]. k is used to know
    # current column number of A[][] and row number of B[][] to be multiplied
    global i
    global j
    global k

    # if all rows traversed 
    if (i >= row1):
        return

    # if i < row1
    if(j < col2):
        if(k < col1):
            C[i][j] += A[i][k] * B[k][j]
            k += 1
            multiplyMatrixRec(row1, col1, A, row2, col2, B,  C)

        k  = 0
        j += 1
        multiplyMatrixRec(row1, col1, A, row2, col2, B, C)


    j = 0
    i += 1
    multiplyMatrixRec(row1, col1, A, row2, col2, B, C)

# Function to multiply two matrixes
# A[][] and B[][]
def multiplyMatrix(row1, col1, A, row2, col2, B):
    if(row2 != col1):
        print("Not Possible")
        return

    C =[[ 0 for i in range(MAX)]
            for i in range(MAX)]
    multiplyMatrixRec(row1, col1, A, row2, col2, B, C)

    # print the result
    for i in range(row1):
        for j in range(col2):
            print(C[i][j], end=" ")
        print()



A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
B = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
 
row1 = 3
col1 = 3
row2 = 3
col2 = 3

multiplyMatrix(row1, col1, A, row2, col2, B)














'''
my tests
'''
def matrix_multiplication(mat1, mat2):
    first_rows =len(mat1)
    first_columns =len(mat1[0])

    second_rows =len(mat2)
    second_columns =len(mat2[0])

    if first_columns == second_rows:
        return "Possible"
    else:
        return "Not Possible"


mat1 =[[12,56],
       [45,78]]

mat2 =[[2,6],
       [5,8]]

# mat1 =[[1,2,3],
#        [4,5,6],
#        [7,8,9]
#        ]

# mat2 =[[1,2,3],
#        [4,5,6],
#        [7,8,9]
#        ]



# print(matrix_multiplication(mat1,mat2))


def calc_matrix_multiplication(mat1, mat2):
    for i in range(len(mat1)):
        # for j in range(len(mat2[i])):
        print(mat1[i],i)



# calc_matrix_multiplication(mat1,mat2)