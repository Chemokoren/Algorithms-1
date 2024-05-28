from typing import List
import collections
import heapq
"""
You are given a network of n nodes labeled from 1 to n. You  are also given times, a list of
travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the
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
    """
    This class provides a solution to find the minimum time required to send information to all nodes in a network.

    The problem considers a network represented as a directed weighted graph. Each edge has a starting node, an ending node,
    and a weight representing the time it takes to transmit information between those nodes. The function calculates the
    minimum time needed to send information from a specific source node (k) to all other nodes in the network,
    assuming information can only be sent along directed edges.

    - A negative weight cycle in the graph would invalidate this algorithm.
    """

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        Calculates the minimum time needed to send information to all nodes in a network.

        Args:
            times (List[List[int]]): A list of lists representing the edges in the network. Each sublist `[u, v, w]`
                                       represents a directed edge from node `u` to node `v` with weight `w` (time).
            n (int): The total number of nodes in the network.
            k (int): The source node (node k) from which information is sent.

        Returns:
            int: The minimum time required to send information to all nodes in the network, or -1 if not possible.
        """

        # Build a dictionary to store outgoing edges (neighbors) and their weights for each node
        neighbors = collections.defaultdict(list)
        for source, destination, weight in times:
            neighbors[source].append((destination, weight))

        # Min-heap to prioritize exploring nodes with the shortest travel time so far
        min_heap = [(0, k)]  # Starting node (k) with initial time 0

        # Set to keep track of visited nodes
        visited = set()
        # Minimum time to reach any visited node yet
        shortest_time = 0

        while min_heap:
            # Extract node with the shortest travel time so far
            current_time, current_node = heapq.heappop(min_heap)

            # Skip if the node has already been visited
            if current_node in visited:
                continue

            visited.add(current_node)
            shortest_time = max(shortest_time, current_time)  # Update minimum time

            # Explore unvisited neighbors of the current node
            for neighbor, edge_weight in neighbors[current_node]:
                if neighbor not in visited:
                    # Add neighbor and updated travel time to the min-heap
                    heapq.heappush(min_heap, (current_time + edge_weight, neighbor))

        # If all nodes were not visited, information cannot reach all nodes
        return shortest_time if len(visited) == n else -1


import unittest
class TestNetworkDelayTime(unittest.TestCase):

    """
    These tests cover various network structures, edge weights, and potential edge cases to validate the code's accuracy and
    robustness for different network topologies.

    test_single_node: Checks the behavior with a single node network.
    test_all_connected: Tests a fully connected network with equal weights to ensure all nodes are reachable.
    test_disconnected_graph: Verifies that the function returns -1 if not all nodes can be reached from the source.
    test_negative_weight: Attempts to call the function with a negative weight edge, which should raise an exception
    (since Dijkstra's algorithm doesn't handle negative weight cycles).
    test_complex_network: Evaluates the function with a more complex network with varying weights to ensure it handles different scenarios.
    """
    def setUp(self):
        self.solution = Solution()

    def test_single_node(self):
        """Tests the function with a network containing a single node."""

        times = []
        n = 1
        k = 1
        result = self.solution.networkDelayTime(times, n, k)
        self.assertEqual(result, 0)


    def test_all_connected(self):
        """Tests the function with a fully connected network with equal weights."""
        times = [[1, 2, 1], [1, 3, 1], [2, 3, 1]]
        n = 3
        k = 1
        result = self.solution.networkDelayTime(times, n, k)
        self.assertEqual(result, 1)

    def test_disconnected_graph(self):
        """Tests the function with a disconnected graph."""
        times = [[1, 2, 1]]
        n = 3
        k = 1
        result = self.solution.networkDelayTime(times, n, k)
        self.assertEqual(result, -1)  # Information cannot reach all nodes

    def test_negative_weight(self):
        """Tests the function with a negative weight edge."""
        times = [[1, 2, -1]]
        n = 2
        k = 1
        with self.assertRaises(Exception):  # Raise an exception for negative weights
            result = self.solution.networkDelayTime(times, n, k)

    def test_complex_network(self):
        """Tests the function with a more complex network with varying weights."""
        times = [[1, 2, 1], [2, 3, 7], [1, 3, 4], [2, 4, 2]]
        n = 4
        k = 1
        result = self.solution.networkDelayTime(times, n, k)
        self.assertEqual(result, 9)

if __name__ == '__main__':
    unittest.main()
