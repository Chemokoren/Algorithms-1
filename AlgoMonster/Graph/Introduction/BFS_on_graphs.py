"""
Breadth First Search on Graphs

Tree vs Graph Traversal

A Tree is a connected, acyclic undirected graph. Statistically, most interview graph problems
are about connected and undirected graphs. So for simplicity, we're gonna define a tree as a
graph without cycle. The search algorithms we have learned in tree modules are applicable to 
graphs as well.

Hopefully, by this point, you are familiar with DFS on tree and BFS on tree. Since the difference
between a tree and a graph is possibility of having a cycle, we just have to handle this 
situtation. We use an extra variable visited to keep track of vertices we have already visited
to prevent re-visiting and getting into infinite loops. Visited can be any data structure that can 
answer existence queries quickly. For example, a hash set or an array where each element
maps to a vertex in the graph can both do this in constant time.

"""