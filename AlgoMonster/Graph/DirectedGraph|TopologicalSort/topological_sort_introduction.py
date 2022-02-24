"""
Topological Sort

Topological sort or topological ordering of a directed graph is an ordering of nodes such that 
every node appears in the ordering before all the nodes it points to. Topological sort is not 
unique. For example, for a graph like this

4 ----> 2
        ^
        |
        5
Both [4,5,2] and [5,4,2] are valid topological sort.

And for the following graph:

4---> 2 --->1
            ^
            |
            3

Task 3 is completely indepedent of task 2 and 4, and it can be anywhere in the order as long
as it is before task 1 which depends on it. All of the following ordering are valid topological
orderings.

[4,2,3,1], [4,3,2,1], [3,4,2,1]

Graph with cycles do not have topological ordering

4--->2--->5--->4

It should be obvious that if a graph with a cycle does not have a topological ordering. In the
example, 2 has to come before 5 which has come before 4 which has to come before 2 which has to 
come before 5... which is impossible.

Circular dependency is a common problem in real-world software engineering:

Kahn's Algorithm
----------------

To obtain a topological order, we can use Kahn's algorithm which is very similar to Breadth 
First Search. 
In order to understand why we must use this algorithm we first look at the problem it is trying
to solve.
Given a directed graph does there exist a way to remove the nodes such that each time we remove
a node we guarantee that no other nodes point to that particular node?

For this algorithm we systematically remove one node at a time, each time removing a node such 
that no  other nodes point to that node. If no such node exists then there exists a cycle and
there does not exist a solution to the probelm(because if there isn't a cycle then we can
always find a node that does not depend on any other node.). 

For each of the neighbouring nodes to that node we then check if it has no other nodes that 
point to it. If there isn't one of them, we can push it into the queue. 

Notice, it is important to keep track of the number of nodes pointing to the node in question 
as we only  push the node into the queue once all the parents have been removed. 
"""

from collections import deque

def count_parents(graph):
    counts ={node: 0 for node in graph}
    for parent in graph:
        for node in graph[parent]:
            counts[node] += 1
    return counts

def topo_sort(graph):
    res =[]
    q = deque()
    counts = count_parents(graph)
    for node in counts:
        if counts[node] == 0:
            q.append(node)
    while len(q) > 0:
        node = q.popleft()
        res.append(node)
        for child in graph[node]:
            counts[child] -= 1
            if counts[child] == 0:
                q.append(child)
    return res