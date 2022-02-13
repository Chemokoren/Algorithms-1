from typing import List
"""
Redundant Connection

In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one 
additional edge added. The added edge has two different vertices chosen from 1 to n, and was 
not an edge that already existed. The graph is represented as an array edges of length n 
where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the 
graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there
are multiple answers, return the answer that occurs last in the input.

Example 1:

    1   -   -   - 2
    |           /
    |         /
    |       /
    |     /
    |   /
    3
Input: edges [[1,2],[1,3],[2,3]]
Output: [2,3]

Naive solution: O(n^2)
Using Union-Find you can reduce the time complexity to O(n)

"""
class Solution:

    def findRedundantConnection(self, edges: List[List[int]])->List[int]:
        par = [i for i in range(len(edges)+1)]
        rank =[1] * (len(edges)+1)

        def find(n):
            p = par[n]
            while p != par[p]:
                par[p] =par[par[p]]
                p = par[p]
            return p

        # return False if cant complete
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False

            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]