"""
Breadth First Traversal (or Search) for a graph is similar to Breadth First Traversal of a
tree.The only catch here is, unlike trees, graphs may contain cycles, so we may come to the 
same node again. To avoid processing a node more than once, we use a boolean visited array. 
For simplicity, it is assumed that all vertices are reachable from the starting vertex.

Breadth first search of a tree
expected: [ABCDEFGHIJK]

                     A
                   / | \
                 B   C  D
                / \    / \
               E   F  G   H
                  / \  \
                 I   J  K   
"""

class Node:
    def __init__(self,name) -> None:
        self.children =[]
        self.name = name

    def addChild(self,name):
        self.children.append(Node(name))

    # O(v + e) time | O(v) space
    def breadthFirstSearch(self, array):
        queue =[self]
        while len(queue) > 0:
            current = queue.pop(0)
            array.append(current.name)
            for child in current.children:
                queue.append(child)
        return array


# Approach 2

"""
Algorithm:
-pick any node, visit the adjacent unvisited vertex, mark it as visited, display it,
and insert it in a queue.
- if there are no remaining adjacent vertices left, remove the first vertex from the
queue.
- repeat step 1 and step 2 above until the queue is empty or the desired node is not 
found
"""
# consider the graph,
graph ={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':['F'],
    'F':[],

}
# List to keep track of nodes visited
visited =[] 

queue =[]

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        # print(s, end=" ")
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
    return visited

print(bfs(visited,graph,'A'))


# implementation 3
print("########################## implementation 3 ########################## ")
"""
implementations of simple Breadth First Traversal from a given source. 
The implementation uses adjacency list representation of graphs. STL‘s list container is
used to store lists of adjacent nodes and queue of nodes needed for BFS traversal.
"""

from collections import defaultdict

# This class represents a directed graph using adjacency list representation
class Graph:

    # constructor
    def __init__(self) -> None:
        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # Function to print a BFS of graph
    def BFS(self,s):

        # mark all the vertices as not visited
        visited =[False] * (max(self.graph)+ 1)

        # create a queue for BFS
        queue = []

        # mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:
            # Dequeue a vertex from queue and print it
            s = queue.pop(0)
            print(s, end=" ")

            # get all djacent vertices of the dequeued vertex s. If a djacent has not been
            # visited, then mark it visited and enqueue it

            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True


# create a graph given in the above diagram

g = Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,3)

g.BFS(2)