import unittest
import numpy as np
from DSA.Graphs.Graph import Graph  # Assuming the Graph class is saved in graph.py

class TestGraph(unittest.TestCase):
    def setUp(self):
        """
        Set up a Graph instance before each test.
        """
        self.graph = Graph(5)  # Create a graph with 5 vertices

    def test_insert_edge(self):
        """
        Test if edges are inserted correctly.
        """
        self.graph.insert_edge(0, 1, 5)
        self.assertEqual(self.graph.get_edge(0, 1), 5, "Edge weight should be 5")

        self.graph.insert_edge(2, 3)
        self.assertEqual(self.graph.get_edge(2, 3), 1, "Default edge weight should be 1")

    def test_delete_edge(self):
        """
        Test if edges are deleted correctly.
        """
        self.graph.insert_edge(0, 1, 5)
        self.graph.delete_edge(0, 1)
        self.assertEqual(self.graph.get_edge(0, 1), 0, "Edge should be deleted")

    def test_get_edge(self):
        """
        Test the retrieval of edge weights.
        """
        self.graph.insert_edge(1, 2, 7)
        self.assertEqual(self.graph.get_edge(1, 2), 7, "Edge weight should be 7")
        self.assertEqual(self.graph.get_edge(0, 1), 0, "Edge weight should be 0 for non-existent edge")

    def test_vertices_count(self):
        """
        Test the number of vertices in the graph.
        """
        self.assertEqual(self.graph.vertices_count(), 5, "Graph should have 5 vertices")

    def test_edge_count(self):
        """
        Test the total number of edges in the graph.
        """
        self.assertEqual(self.graph.edge_count(), 0, "Initial edge count should be 0")

        self.graph.insert_edge(0, 1)
        self.graph.insert_edge(1, 2)
        self.graph.insert_edge(2, 3)
        self.assertEqual(self.graph.edge_count(), 3, "Graph should have 3 edges")

    def test_indegree(self):
        """
        Test the calculation of indegree for vertices.
        """
        self.graph.insert_edge(0, 1)
        self.graph.insert_edge(2, 1)
        self.graph.insert_edge(3, 1)
        self.assertEqual(self.graph.indegree(1), 3, "Vertex 1 should have an indegree of 3")

    def test_outdegree(self):
        """
        Test the calculation of outdegree for vertices.
        """
        self.graph.insert_edge(1, 2)
        self.graph.insert_edge(1, 3)
        self.graph.insert_edge(1, 4)
        self.assertEqual(self.graph.outdegree(1), 3, "Vertex 1 should have an outdegree of 3")

    def test_display(self):
        """
        Test the display method for correct adjacency matrix representation.
        """
        self.graph.insert_edge(0, 1)
        self.graph.insert_edge(1, 2)
        expected_matrix = np.zeros((5, 5))
        expected_matrix[0][1] = 1
        expected_matrix[1][2] = 1

        with self.assertLogs(level='INFO') as log:
            self.graph.display()
        np.testing.assert_array_equal(self.graph._adjMat, expected_matrix, "Adjacency matrix should match the expected matrix")

if __name__ == '__main__':
    unittest.main()
