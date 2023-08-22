"""
BFS or DFS

When should you use one over the other?

If you just have to visit each node once without memory constraints e.g. number of islands
problem, then it doesn't really matter which one you use. It comes down to your personal 
preference for recursion /stack vs queue.

BFS is better at:
-finding the shortest distance between two vertices
-graph of unknown size e.g. word ladder, or even infinite size, e.g. knight shortest path

DFS is better at:
-uses less memory than BFS  for wide graphs, since BFS has to keep all the nodes in the queue
, and for wide graphs this can be quite large.
-finding nodes far away from the root, e.g. looking for an exit in a maze.


"""