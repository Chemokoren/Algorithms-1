"""
Transpose graph

-Transpose of a directed graph G is another directed graph on the same set of 
vertices with all of the edges reversed compared to the orientation of the 
corresponding  edges in G. That is, if G contains an edge(u, v) then the 
converse/transpose/reverse of G contains an edge(v, u) and vice versa.
Given a graph(represented as adjacency list), we need to find another graph 
which is the transpose of the given graph.

We traverse the adjacency list and as we find a vertex v in the adjacency list of
vertex u which indicates an edge from u to v in main graph, we just add an edge from
v to u in the transpose graph. i.e. add u in the adjacency list of the vertex v of 
the new graph. Thus the total time complexity of the algorithm is O(V+E) where v is the
number of vertices of graph and E is the number of edges of the graph.
Note: It is simple to get the transpose of a graph which is stored in adjacency
matrix format you just need to get the transpose of that matrix.

"""

# Python3 program to find transpose of a graph.

# function to add an edge from vertex
# source to vertex dest
def addEdge(adj, src, dest):
	adj[src].append(dest)

# function to pradjacency list
# of a graph
def displayGraph(adj, v):
	for i in range(v):
		print(i, "--> ", end = "")
		for j in range(len(adj[i])):
			print(adj[i][j], end = " ")
		print()

# function to get Transpose of a graph
# taking adjacency list of given graph
# and that of Transpose graph
def transposeGraph(adj, transpose, v):
	
	# traverse the adjacency list of given
	# graph and for each edge (u, v) add
	# an edge (v, u) in the transpose graph's
	# adjacency list
	for i in range(v):
		for j in range(len(adj[i])):
			addEdge(transpose, adj[i][j], i)

# Driver Code
if __name__ == '__main__':

	v = 5
	adj = [[] for i in range(v)]
	addEdge(adj, 0, 1)
	addEdge(adj, 0, 4)
	addEdge(adj, 0, 3)
	addEdge(adj, 2, 0)
	addEdge(adj, 3, 2)
	addEdge(adj, 4, 1)
	addEdge(adj, 4, 3)

	# Finding transpose of graph represented
	# by adjacency list adj[]
	transpose = [[]for i in range(v)]
	transposeGraph(adj, transpose, v)

	# displaying adjacency list of
	# transpose graph i.e. b
	displayGraph(transpose, v)
