"""
Find a Mother Vertex in a Graph

What is a Mother Vertex?

a mother vertex in a graph G =(V, E) is a vertex v such that all other vertices in G 
can be reached by a path from V.

There can be more than one mother vertices in a graph. We need to output anyone of them.
For example, in the below graph, vertices 0, 1 and 2 are mother vertices.

Case 1:- Undirected Connected Graph : 
In this case, all the vertices are mother vertices as we can reach to all the other
nodes in the graph.
Case 2:- Undirected/Directed Disconnected Graph : 
In this case, there is no mother vertices as we cannot reach to all the other nodes in
the graph.
Case 3:- Directed Connected Graph : 
In this case, we have to find a vertex -v in the graph such that we can reach to all
the other nodes in the graph through a directed path.

Naive Approach:
A trivial approach will be to perform a DFS/BFS on all the vertices and find whether
we can reach all the vertices from that vertex. This approach takes O(V(V+E)) time, 
which is very inefficient for large graphs.

Can we do better?
We can find a mother vertex in O(V+E) time. The idea is based on Kosaraju's strongly
connected component Algorithm. In a graph of strongly connected components, mother
vertices are always vertices of source component in component graph. The idea is based
on the following facts:

If there exist mother vertex or vertices, then one of the mother vertices is the last
finished vertex in DFS Or a mother vertex has the maximum finish time in DFS traversal.
A vertex is said to be finished in DFS if a recursive call for its DFS is over, i.e. all
descendants of the vertext have been visited.

How does the above idea work?

Let the last finished vertex be v. Basically, we need to prove that there cannot be an
 edge from vertex u to v if u is not another mother vertex or there cannot exist a 
 non-mother vertex u such that u -> is an edge. There can be two possibilities.

 1. Recursive DFS call is made for u before v. If an edge u->v exists then, v must 
 have finished  before u because v is reachable through u and a vertex finishes after 
 all its descendants.

 2. Recursive DFS call is made for v before u. In this case also, if an edge u-> v 
 exists, then either v must finish before u (which contradicts our assumption that
 v is finished at the end ) OR u should be reachable from v which means u is 
 another mothervertex.

 Algorithm:
 1: Do DFS traversal of the given graph. While doing traversal keep track of last 
 finished vertex 'v' This step takes O(V+E) time.
 2. If there exist mother vertex or vertices, then v must be one of them. Check if
 v is a mother vertex by doing DFS/BFS from v. This step also takes O(V+E) time.

 Time Complexity : O(V + E)

"""

# program to find a mother vertex in O(V+E) time
from collections import defaultdict

# This class represents a directed graph using adjacency list representation
class Graph:
    def __init__(self, vertices) -> None:
        self.V = vertices # No. of vertices
        self.graph = defaultdict(list) # default dictionary

    # a recursive function to print DFS starting from v
    def DFSUtil(self, v, visited):
        # Mark the current node as visited and print it
        visited[v] =True

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)

    # Add w to the list of v
    def addEdge(self, v, w):
        self.graph[v].append(w)

    # Returns a mother vertex if exists. Otherwise returns -1
    def findMother(self):
        # visited[] is used for DFS. Initially all are initialized as not visited
        visited =[False] * (self.V)
        
        # To store last finished vertex or mother vertex
        v = 0

        # Do a DFS traversal and find the last finished vertex
        for i in range(self.V):
            if visited[i] == False:
                self.DFSUtil(i, visited)
                v = i

        # if there exist mother vertex or vertices in given graph, then v must be one of
        # them

        # Now check if v is actually a mother vertex or graph has a mother vertex. We 
        # basically check if every vertex is reachable from v or not.
        # Reset all values in visited[] as false and do DFS beginning from v to check if
        # all vertices are reachable from it or not.
        visited =[False] * (self.V)
        self.DFSUtil(v, visited)
        if any(i == False for i in visited):
            return -1
        else:
            return v
        
# Create a graph given in the above diagram
g = Graph(7)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(4, 1)
g.addEdge(6, 4)
g.addEdge(5, 6)
g.addEdge(5, 2)
g.addEdge(6, 0)
print("A mother vertex is " + str(g.findMother()))
    
                
