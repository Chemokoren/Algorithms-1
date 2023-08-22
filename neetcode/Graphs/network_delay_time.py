from typing import List
import collections
import heapq
"""
You are given a netwrok of n nodes labeled from 1 to n. You  are also given times, a list of
travel times as directed edges times[i] =(ui, vi, wi), where ui is the source node, vi is the
target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the time it takes for all the n nodes to
reveive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

Example 1:


                2
              1/  \1
              1    3
                 1/
                 4

input: times =[[2,1,1],[2,3,1],[3,4,1]], n =4, k =2
output: 2

Time Complexity: O(E(log(V))) derived from O(E(logv^2)) because E =v^2 ie the number of edges
is a square of the number of vertices.
"""

class Solution:

    def networkDelayTime(self, times: List[List[int]], n:int, k:int)->int:
        edges = collections.defaultdict(list)

        for u, v, w in times:
            edges[u].append((v,w)) # add outgoing edges & their weights

        minHeap =[(0, k)] # starting edge is k and the time to reach k is 0
        visit = set()
        t = 0

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit: # check if node is already visited
                continue
            visit.add(n1)
            t = max(t, w1)

            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w1 + w2, n2))

        return t if len(visit) == n else -1
