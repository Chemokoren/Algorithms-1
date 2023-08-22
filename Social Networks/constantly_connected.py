#
# Design and implement an algorithm that can preprocess a
# graph and then answer the question "is x connected to y in the
# graph" for any x and y in constant time Theta(1).
#

#
# `process_graph` will be called only once on each graph.  If you want,
# you can store whatever information you need for `is_connected` in
# global variables
#
global_G = {}

def process_graph(G):
	global global_G
	global_G = G
	for node in global_G:
		to_visit = global_G[node].keys()

		while to_visit:
			new_node = to_visit.pop()

			global_G[node][new_node] = 1
			global_G[new_node][node] = 1

			for x in global_G[new_node]:
				if x not in global_G[node]:
					to_visit += [x]

#
# When being graded, `is_connected` will be called
# many times so this routine needs to be quick
#
def is_connected(i, j):
	# your code here
	return i in global_G[j] or j in global_G[i]

#######
# Testing
#
def test():
	G = {'a':{'b':1},
		 'b':{'a':1},
		 'c':{'d':1},
		 'd':{'c':1},
		 'e':{}}
	process_graph(G)
	assert is_connected('a', 'b') == True
	assert is_connected('a', 'c') == False

	G = {'a':{'b':1, 'c':1},
		 'b':{'a':1},
		 'c':{'d':1, 'a':1},
		 'd':{'c':1},
		 'e':{}}
	process_graph(G)
	assert is_connected('a', 'b') == True
	assert is_connected('a', 'c') == True
	assert is_connected('a', 'e') == False

if __name__ == '__main__':
	test()
	print("Test passes")
