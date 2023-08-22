"""
Maximum path sum in matrix

Given a matrix of N*M, find the maximum path sum in matrix. The maximum path is sum of all the
elements from first row to last row where you are allowed to move only down or diagonally to left
or right. You can start from any element in the first row.

Input : mat[][] = 10 10  2  0 20  4
                   1  0  0 30  2  5
                   0 10  4  0  2  0
                   1  0  2 20  0  4
Output : 74
The maximum sum path is 20-30-4-20.

Input : mat[][] = 1 2 3
                  9 8 7
                  4 5 6
Output : 17
The maximum sum path is 3-8-6.

We are given a matrix of N * M. To find max path sum first we have to find max value in first 
row of matrix. Store this value in res. Now for every element in matrix update element with max 
value which can be included in max path. If the value is greater then res then update res. 

In last return res which consists of max path sum value.

Time Complexity: O(N*M), where N and M are the dimensions of the matrix
Space Complexity: O(1), since no extra space has been taken.

"""
# program for finding max path in matrix to calculate max path in matrix
def find_max_path(mat):
    N = len(mat)
    M = len(mat[0])
    for i in range(1, N):
        res = -1
        for j in range(M):
            # when all paths are possible
            if(j > 0 and j < M-1):
                mat[i][j] += max(mat[i-1][j], max(mat[i-1][j-1],mat[i-1][j+1]))
            
            # when diagonal right is not possible
            elif(j > 0):
                mat[i][j] += max(mat[i-1][j],mat[i-1][j-1])

            # when diagonal left is not possible
            elif(j < M-1):
                mat[i][j] += max(mat[i-1][j],mat[i-1][j+1])

            # store max path sum
            res = max(mat[i][j], res)
    return res

mat = ([[ 10, 10, 2, 0, 20, 4 ],
        [ 1, 0, 0, 30, 2, 5 ],
        [ 0, 10, 4, 0, 2, 0 ],
        [ 1, 0, 2, 20, 0, 4 ]])
               
print(find_max_path(mat))


