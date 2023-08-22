"""
Program for scalar multiplication of a matrix

Given a matrix and a scalar element k, our task is to find out the scalar product of that 
matrix.

Input : mat[][] = {{2, 3}
                   {5, 4}}
        k = 5
Output : 10 15 
         25 20 
We multiply 5 with every element.

Input : 1 2 3 
        4 5 6
        7 8 9
        k = 4
Output :  4 8  12
          16 20 24
          28 32 36 

The sclar multiplication of a number k(scalar), multiply it on every entry in the matrix and
a matrix A is the matrix kA.

Time Complexity: O(n2),

Auxiliary Space: O(1), since no extra space has been taken.

"""







'''
my tests
'''
def my_tests(mat, key):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            mat[i][j] =mat[i][j] * key
    return mat


def print_mat(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            print(mat[i][j], end=" ")
        print()

mat = [[2, 3],[5, 4]]

print_mat(my_tests(mat,5))

mat =[
    [1, 2, 3],
    [4, 5 , 6],
    [7, 8 , 9]
    ]

print_mat(my_tests(mat,4))