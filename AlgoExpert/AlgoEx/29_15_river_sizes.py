"""
River sizes

Expected: [1, 2, 2, 2, 5]

1   0   0   1   0

1   0   1   0   0

0   0   1   0   1

1   0   1   0   1

1   0   1   1   0

you are given a matrix(two-dimensional array) which does not necessarily have an equal width  
and height. The matrix consists of only 0's and 1's. Every 0 represents a part of land and 
every 1 represents a part of a river.A river basically consists of a bunch of 1's that are
adjacent next to each other horizontally or vertically. 
You have to write a function/algorithm that returns an array of all the sizes of the rivers
contained in the matrix.
"""
# O(wh)or (n) time | O(wh) space where n is the total number of items in the matrix
def riverSizes(matrix):
    sizes =[]
    visited =[[False for value in row] for row in matrix]
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if visited[i][j]:
                continue
            traverseNode(i,j,matrix,visited, sizes)
    return sizes

def traverseNode(i, j, matrix, visited, sizes):
    currentRiverSize = 0
    nodesToExplore =[[i, j]] # stack
    while len(nodesToExplore):
        currentNode = nodesToExplore.pop()
        i = currentNode[0]
        j = currentNode[1]
        if visited[i][j]:
            continue
        visited[i][j] = True

        if matrix[i][j]== 0:
            continue
        currentRiverSize += 1
        unvisitedNeighbors = getUnvisitedNeighbors(i, j, matrix, visited)
        for neighbor in unvisitedNeighbors:
            nodesToExplore.append(neighbor)
    if currentRiverSize > 0:
        sizes.append(currentRiverSize)

def getUnvisitedNeighbors(i, j, matrix, visited):
    unvisitedNeighbors = []
    if i > 0 and not visited[i -1][j]:
        unvisitedNeighbors.append([i -1, j])
    if i < len(matrix) -1 and not visited[i + 1][j]:
        unvisitedNeighbors.append([i+1, j])
    if j > 0 and not visited[i][j-1]:
        unvisitedNeighbors.append([i, j-1])
    if j < len(matrix[0]) -1  and not visited[i][j+1]:
        unvisitedNeighbors.append([i, j+1])
    return unvisitedNeighbors
