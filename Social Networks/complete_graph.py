def make_link(G, node1,node2):
	if node1 not in G:
		G[node1] ={}
	(G[node1])[node2] =1
	if node2 not in G:
		G[node2] ={}
	(G[node2])[node1] =1

#
# How many edges in a complete graph on n nodes?
#

def clique(n):
	# Return the number of edges
	# Try to use a mathematical formula ...
	# make an empty graph
	G ={}

	# Add in the edges
	for i in range(n):
		for j in range(n):
			if i<j: make_link(G, i, j)
	return sum([len(G[node]) for node in G.keys()])/2

for n in range(1, 10):
	print(n, clique(n))
