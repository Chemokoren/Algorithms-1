"""
Longest Cycle

For this question we ask you to compute the length of the longest possible cycle on a 
tree after adding an edge to a graph connecting any 2 nodes in a graph. As a reminder, a 
tree is a special subset of graphs that have n nodes, n - 1 edges and possess no cycles.
The input will have n the number of nodes in the tree where the nodes will be numbered 
from 1 to n. t Then, a list of size n -1 called edges denoting the edges in the graph. 
It should be noted that adding any 1 edge to a tree will make at least 1 cycle in the 
graph.

Constraints

1 <= n <= 100000
Examples:

Example 1:
Input 1: n = 4, edges = [[1, 2], [2, 3], [2, 4]]
Output 1: 3

Explanation:

We connect the edge between nodes 1 and 3 thus creating a cycle of size 3 which is the
longest possible cycle.

"""
from typing import List

def longest_cycle(n: int, edges: List[List[int]]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    return 0

if __name__ == '__main__':
    n = int(input())
    edges = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = longest_cycle(n, edges)
    print(res)

