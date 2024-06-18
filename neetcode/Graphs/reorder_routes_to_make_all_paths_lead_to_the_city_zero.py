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


It's guaranteed that each city can reach city 0 after reorder.

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

from typing import List

class Solution:
    def min_reorder(self, n: int, connections: List[List[int]]) -> int:
        """
        Determines the minimum number of edges that need to be reversed to make all paths lead to city 0.

        Parameters:
        n (int): The number of cities.
        connections (List[List[int]]): The list of directed edges representing the connections between cities.

        Returns:
        int: The minimum number of edge reversals needed.
        """
        # Initialize a set of edges as tuples for quick lookup
        edges = {(a, b) for a, b in connections}
        
        # Create a dictionary to store neighbors of each city
        neighbors = {city: [] for city in range(n)}
        
        # Set to keep track of visited cities
        visit = set()
        
        # Variable to count the number of changes needed
        changes = 0

        # Populate the neighbors dictionary with bidirectional connections
        for a, b in connections:
            neighbors[a].append(b)
            neighbors[b].append(a)

        def dfs(city):
            """
            Depth-first search to explore the graph and count the necessary edge reversals.

            Parameters:
            city (int): The current city being visited.
            """
            nonlocal edges, neighbors, visit, changes

            # Explore each neighbor of the current city
            for neighbor in neighbors[city]:
                # Skip the neighbor if it has already been visited
                if neighbor in visit:
                    continue
                
                # If the edge is not in the correct direction (neighbor -> city), increment changes
                if (neighbor, city) not in edges:
                    changes += 1
                
                # Mark the neighbor as visited
                visit.add(neighbor)
                
                # Recursively perform DFS on the neighbor
                dfs(neighbor)

        # Start the DFS from city 0
        visit.add(0)
        dfs(0)
        
        # Return the total number of edge reversals needed
        return changes


import unittest
class TestReorderPaths(unittest.TestCase):

    def setUp(self) -> None:
        self.solution =Solution()

    def test_sample_case(self):
        connections =[[0,1],[1,3],[2,3],[4,0],[4,5]]
        self.assertEqual(self.solution.min_reorder(6,connections), 3)

    def test_example_case(self):
        n = 6
        connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
        expected_output = 3
        self.assertEqual(self.solution.min_reorder(n, connections), expected_output)

    def test_no_reordering_needed(self):
        n = 5
        connections = [[1,0],[2,0],[3,0],[4,0]]
        expected_output = 0
        self.assertEqual(self.solution.min_reorder(n, connections), expected_output)

    def test_all_reordering_needed(self):
        n = 5
        connections = [[0,1],[0,2],[0,3],[0,4]]
        expected_output = 4
        self.assertEqual(self.solution.min_reorder(n, connections), expected_output)

    def test_already_ordered(self):
        n = 4
        connections = [[1,0],[2,0],[3,1]]
        expected_output = 0
        self.assertEqual(self.solution.min_reorder(n, connections), expected_output)

    def test_complex_case(self):
        n = 7
        connections = [[0,1],[2,0],[3,2],[3,4],[5,3],[5,6]]
        expected_output = 3
        self.assertEqual(self.solution.min_reorder(n, connections), expected_output)

    def test_single_city(self):
        n = 1
        connections = []
        expected_output = 0
        self.assertEqual(self.solution.min_reorder(n, connections), expected_output)

    def test_two_cities_no_reordering_needed(self):
        n = 2
        connections = [[1,0]]
        expected_output = 0
        self.assertEqual(self.solution.min_reorder(n, connections), expected_output)

    def test_two_cities_reordering_needed(self):
        n = 2
        connections = [[0,1]]
        expected_output = 1
        self.assertEqual(self.solution.min_reorder(n, connections), expected_output)


if __name__=="__main__":
    unittest.main()

"""
Documentation

The Solution class contains the min_reorder method, which is responsible for determining 
the minimum number of edge reversals needed to ensure all paths lead to city 0.


Depth-First Search (DFS):

    The dfs function is defined to explore the graph and count the necessary edge reversals.
    It recursively visits each neighbor of the current city.
    If a neighbor has already been visited, it is skipped.
    If the edge is not in the correct direction (neighbor -> city), the changes counter is 
    incremented.
    The neighbor is marked as visited and dfs is called recursively on the neighbor.

    
"""