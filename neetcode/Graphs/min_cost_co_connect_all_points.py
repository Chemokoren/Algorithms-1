from typing import List
import heapq

"""
Min Cost to Connect All Points
You are given an array points representing integer coordinates of some points on a 2D-plane,
where points[i] =[xi, yi].
The cost of connecting two points [xi, yi] and [xj,yj] is the manhanttan distance between them:
|xi-xj| + | yi -yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is
exactly one simple path between any two points.

Example 1:

        ^
      10|          x
       9|
       8|
       7|
       6|
       5|
       4|
       3|
       2|       x       x
       1|               
        |x__ __ __ __ __ __ __ _x_ __ > 
        0    1   2  3  4  5 6  7  8  

Input: points =[[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20

It is a concept on MST - Minimum spanning Trees (Prim's algorithm)

1) create edges
2) Prim's algorithm O(n^2(log(n))) where n^2 is the number of edges we will have & n the no
 of points we are given and log n because we will use the Min Heap
"""
class Solution:

    def minCostConnectPoints(self, points: List[List[int]])->int:
        N = len(points)

        adj ={i: [] for i in range(N)} # i: list of [cost, node]

        for i in range(N):
          x1, y1 = points[i]
          for j in range(i+1, N):
            x2, y2 = points[j]
            dist = abs(x1 - x2) + abs(y1 - y2)
            adj[i].append([dist, j])
            adj[j].append([dist, i])

        # prim's
        res = 0
        visit =set()
        minH =[[0,0]] # [cost, point]
        while len(visit) < N:
          cost, i = heapq.heappop(minH)
          if i in visit:
            continue
          res += cost
          visit.add(i)
          for neiCost, nei in adj[i]:
            if nei not in visit:
              heapq.heapppush(minH, [neiCost, nei])

        return res