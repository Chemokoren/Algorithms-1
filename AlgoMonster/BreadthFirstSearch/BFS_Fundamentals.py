"""
Breadth First Search on Trees

It visits all nodes in a level before starting to visit the next level
While DFS uses recursion/stack to keep track of progress, BFS uses a queue(FIFO). When we dequeue
a node, we enqueue its children.

DFS vs BFS

Now, a question naturally arises: which should I use? Or more fundamentally, which tasks do each 
excel at? Since they are both algorithms that traverse nodes in a tree, the only differences
are caused by the different order of traversal:

DFS is better at:
-narrow but deep trees
-finding nodes far away from the root

BFS is better for:
- shallow but wide trees
- finding nodes close/closest to the root

Template
We can implement BFS using a queue. Important things to remember:

"""