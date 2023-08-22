"""
Sort the given matrix

Given a n*n matrix. The problem is to sort the given matrix in strict order. Here strict order 
means that the matrix is sorted in a way such that all elements in a row are sorted in increasing
order and for row "i", where 1 <= i <=n-1, the first element of row "i" is greater than or equal
to the last element of row "i-1".


Input : mat[][] = { {5, 4, 7},
                    {1, 3, 8},
                    {2, 9, 6} }
Output : 1 2 3
         4 5 6
         7 8 9


Approach:

- Create a temp[] array of size n^2. Starting with the first row one by one copy the elements of
the given matrix into temp[]. Sort temp[]. Now one by one copy the elements of the temp[] back to
the given matrix.


Time Complexity: O(n2log2n). 
Auxiliary Space: O(n2), since n * n extra space has been taken.


"""
# implementation to sort the given matrix
SIZE = 10

# Function to sort the given matrix
def sortMat(mat, n):
    # Temporary matrix of size n^2
    temp =[0] * (n * n)
    k = 0

    # copy the elements of matrix one by one into temp[]
    for i in range(0, n):
        for j in range(0, n):
            temp[k] = mat[i][j]
            k +=1

    # sort temp[]
    temp.sort()

    # copy the elements of temp[]
    # one by one in mat[][]
    k = 0

    for i in range(0, n):
        for j in range(0, n):
            mat[i][j] = temp[k]
            k += 1

# Function to print the given matrix
def printMat(mat, n):
    for i in range(0, n):
        for j in range(0, n):
            print(mat[i][j], end=" ")

        print()


mat = [ [ 5, 4, 7 ],
        [ 1, 3, 8 ],
        [ 2, 9, 6 ] ]
n = 3
 
print( "Original Matrix:")
printMat(mat, n)
 
sortMat(mat, n)
 
print("\nMatrix After Sorting:")
printMat(mat, n)


