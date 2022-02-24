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
- We need at least one element to kick start the process
- Right after we dequeue an element, we'd want to enqueue its children if there is any


"""

from collections import deque
from http.client import NOT_FOUND
def bfs_by_queue(root):
    queue =deque([root]) # at least one element in the queue to kick start bfs
    while len(queue)>0: # as long as there is element in the queue
        node = queue.popleft() # dequeue
        for child in node.children: # enqueue children
            if OK(child): # early return if problem condition met
                return FOUND(child)
            queue.append(child)
    return NOT_FOUND

