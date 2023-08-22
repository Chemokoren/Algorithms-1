from typing import List
"""
Number of Connected Componenets in an Undirected Graph

You have a graph of n nodes. You are given an integer n and an array edges where edges[i]=[ai,bi]
indicates that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.

Example 1:

0---1       3
    |       |
    |       |
    2       4

Input: n = 5, edges =[[0,1],[1,2],[3,4]]
Output: 2
natural solution: O(e+v)
UnionFind - is designed to solve solutions like this one - finding connected components
(path compression in UnionFind)
similar problem: Number of Provinces on Leetcode
"""
class Solution:

    def countComponents(self, n:int, edges: List[List[int]])->int:
        par  =[i for i in range(n)]
        rank =[1] * n

        def find(n1):
            res = n1

            while res != par[res]:
                par[res] = par[par[res]] #path compression
                res = par[res]
            return res

        def union(n1, n2):
            p1, p2  = find(n1), find(n2)

            if p1 == p2:
                return 0
            
            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]

            else:
                par[p2] = p1
                rank[p1] += rank[p2]
            return 1

        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)
        return res