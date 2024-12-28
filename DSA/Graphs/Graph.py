import numpy as np

class Graph:
    """
    A class to represent a directed graph using an adjacency matrix.

    Attributes:
    -----------
    _adjMat : numpy.ndarray
        A 2D array representing the adjacency matrix of the graph.
    _vertices : int
        The number of vertices in the graph.

    Methods:
    --------
    insert_edge(u, v, w=1):
        Inserts a directed edge from vertex u to vertex v with weight w.
    delete_edge(u, v):
        Deletes the edge from vertex u to vertex v.
    get_edge(u, v):
        Returns the weight of the edge from vertex u to vertex v.
    vertices_count():
        Returns the number of vertices in the graph.
    edge_count():
        Returns the total number of edges in the graph.
    indegree(u):
        Returns the indegree of the vertex u.
    outdegree(u):
        Returns the outdegree of the vertex u.
    display():
        Prints the adjacency matrix of the graph.
    """

    def __init__(self, vertices) -> None:
        """
        Initializes the Graph with a specified number of vertices.

        Parameters:
        ----------
        vertices : int
            The number of vertices in the graph.
        """
        self._adjMat = np.zeros((vertices, vertices))
        self._vertices = vertices

    def insert_edge(self, u, v, w=1):
        """
        Inserts a directed edge from vertex u to vertex v with an optional weight.

        Parameters:
        ----------
        u : int
            The starting vertex.
        v : int
            The ending vertex.
        w : int, optional
            The weight of the edge (default is 1).
        """
        self._adjMat[u][v] = w

    def delete_edge(self, u, v):
        """
        Deletes the directed edge from vertex u to vertex v.

        Parameters:
        ----------
        u : int
            The starting vertex.
        v : int
            The ending vertex.
        """
        self._adjMat[u][v] = 0

    def get_edge(self, u, v):
        """
        Returns the weight of the edge from vertex u to vertex v.

        Parameters:
        ----------
        u : int
            The starting vertex.
        v : int
            The ending vertex.

        Returns:
        -------
        float
            The weight of the edge (0 if no edge exists).
        """
        return self._adjMat[u][v]

    def vertices_count(self):
        """
        Returns the number of vertices in the graph.

        Returns:
        -------
        int
            The number of vertices.
        """
        return self._vertices

    def edge_count(self):
        """
        Returns the total number of edges in the graph.

        Returns:
        -------
        int
            The total number of edges.
        """
        count = 0
        for i in range(self._vertices):
            for j in range(self._vertices):
                if self._adjMat[i][j] != 0:
                    count += 1
        return count

    def indegree(self, u):
        """
        Returns the indegree of a given vertex.

        Parameters:
        ----------
        u : int
            The vertex for which indegree is to be calculated.

        Returns:
        -------
        int
            The indegree of the vertex.
        """
        count = 0
        for i in range(self._vertices):
            if self._adjMat[i][u] != 0:
                count += 1
        return count

    def outdegree(self, u):
        """
        Returns the outdegree of a given vertex.

        Parameters:
        ----------
        u : int
            The vertex for which outdegree is to be calculated.

        Returns:
        -------
        int
            The outdegree of the vertex.
        """
        count = 0
        for i in range(self._vertices):
            if self._adjMat[u][i] != 0:
                count += 1
        return count

    def display(self):
        """
        Prints the adjacency matrix of the graph.
        """
        print(self._adjMat)


# Example usage of the Graph class
if __name__ == "__main__":
    G = Graph(7)
    print('Graph Adjacency Matrix (Initial)')
    G.display()

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

    print('Graph Adjacency Matrix (After Adding Edges)')
    G.display()
    print('Number of Vertices:', G.vertices_count())
    print('Number of Edges:', G.edge_count())
    print('Outdegree of Vertex 2:', G.outdegree(2))
