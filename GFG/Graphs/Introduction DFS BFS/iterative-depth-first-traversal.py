"""
Iterative Depth First Traversal of Graph

Depth First Traversal or search for a graph is similar to Depth First Traversal of
a tree. the only catch here is unlike trees, graphs may contain cycles, so a node 
might be visited twice. To avoid processing a node more than once, use a boolean 
visited array.

Input: n = 4, e = 6 
0 -> 1, 0 -> 2, 1 -> 2, 2 -> 0, 2 -> 3, 3 -> 3 
Output: DFS from vertex 1 : 1 2 0 3 


Input: n = 4, e = 6 
2 -> 0, 0 -> 2, 1 -> 2, 0 -> 1, 3 -> 3, 1 -> 3 
Output: DFS from vertex 2 : 2 0 1 3 

Solution:

Approach:

Depth-first search is an algorithm for traversing or searching tree or graph
data structures. The algorithm starts at the root node(selecting some arbitrary node
as the root node in the case of a graph) and explores as far as possible along each 
branch before backtracking. So the basic idea is to start  from the root or any 
arbitrary node and mark the node and move to the adjacent unmarked node and continue 
this loop until there is no unmarked adjacent node. Then backtrack and check for other 
unmarked nodes  and traverse them. Finally print the ndoes in the path.

The only difference between iterative DFS and recursive DFS is that recursive stack is
replaced by a stack of nodes.

Algorithm:
- created a stack of nodes and visited array.
- insert the root in the stack.
- Run a loop till the stack is not empty.
- Pop the element from the stack and print the element.
- For every adjacent and unvisited node of current node, mark the node and insert it
in the stack


implementation of iterative DFS. This is similar to BFS, the only difference is queue
 is replaced by stack.


 Following is Depth First Traversal
0 3 2 1 4
Complexity Analysis: 
Time complexity: O(V + E), where V is the number of vertices and E is the number 
of edges in the graph.
Space Complexity: O(V). Since an extra visited array is needed of size V.


"""

# iterative program to do DFS traversal from a given source vertex. DFS(int s) traverses
# vertices reachable from s.

# This class represents a directed graph using adjacency list representation

class Graph:
    def __init__(self, V) -> None:
        self.V = V # No. of vertices
        self.adj =[[] for i in range(V)] # adjacency lists

    def addEdge(self, v, w): # to add an edge to graph
        self.adj[v].append(w)   # Add w to v's list


    # prints all not yet visited vertices reachable from s 
    def DFS(self, s):  # prints all vertices in DFS  manner from a given source.
                        # Inially mark all vertices as not visited
        visited =[False for i in range(self.V)]


        # Create a stack for DFS
        stack =[]

        # Push the current source node
        stack.append(s)

        while(len(stack)):
            # pop a vertex from stack and print it
            s = stack[-1]
            stack.pop()

            # stack may contain same vertex twice. So we need to print the popped item only
            # if it is not visited.
            if(not visited[s]):
                print(s, end=' ')
                visited[s] =True


            #Get all adjacent vertices of the popped vertex s 
            # If a adjacent has not been visited, then push it to the stack
            for node in self.adj[s]:
                if(not visited[node]):
                    stack.append(node)

g = Graph(5); # Total 5 vertices in graph
g.addEdge(1, 0)
g.addEdge(0, 2)
g.addEdge(2, 1)
g.addEdge(0, 3)
g.addEdge(1, 4)
 
print("Following is Depth First Traversal")
g.DFS(0)

print("\n Modification of the above solution: \n")

"""
Modification of the above solution:

Note that the above implementation prints only vertices that are reachable from a given
vertex. For example, if the edges 0-3 and 0-2 are removed, then the above program would
only print 0. To print all vertices of a graph, call DFS for every unvisited vertex.

Like recursive traversal, the time complexity of iterative implementation is O(V + E).

"""

# program to do DFS traversal from a given source vertex. DFS(s) traverses vertices
# reachable from s.

class Graph:
    def __init__(self, V) -> None:
        self.V = V
        self.adj= [[] for i in range(V)]

    def addEdge(self, v, w):
        self.adj[v].append(w) #  Add w to v's list.

    # prints all not yet visited vertices reachable from s
    def  DFSUtil(self, s , visited):
        # create a stack fro DFS
        stack = []
        
        # push the current source node
        stack.append(s)

        while(len(stack) != 0):

            # pop a vertex from stack and print it
            s = stack.pop()

            # stack may contain same vertex twice. So we need to print the popped item 
            # only if it is not visited.

            if(not visited[s]):
                print(s, end=" ")
                visited[s] = True

            # Get all adjacent vertices of the popped vertex s. If a adjacent has not been
            # visited, then push it to the stack.
            i = 0
            while i < len(self.adj[s]):
                if(not visited[self.adj[s][i]]):
                    stack.append(self.adj[s][i])

                i += 1


    #  prints all vertices in DFS manner
    def DFS(self):

        # Mark all the vertices as not visited
        visited =[False] * self.V
        for i in range(self.V):
            if( not visited[i]):
                self.DFSUtil(i, visited)

if __name__ == '__main__':
 
    g = Graph(5) # Total 5 vertices in graph
    g.addEdge(1, 0)
    g.addEdge(2, 1)
    g.addEdge(3, 4)
    g.addEdge(4, 0)
 
    print("Following is Depth First Traversal")
    g.DFS()
