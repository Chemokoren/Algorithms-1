"""
Reconstruct Itinerary

You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure
 and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin
with "JFK". If there are multiple valid itineraries, you should return the itinerary that has
the smallest lexical order when read as a single string.
- For example, the itinerary ["JFK","LGA"] has a smaller lexical order than ["JFK","LGB"].

You may assume all tickets form at least one valid itinerary. You must use all the tickets
once and only once.

Example 1:
MUC --> LHR --> SFO
 ^              |
 |              |
 |              V
 JFK            SJC

 Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR", "SFO"]]
 Output: ["JFK","MUC","LHR","SFO","SJC"]

Example 2:

SFO
^\  \
|   \   \
|       \   \
|           \   \
JFK------------>ATL
<----------------

Iput: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
OUtput: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is
["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.

Time complexity is O(V+E) but since we are backtracking potentially for every single edge in the
graph, the overall time complexity is going to be O(V+E)^2. But since we know that the number of
edges is approximately equal to or greater than the number of vertices, we can think of this as 
E^2

Time complexity : O(E + V)^2 == E^2 if V== E
Space Complexity: O(E) because we will be storing it in an adjacency list & when done recursively
this could be the size of the callstack.

"""
from typing import List
class Solution:

    def findItinerary(self, tickets: List[List[str]])->List[str]:
        adj ={src: [] for src, dst in tickets}

        tickets.sort()

        for src, dst in tickets:
            adj[src].append(dst)

        res =["JFK"]

        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in adj:
                return False

            temp = list(adj[src])

            for i, v in enumerate(temp):
                adj[src].pop(i)
                res.append(v)
                if dfs(v): return True
                adj[src].insert(i, v)
                res.pop()

            return False
        dfs("JFK")
        return res

tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR", "SFO"]]
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]

sol = Solution()
print(sol.findItinerary(tickets))