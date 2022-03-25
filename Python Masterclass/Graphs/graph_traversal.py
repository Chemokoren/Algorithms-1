"""
Uses of Grph Traversal
- peer to peer networking
- web crawlers
- finding "closest"
matches/recommendations
-shortest path problems
    - GPS Navigation
    - Solving mazes
    - AI(Shortest path to win the game)

DFS
- explore as far as possible down one branch before "backtracking" (deepen before you 
widen or prioritize children over siblings)

DFS Recursive Pseudocode

DFS(vertex):
    if vertex is empty
        return (this is the base case)
    add vertex to results list
    mark vertex as visited
    for each neighbor in vertex's neighbors:
        if neighbor is not visited:
            recursively call DFS on neighbor


Detailed Pseudocode (Recursive)

- The function should accept a starting node
- Create a list to store the end result, to be returned at the very end
- Create an object to store visited vertices
- Create a helper function which accepts a vertex
    - The helper function should return early if the vertex is empty
    - The helper function should place the vertex it accepts into the visited object and
    push that vertex into the result array.
    - Loop over all of the values in the adjacencyList for that vertex
    - If any of those values have not been visited, recursively invoke the helper function
    with that vertex
- invoke the helper function with a starting vertex
- return the results array

DFS Iterative Pseudocode

DFS-iterative(start):
let S be a stack
S.push(start)

while S is not empty
    vertex = S.pop()
    if vertex is not labeled as discovered:
        visit vertex (add to result list)
        lavel vertex as discored
        for each of vertex's neighbors, N do
            S.push(N)

Detailed Pseudocode (Iterative)

- The function should accept a starting node
- Create a stack to help us keep track of vertices(use a list/array)
- Create a list to store the end result, to be returned at the very end
- Create an object to store visited vertices
- Add the starting vertex to the stack, and mark it visited
- While the stack has something in it:
    -pop the next vertex from the stack
    - if that vertex hasn't been visited yet:
        - mark it as visited
        - add it to the result list
        - push all of its neighbors into the stack
- return the result array

"""
import sys
sys.setrecursionlimit(1500)

class Graph():

    def __init__(self) -> None:
        self.adjacency_list ={}

    def addVertex(self,vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] =[]

    def addEdge(self,vertex1,vertex2):
        if vertex1 in self.adjacency_list: 
            self.adjacency_list[vertex1].append(vertex2)
        if vertex2 in self.adjacency_list: 
            self.adjacency_list[vertex2].append(vertex1)
    
    def removeEdge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list: 
            self.adjacency_list[vertex1].remove(vertex2)
        if vertex2 in self.adjacency_list: 
            self.adjacency_list[vertex2].remove(vertex1)

    def removeVertex(self, vertex):
        # if vertex1 in self.adjacency_list: 
        while len(self.adjacency_list[vertex]):
            item =self.adjacency_list[vertex].pop()
            self.removeEdge(vertex,item)
                # 
            # self.adjacency_list.pop(vertex1)
    
    # def __init__(self, start_node) -> None:
    

    def __str__(self) -> str:
        print(self.adjacency_list)

    def RecursiveDFS(self, vertex):
        result =[]
        visited ={}

        def dfs(vertex):
            if not vertex:
                return None
            if vertex not in  visited:
                visited[vertex]=True
                result.append(vertex)
                for i in self.adjacency_list[vertex]:
                    if i not in visited:
                        dfs(i)
            return result
        return dfs(vertex)

    


#                   A
#                 /   \
#                B     C
#                |     |
#                D --- E
#                 \   /   
#                   F    
g = Graph()
g.addVertex("A")
g.addVertex("B")
g.addVertex("C")
g.addVertex("D")
g.addVertex("E")
g.addVertex("F")

g.addEdge("A", "B")
g.addEdge("A", "C")
g.addEdge("B", "D")
g.addEdge("C", "E")
g.addEdge("D", "E")
g.addEdge("D", "F")
g.addEdge("E", "F")
g.__str__()
print("result: ",g.RecursiveDFS("A"))
