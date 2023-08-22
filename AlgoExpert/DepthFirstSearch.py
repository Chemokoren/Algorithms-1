class Node:
    def __init__(self, name):
        self.children =[]
        self.name =[]

    def  addChild(self,name):
        self.children.append(Node(name))

    # O(v + e) | O(v) space
    def depthFirstSearch(self,array):
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array

root =Node(1)
root.left =Node(2)
root.right =Node(3)
root.left.left =Node(4)
root.left.right =Node(5)
root.right.left =Node(20)
root.right.right =Node(22)

array =[3, 5,6,0,7,9,3]
print(root.depthFirstSearch(array))


print("################################")
# DFS Traversal
from collections import defaultdict
# The class represents a directed graph using adjacency list representation

class Graph:
    # Constructor
    def __init__(self):
        # default dictionary to store graph
        self.graph =defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A function used by DFS
    def DFSUtil(self, v, visited):
        # Mark the current node as visited and print it
        visited.add(v)
        print(v,end=' ')

        # Recur for all the vertices & adjacent to this vertex
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)


    # The function to do DFS traversal. It uses recursive DFSUtil()
    def DFS(self, v):
        # create a set to store visited vertices
        visited =set()

        # call the recursive helper function
        # to print DFS traversal
        self.DFSUtil(v, visited)


# Test Code- Create a graph given in the above diagram
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Following is DFS from (starting from vertex 2)")
g.DFS(3)

