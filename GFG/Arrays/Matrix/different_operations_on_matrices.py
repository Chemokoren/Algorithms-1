"""
Different Operations on Matrices

We will discuss the following operations on matrices and their properties:
- Matrices Addition
- Matrices Subtraction
- Matrices Multiplication

Matrices Addition
-----------------
The addition of two matrices A(m*n) and B(m*n) gives a matrix C(m*n). The elements of c are the
sum of the corresponding elements in A and B as follows:

1   2           5   6           6   8
            +               =   
4   5           8   9           12  14

Key Points:
- The addition of matrices is commutative, i.e A+B = B+A
- The addition of matrices is associative, i.e, A+(B+C) =(A+B)+C
- The order of matrices A, B and A+B is always the same
- If the order of A and B are different, A+B can't be computed
- The complexity of the addition operation is O(M*N) where M*N is the order of matrices

Time Complexity: O(N*M)
Auxiliary Space: O(N*M)
"""
# program for addition of two matrices

N = 4
# This function adds A[][] and B[][], and stores the result in c[][]
a = [ [2, 5],
    [1, 7]]
 
b= [ [3, 7],
    [2, 9]]

N = 2

c =a[:][:] # To store result
for i in range(N):
    for j in range(N):
        c[i][j] = a[i][j]+b[i][j]

for i in range(N):
    for j in range(N):
        print(c[i][j], " ", end=' ')
    print()

"""
Matrices Subtraction

The subtraction of two matrices A(m*n) and B(m*n) give a matrix C(m*n). The elements of c are the 
difference of corresponding elements in A and B which can be represented as:

5   6       1   2       4   4
        -           =
8   9       4   5       4   4

Key points
- Subtraction of matrices is non-commutative i.e, A-B is not equal to B-A
- substration of matrices is non-associative i.e, A-(B-C) not qual to (A-B)-C
- The order of matrices A,B and A-B is always the same
- If the order of A and B are different, A-B can't be computed
- The complexity of substration operation is O(M*N) where M*N is the order of matrices

Time Complexity: O(N*M)
Auxiliary Space: O(N*M)

"""
a = [[2, 5],
     [1, 7]]
 
b = [[3, 7],
     [2, 9]]
 
N = 2
c =a[:][:]
for i in range(N):
    for j in range(N):
        c[i][j] = a[i][j]-b[i][j]

for i in range(N):
    for j in range(N):
        print(c[i][j], " ", end='')
    print()



"""

Matrices Multiplicaiton
- The multiplication of two matrices A(m*n) and B(n*p) give a matrix C(m*p). It means a number of
columns in A must be equal to the number of rows in B to calculate C =A*B. To calculate element
c11, multiply elements of 1st row of A with 1st column of B and add them i.e.,(5*1 + 6*4)

Key points:
- Multiplication of matrices is non-commutative i.e., A*B not equal to B*A
- Multiplication of matrices is associative which means A*(B*C) =(A*B)*C
- For computing A*B, the number of columns in A must be equal to the number of rows in B
- The existence of A*B does not imply the existence of B*A
- The complexity of multiplication operation(A*B) is O(m*n*p) where m*n and n*p are the order of
A and B respectively
-The order of matrix C computed as A*B is m*p where m*n and n*p are the order of A and B 
respectively.

Time Complexity: O((N^2)*M)
Auxiliary Space: O(N*M)

"""
# Program for matrix multiplication
n, m = 2, 2
a = [[ 2, 5 ], [ 1, 7 ]]
b = [[ 3, 7 ], [ 2, 9 ]]
c = [ [0 for i in range(n)] for j in range(m)]

for  i  in range(0,n):
    for j in range(0, n):
        c[i][j] = 0
        for k in range(0, n):
            c[i][j] += a[i][k] * b[k][j]
    
for  i in range(0, n):
    for j  in range(0,n):
        print(c[i][j], end=" ")
    print("")








print("\n my tests \n")

def my_tests_addition(mat1, mat2):
    c =[[0 for i in range(len(mat1))] for j in range(len(mat1[0]))]
    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            c[i][j] =mat1[i][j]+mat2[i][j]

    return c



a = [ [2, 5],
    [1, 7]]
 
b= [ [3, 7],
    [2, 9]]
print("Expected:, Actual:",my_tests_addition(a, b))



def my_tests_subtraction(mat1, mat2):
    c =[[0 for i in range(len(mat1))] for j in range(len(mat1[0]))]
    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            c[i][j] =mat1[i][j]- mat2[i][j]

    return c



a = [ [2, 5],
    [1, 7]]
 
b= [ [3, 7],
    [2, 9]]
print("Expected:, Actual:",my_tests_subtraction(a, b))
