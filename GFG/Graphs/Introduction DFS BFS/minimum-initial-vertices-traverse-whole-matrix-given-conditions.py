"""
Minimum initial vertices to traverse whole matrix with given conditions

- We are given a matrix that contains different values in each cell. Our aim is to find
the minimal set of positions in the matrix such that the entire matrix can be traversed
starting from the positions in the set. We can traverse the matix under the following
conditions:
- We can move only to those neighbors that contain values less than or equal to the 
current cell's value. A neighbor of the cell is defined as the cell that shares a 
side with the given cell.

Input : 1 2 3
        2 3 1
        1 1 1
Output : 1 1
         0 2
If we start from 1, 1 we can cover 6 
vertices in the order (1, 1) -> (1, 0) -> (2, 0) 
-> (2, 1) -> (2, 2) -> (1, 2). We cannot cover
the entire matrix with this vertex. Remaining 
vertices can be covered (0, 2) -> (0, 1) -> (0, 0). 

Input : 3 3
        1 1
Output : 0 1
If we start from 0, 1, we can traverse 
the entire matrix from this single vertex 
in this order (0, 0) -> (0, 1) -> (1, 1) -> (1, 0). 
Traversing the matrix in this order 
satisfies all the conditions stated above.

From the above examples, we can easily identify that in order to use a minimum number of
positions, we have to start from the positions having the highest cell value. Therefore,
we pick the positions that contain the highest value in the matrix. We take the vertices
having the highest values in a seperate array. We perform DFS at every vertex starting 
from the highest value. If we encounter any unvisited vertex during dfs then we have
to include this vertex in our set. Then all the cells have been processed, then the set
contains the required vertices. 

How does this work?
We need to visit all vertices and reach the largest value we must start with them. If the
two largest values are not adjacent, then both of them must be picked. If the two 
largest values are adjacent, then any of them can be picked as moving to equal value 
neighbors is allowed.
"""

# program to find minimum initial vertices to reach whole matrix
MAX = 100

#(n, m) is current source cell from which we need to do DFS. N and M are total no. of 
# rows and columns.
def dfs(n, m, visit, ajd, N, M):
    # Marking the vertex as visited
    visit[n][m] = 1

    # If below neighbor is valid and has value less than or equal to current cell's value
    if(n+1 < N and adj[n][m] >= adj[n + 1][m] and not visit[n +1][m]):
        dfs(n + 1, m, visit, adj, N, M)

    # If right neigbor is valid and has value less than or equal to  current cell's value
    if(m + 1 < M and adj[n][m] >= adj[n][m+1] and not visit[n][m+1]):
        dfs(n, m + 1, visit, adj, N, M)

    # If above neighbor is valid and has value less than or equal to current cell's value
    if n - 1 >= 0 and adj[n][m] >= adj[n -1][m] and not visit[n -1][m]:
        dfs(n-1, m, visit, adj, N, M)

    # If left neighbor is valid and has value less than or equal to current cell's value
    if(m-1 >= 0 and adj[n][m] >= adj[n][m -1] and not visit[n][m-1]):
        dfs(n, m-1, visit, adj, N, M)

def printMinSources(adj, N, M):
    # storing the cell value and cell indices in a vector
    x = []

    for i in range(N):
        for j in range(M):
            x.append([adj[i][j], [i, j]])

    # sorting the newly created array according to cells values
    x.sort()

    # Create a visited array for DFS and initialize it as false.
    visit =[[ False for i in range(MAX)] for i in range(N)]

    # Applying dfs for each vertex with highest value
    for i in range(len(x) - 1, -1, -1):

        # if the given vertex is not visited then include it in the set
        if(not visit[x[i][1][0]] [x[i][1][1]]):
            print('{} {}'.format(x[i][1][0],x[i][1][1]))

            dfs(x[i][1][0],
                x[i][1][1],
                visit, adj, N, M)

            
if __name__=='__main__':
 
    N = 2
    M = 2
  
    adj = [ [ 3, 3 ], [ 1, 1 ] ]
     
    printMinSources(adj, N, M)
