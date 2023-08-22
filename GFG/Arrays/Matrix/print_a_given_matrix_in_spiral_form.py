"""
Print a given matrix in spiral form

Given a 2D array, print it in spiral form


Input:  {{1,    2,   3,   4},
              {5,    6,   7,   8},
             {9,   10,  11,  12},
            {13,  14,  15,  16 }}
Output: 1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10 
Explanation: The output is matrix in spiral format.

1--> 2--> 3 --> 4
                |
                V
5-->6-->7       8
^       |       |
|       V       V
9  10<--11     12
^               |
|               V
13<--14<--15<--16

Input: { {1,   2,   3,   4,  5,   6},
           {7,   8,   9,  10,  11,  12},
          {13,  14,  15, 16,  17,  18}}

Output: 1 2 3 4 5 6 12 18 17 16 15 14 13 7 8 9 10 11
Explanation :The output is matrix in spiral format.

Best Optimized Method 1: Simulation aproach
-------------------------------------------

- Draw the path that the spiral makes. We know that the path should turn clockwise whenever
it would go out of bounds or into a cell that was previous visited.

Algorithm

- Let the array have R rows and C columns. Seen[r] denotes that the cell on the r-th row and 
c-th column was previously visited. Our curent position is(r,c), facing direction di, and we
want to visiti R*C total cells.

- As we move through the matrix, our candidate's next position is(cr,cc). If the candidate is
in the bounds of the matrix and unseen, then it becomes our next position; otherwise, our 
next position is the one after performing a clockwise turn.

Time Complexity: O(N), where N is the total number of elements in the input matrix. 
We add every element in the matrix to our final answer.
Auxiliary Space: O(N), the information stored in seen and in ans.

"""
def spiral_order(matrix):

    ans =[]
    
    if(len(matrix) == 0):
        return ans

    m = len(matrix)
    n = len(matrix[0])
    seen =[[0 for i in range(n)] for j in range(m)]
    dr =[0, 1, 0, -1]
    dc =[1, 0, -1, 0]
    x = 0
    y = 0
    di =0

    # Iterate from 0 to R * C -1
    for i in range(m*n):
        ans.append(matrix[x][y])
        seen[x][y] = True
        cr = x + dr[di]
        cc = y + dc[di]

        if(0 <= cr and cr < m and 0 <= cc and cc < n and not (seen[cr][cc])):
            x = cr
            y = cc
        else:
            di =(di + 1) % 4
            x += dr[di]
            y += dc[di]
    return ans


a = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]
  
for x in spiral_order(a):
    print(x, end=" ")
print()

"""

Method 2: This is a simple method to solve the following problem
- The problem can be solved by dividing the matrix into loops or squares or boundaries. It can
be seen that the elements of the outer loop are printed first in a clockwise manner then the
elements of the inner loop is printed. So, printing the elements of a looop can be solved using
four loops that print all the elements. Every 'for' loop defines a single direction movement 
along with the matrix. The first for loop represents the movement from left to right, whereas
the second crawl represents the movement from top to bottom, the third represents the movement
from the right to left, and the fourth represents the movement from bottom to up.
- Create and initialize variables k - starting row index, m -ending row index, l - starting
column index, n -ending column index
- Run a loop untill all the squares of loops are printed.
- In each outer loop traveral print the elements of a square in a clockwise manner.
- Print the top row, i.e. Print the elements of the kth row from column index l to n, and
increase the count of k.
- Print the right column, i.e. Print the last column or n-1th column from row index k to m and
decrease the count of n.
- Print the bottom row, i.e. if k<m, then print the elements of m-1th row from column n-1 to l 
and decrease the count of m
- Print the left column, i.e. if l<n, then print the elements of lth column from m-1th row to k 
and increase the count of l.


    Time Complexity: O(m*n). 
    To traverse the matrix O(m*n) time is required.
    Auxiliary Space: O(1). 
    No extra space is required.
"""

# program to print given matrix in spiral form

def spiral_print_two(m, n, a):
    k =0
    l =0

    '''
    k - starting row index
    m - ending row index
    l - starting column index
    n - ending column index
    i - iterator
    '''
    while(k < m and l < n):
        # print the first row from the remaining rows
        for i in range(l, n):
            print(a[k][i], end=" ")

        k += 1

        # Print the last column from the remaining columns
        for i in range(k, m):
            print(a[i][n-1], end=" ")
        n -=1

        # print the last row from the remaining rows
        if(k < m):
            for i in range(n-1, (l-1), -1):
                print(a[m-1][i], end=" ")
            m -= 1
        # print the first column from the remaining columns
        if(l < n):
            for i in range(m-1, k-1, -1):
                print(a[i][l], end=" ")
            l +=1

a = [[ 1, 2, 3, 4 ],
     [ 5, 6, 7, 8 ],
     [ 9, 10, 11, 12 ],
     [ 13, 14, 15, 16 ]]
  
R = 4
C = 4
  
spiral_print_two(R, C, a)

"""
Method 3: Recursive Approach
- The above problem can be solved by printing the boundary of the Matrix recursively. In each 
recursive call, we decrease the dimensions of the matrix. The idea of printing the boundary or
loops is the same.

Algorithm
- Create a recursive function that takes a matrix and some variables(k-starting row index, 
 m- ending row index, l-starting column index, n-ending column index) as parameters.
- Check the base cases(starting index is less than or equal to ending index) and print the 
boundary elements in clockwise manner
- Print the top row, i.e. Print the elements of kth row from column index l to n, and increase
the count of k
- Print the right column, i.e. Print the last column or n-1th column from row index k to m and 
decrease the count of n.
- Print the bottom row, i.e. if k>m, the print the elements of m-1th row from column n-1 to
l and decreaase the count of m
- Print the left column, i.e. if l < n, then print the elements of lth column from m-1th row to 
k and increase the count of l.
- Call the function recursively with the values of starting and ending indices of rows and 
columns.

    Time Complexity: O(m*n). 
    To traverse the matrix O(m*n) time is required.
    Auxiliary Space: O(1). 
    No extra space is required.

"""

# function for printing matrix in spiral form i, j: start index of matrix, row and column
# respectively m, n: End index of matrix row and column respectively
def print_data(arr,i, j, m, n):
    # if i or j lies outside the matrix
    if(i >=m or j>=n):
        return

    # print first row
    for p in range(i,n):
        print(arr[i][p], end=" ")

    # print last column
    for p in range(i + 1, m):
        print(arr[p][n-1], end=" ")
    
    # print Last Row, if Last and First Row are not same
    if((m -1) != i):
        for p in range(n-2, j-1, -1):
            print(arr[m-1][p], end=" ")

    # print first column, if last and first column are not same
    if((n-1) != j):
        for p in range(m-2, i, -1):
            print(arr[p][j], end=" ")
    print_data(arr, i+1, j +1, m-1, n-1)


R = 4
C = 4
arr = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]
print("\n end \n")
print_data(arr, 0, 0, R, C)

"""
Method 4: DFS Recursive Approach
- Another recursive approach is to consider DFS movement within the matrix
(right->down->left->up->right->..->end).

We do this by modifying the matrix itself such that when DFS algorithm visits each matrix cell
it's changed to a value which cannot be contained within the matrix. The DFS algorithm is 
terminated when it visits a cell such that all of its surrounding cells are already visited. 
The direction of the DFS search is controlled by a variable.

Algorithm:
1. Create a DFS function that takes matrix, cell indices and direction
2. checks are cell indices pointing to a valid cell(that is, not visited and in bounds)? if not,
skip this call
3. print cell value
4. mark matrix cell pointed by indicating as visited by changeing it to a value not supported
in the matrix
5. checks are surrounding cells valid? if not stop the algorithm, else continue
6. if the direction given is right then check,if the cell to the right is valid? if so, DFS
to the right cell given the steps above, else, change the direction to down and DFS downwards 
given the steps above.
7. else, if the direction given is down then check, if the cell to the down is valid? if so,
DFS to the cell below given the steps above, else, change the direction to left and DFS 
leftwards given the steps above.
8. else, if the direction given is left then check, if the cell to the left is valid? if so, DFS 
to the left cell given the steps above, else, change the direction to up and DFS upwards given 
the steps above.
9. else, if the direction given is up then check, if the cell to the up is valid? if so, DFS to 
the upper cell given the steps above, else, change the direction to right and DFS rightwards 
given the steps above.

    Time Complexity: O(m*n). To traverse the matrix O(m*n) time is required.
    Auxiliary Space: O(1). No extra space is required (without consideration of the stack used 
    by the recursion). 

"""
R = 4
C = 4
def is_in_bounds(i, j):
    global R
    global C
    if(i < 0 or i >= R or j < 0 or j >=C):
        return False
    return True

# check if the position is blocked
def is_blocked(matrix, i, j):
    if (not is_in_bounds(i, j)):
        return True
    if(matrix[i][j] == -1):
        return True

    return False

# DFS code to traverse spirally
def spirallyDFSTraverse(matrix, i, j, Dir, res):
    if(is_blocked(matrix, i, j)):
        return 
    allBlocked = True
    for k in range(-1, 2, 2):
        allBlocked= allBlocked and is_blocked(matrix, k+i, j) and is_blocked(matrix, i, j+k)
    res.append(matrix[i][j])
    matrix[i][j] = -1
    if(allBlocked):
        return

    # dir: 0 - right, 1 - down, 2 - left, 3 - up
    nxt_i = i
    nxt_j = j

    nxt_dir = Dir
    if(Dir == 0):
        if(not is_blocked(matrix, i, j+1)):
            nxt_j +=1
        else:
            nxt_dir = 1
            nxt_i +=1

    elif(Dir ==1):
        if(not is_blocked(matrix, i+1, j)):
            nxt_i +=1
        else:
            nxt_dir =2
            nxt_j -=1
    elif(Dir == 2):
        if(not is_blocked(matrix, i, j-1)):
            nxt_j -=1
        else:
            nxt_dir =3
            nxt_i -=1
    elif(Dir == 3):
        if(not is_blocked(matrix, i-1, j)):
            nxt_i -= 1
        else:
            nxt_dir = 0
            nxt_j += 1
    spirallyDFSTraverse(matrix, nxt_i, nxt_j, nxt_dir, res)

# To traverse spirally
def spirallyTraverse(matrix):
    res =[]
    spirallyDFSTraverse(matrix, 0, 0, 0, res)
    return res

print("\n \n")

a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
  
res = spirallyTraverse(a)
print(*res)