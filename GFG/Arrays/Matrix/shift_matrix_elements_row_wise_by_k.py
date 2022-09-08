"""
Shift matrix elements row-wise by k

Given a square matrix mat[][] and a number k. The task is to shift the first k elements of each
row to the right of the matrix.

Input : mat[N][N] = {{1, 2, 3},
                     {4, 5, 6},
                     {7, 8, 9}}
        k = 2
Output :mat[N][N] = {{3, 1, 2}
                     {6, 4, 5}
                     {9, 7, 8}}

Input : mat[N][N] = {{1, 2, 3, 4}
                     {5, 6, 7, 8}
                     {9, 10, 11, 12}
                     {13, 14, 15, 16}}
        k = 2
Output :mat[N][N] = {{3, 4, 1, 2}
                     {7, 8, 5, 6}
                     {11, 12, 9, 10}
                     {15, 16, 13, 14}}
Note: Matrix should be a square matrix 

Time Complexity: O(n^2)
Auxiliary Space: O(1)
"""
# program to shift k elements in a matrix
N = 4
# Function to shift k elements of each row of matrix
def shiftMatrixByK(mat, k):
    if(k > N):
        print("shifting is not possible")
        return 

    j = 0
    while(j < N):
        # print elements from index k
        for i in range(k, N):
            print("{} ".format(mat[j][i]), end="")

        # print elements before index k
        for i in range(0, k):
            print("{} ".format(mat[j][i], end=""))

        print("")
        j = j +1


mat = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]

shiftMatrixByK(mat, 2)
