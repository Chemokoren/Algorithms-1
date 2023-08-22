"""
count all possible paths between two vertices

count the total number of ways or paths that exist between two vertices in a directed 
graph. These paths don't contain a cycle, the simple enough reason is that a cycle 
contains  an infinite number of paths and hence they create a problem.

Approach:
The problem can be solved using backtracking, that says take a path and start walking on
it and check if it leads us to the destination vertex then count the path and backtrack 
to take  another path. If the path doesn't lead to the destination vertex, discard the
path.
This type of graph traversal is called Backtracking.

Algorithm:

1 - Create a recursive function that takes index of node of a graph and the destination
index. Keep a global or a static variable count to store the count. Keep a record of the
nodes visited in the current path by passing a visited array by value(instead of 
reference, which would not be limited to the current path).
2. If the current nodes is the destination icrease the count.
3. Else for all the adjacent nodes, i.e. nodes that are accesssible from the current node,
call the recursive function with the index of adjacent node and the destination.
4. print the count.

Complexity Analysis: 

Time Complexity: O(N!). 
If the graph is complete then there can be around N! recursive calls, so the time Complexity is O(N!)
Space Complexity: O(1). 
Since no extra space is required.


"""

# program to count all paths from a source to a destination.

# A directed graph using adjacency list representation
class Graph:
    def __init__(self, V) -> None:
        self.V = V
        self.adj =[[] for i in range(V)]

    def addEdge(self, u, v):
        # Add v to u's list.
        self.adj[u].append(v)

    # Returns count of paths from 's' to 'd'
    def countPaths(self, s, d):
        # Mark all the vertices as not visited
        visited =[False] * self.V

        # Call the recursive helper function to print all paths
        pathCount =[0]
        self.countPathsUtil(s, d, visited, pathCount)
        return pathCount[0]


    # A recursive function to print all paths from 'u' to 'd'. visited[] keeps track
    # of vertices in current path. path[]  stores actual vertices and path_index is
    # current index in path[]
    def countPathsUtil(self, u, d, visited, pathCount):
        visited[u] = True

        # If current vertex is same as destination, then increment count
        if(u == d):
            pathCount[0] += 1

        # If current vertex is not destination
        else:
            # Recur for all the vertices adjacent to current vertex
            i = 0
            while i < len(self.adj[u]):
                if(not visited[self.adj[u][i]]):
                    self.countPathsUtil(self.adj[u][i], d, visited, pathCount)

                i += 1

        visited[u] = False

if __name__ == '__main__':
 
    # Create a graph given in the
    # above diagram
    g = Graph(4)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(0, 3)
    g.addEdge(2, 0)
    g.addEdge(2, 1)
    g.addEdge(1, 3)
 
    s = 2
    d = 3
    print(g.countPaths(s, d))