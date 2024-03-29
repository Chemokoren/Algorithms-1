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
        label vertex as discovered
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
        while len(self.adjacency_list[vertex]):
            for i in self.adjacency_list[vertex]:
                self.removeEdge(vertex,i)

        self.adjacency_list.pop(vertex)
    

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

    '''
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
    '''
    def IterativeDFS(self, vertex):
        s =[]
        result =[]
        visited ={}

        s.append(vertex)

        while s:
            print(s)
            item =s.pop()
            if item not in visited:
                visited[item]=True
                result.append(item)
                for i in self.adjacency_list[item]:
                    s.append(i)
        return result

    def IterativeDFSMain(self, vertex):
        s =[]
        result =[]
        visited ={}

        s.append(vertex)
        visited[vertex]=True


        while s:
            print(s)
            item =s.pop()
            result.append(item)
            
            for i in self.adjacency_list[item]:
                if i not in visited:
                    visited[i]=True
                    s.append(i)
        return result


    '''
    BFS
    - This function should accept a starting vertex
    - Create a queue(you can use an array) and place the starting vertex in it
    - create an array to store the nodes visited
    - Create an object to store nodes visited
    - Mark the starting vertex as visited
    - Loop as long as there is anything in the queue
    - Remove the first vertex from the queue and push it into the array that stores nodes visited
    - Loop over each vertex in the adjacency list for the vertex you are visiting
    - If it is not inside the object that stores nodes visited, mark it as visited and 
    enque that vertex
    - Once you have finished looping, return the array of visited nodes

    '''
    def BFS(self, vertex):
        queue =[vertex]
        result =[]
        visited={}

        visited[vertex]=True

        while queue:
            item = queue.pop(0)
            result.append(item)

            for i in (self.adjacency_list[item])[::-1]:
                if i not in visited:
                    visited[i]=True
                    queue.append(i)
        return result



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
print("DFS Recursive result: ",g.RecursiveDFS("A"))
print("DFS iterative result: ",g.IterativeDFS("A"))

print("BFS result: ",g.BFS("A"))

# BFS result:  ['A', 'B', 'C', 'D', 'E', 'F']
# BFS result:  ['A', 'C', 'B', 'E', 'D', 'F']
