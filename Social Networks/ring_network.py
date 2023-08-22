def make_link(G, node1, node2):
	if node1 not in G:
		G[node1] ={}
	(G[node1])[node2] =1
	if node2 not in G:
		G[node2] ={}
	(G[node2])[node1] = 1
	return G

#Make an empty graph
a_ring ={}

n = 5

#Add in the edges
for i in range(n):
	make_link(a_ring, i, (i+1) % n)

#How many nodes?
print (len(a_ring))

#How many edges?
print(sum([len(a_ring[node]) for node in a_ring.keys()])/2)

print(a_ring)
