"""
Breadth First Traversal(or search) for a graph is similar to Breadth First Traversal of
a tree. The only catch here is, unlike trees, graphs may contain cycles, we may come
to the same node again. To avoid processing a node more than once, we use a boolean 
visited array.  For simplicity, it is assumed that all vertices are reachable from the 
starting vertex.

The implementation uses adjacency list representation of graphs. STL's list container
is used to store lists of adjacent nodes and queues of nodes needed for BFS traversal.

Note that the above code traverses only the vertices reachable from a given source vertex.
All the vertices may not be reachable from a given vertex (example Disconnected graph).
To print all the vertices, we can modify the BFS function to do traversal starting from 
all nodes one by one (Like the DFS modified version). 

Time Complexity: O(V+E) where V is number of vertices in the graph and E is number of
edges in the graph.

"""
# Program to print BFS traversal
# from a given source vertex. BFS(int s)
# traverses vertices reachable from s.
from collections import defaultdict

# This class represents a directed graph
# using adjacency list representation
class Graph:

	# Constructor
	def __init__(self):

		# default dictionary to store graph
		self.graph = defaultdict(list)

	# function to add an edge to graph
	def addEdge(self,u,v):
		self.graph[u].append(v)

	# Function to print a BFS of graph
	def BFS(self, s):

		# Mark all the vertices as not visited
		visited = [False] * (max(self.graph) + 1)

		# Create a queue for BFS
		queue = []

		# Mark the source node as visited and enqueue it
		queue.append(s)
		visited[s] = True

		while queue:

			# Dequeue a vertex from # queue and print it
			s = queue.pop(0)
			print (s, end = " ")

			# Get all adjacent vertices of the dequeued vertex s. If a adjacent
			# has not been visited, then mark it visited and enqueue it
			for i in self.graph[s]:
				if visited[i] == False:
					queue.append(i)
					visited[i] = True



# Create a graph given in the above diagram
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print ("Following is Breadth First Traversal"
				" (starting from vertex 2)")
g.BFS(2)



