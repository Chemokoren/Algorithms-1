import unittest
import numpy as np
from graph import Graph  # Replace with the path to your Graph module
from LinkedQueue import LinkedQueue


class TestGraph(unittest.TestCase):
    def setUp(self):
        """Set up a graph instance for testing."""
        self.graph = Graph(5)  # Create a graph with 5 vertices

    def test_insert_edge(self):
        """Test inserting edges into the graph."""
        self.graph.insert_edge(0, 1, 10)
        self.assertEqual(self.graph.get_edge(0, 1), 10)
        self.assertEqual(self.graph.get_edge(1, 0), 0)  # Check directionality

    def test_delete_edge(self):
        """Test deleting edges from the graph."""
        self.graph.insert_edge(0, 1)
        self.graph.delete_edge(0, 1)
        self.assertEqual(self.graph.get_edge(0, 1), 0)

    def test_get_edge(self):
        """Test retrieving edge weights."""
        self.graph.insert_edge(0, 2, 5)
        self.assertEqual(self.graph.get_edge(0, 2), 5)
        self.assertEqual(self.graph.get_edge(2, 0), 0)

    def test_vertices_count(self):
        """Test counting vertices in the graph."""
        self.assertEqual(self.graph.vertices_count(), 5)

    def test_edge_count(self):
        """Test counting edges in the graph."""
        self.graph.insert_edge(0, 1)
        self.graph.insert_edge(1, 2)
        self.graph.insert_edge(2, 3)
        self.assertEqual(self.graph.edge_count(), 3)

    def test_indegree(self):
        """Test calculating the indegree of a vertex."""
        self.graph.insert_edge(0, 1)
        self.graph.insert_edge(2, 1)
        self.graph.insert_edge(3, 1)
        self.assertEqual(self.graph.indegree(1), 3)
        self.assertEqual(self.graph.indegree(0), 0)

    def test_outdegree(self):
        """Test calculating the outdegree of a vertex."""
        self.graph.insert_edge(1, 0)
        self.graph.insert_edge(1, 2)
        self.graph.insert_edge(1, 3)
        self.assertEqual(self.graph.outdegree(1), 3)
        self.assertEqual(self.graph.outdegree(0), 0)

    def test_bfs(self):
        """Test the BFS traversal."""
        self.graph.insert_edge(0, 1)
        self.graph.insert_edge(0, 2)
        self.graph.insert_edge(1, 3)
        self.graph.insert_edge(2, 4)

        # Capture BFS output
        from io import StringIO
        import sys
        captured_output = StringIO()
        sys.stdout = captured_output

        self.graph.BFS(0)

        sys.stdout = sys.__stdout__  # Restore standard output
        output = captured_output.getvalue().strip()

        # Verify the BFS traversal output
        expected_output = "0 - 1 - 2 - 3 - 4 -"
        self.assertEqual(output, expected_output)

    def test_display(self):
        """Test displaying the adjacency matrix."""
        self.graph.insert_edge(0, 1)
        self.graph.insert_edge(1, 2)

        # Expected adjacency matrix
        expected_matrix = np.zeros((5, 5))
        expected_matrix[0][1] = 1
        expected_matrix[1][2] = 1

        np.testing.assert_array_equal(self.graph._adjMat, expected_matrix)


if __name__ == "__main__":
    unittest.main()

"""
Explanation of Tests:

    setUp Method:
        Initializes a Graph instance before each test to ensure tests are independent.

    Edge Operations:
        Tests for insert_edge, delete_edge, and get_edge validate edge handling.

    Graph Properties:
        vertices_count and edge_count ensure the graph maintains accurate vertex and edge counts.

    Degree Methods:
        indegree and outdegree tests confirm the calculation of incoming and outgoing edges.

    BFS:
        Captures and verifies the BFS traversal output for correctness.

    Display:
        Compares the adjacency matrix output directly with the expected matrix using NumPy's assert_array_equal.

Running the Tests:

Save the above test code in a file (e.g., test_graph.py) and run it using:

python -m unittest test_graph.py

Coverage:

These tests cover all methods in the Graph class and ensure they work as expected under various scenarios.

"""