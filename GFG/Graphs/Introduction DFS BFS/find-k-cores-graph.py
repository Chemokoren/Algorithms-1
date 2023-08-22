"""
Find k-cores of an undirected graph

Given a graph G and an integer K, K-cores of the graph are connected components that
are left after all vertices of degree less than k have been moved

Input : Adjacency list representation of graph shown
        on left side of below diagram

Output: K-Cores : 
[2] -> 3 -> 4 -> 6
[3] -> 2 -> 4 -> 6 -> 7
[4] -> 2 -> 3 -> 6 -> 7
[6] -> 2 -> 3 -> 4 -> 7
[7] -> 3 -> 4 -> 6


The standard algorithm to find a k-core graph is to remove all the verticces that have
degree less than - 'K' from the input graph. We must be careful that removing a vertex
reduces the degreee of all the vertices adjacent to it, hence the degree of adjacent 
vertices can also drop below - 'K'. 
And thus, we may have to remove those vertices also.  This process
may / may not go until there are no vertices left in the graph.

To implement above algorithm, we do a modified DFS on the input graph and delete all the 
vertices having degree less than 'K', then update degrees of all the adjacent vertices, 
and if their degrees falls below 'K' we will delete them too.

Note that the below program only prints vertices of k cores, but it can be easily extended
to print the complete k cores as we have modified adjacency list.

Time complexity of the above solution is O(V + E) where V is number of vertices and 
E is number of edges.

Related Concepts : 

Degeneracy : Degeneracy of a graph is the largest value k such that the graph has a
k-core. For example, the above shown graph has a 3-Cores and doesn’t have 4 or higher
cores. Therefore, above graph is 3-degenerate. 
Degeneracy of a graph is used to measure how sparse graph is.

"""

# program to find k-cores of a graph
from collections import defaultdict

# this class represents a undirected graph using adjacency list representation

class Graph:
    def __init__(self) -> None:
        #default dictionary to store graph
        self.graph =defaultdict(list)

    # function to add an edge to undirected graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)


    # a recursive function to call DFS starting from v. It returns true if vDegree of v
    # after processing is less than k else false. It also updates vDegree of adjacent 
    # if vDegree of v is less than k . And if vDegree of a processed adjacent becomes
    # less than k, then it reducess vDegree of v also,
    def DFSUtil(self, v, visited, vDegree, k):
        # mark the current node as visited
        visited.add(v)

        # recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            #vDegree of v is less than k, then vDegree of adjacent must be reduced
            if vDegree[v] < k:
                vDegree[i] = vDegree[i] - 1

            # if adjacent is not processed, process it
            if i not in visited:

                # if vDegree of adjacent after processing becomes less than k, then 
                # reduce vDegree of v also
                self.DFSUtil(i, visited, vDegree, k)

    def PrintKCores(self, k):
        visit =set()
        degree = defaultdict(lambda: 0)

        for i in list(self.graph):
            degree[i] =len(self.graph[i])

        for i in list(self.graph):
            if i not in visit:
                self.DFSUtil(i, visit, degree, k)


        # print (degree)
        # print(self.graph)
        for i in list(self.graph):
            if degree[i] >= k :
                print(str("\n[")+ str(i) + str("]"), end=" ")

                for j in self.graph[i]:
                    if degree[j] >= k:
                        print("->" + str(j), end=" ")

                print()

    
k = 3
g1 = Graph()
g1.addEdge(0, 1)
g1.addEdge(0, 2)
g1.addEdge(1, 2)
g1.addEdge(1, 5)
g1.addEdge(2, 3)
g1.addEdge(2, 4)
g1.addEdge(2, 5)
g1.addEdge(2, 6)
g1.addEdge(3, 4)
g1.addEdge(3, 6)
g1.addEdge(3, 7)
g1.addEdge(4, 6)
g1.addEdge(4, 7)
g1.addEdge(5, 6)
g1.addEdge(5, 8)
g1.addEdge(6, 7)
g1.addEdge(6, 8)
g1.PrintKCores(k)
