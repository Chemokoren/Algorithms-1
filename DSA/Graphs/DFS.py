import numpy as np
from LinkedQueue import LinkedQueue

class Graph:
    """
    A class to represent a directed graph using an adjacency matrix.

    Attributes:
        _adjMat (numpy.ndarray): The adjacency matrix of the graph.
        _vertices (int): The number of vertices in the graph.
        _visited (list[int]): Tracks visited vertices during traversals.
    """

    def __init__(self, vertices) -> None:
        """
        Initialize a graph with a given number of vertices.

        Parameters:
        vertices (int): The number of vertices in the graph.
        """
        self._adjMat   = np.zeros((vertices, vertices))  # Initialize adjacency matrix with zeros
        self._vertices = vertices  # Store the number of vertices
        self._visited  = [0] * vertices  # Initialize visited list for traversal algorithms

    def insert_edge(self, u, v, w=1):
        """
        Insert an edge between two vertices.

        Parameters:
        u (int): The source vertex.
        v (int): The destination vertex.
        w (int, optional): The weight of the edge (default is 1).
        """
        self._adjMat[u][v] = w  # Add the edge to the adjacency matrix

    def delete_edge(self, u, v):
        """
        Delete an edge between two vertices.

        Parameters:
        u (int): The source vertex.
        v (int): The destination vertex.
        """
        self._adjMat[u][v] = 0  # Remove the edge from the adjacency matrix

    def get_edge(self, u, v):
        """
        Retrieve the weight of an edge between two vertices.

        Parameters:
        u (int): The source vertex.
        v (int): The destination vertex.

        Returns:
        int: The weight of the edge, or 0 if no edge exists.
        """
        return self._adjMat[u][v]

    def vertices_count(self):
        """
        Get the total number of vertices in the graph.

        Returns:
        int: The number of vertices.
        """
        return self._vertices

    def edge_count(self):
        """
        Count the total number of edges in the graph.

        Returns:
        int: The number of edges.
        """
        count = 0
        # Iterate through the adjacency matrix to count non-zero entries
        for i in range(self._vertices):
            for j in range(self._vertices):
                if self._adjMat[i][j] != 0:
                    count += 1
        return count

    def indegree(self, u):
        """
        Calculate the indegree of a vertex.

        Parameters:
        u (int): The vertex index.

        Returns:
        int: The number of incoming edges to the vertex.
        """
        count = 0
        # Count non-zero entries in the column corresponding to vertex u
        for i in range(self._vertices):
            if self._adjMat[i][u] != 0:
                count += 1
        return count

    def outdegree(self, u):
        """
        Calculate the outdegree of a vertex.

        Parameters:
        u (int): The vertex index.

        Returns:
        int: The number of outgoing edges from the vertex.
        """
        count = 0
        # Count non-zero entries in the row corresponding to vertex u
        for i in range(self._vertices):
            if self._adjMat[u][i] != 0:
                count += 1
        return count

    def display(self):
        """
        Display the adjacency matrix of the graph.
        """
        print(self._adjMat)

    def DFS(self, source):
        """
        Perform Depth-First Search (DFS) starting from a given vertex.

        Parameters:
        source (int): The index of the starting vertex.

        This method prints the vertices in the order they are visited.
        """
        # If the vertex has not been visited
        if self._visited[source] == 0:
            print(source, end=' - ')  # Print the current vertex
            self._visited[source] = 1  # Mark as visited

            # Explore all adjacent vertices
            for j in range(self._vertices):
                if self._adjMat[source][j] == 1 and self._visited[j] == 0:
                    self.DFS(j)  # Recursively perform DFS on adjacent vertices


# Example usage
if __name__ == "__main__":
    G = Graph(7)

    # Insert edges into the graph
    G.insert_edge(0, 1)
    G.insert_edge(0, 5)
    G.insert_edge(0, 6)
    G.insert_edge(1, 0)
    G.insert_edge(1, 2)
    G.insert_edge(1, 5)
    G.insert_edge(1, 6)
    G.insert_edge(2, 3)
    G.insert_edge(2, 4)
    G.insert_edge(2, 6)
    G.insert_edge(3, 4)
    G.insert_edge(4, 2)
    G.insert_edge(4, 5)
    G.insert_edge(5, 2)
    G.insert_edge(5, 3)
    G.insert_edge(6, 3)

    # Perform DFS traversal
    print("DFS Traversal starting from vertex 0:")
    G.DFS(0)
