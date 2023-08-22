"""

Print a given matrix in counter-clockwise spiral form

Given a 2D array, print it in counter-clockwise spiral form

Input:
        1    2   3   4
        5    6   7   8
        9   10  11  12
        13  14  15  16
Output: 
1 5 9 13 14 15 16 12 8 4 3 2 6 10 11 7 

Input:
        1   2   3   4  5   6
        7   8   9  10  11  12
        13  14  15 16  17  18
Output: 
1 7 13 14 15 16 17 18 12 6 5 4 3 2 8 9 10 11 


Time Complexity : O(mn).

Auxiliary Space: O(1) because constant space has been used

"""
# implementation for printing the counter clock-wise spiral traversal of matrix
R = 4
C = 4

# Function to print the required traversal
def counterClockspiralPrint(m, n, arr):
    k = 0
    l = 0

    """
    k - starting row index
    m - ending row index
    l - starting column index
    n - ending column index
    i - iterator

    """
    # Initialize the count
    cnt = 0

    # total number of elements in matrix
    total = m*n

    while(k < m and l < n):
        if(cnt == total):
            break

        # Print the first column from the remaining columns
        for i in range(k, m):
            print(arr[i][l], end=" ")
            cnt += 1
        l +=1

        if(cnt == total):
            break
        # print the last row from the remaining rows
        for i in range(l, n):
            print(arr[m-1][i], end=" ")
            cnt += 1

        m -= 1

        if(cnt == total):
            break

        # print the first row from the remaining rows
        if(l < n):
            for i in range(n-1, l-1, -1):
                print(arr[k][i], end=" ")
                cnt += 1
            k += 1

arr = [ [ 1, 2, 3, 4 ],
        [ 5, 6, 7, 8 ],
        [ 9, 10, 11, 12 ],
        [ 13, 14, 15, 16 ] ]
         
counterClockspiralPrint(R, C, arr)

"""
Alternate implementation

Time Complexity: O(n2)

Auxiliary Space: O(1), since no extra space has been taken.
"""
# function to print Matrix in CounterClockwise
def counterClockspiralPrint(Matrix):
    size =len(Matrix)
    flag =0
    k, i = 0, size

    # print all layers one by one
    while(i > 0):

        # print First Column of current layer
        for j in range(flag, i):
            print(Matrix[j][k], end=' ')
        i = i -1
        k = j

        # print bottom row and last column of current layer
        if(i > 0):
            for j in range(size -i , i+1):
                print(Matrix[k][j], end=' ')
            for j in range(k-1, size-i-2, -1):
                print(Matrix[j][k], end=' ')
        else: break
        k = j
        i = i -1

        # print top of row of current layer
        if(i>0):
            for j in range(i, size -i-2, -1):
                print(Matrix[k][j], end=' ')
            k, i = k + 1, i + 1
            flag = flag + 1
        else: break

arr = [ [ 1, 2, 3, 4 ],
        [ 5, 6, 7, 8 ],
        [ 9, 10, 11, 12 ],
        [ 13, 14, 15, 16 ] ]

print("\n")
counterClockspiralPrint(arr)
  