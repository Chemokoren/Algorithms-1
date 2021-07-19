"""
Depth First Traversal (or Search) for a graph is similar to Depth First Traversal of a 
tree. The only catch here is, unlike trees, graphs may contain cycles, 
a node may be visited twice. To avoid processing a node more than once, 
use a boolean visited array. 

Example: 

Input: n = 4, e = 6 
0 -> 1, 0 -> 2, 1 -> 2, 2 -> 0, 2 -> 3, 3 -> 3 
Output: DFS from vertex 1 : 1 2 0 3 


Input: n = 4, e = 6 
2 -> 0, 0 -> 2, 1 -> 2, 0 -> 1, 3 -> 3, 1 -> 3 
Output: DFS from vertex 2 : 2 0 1 3 

Solution:

Approach: Depth-first search is an algorithm for traversing or searching tree or graph
data structures. The algorithm starts at the root node(selecting some arbitrary node as
the root node in the case of a graph) and explores as far as possible along each branch
before backtracking. So, the basic idea is to start from the root or any arbitrary node 
and mark the node and move to the adjacent unmarked node and continue this loop until 
there is no unmarked adjacent node. Then backtrack and check for other unmarked nodes
and traverse them. Finally print the nodes in the path.

Algorithm:
- Create a recursive function that takes the index of node and a visited array.
- Mark the current node as visited and print the node
- Traverse all the adjacent and unmarked nodes and call the recursive function with the
index of adjacent node.

Complexity Analysis: 

Time complexity: O(V + E), where V is the number of vertices and E is the number of 
edges in the graph.
Space Complexity: O(V). 
Since, an extra visited array is needed of size V.

"""
# program to print DFS traversal for a given graph
from collections import defaultdict

# This class represents a directed graph using adjacency list representation

class Graph:
    # Constructor
    def __init__(self) -> None:
        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A function used by DFS
    def DFSUtil(self, v, visited):
        # mark the current node as visited and print it
        visited.add(v)
        print(v, end=' ')

        # Recur for all the vertices adjacent to this vertex
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)

    # The function to do DFS traversal. It uses recursive DFSUtil()
    def DFS(self, v):
        # Create a set to store visited vertices
        visited =set()
        # Call the recursive helper function to print DFS traversal
        self.DFSUtil(v, visited)

    
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Following is DFS from (starting from vertex 2)")
g.DFS(2)


print("\n Handling Disconnected Graph: \n")
"""
Handling Disconnected Graph

Solution:
This will happen by handling a corner case. The above code traverses only the vertices
reachable from a given source vertex. All the vertices may not be reachable from a given
vertex as in the case of a Disconnected graph. To do complete DFS traversal of such graphs
, run DFS from all unvisited nodes after a DFS. The recursive function remains the same.

Algorithm:
-Create a recursive function that takes the index of node and a visited array.
-Mark the current node as visited and print the node
-Traverse all the adjacent and unmarked nodes and call the recursive function with index
of adjacent node.
- Run a loop from 0 to number of vertices and check if the node is unvisited in previous
DFS then call the recursive function with current node.

Complexity Analysis: 

Time complexity: O(V + E), where V is the number of vertices and E is the number of
edges in the graph.
Space Complexity :O(V). 
Since an extra visited array is needed of size V.

"""

# program to print DFS traversal for complete graph
from collections import defaultdict

# class represents a directed graph using adjacency list representation

class Graph:
    # constructor
    def __init__(self) -> None:
        #default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # function used by DFS
    def DFSUtil(self, v, visited):
        # mark the current node as visited and print it
        visited.add(v)
        print(v)

        # Recur for all the vertices adjacent to this vertex
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)


    # The function to do DFS traversal . It uses recursive DFSUtil()
    def DFS(self):
        # create a set to store all visited vertices
        visited =set()

        # call the recursive helper function to print DFS traversal starting from all
        # vertices one by one
        for vertex in list(self.graph):
            if vertex not in visited:
                self.DFSUtil(vertex, visited)

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
 
print("Following is Depth First Traversal")
g.DFS()