# Finding a Favor v2
#
# Each edge (u,v) in a social network has a weight p(u,v) that
# represents the probability that u would do a favor for v if asked.
# Note that p(v,u) != p(u,v), in general.
#
# Write a function that finds the right sequence of friends to maximize
# the probability that v1 will do a favor for v2.
#

#
# Provided are two standard versions of dijkstra's algorithm that were
# discussed in class. One uses a list and another uses a heap.
#
# You should manipulate the input graph, G, so that it works using
# the given implementations.  Based on G, you should decide which
# version (heap or list) you should use.
#

# code for heap can be found in the instructors comments below

"""
Be careful of underflow errors - which can happen when multiplying lots of small numbers (like probabilities) together: http://en.wikipedia.org/wiki/Arithmetic_underflow.

The heap module can be found on the wiki: http://www.udacity.com/wiki/CS215Final or copied from:
"""
from heap import *
from operator import itemgetter
from collections import defaultdict
from math import log, exp

def reform_graph(G):
	new_graph = defaultdict(dict)
	for node in G:
		for neighbor in G[node]:
			new_graph[node][neighbor] = log(G[node][neighbor]) * -1
	return new_graph

def maximize_probability_of_favor(G, v1, v2):
	# your code here
	# call either the heap or list version of dijkstra
	# and return the path from `v1` to `v2`
	# along with the probability that v1 will do a favor
	# for v2

	def _count_edges():
		return sum([len(G[v]) for v in G])

	G = reform_graph(G)

	# Theata(dijkstra_list) = Theata(n^2 + m) = Theata(n^2)
	# Theata(dijkstra_heap) = Theata(n * log(n) + m * log(n)) = Theata(m * log(n))
	node_num = len(G.keys())
	edge_num = _count_edges()

	if edge_num * log(node_num) <= node_num ** 2:
		dist_dict = dijkstra_heap(G, v1)
	else:
		dist_dict = dijkstra_list(G, v1)

	path = []
	node = v2
	while True:
		path += [node]
		if node == v1:
			break
		_, node = dist_dict[path[-1]]

	path = list(reversed(path))
	prob_log = dist_dict[v2][0] * -1

	return path, exp(prob_log)

#
# version of dijkstra implemented using a heap
#
# returns a dictionary mapping a node to the distance
# to that node and the parent
#
# Do not modify this code
#
def dijkstra_heap(G, a):
	# Distance to the input node is zero, and it has
	# no parent
	first_entry = (0, a, None)
	heap = [first_entry]
	# location keeps track of items in the heap
	# so that we can update their value later
	location = {first_entry:0}
	dist_so_far = {a:first_entry}
	final_dist = {}
	while len(dist_so_far) > 0:
		dist, node, parent = heappopmin(heap, location)
		# lock it down!
		final_dist[node] = (dist, parent)
		del dist_so_far[node]
		for x in G[node]:
			if x in final_dist:
				continue
			new_dist = G[node][x] + final_dist[node][0]
			new_entry = (new_dist, x, node)
			if x not in dist_so_far:
				# add to the heap
				insert_heap(heap, new_entry, location)
				dist_so_far[x] = new_entry
			elif new_entry < dist_so_far[x]:
				# update heap
				decrease_val(heap, location, dist_so_far[x], new_entry)
				dist_so_far[x] = new_entry
	return final_dist

#
# version of dijkstra implemented using a list
#
# returns a dictionary mapping a node to the distance
# to that node and the parent
#
# Do not modify this code
#
def dijkstra_list(G, a):
	dist_so_far = {a:(0, None)} #keep track of the parent node
	final_dist = {}
	while len(final_dist) < len(G):
		node, entry = min(dist_so_far.items(), key=itemgetter(1))
		# lock it down!
		final_dist[node] = entry
		del dist_so_far[node]
		for x in G[node]:
			if x in final_dist:
				continue
			new_dist = G[node][x] + final_dist[node][0]
			new_entry = (new_dist, node)
			if x not in dist_so_far:
				dist_so_far[x] = new_entry
			elif new_entry < dist_so_far[x]:
				dist_so_far[x] = new_entry
	return final_dist

##########
#
# Test

def test():
	G = {'a':{'b':.9, 'e':.5},
		 'b':{'c':.9},
		 'c':{'d':.01},
		 'd':{},
		 'e':{'f':.5},
		 'f':{'d':.5}}
	path, prob = maximize_probability_of_favor(G, 'a', 'd')
	assert path == ['a', 'e', 'f', 'd']
	assert abs(prob - .5 * .5 * .5) < 0.001

if __name__ == '__main__':
	test()
	print ("Test passes")
