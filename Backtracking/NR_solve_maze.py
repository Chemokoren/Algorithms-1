"""
Backtracking solves problems by trying a series of actions. If a series fails, we back up and try a different
series.

A maze is a classic example, but the approach can be used on a wide variety of problems. 

Basically any problem that can be described as a series of discreet choices can be worked using the 
backtracking idea.

When the performance difference between solutions is small, the best choice to solve a problem may just be
whichever one that makes the most sense to you.

"""

def NR_solve_maze(maze, start, finish):
    visited=[]
    path =[]

    path.append(start)
    currentPoint = start
    visited.append(currentPoint)

    while(path[-1] !=finish and len(path) !=0):
        iter =maze[currentPoint]
        foundOutlet = False
        while((iter !=maze[currentPoint]) and (not foundOutlet)):

            # check if connection leads to unvisited point
            if(visited.__contains__(iter) == False):
                foundOutlet =True
            else:
                iter +=1

            if(foundOutlet):
                path.append(iter)
                visited.append(iter)
            else:
                path.pop()
            currentPoint=path[-1]
    return path

'''
maze
'''

# maze =[
#     [1,1,1,1,1],
#     [0,1,0,0,0],
#     [1,1,1,1,1],
#     [1,0,0,0,0],
#     [1,1,1,1,1]
# ]

maze =[
    [1,1,1,1,1],
    [0,0,0,0,1],
    [1,1,1,1,1],
    [1,0,0,0,0],
    [1,1,1,1,1]
]

row =len(maze)
col =len(maze[0])

def print_sol(sol):
    for i in sol:
        for j in i:
            print(str(j),end=' ')
        print()


def isSafe(maze, x, y):
    if 0 <= x < row and 0 <= y < col and maze[x][y] ==1:
        return True
    return False

def solvemaze(maze, x, y, sol, d):
    if x == row-1 and y==col-1:
        sol[x][y]=1
        return True

    if isSafe(maze, x, y):
        sol[x][y] =1
        if d !='up' and solvemaze(maze, x+1, y, sol, 'down'): # down
            return True
        if d !='left' and solvemaze(maze,x, y+1, sol, 'right'): # right
            return True
        if d !='down' and solvemaze(maze, x-1, y , sol, 'up'): # up
            return True
        if d !='right' and solvemaze(maze, x, y-1, sol, 'left'): # left
            return True
        sol[x][y] = 0
        return False

def solution(maze, row, col):
    sol=[[0 for j in range(col)]for i in range(row)]
    if not(solvemaze(maze, 0, 0, sol, 'down')):
        return 'no path'
    print_sol(sol)
    return True


print(solution(maze,row, col))