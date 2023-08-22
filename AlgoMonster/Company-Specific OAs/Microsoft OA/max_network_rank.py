"""
Microsoft Online Assessment (OA) 2021 - Max Network Rank | Codility

An infrastructure consisting of n cities from l to n, and m bidirectional roads between them are 
given. Roads do not intersect apart from at their start and endpoints (they can pass through 
underground tunnels to avoid collisions).

For each pair of cities directly connected by a road, let’s define their network rank as the total 
number of roads that are connected to either of the two cities.

Write a function, given two arrays starts, ends consisting of m integers each and an integer n, 
where starts[i] and ends[i] are cities at the two ends of the i-th road, returns the maximal network 
rank in the whole infrastructure.

Example:
Input:

starts = [1, 2, 3, 3]

ends = [2, 3, 1, 4]

n = 4

Output:

4

Explanation:

The chosen cities may be 2 and 3, and the four roads connected to them are: (2,1), (2,3), (3,1),
(3,4).

"""
from typing import List

def max_network_rank(starts: List[int], ends: List[int], n: int)->int:
    adj =[0] * (n+1)

    for a, b in zip(starts, ends):
        adj[a] += 1
        adj[b] += 1
    max_rank = 0

    for a, b in zip(starts, ends):
        max_rank =max(max_rank, adj[a]+adj[b] -1)
    return max_rank

if __name__=='__main__':
    starts =[int(x) for x in input().split()]
    ends =[int(x) for x in input().split()]
    n = int(input())
    res =max_network_rank(starts, ends, n)
    print(res)