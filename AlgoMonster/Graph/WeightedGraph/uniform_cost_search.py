"""
Uniform Cost Search | Shortest Path in a Weighted Graph

In Dijkstra's algorithm, we add all vertices to the priority queue at the beginning. However,
this is not possible when we have a large graph that does not fit in memory, or even infinite
graph. The Uniform Cost Search algorithm is a variant of Dijkstra's algorithm. We start with 
the priority queue containing only the root node, and add new vertices as we checking the 
neighbours.

An optimization is to terminate the search as soon as you reach a destination node. This is if
you are finding the distance only between 2 nodes. If this is the case you can terminate the 
search early and exit the loop as soon as you reach the destination node.

"""
from typing import List, Tuple
from heapq import heappush, heappop

def shortest_path(graph: List[List[Tuple[int, int]]], a: int, b:int)->int:
    
    def get_neighbors(node:int):
        return graph[node]
    
    def bfs(root: int, target: int):
        queue =[(0, root)]
        distances =[float('inf')] * len(graph)
        distances[root] = 0

        while len(queue) > 0:
            distance, node = heappop(queue)
            if node == target:
                return distance
            if distance > distances[node]:
                continue
            for neighbor, weight in get_neighbors(node):
                d = distances[node] + weight
                if distances[neighbor] <= d:
                    continue
                heappush(queue, (d, neighbor))
                distances[neighbor] =d
        return distances[target]
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
res =shortest_path(graph, a, b)
print(res)