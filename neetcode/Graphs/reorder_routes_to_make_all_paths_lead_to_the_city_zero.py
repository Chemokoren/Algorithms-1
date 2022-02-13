from typing import List
"""
Reorder routes to make all paths lead to the city zero

There are n citities numbered from 0 to n-1 and n-1 roads such that there is only one way to 
travel between two different cities(this network form a tree). Last year, the ministry of 
transport decided to orient the roads in one direction because they are too narrow.

Roads are represented by connections where connections[i]=[a,b] represents a road from city a
to b.
This year, there will be a big event in the capital(city 0), and many people want to travel
to this city.

Your task consists of reorienting some roads such that each city can visit the city 0,
Return the minimum number of edges changed.


It's guaranteed that each city can reach they city 0 after reorder.

Example 1:

                                        3<---2
                                        ^
                                       /
                                      1 
                                      ^
                                     /
                                    0 <--- 4---> 5

Input: n=6, connections =[[0,1],[1,3],[2,3],[4,0],[4,5]]
Output: 3

Explanation: Change the direction of edges shown in red

Time complexity: O(n) because we are visiting every node at most once
Space complexity: O(n) because of the different data structures we are using
"""

class Solution:

    def minReorder(self, n:int, connections: List[List[int]])->int:
        # start at city 0
        # recursively check its neighbors
        # count outgoing edges

        edges ={(a,b) for a, b in connections}
        neighbors ={city: [] for city in range(n)}
        visit =set()
        changes = 0

        for a, b in connections:
            neighbors[a].append(b)
            neighbors[b].append(a)

        def dfs(city):
            nonlocal edges, neighbors, visit, changes

            for neighbor in neighbors[city]:
                if neighbor in visit:
                    continue
                
                # check if this neighbor can reach city 0
                if(neighbor,city) not in edges:
                    changes +=1
                visit.add(neighbor)
                dfs(neighbor)
        visit.add(0)
        dfs(0)
        return changes
