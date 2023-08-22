"""
Dijkstra's Algorithm | Shortest Path in a Weighted Graph

When to use Dijkstra Algorithm?



Given a weighted graph, what is fastest way to compute the shortest path from a node to every 
other node? What we mean by weighted graph is that every edge is now assigned a weight that and 
our distance increases by the weight instead of 1. This problem means that our previous graph 
theory algorithms such as Vanilla Breadth First Search don't work anymore as they are designed
for unweighted graphs. The previous algorithms assumed each edge was equal so only need to visit
each node once. That no longer works as the first time we visit a node does not guarantee 
minimum distance and we may need to revisit the node if we find a shorter path. Is there a way
to update them to account for weighted graphs?

The Shortest-Path Faster Algorithm (SPFA)

The Shortest-Path Faster Algorithm abbreviated to SPFA can be thought of as a BFS variant.
Instead of checking whether or not the neighbour node has been visited we instead see if we can
improve our distance by checking the neighbor nodes and if it possible to update to a smaller
distance and push the node into our queue. If it is greater then we want to update the node's 
distance since we have found a shorter path and push the node into our queue. This algorithm 
runs in worst case O(n * m) where n is the number of nodes in our graph and m is thg number of
edges. Here is an implementation for how the Shortest-Path Faster Algorithm would work.



"""
from collections import deque
from typing import List, Tuple

def shortest_path(graph: List[List[Tuple[int, int]]], a: int, b: int)->int:
    def get_neighbors(node: int):
        return graph[node]

    def bfs(root: int, target: int):
        queue = deque([root])
        distance =[float('inf')] * len(graph)
        distance[root] = 0

        while len(queue) > 0:
            node = queue.popleft()
            for neighbor, weight in get_neighbors(node):
                if distance[neighbor] <= distance[node]+weight:
                    continue
                queue.append(neighbor)
                distance[neighbor] = distance[node] + weight
        return distance[target]
    return -1 if bfs(a, b) == float('inf') else bfs(a,b)

if __name__=='__main__':
    graph =[]
    for _ in range(int(input())):
        s = input().split()
        neighbours =[]
        for i in range(0, len(s), 2):
            neighbours.append((int(s[i]), int(s[i+1])))
        graph.append(neighbours)
    a = int(input())
    b = int(input())
    res = shortest_path(graph, a, b)
    print(res)

# custom input
# 4
# 1 1 2 1
# 0 1 2 1 3 1
# 0 1 1 1
# 1 1
# 0
# 3

# output: 2

"""
This algorithm works for smaller graphs and is easy to implement, so if you are in a rush and can
afford to have a less efficient algorithm, you may want to use SPFA. Can we do better though?

Dijkstra's Algorithm

The Dijkstra's algorithm uses of a priority queue to store nodes by the distance from our root
node. When we pop a node and its distance, we know that the distance is the shortest distance 
from our source node to the node. And we update the distances of the neighbours of the node by 
decrease_priority to make sure the distances of other nodes in the priority queue is the shortest
from source node. Each time we pop a node from the queue it takes time logarithmic to the size of
the queue. Therefore, our final time complexity is O(nlog(e)) as maintaining the edges in the 
queue takes logarithmic time. Here is the pseudocode from wikipedia.

function Dijkstra(Graph, source):
    dist[source] <-- 0 # initialization
    create vertex priority queue Q
    for each vertex v in Graph:
        if v (is not equal to)  source
            dist[v]<--INFINITY # unknown distance from source to v
            prev[v]<--UNDEFINED # predecessor of v
        Q.add_with_priority(v, dist[v])
    while Q is not empty: # The main loop
        u <--Q.extract_min() # Remove and return best vertex
        for each neighbor v of u: # only v that are still in Q
            alt<--dist[u] + weight(u, v)
            if alt < dist[v]
                dist[v] <-- alt
                prev[v] <-- u
                Q.decrease_priority(v, alt)
    return dist, prev

Dijkstra's Algorithm Alternative Implementation

There are some optimizations we can do for dijkstra, that can improve the time complexity.

    We can check our priority queue and if the distance in our priority queue is greater than 
    the distance that is currrently in the array we pop it out and skip to the next iteration 
    of the loop.
    We can terminate the search as soon as you reach a destination node. This is if you are using
    Dijkstra specifically to find the distance only between 2 nodes. 
    If this is the case you can terminate the search early and exit the loop as soon as you reach
    the destination node.

Moreover, this original version needs decrease_priority from Fibonacci heap,
                                                             --------------   
which is not easy to implement and not efficient in practice. Instead of updating the distances
by decrease_priority, we can simply add the new distance of the node to the priority heap.
When we pop the node with the old large distance, nothing will be updated and the result will be 
same.
Here is an implementation of this alternative Dijkstra's algorithm.

"""
from typing import List, Tuple
from heapq import heappush, heappop

def shortest_path(graph: List[List[Tuple[int, int]]], a: int, b:int)->int:
    def get_neighbors(node: int):
        return graph[node]

    def bfs(root:int, target: int):
        queue =[(0, root)]
        distances =[]
        for i in range(len(graph)):
            if i == root:
                distances.append(0)
                heappush(queue, (0, i))
            else:
                distances.append(float('inf'))
                heappush(queue, (float('inf'), i))

        while len(queue) > 0:
            _, node  = heappop(queue)
            for neighbor, weight in get_neighbors(node):
                d = distances[node] + weight
                if distances[neighbor] <= d:
                    continue
                heappush(queue, (d, neighbor))
                distances[neighbor] =d
        return distances[target]
    return -1 if bfs(a, b) == float('inf') else bfs(a,b)

if __name__ =='__main__':
    graph =[]
    for _ in range(int(input())):
        s = input().split()
        neighbours =[]
        for i in range(0, len(s), 2):
            neighbours.append((int(s[i]), int(s[i+1])))
        graph.append(neighbours)
    a = int(input())
    b = int(input())
    res = shortest_path(graph, a, b)
    print(res)

"""
Instead of adding all vertices to the priority queue at the beginning, we can add new vertices 
as we checking the neighbours. This method is called Uniform Cost Search, which is useful when
the graph is large or even infinite.

Does Dijkstra's Algorithm Work with Negative Weights

First of all, why would a graph have any negative weight in the real world? One example would 
be nodes representing account and edges representing money transfers and negative weights means 
transferring from target node to source node. It's easy to see Dijkstra's won't work with graphs
with negative weighted edges because adding an edge means decreasing distance and this can go to
negative infinity.

Do I Need to Know Dijkstra's Algorithm for Interviews?

Probably not. Dijkstra's algorithm is used to solve for a very specific problems - finding 
shortest path in a weighted graph. As we discussed in the introductory chapter, weighted graphs
problems are not the most common in interviews. And asking a specific academic algorithm is even 
rarer. It's useful to understand the idea of Dijitra's algorithm and know when to use it.
BFS and DFS 10x more important.

"""
