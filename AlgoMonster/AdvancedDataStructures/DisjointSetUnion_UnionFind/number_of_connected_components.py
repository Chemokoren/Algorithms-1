"""
Number of Connected Components

    Prereq: DSU Introduction

For this question we start with n nodes in a graph that are all independent of each other.
We will then begin connecting nodes in the graph. After each connection connecting two 
different nodes we ask you to compute the number of connected components in a graph. 
A connected component is a series of node such that there exists a path between any two 
nodes in the graph. Nodes will be 0-indexed and will be integers from 0 to n - 1.

Example
Input: n = 5, connections = [[1, 2], [2, 3], [1, 3], [0, 4], [0, 4]]
Output: [4, 3, 3, 2, 2]
Explanation:
"""