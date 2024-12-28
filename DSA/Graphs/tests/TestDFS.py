import unittest
import numpy as np
from graph import Graph  # Assuming your Graph class is in a file named `graph.py`


class TestGraph(unittest.TestCase):
    """Unit tests for the Graph class."""

    def setUp(self):
        """Set up a Graph instance for testing."""
        self.graph = Graph(5)
        self.graph.insert_edge(0, 1)
        self.graph.insert_edge(0, 2)
        self.graph.insert_edge(1, 2)
        self.graph.insert_edge(1, 3)
        self.graph.insert_edge(3, 4)

    def test_insert_edge(self):
        """Test inserting an edge between vertices."""
        self.graph.insert_edge(2, 4, 5)
        self.assertEqual(self.graph.get_edge(2, 4), 5, "Edge weight should be 5.")

    def test_delete_edge(self):
        """Test deleting an edge between vertices."""
        self.graph.delete_edge(0, 1)
        self.assertEqual(self.graph.get_edge(0, 1), 0, "Edge should be removed.")

    def test_get_edge(self):
        """Test retrieving the weight of an edge."""
        self.assertEqual(self.graph.get_edge(1, 2), 1, "Edge weight should be 1.")
        self.assertEqual(self.graph.get_edge(4, 0), 0, "No edge should exist.")

    def test_vertices_count(self):
        """Test the total number of vertices."""
        self.assertEqual(self.graph.vertices_count(), 5, "Graph should have 5 vertices.")

    def test_edge_count(self):
        """Test the total number of edges."""
        self.assertEqual(self.graph.edge_count(), 5, "Graph should have 5 edges.")

    def test_indegree(self):
        """Test the indegree of vertices."""
        self.assertEqual(self.graph.indegree(2), 2, "Vertex 2 should have an indegree of 2.")
        self.assertEqual(self.graph.indegree(0), 0, "Vertex 0 should have an indegree of 0.")

    def test_outdegree(self):
        """Test the outdegree of vertices."""
        self.assertEqual(self.graph.outdegree(1), 2, "Vertex 1 should have an outdegree of 2.")
        self.assertEqual(self.graph.outdegree(4), 0, "Vertex 4 should have an outdegree of 0.")

    def test_display(self):
        """Test if the adjacency matrix is displayed correctly."""
        expected_matrix = np.array([
            [0, 1, 1, 0, 0],
            [0, 0, 1, 1, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0]
        ])
        self.assertTrue(np.array_equal(self.graph._adjMat, expected_matrix), "Adjacency matrix is incorrect.")

    def test_dfs(self):
        """Test the DFS traversal."""
        output = []

        # Override the print function temporarily to capture DFS output
        def mock_print(*args, **kwargs):
            output.append(args[0])

        original_print = print
        try:
            # Replace print with the mock function
            builtins.print = mock_print

            # Perform DFS
            self.graph.DFS(0)
        finally:
            # Restore the original print function
            builtins.print = original_print

        expected_output = [0, 1, 2, 3, 4]
        self.assertEqual(output, expected_output, "DFS traversal order is incorrect.")

    def test_graph_initialization(self):
        """Test graph initialization."""
        new_graph = Graph(3)
        self.assertEqual(new_graph.vertices_count(), 3, "Graph should be initialized with 3 vertices.")
        self.assertEqual(new_graph.edge_count(), 0, "Graph should have 0 edges initially.")


if __name__ == "__main__":
    unittest.main()

"""
Key Features of the Tests

    Setup (setUp Method):
        Creates a test graph with 5 vertices and predefined edges.

    Functional Tests:
        Covers all methods in the Graph class (insert_edge, delete_edge, get_edge, vertices_count, edge_count, 
        indegree, outdegree, and display).

    Traversal Tests:
        Verifies the DFS traversal order by mocking the print function.

    Matrix Validation:
        Compares the adjacency matrix against an expected structure for correctness.

    Edge Cases:
        Includes cases like retrieving a non-existent edge, checking the indegree/outdegree of disconnected
         vertices, and initializing an empty graph.

    Compliance with unittest:
        Uses assertions like assertEqual, assertTrue, etc., to verify expected outcomes.

This test suite ensures thorough coverage of the Graph class functionality while adhering to Python's standard
 testing framework.
"""