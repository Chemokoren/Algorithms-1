"""
Clone Graph

Given a reference of a node in a connected undirected graph.

Return a deep copy(clone) of the graph.

Each node in the graph contains a val(int) and a list(List[Node]) of its neighbors.

class Node{

    public int val;
    public List<Node> neighbors;
}
Time : O(n) =E+V
"""

class Node:
    """
    Represents a node in a graph.
    """

    def __init__(self, val=0, neighbors=None):
        """
        Initializes a new Node.

        Args:
            val (int): The value associated with the node (default is 0).
            neighbors (List[Node]): List of neighboring nodes (default is an empty list).
        """
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    """
    Provides a solution for cloning a graph.
    """

    def cloneGraph(self, node: Node) -> Node:
        """
        Clones the given graph starting from the specified node.

        Args:
            node (Node): The starting node to clone.

        Returns:
            Node: The cloned graph.
        """
        oldToNew = {}

        def dfs(node):
            """
            Performs depth-first search to clone the graph.

            Args:
                node (Node): The current node to process.

            Returns:
                Node: The cloned node.
            """
            if node in oldToNew:
                return oldToNew[node]

            copy = Node(node.val)
            oldToNew[node] = copy

            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node) if node else None


import unittest

class TestSolution(unittest.TestCase):
    def test_cloneGraph_single_node(self):
        # Test with a single node graph
        node1 = Node(1)
        s = Solution()
        cloned_node1 = s.cloneGraph(node1)
        self.assertEqual(cloned_node1.val, 1)
        self.assertEqual(len(cloned_node1.neighbors), 0)

    def test_cloneGraph_multiple_nodes(self):
        # Test with a graph containing multiple nodes
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node1.neighbors = [node2, node3]
        node2.neighbors = [node1, node3]
        node3.neighbors = [node1, node2]

        s = Solution()
        cloned_node1 = s.cloneGraph(node1)

        # Check values
        self.assertEqual(cloned_node1.val, 1)
        self.assertEqual(cloned_node1.neighbors[0].val, 2)
        self.assertEqual(cloned_node1.neighbors[1].val, 3)

        # Check references (should be different objects)
        self.assertIsNot(cloned_node1, node1)
        self.assertIsNot(cloned_node1.neighbors[0], node2)
        self.assertIsNot(cloned_node1.neighbors[1], node3)

    def test_cloneGraph_empty_graph(self):
        # Test with an empty graph (None input)
        s = Solution()
        cloned_node = s.cloneGraph(None)
        self.assertIsNone(cloned_node)

if __name__ == "__main__":
    unittest.main()
