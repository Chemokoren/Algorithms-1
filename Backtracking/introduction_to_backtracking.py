"""
 specific types of problems that lie under backtracking 

1) Decision Making ~ It means the problem where you have choices like whether to go left,
down, up, or down. 

2) Permutations ~ To find all possible permutations of any sequence data type we can 
use backtracking.

3) Subsets ~ Programming question where we are supposed to find all possible subset,
subsequence-like things from any sequence data type then they are mostly solved 
using Backtracking.


How to Identify the Backtracking Problem

Some basic points that help in identifying the problem are backtracking.

    - Exponential Complexity or Factorial Complexity ~ You will be given that solution 
    can be expected in exponential complexity because you have to explore each and every 
    path.
    - Constraints ~ If complexity is more then obviously constraints will be less like
    N is less than 500.
    - No guarantee that which path to go first to find a solution because you are asked 
    to find any solution or all possible solutions.

1) Subset of a set
- Given a set of distinct integers, form a different subset of one single set.

# sample input 
set =[1,2,3]

# sample output
[[],[1],[1,2],[1,2,3],[1,3],[2],[2,3],[3]]


Explanation - One we can have an empty set as a subset of set and break all integers with 
every other element which forms a subset. 
on reversing a subset it is also a subset because both are the same so keep only one.

"""

from matplotlib.pyplot import grid


def findAllSubset(arr, subset, idx):
    print(*subset)
    for i in range(idx, len(arr)):
        subset.append(arr[i])

        # recursive call for each forward element
        # so set with 1 element as well as double and further will be in res
        findAllSubset(arr, subset, i +1)

        # remove the arr[i] from subset by doing backtracking
        subset.pop(-1)

    return

arr =[1,2,3]
subset =[]
idx =0
findAllSubset(arr, subset, idx)


"""
2) Generate All Valid IP Addresses

The problem statement is something like we are given a string containing only digits. 
our task is to generate all possible IPv4 Address combinations and print each 
combination in lexicographic order. 

🔰NOTE - A valid IPv4 address contains exactly four integers. each integer is between 0
and 255 separated by single dots, and cannot have leading zeros except in the case of 
zero itself. 
read the example snippet below to get a better idea about what the IPv4 address should look like.

// The following are valid IP addresses:
0.1.24.255
18.5.244.1

// Following are invalid IP addresses:
0.01.24.255  (as  01  contains one leading zero).
18.312.244.1 (as 312 not lies between 0 and 255).

// Sample Input 1 :
2 
2122
23579

// Sample Output 1 :
[“2.1.2.2”]
[“2.3.5.79”, “2.3.57.9”, “2.35.7.9”, “23.5.7.9”]

--------------------------------------------------

// Sample Input 2 :
2
123
02300

// Sample Output 2 :
[]
[“0.2.30.0”, “0.23.0.0”]

Approach to Solve the Problem 😃

Each four-part of IP address should be in the range of 0 to 255. To generate all possible 
approaches we need to break a string into four different parts and check whether each 
part is a valid part or not. 

If it is valid then we will form its combination by placing the dots and saving the
solution. So we can approach this problem using iterative as well as recursive ways. 

So let us discuss each approach because the time complexity of both is the same. So,
both the solution will work absolutely fine.

A] Iterative Approach (Brute-Force method)
------------------------------------------

As we discuss, the idea is to divide the string into four parts and check if each part 
is valid and form its combination using 3 dots and add it to the resultant list. 

To check the valid part it must satisfy the  below 2 conditions.

    - Each part must be between 0 and 255
    - No part should have leading zeros.

So we have to run a three-loop to complete the algorithm where we say that the first part
is from 0 to I, the second part is I+1 to J, the third part is J+1 to K, 
and the fourth part is from K+1 to  N(length of the string). 

So we can conclude the algorithm in the below steps.

    - Create a function to check whether each part is valid or not.
    - Create an empty list of results to store each combination
    - Now we will run 3 loops.
        - First will be I from 0 to n-3 which represents that it is the first part and 
        after it, 3 parts are also there so the last 3 digits of string can never come
        in the first part.
        - The second loop (j) will be from i+1 to n-2 which represents that the second 
        part is after the last digit of the first part and after it, two more parts are 
        present so the last 2 digits can never be part of the second part.
        - The third loop (k) will be from j+1 to n-1 which represents that the third part 
        is after the last digit of the second part and after it, 
        one more part is present which should have at least one integer.
        - The last part will be after k+1 to n so no loop is required for it.

"""

def checkPart(part):
    # if it is empty, space, or greater then 3 then Invalid
    if len(part) < 0 or len(part) >3:
        return False
    # if first char is 0 then it should only be 0
    if part[0] == "0":
        if len(part) != 1:
            return False
    # range between 0 - 255
    if int(part) < 0 or int(part)>255:
        return False
    return True

def isValidIP(s,i, j, k):
    # let's form all four parts
    first =s[:i+1]
    second=s[i+1:j+1]
    third =s[j+1:k+1]
    fourth = s[k+1:]

    # check if all four are valid then IP is valid
    if(checkPart(first) and checkPart(second) and checkPart(third) and checkPart(fourth)):
        return True
    return False

def main(s):
    res =[] # to store all possible combs
    n = len(s)
    for i in range(0, n-3):
        for j in range(i+1, n-2):
            for k in range(j+1, n-1):
                if isValidIP(s,i, j, k):
                    ip =s[:i+1] +"."+s[i+1:j+1]+"."+s[j+1:k+1]+"."+s[k+1:]
                    res.append(ip)
    return res

# s = input("input a valid ip string")
# res=main(s)
# res.sort()
# print(res)

"""

B] Backtracking Approach

- The key idea of observation here is we can select either  1 or 2 or 3 digits at a time
so in each step, we will select 1,2,3 digits and move to next segment. 
Before moving we will also check that the current segment  is valid of not. If it is not 
valid then there is no need to explore this path. 

backtracking steps:
- Create check functions that accept strings and check their validity for valid IP
addresses
- We define an empty list to store all possible combinations.
- We implement a function e.g. backtracking which accepts 5 arguments as an original 
string(s), answer, current index(denoting current index), segments used to store segments,
segment index which is used to store the current number of segments we are currently in.
- The initial current index and segment index will be 0.

Base Case
- If the current index is equal to N and the segment index is 4 then add the current path
to answer and return.
- The recursion will also break when the current index equals N and the segment index 
is greater than 4

Constraints
- Add s[currentIndex+steps] to segment[segmentIndex]
- If the current index is valid then we will recur for the next segment and increase the
current index and segment index by 1
-Else if it is not valid then we will move to the next iteration


Complexity
- Time complexity is O(1)
- In the worst case, the total number of IP addresses is fixed so our function will remain
constant after some particular value of the input. Hence the time complexity will be O(1)
-Space Complexity is O(1) - we used constant extra space
"""
# check for part is valid or not
#check for part is valid or not
def isValidIP(part):
    if part == "" or len(part) > 3:
        return False
        
    if part[0] == "0" and len(part) != 1:
        return False
            
    if int(part) < 0 or int(part) > 255:
        return False
        
    return True

# def validIPAddressBacktracking(ip, answer, curridx, segment, segnum):
#     if curridx == len(ip) and segnum == 4:
#         temp = ".".join(segment)
#         answer.append(temp)
#         return
        
#     if curridx >= len(s) or segnum >= 4:
#         return
        
#     curr_part = ""
#     for i in range(1, 4):
#         print("aa:", i)
#         curr_part = s[curridx: curridx+i]
#         if isValidIP(curr_part):
#             segment[segnum] = curr_part
#             validIPAddressBacktracking(ip, answer, curridx+i, segment, segnum+1)
            
#     return
    
# s = "23579"
# global answer
# answer = []
# segment = [""] * 4

def validIPAddressBacktracking(ip):
    answer = []
    curridx = 0
    segment = [""] * 4
    segnum =0


    def backtracking(ip,curridx, segment,segnum):
        if curridx == len(ip) and segnum == 4:
            temp = ".".join(segment)
            answer.append(temp)
            return
            
        if curridx >= len(s) or segnum >= 4:
            return
            
        curr_part = ""
        for i in range(1, 4):
            curr_part = s[curridx: curridx+i]
            if isValidIP(curr_part):
                segment[segnum] = curr_part
                backtracking(ip, curridx+i, segment, segnum+1)
        
    backtracking(ip,curridx,segment,segnum)
    return answer
    
s = "23579"

print("######################## backtracking ########################")
print("sol:::", validIPAddressBacktracking(s))


print("######################## Rat in a maze ########################\n")

"""
Rat in a maze
--------------

Has different names like: Shortest Path in a maze, Total steps in the path to reach a
destination

We are given an N*N matrix of binary value blocks where the source cell is the upper 
left most block  and the destination block is the lower rightmost block.

The rat can only move in two directions as forward and downward.

If the block number is 0 then it means it is a dead block(No entry) and the rat cannot 
visit there. 
If the block value is 1 then it is a valid block. 
Find if there is a way to reach the destination and find the path and print it.

Input and Output Format

-Given N as input denoting the number of rows and number of columns. And form N rows
with N space-seperated digits which form N*N Grid.
Return True if there exists a path to reach destination cell from source cell.
Otherwise return False if no such path exists.

// Sample Input - 1

N = 4

1  0  0  0 
1  1  0  0 
0  1  0  0 
0  1  1  1

// Sample Output - 1
True

Backtracking Approach
-Using recursion we will start from the initial position of the rat and check-in right and
down direction to see if it is a safe path to move forward. 
- If the path is valid then we move forward and again check both directions recursively.
Whichever path gives us the solution after reaching the destination we return. 
- If we reach a dead-end before reaching the destination then we backtrack and start 
exploring another path.

Algorithm
- main function accepts the maze(matrixx) a nd the source position of the rat in a maze
- Create an empty matrix solution to store the path filled with 0's
- Create a recursive function that accepts the initial matrix, rat position coordinates,
solution matrix, and length of a matrix.
- Our base case is if we reach the destination then we have a valid path
- We check whether the current position is valid or not. If it is valid then check if it is already 
part of the solution matrix.
- Otherwise, add the path in the solution matrix and explore other paths in both the forward and 
downward directions using recursion.
- If any path is not valid then backtrack and explore other paths.

"""
n = 4
def is_safe(maze, x, y):
    if x >= 0 and x < n and y>=0 and y <n and maze[x][y] ==1:
        return True
    return False

def solve_maze_util(maze, x, y, sol):
    # if x and y is the goal then return True from here only
    if x == n-1 and y == n-1 and maze[x][y]==1:
        sol[x][y]= 1
        return True

    # check if x-y pos is valid
    if is_safe(maze, x, y):

        # if it is already part of sol
        if sol[x][y] == 1:
            return False

        # mark x-y as safe
        sol[x][y] = 1

        #move forward in x-direction
        if solve_maze_util(maze, x+1, y, sol):
            return True
        
        # if x does not give sol then try to move in y direction
        if solve_maze_util(maze, x, y+1, sol):
            return True

        # if moving forward in either x-y does not give sol then backtrack
        if solve_maze_util(maze, x-1, y, sol):
            return True

        if solve_maze_util(maze, x, y-1, sol):
            return True

        sol[x][y] = 0
        return False
    
def solve_maze(maze):
    sol =[[0 for j in range((4))] for i in range(4)]
    if solve_maze_util(maze, 0, 0, sol)==False:
        print("solution does not exist")
        return False
    return True

maze = [[1, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 1, 0, 0],
        [1, 1, 1, 1] 
       ]
              
print(solve_maze(maze))



"""

N-Queens Puzzle Problem
-----------------------

Name of the problem differes for example:
    - N-Queens problem to return any solution
    - N-Queens problem to return all possible solutions.
You are given an N*N matrix(square chessboard), and your task is to find all the possible 
ways that you can place N number of queens on that board such that no two queens 
can attack each other.

Chance of Two Queens attacking each-other
- If two queens are placed in the same Row
- If the two queens are placed in the same column
- If the two queens are placed in the same Diagonal.

Initially, we have a board of N*N which has all the values as 0. Now we have to find
the feasible place of Queens and change 0 to 1 and if you can place N queens in N*N
return the solution

Input and Output Format
-The first line of input contains the number of a test case and each line of the test case
 contains an integer 'N' denoting the size of the chessboard. 
 For each test case, print all the possible solutions If no solution is possitble then
 print an empty list.


// Sample Input 1:

4   

// Sample Output 1:

0 0 1 0
1 0 0 0 
0 0 0 1 
0 1 0 0

0 1 0 0
0 0 0 1 
1 0 0 0 
0 0 1 0 

Explanation

The 4 queens can be placed in a 4*4 chessboard in two ways.


Backtracking approach
- So in each row, we have to check each position that is safe to place the Queen and if 
it is safe, then we can move to the next row and do the same till we do not reach the
Nth row.
-And if in that row, position is not safe then we have to move to the next column in 
the same row till we find a safe place in the row.
- Now, if we are not able to find any safe place in that row, it means that in the above
row, we have placed the queen in the wrong position so we will backtrack from there and 
change the position of the queen in the previous row.


How to check that position is safe or not?

- we already know that if one queen is already there in the same row, column, or diagonal
then we cannot place a queen. 
- So, we will have the position of row and column where we want to place a queen and 
we also know that the initial matrix contains all zeros  and that means if already a 
queen is there, it can only be present before our current position.
-So, we will check only in the above row and column position then the current position
- If a queen is already present in this direction then we cannot place a queen at the
current position else it is valid. 

"""

def n_queens(n):

    res =[]

    def is_safe(mat, row, col):
        for i in range(row):
            if mat[i][col] ==1:
                return False

        # check if queen is already present in upper left diagonal
        i, j = row, col

        while i>=0 and j >=0:
            if mat[i][j] ==1:
                return False
            i = i -1
            j = j -1

        # check for upper right diagonal
        i, j = row, col
        while i >=0 and j < len(mat):
            if mat[i][j] == 1:
                return False
            i = i - 1
            j = j + 1
        
        return True

    # function to add solution
    def add_solution(chessboard):
        currans =[]
        for i in chessboard:
            currans.extend(i)
        res.append(currans)
    
    # recursive function
    def solve_n_queens(mat, row):
        if row ==len(mat):
            add_solution(mat)
            return

        for i in range(len(mat)):
            if is_safe(mat, row, i):
                mat[row][i] =1

                solve_n_queens(mat, row+1)

                mat[row][i] = 0

    mat =[[0 for _ in range(n)] for _ in range(n)]
    solve_n_queens(mat,0)
    return res
n =4
res =n_queens(n)
print(res)

"""
Given a 9*9 matrix in which some cells are filled with numbers between 1-9 and some cells are empty
(denoted by 0). You need to find a way to fill the empty cells with some digits (between 1-9) such that the
final matrix represents a valid sudoku solution. 
The question is also asked like whether there exists a solution to solve this puzzle. If yes then return True 
Otherwise return False.

A sudoku solution is valid if it satisfies the following conditions

    -In each row, all unique digits should be there (digits between 1-9 occur only once)
    -In each column, unique digits should be there (digits between 1-9 occur only once)
    -Each of digits 1-9 must occur exactly once in each of the 9, 3*3 sub-matrices of a matrix.

// Sample Input - 1

3 0 6 5 0 8 4 0 0 
5 2 0 0 0 0 0 0 0 
0 8 7 0 0 0 0 3 1 
0 0 3 0 1 0 0 8 0 
9 0 0 8 6 3 0 0 5 
0 5 0 0 9 0 6 0 0 
1 3 0 0 0 0 2 5 0 
0 0 0 0 0 0 0 7 4 
0 0 5 2 0 6 3 0 0 

// Sample Output - 1

3 1 6 5 7 8 4 9 2
5 2 9 1 3 4 7 6 8
4 8 7 6 2 9 5 3 1
2 6 3 4 1 5 9 8 7
9 7 4 8 6 3 1 2 5
8 5 1 7 9 2 6 4 3
1 3 8 9 4 7 2 5 6
6 9 2 3 5 1 8 7 4
7 4 5 2 8 6 3 1 9


Backtracking approach

- So the approach is we have to start from the top-left position array[0][0] to the bottom right 
array[8][8] and check for each position. If the position is already filled then we can simply move forward, 
Otherwise, it's our responsibility to find the digit between 1-9 which fits best at that position.


Algorithm:
-implement a function that accepts a Grid, row, and column value. Initially, we have to start with a 0-0
position, so the value of the row and column will be 0
- Check if the current position is already filled then we have to move to the next position which has two
cases.
    - we have to check that the current column is not last, which means we have to move to the next row
    because the matrix ends here
    - If we are not in the next column then in the same row we have to move forward meaning increasing the
    column by 1
- If the value at the current position is empty(denoted as 0) then we will run a loop from 1 to 9 and for
each value, we will check if this position is safe for the value then we will insert that value. And then 
we will move forward in the same way  as we have done in the above step.
-In any case, if we are not able to fill the next value in the next row, then we will backtrack to the 
previous value and make it zero, and check it for another value that is safe at that position.

In this way, if we successfully reach the last row and can fill it correctly then we have solved sudoku. 
The base case will be when row will be equal to 9 it means we have successfully reached a valid sudoku
solution. And for checking the value is valid or not we will build a separate function to check the value
should be unique in a row, column, and in a 3*3 sub-matrix.

"""

###CONSTRAINT-1 (All elements in row should be unique)
def row_valid(row, col, grid, k):
    for i in range(9):
        if grid[row][i] == k:
            return False
    return True
    
###CONSTRAINT-2 (All elements in column should be unique)
def column_valid(row, col, grid, k):
    for i in range(9):
        if grid[i][col] == k:
            return False
    return True
    
###CONSTRAINT-3 (All elements in sub-matrix should be unique) 
## 9*9 grid divided into 3*3 sub-matrix of 9 elements
def subbox_valid(row, col, grid, k):
    for i in range(0, 9, 3):
        if row >= i and row  < i+3:
            row_start = i
            row_end = i+3
        
        if col >= i and col < i+3:
            col_start = i
            col_end = i+3 
    
    for i in range(row_start, row_end):
        for j in range(col_start, col_end):
            if grid[i][j] == k:
                return False
                
    #else k in unique so return True
    return True

# Function which will check all the three cond is valid on element at cur pos
def valid(row, col, grid, k):
    if (row_valid(row, col, grid, k) and column_valid(row, col, grid, k) and subbox_valid(row, col, grid, k)):
        return True
    
    return False

# Backtracking and solving SUDOKU Logic
def SUDOKU(i, j, grid):
    ## Base case 
    if i == len(grid):
        return True

    #If the element is present (already filled)
    if grid[i][j] != 0:
        if j == 8:
            #chang the row(new row)
            return SUDOKU(i+1, 0, grid)
        else:
            #chang the col
            return SUDOKU(i, j+1, grid)
            
    #Else element is not filled
    for k in range(1, 10):
        if valid(i, j, grid, k):
            grid[i][j] = k
            if j==8:
                if(SUDOKU(i+1, 0, grid)):
                    return True
            else:
                if(SUDOKU(i, j+1, grid)):
                    return True
            #Backtracking
            grid[i][j] = 0
    
    return False
    
def main(grid):
    #If sol find then True, else False
    print(SUDOKU(0, 0, grid))


# global grid
grid = [ [3, 0, 6, 5, 0, 8, 4, 0, 0], 
         [5, 2, 0, 0, 0, 0, 0, 0, 0], 
         [0, 8, 7, 0, 0, 0, 0, 3, 1], 
         [0, 0, 3, 0, 1, 0, 0, 8, 0], 
         [9, 0, 0, 8, 6, 3, 0, 0, 5], 
         [0, 5, 0, 0, 9, 0, 6, 0, 0], 
         [1, 3, 0, 0, 0, 0, 2, 5, 0], 
         [0, 0, 0, 0, 0, 0, 0, 7, 4], 
         [0, 0, 5, 2, 0, 6, 3, 0, 0] 
        ]

main(grid)

#If you want to print the sol row-wise in space separated way
for row in grid:
    print(*row)




'''
-Backtracking is a general algorithm for finding all(or some )solutions to some computational problems, that
incrementally builds candidates to the solutions.
-As soon as it determines that a candidate cannot possibly lead to a valid complete solution, it abandons 
this partial candidate and "backtracks" (return to the upper level) and reset to the upper level's state so
that the search process can continue to explore the next branch.
- Backtracking is all about choices and consequences, making the most suitable algorithm for solving 
constraint satisfaction problem(CSP).
-CSPs are mathematical questions defined as a set of objects whose state must satisfy a number of constraints
or limitations e.g.
        - Eight Queens puzzle
        - Map coloring problem
        - Sudoku
        - Crosswords
        - Many other logic puzzles
Properties and Applications
- No Repetition and Completion: It is a systematic generating method that avoids repetitions and missing any 
possible right solution. This property makes it ideal for solving combinatorial problems such as combination
and permutation which requires us to enumerate all possible solutions.
- Search Pruning: Because the final solution is built incrementally, in the process of working with partial
solutions, we can evaluate the partial solution and prune branches that would never lead to the acceptable
complete solution: either it is invalid configuration or it is worse thn known possible complete solution.

Scope
1. Show property 1: How backtrack construct the complete solution incrementally and how it backtrack to its 
previous state.
2. implicit graph: Enumerating all the paths between the source and the target vertex in a graph drawing
3. Show property 2: Demonstrate the application of search pruning in backtracking through CSP problems 
like sudoku

Permutation
-----------
Given a set of integers {1,2,3}, enumerate all the possible permutations using all the items from the set
without repetition. A permutation describes an arrangement or ordering of items. It is trivial to figure
out that we can have the following six permutations: [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], and [3, 2, 1].

                            []
                
                [1]         [2]             [3]

        [1,2]   [1,3]   [2,1]   [2,3]   [3,1]   [3,2]

        [1,2,3] [1,3,2] [2,1,3] [2,3,1] [3,1,2] [3,2,1]

This is a combinatorial problem.

To construct the final solution, we can start from an empty ordering shown at the first level, [ ]. 
Then we try to add one item where we have three choices :1, 2, and 3. We get three partial 
solutions [1], [2], [3] at the second level. 
Next, for each of these partial solutions, we have two choices, for [1], we can either put 2 or 3 first. 
Similarly, for [2], we can do either 1 and 3, and so on. 
Given n distinct items, the number of possible permutations are n*(n-1)*…*1 = n!.

Implicit Graph
-Each node is either a partial or final solution in the graph
-Examining it as a tree reveals the internal node as a partial solution and all leaves are final solutions.
-One edge represents generating the next solution based on the current solution.
-The vertices and edges are not given by an explicitly defined graph or trees, the vertices are generated 
on the fly and the edges are implicit relation between these nodes.

Backtracking and DFS
--------------------
- The implementation of the state transfer we can use either BFS or DFS on the implicit vertices
- DFS is preferred because theoretically it takes O(log n!) space used by stack while BFS uses n! because
of the number of vertices saved in the queue.

With recursive DFS, we can start from node [], and traverse to [1,2], then [1,2,3]. Then we backtrack to 
[1,2], backtrack to [1], and go to [1, 3], to [1, 3, 2]. To clear the relation between backtracking and DFS,
we can say backtracking is a complete search technique and DFS is an ideal way to implement it.

We can generalize Permutation, Permutations refer to the permutation of n things taken kat a time without
repetition, the math formula is A_{n}^{k} = n *(n-1)*(n-2)*…*k. In Fig above, we can see from each level kshows
all the solution of A_{n}^{k}. The generation of A_{n}^{k} is shown in the following Python Code:

'''
    
def a_n_k(a, n, k, depth, used, curr, ans):
  '''
  Implement permutation of k items out  of n items
  depth: start from 0, and represent the depth of the search
  used: track what items are  in the partial solution from the set of n
  curr: the current partial solution
  ans: collect all the valide solutions
  '''
  if depth == k: #end condition
    ans.append(curr[::]) # use deepcopy because curr is tracking all partial solution, it eventually become []
    return
  
  for i in range(n):
    if not used[i]:
      # generate the next solution from curr
      curr.append(a[i])
      used[i] = True
      print(curr)
      # move to the next solution
      a_n_k(a, n, k, depth+1, used, curr, ans)
      
      #backtrack to previous partial state
      curr.pop()
      print('backtrack: ', curr)
      used[i] = False
  return


print("################################# permutations #################################\n")
a = [1, 2, 3]
n = len(a)
ans = [[None]]
used = [False] * len(a)
ans = []
a_n_k(a, n, n, 0, used, [], ans)
print(ans)


'''
Two Passes

Therefore, we can say backtrack visit these implicit vertices in two passes: First forward pass to build the 
solution incrementally, second backward pass to backtrack to previous state. We can see within these two 
passes, the curr list is used as all vertices, and it start with [] and end with []. This is the character of 
backtracking.

Time Complexity of Permutation

In the example of permutation, we can see that backtracking only visit each state once. The complexity of this
is similar to the graph traversal of O(|V|+|E|), where |V| = \sum_{i=0}^{n}{A_{n}^{k}}, because it is a tree 
structure, |E| = |v|-1. This actually makes the permutation problem NP-hard.

'''

def c_n_k(a,n,k,start, depth, curr, ans):
    '''
    Implement combination of k items out of n items
    start: the start of candinate
    depth: start from 0, and represent the depth of the search
    curr: the current partial solution
    ans: collect all the valid solutions
    '''
    if depth ==k: # end condition
        ans.append(curr[::])
        return
    for i in range(start, n):
        # generate the next solution from curr
        curr.append(a[i])
        # move to the next solution
        c_n_k(a,n, k,i+1,depth+1,curr, ans)

        #backtrack to previous partial state
        curr.pop()
    return

print("################################# combination #################################\n")
a = [1, 2, 3]
n = len(a)
ans = [[None]]
ans = []
c_n_k(a, n, 2, 0, 0, [], ans)
print(ans)

"""
References:

https://www.crazytechie.com/2022/02/popular-backtracking-problems-explained-in-python-from-scratch.html

"""