"""
Rotate a Matrix by 180 degree

Given a square matrix, the task is that we turn it by 180 degrees in an anti-clockwise direction
without using any extra space.

Input :  1  2  3
         4  5  6
         7  8  9
Output : 9 8 7 
         6 5 4 
         3 2 1

Input :  1 2 3 4 
         5 6 7 8 
         9 0 1 2 
         3 4 5 6 
Output : 6 5 4 3 
         2 1 0 9 
         8 7 6 5 
         4 3 2 1

Method 1: Only prints rotated matrix
- The solution of this problem is that to rotate by 180 degrees, we can easily follow that step.

Matrix =  a00 a01 a02
          a10 a11 a12
          a20 a21 a22

when we rotate it by 90 degree
then matrix is
Matrix = a02 a12 a22
         a01 a11 a21
         a00 a10 a20
  
when we rotate it by again 90 
degree then matrix is 
Matrix = a22 a21 a20
         a12 a11 a10
         a02 a01 a00 

Time complexity: O(N*N) 
Auxiliary Space: O(1)

"""
# program to rotate a matrix by 180 degrees
N = 3

# Function to rotate the matrix by 180 degree
def rotate_matrix(mat):

    # print from last cell to first cell
    i = N -1
    while(i >= 0):
        j = N-1
        while(j >= 0):
            print(mat[i][j], end=" ")
            j = j-1
        print()
        i = i -1


mat = [
        [ 1, 2, 3 ],
        [ 4, 5, 6 ],
        [ 7, 8, 9 ]
       ]

rotate_matrix(mat)

"""
Method: In-Place Rotation
There are four steps:
- Find transpose of a matrix
- Reverse columns of the transpose
- Find transpose of a matrix
- Reverse columns of the transpose


Let the given matrix be
1  2  3  4
5  6  7  8
9  10 11 12
13 14 15 16

First we find transpose.
1 5 9 13
2 6 10 14
3 7 11 15
4 8 12 16

Then we reverse elements of every column.
4 8 12 16
3 7 11 15
2 6 10 14
1 5  9 13

then transpose again 
4 3 2 1 
8 7 6 5 
12 11 10 9
16 15 14 13 

Then we reverse elements of every column again
16 15 14 13 
12 11 10 9 
8 7 6 5 
4 3 2 1


Time complexity : O(R*C) 
Auxiliary Space : O(1)
In the code above, the transpose of the matrix has to be found twice, and also, columns have to 
be reversed twice. 


"""
# program for left rotation of matrix by 180
R = 4
C = 4

# function to rotate the matrix by 180 degree
def reverse_columns(arr):
    for i in range(C):

        j = 0
        k = C-1
        while j < k:
            t = arr[j][i]
            arr[j][i] = arr[k][i]
            arr[k][i] = t
            j += 1
            k -= 1

# Function for transpose of matrix
def transpose(arr):
    for i in range(R):
        for j in range(i, C):
            t = arr[i][j]
            arr[i][j] =arr[j][i]
            arr[j][i] = t

# Function for displaying the matrix
def print_matrix(arr):
    for i in range(R):
        for j in range(C):
            print(arr[i][j], end=" ")
        print()

# Function to rotate matrix vy 180 degree anticlockwise
def rotate_180(arr):
    transpose(arr)
    reverse_columns(arr)
    transpose(arr)
    reverse_columns(arr)


arr = [ [ 1, 2, 3, 4 ],
        [ 5, 6, 7, 8 ],
        [9, 10, 11, 12 ],
        [13, 14, 15, 16 ] ]

rotate_180(arr)
print_matrix(arr)


"""

Method 3: Position swapping
- Here, we swap the values in the respective positions

Time complexity : O(R*C) 
Auxiliary Space : O(1), since no extra space has been taken.

"""
# Reverse row at specified index in the matrix
def reverse_row(data, index):

    cols =len(data[index])
    for i in range(cols // 2):
        temp = data[index][i]
        data[index][i] = data[index][cols-i-1]
        data[index][cols -i -1] = temp

    return data

# print matrix data
def print_matrix(data):

    for i in range(len(data)):
        for j in range(len(data[0])):
            print(data[i][j], end=' ')

        print()

# Rotate Matrix by 180 degrees
def rotate_matrix(data):
    rows = len(data)
    cols = len(data[0])

    if(rows % 2):
        # if N is odd reverse the middle row in the matrix
        data = reverse_row(data, len(data) // 2)

        # swap the value of matrix [i][j] with [rows - i - 1][cols - j - 1 ] for
        # half the rows size.
        for i in range(rows // 2):
            for j in range(cols):
                temp = data[i][j]
                data[i][j] = data[rows -i - 1][cols -j -1]
                data[rows - i - 1][cols -j -1] =temp

        return data

data = [ [ 1, 2, 3, 4, 5 ],
         [ 6, 7, 8, 9, 10 ],
         [ 11, 12, 13, 14, 15 ],
         [ 16, 17, 18, 19, 20 ],
         [ 21, 22, 23, 24, 25 ] ]


data = rotate_matrix(data)
print_matrix(data)