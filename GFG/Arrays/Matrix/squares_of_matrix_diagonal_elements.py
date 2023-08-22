"""
Squares of Matrix Diagonal Elements

You have given an integer matrix with odd dimensions. Find the square of the diagonals elements on
both sides.


Input  :  1 2 3
          4 5 6
          7 8 9
Output :  Diagonal one: 1 25 81
          Diagonal two: 9 25 49

Input  :  2 5 7  
          3 7 2
          5 6 9
Output :  Diagonal one : 4 49 81
          Diagonal two : 49 49 25

Method 1: Firstly, we find the diagonal element of the matrix and then we print the square of that
element.

Time Complexity O(n*n)

"""
# function of diagonal square
def diagonal_square(mat, row, column):

    # This loop is for finding square of first diagonal elements
    print("Diagonal one: ", end="")
    for i in range(0, row):
        for j in range(0, column):
            # if this condition will become true then we will get diagonal element
            if(i == j):
                # printing square of diagonal element
                print ("{} ".format(mat[i][j] *  mat[i][j]), end = "")
                
    # This loop is for finding square of second side of diagonal elements
    print("\n\n Diagonal two: ", end="")
    for i in range(0, row):
        for j in range(0, column):
            # if this condition will become true then we will get second side diagonal element
            if(i + j == column -1):
                # printing square of diagonal element
                print("{} ".format(mat[i][j] * mat[i][j]), end = "")


mat = [[ 2, 5, 7 ],
        [ 3, 7, 2 ],
        [ 5, 6, 9 ]]
diagonal_square(mat, 3, 3)


"""
Method 2
- An efficient solution is also same as in naive approach but in this, we are taking only one
loop to find the diagonal element and then we print the square of that element.

Time Complexity O(n)
Space Complexity O(n^2) for creating 2-Dimensional array
"""
def diagonal_square_two(mat, row, column):

    print ("Diagonal one : ", end = "")
    for i in range(0, row):
        # printing direct square of diagonal element there is no need to check condition
        print(mat[i][i] *mat[i][i], end=" ")
    
    print ("\n\nDiagonal two : ",  end = "")

    for i in range(0, row):
        print (mat[i][row - i - 1] * mat[i][row - i - 1] , end = " ")
 
mat = [[2, 5, 7 ],
       [3, 7, 2 ],
       [5, 6, 9 ]]
diagonal_square_two(mat, 3, 3)


print("\n my tests \n")
'''
my tests

'''
import copy
def my_tests(mat):
    N = len(mat[0])
    c =copy.deepcopy(mat)
    for i in range(len(mat)):
        mat[i][i] =pow(c[i][i],2)
        mat[i][N-i-1]=pow(c[i][N-i-1], 2)
    return mat

mat =[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
mat = [[ 2, 5, 7 ],
        [ 3, 7, 2 ],
        [ 5, 6, 9 ]]
print(my_tests(mat))