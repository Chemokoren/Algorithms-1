import numpy as np
from LinkedQueue import LinkedQueue


class Graph:
    """
    A class to represent a directed graph using an adjacency matrix.

    Attributes:
    ----------
    _adjMat : numpy.ndarray
        A 2D array representing the adjacency matrix of the graph.
        Each entry _adjMat[u][v] indicates the weight of the edge from vertex u to vertex v.
    _vertices : int
        The number of vertices in the graph.

    Methods:
    -------
    insert_edge(u, v, w=1):
        Inserts an edge from vertex u to vertex v with weight w.
    delete_edge(u, v):
        Removes the edge from vertex u to vertex v.
    get_edge(u, v):
        Returns the weight of the edge from vertex u to vertex v.
    vertices_count():
        Returns the number of vertices in the graph.
    edge_count():
        Returns the total number of edges in the graph.
    indegree(u):
        Returns the indegree (number of incoming edges) of vertex u.
    outdegree(u):
        Returns the outdegree (number of outgoing edges) of vertex u.
    display():
        Prints the adjacency matrix of the graph.
    BFS(source):
        Performs Breadth-First Search starting from a given source vertex.
    """

    def __init__(self, vertices) -> None:
        """
        Initialize the graph with the given number of vertices.

        Parameters:
        vertices (int): The number of vertices in the graph.
        """
        self._adjMat = np.zeros((vertices, vertices))
        self._vertices = vertices

    def insert_edge(self, u, v, w=1):
        """
        Insert an edge from vertex u to vertex v with an optional weight.

        Parameters:
        u (int): The source vertex.
        v (int): The destination vertex.
        w (int): The weight of the edge (default is 1).
        """
        self._adjMat[u][v] = w

    def delete_edge(self, u, v):
        """
        Remove the edge from vertex u to vertex v.

        Parameters:
        u (int): The source vertex.
        v (int): The destination vertex.
        """
        self._adjMat[u][v] = 0

    def get_edge(self, u, v):
        """
        Retrieve the weight of the edge from vertex u to vertex v.

        Parameters:
        u (int): The source vertex.
        v (int): The destination vertex.

        Returns:
        float: The weight of the edge.
        """
        return self._adjMat[u][v]

    def vertices_count(self):
        """
        Get the number of vertices in the graph.

        Returns:
        int: The number of vertices.
        """
        return self._vertices

    def edge_count(self):
        """
        Calculate the total number of edges in the graph.

        Returns:
        int: The total number of edges.
        """
        count = 0
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
        for i in range(self._vertices):
            if self._adjMat[u][i] != 0:
                count += 1
        return count

    def display(self):
        """
        Display the adjacency matrix of the graph.
        """
        print(self._adjMat)

    def BFS(self, source):
        """
        Perform Breadth-First Search (BFS) starting from a source vertex.

        Parameters:
        source (int): The starting vertex for the BFS traversal.

        Prints:
        The vertices visited during the BFS traversal in order.
        """
        # Start with the given source vertex
        i = source

        # Create a queue to manage vertices to be explored
        q = LinkedQueue()

        # Track visited vertices, initialized to 0 (not visited)
        visited = [0] * self._vertices

        # Print and mark the source vertex as visited
        print(i, end=' - ')
        visited[i] = 1

        # Add the source vertex to the queue
        q.enqueue(i)

        # Continue traversal until there are no more vertices to explore
        while not q.is_empty():
            # Remove a vertex from the queue
            i = q.dequeue()

            # Check all vertices to find adjacent vertices
            for j in range(self._vertices):
                # If an edge exists and the vertex hasn't been visited
                if self._adjMat[i][j] == 1 and visited[j] == 0:
                    # Print and mark the vertex as visited
                    print(j, end=' - ')
                    visited[j] = 1

                    # Add the vertex to the queue for further exploration
                    q.enqueue(j)


# Example usage
if __name__ == "__main__":
    G = Graph(7)
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

    print("Number of vertices: ", G.vertices_count())
    print("Adjacency Matrix:")
    G.display()
    print("BFS Traversal from vertex 0:")
    G.BFS(0)
