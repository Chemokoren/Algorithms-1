"""
Transitive Closure of a Graph using DFS

Given a directed graph, find out if a vertex v is reachable from another vertex u for all 
vertex pairs(u, v) in the given graph. Here reachable mean that there is a path from
 vertex u t v. The reach-ability matrix is called transitive closure of a graph.

 For example, consider below graph

Transitive closure of above graphs is 
     1 1 1 1 
     1 1 1 1 
     1 1 1 1 
     0 0 0 1 

We have discussed a O(V^3) - The solution was based on Floyd Warshall Algorithm.

Here we look at O(V^2) algorithm for the same.

Abstract steps of algorithm:

1. Create a matrix tc[V][V] that would finally have transitive closure of given graph.
Initialize  all entries of tc[][] as 0.
2. Call DFS for every node of graph to mark reachable vertices in tc[][]. In recursive
calls to DFS, we don't call DFS for an adjacent vertex if it is already marked as
reachable in tc[][]


Implementation:

The code uses adjacency list representation of input graph and builds a matrix tc[V][V]
such that tx[u][v] would be true if v is reachable from u.

expected:

Transitive closure matrix is 
1 1 1 1 
1 1 1 1 
1 1 1 1 
0 0 0 1 
                                                                                                                              

"""

# program to print transitive closure of a graph
from collections import defaultdict

# This class represents a directed graph using adjacency list representation

class Graph:
    def __init__(self, vertices) -> None:
        # N. of vertices
        self.V =vertices

        # default dictionary to store graph
        self.graph = defaultdict(list)

        # To store transitive closure
        self.tc =[[0 for j in range(self.V)] for i in range(self.V)]

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A recursive DFS traversal function that finds all reachable vertices for s
    def DFSUtil(self, s, v):
        # Mark reachability from s to v as true
        if(s == v):
            if( v in self.graph[v]):
                self.tc[s][v] =1
        
        else:
            self.tc[s][v] =1

        # find all the vertices reachable through v
        for i in self.graph[v]:
            if self.tc[s][i] == 0:
                self.DFSUtil(s,i)

    # The function to find transtive closure. It uses recursive DFSUtil()
    def transitiveClosure(self):
        # call the recursive helper function to print DFS traversal starting from all 
        # vertices one by one
        for i in range(self.V):
            self.DFSUtil(i, i)
        print(self.tc)

# Create a graph given in the above diagram
g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
 
print("Transitive closure matrix is")
g.transitiveClosure()