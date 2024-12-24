import numpy as np
from LinkedQueue import LinkedQueue

class Graph:
    def __init__(self, vertices) -> None:
        self._adjMat = np.zeros((vertices, vertices))
        self._vertices = vertices

    def insert_edge(self, u, v, w=1):
        self._adjMat[u][v] =w

    def delete_edge(self,u, v):
        self._adjMat[u][v] =0

    def get_edge(self, u,v):
        return self._adjMat[u][v]

    def vertices_count(self):
        return self._vertices

    def edge_count(self):
        count = 0
        for i in range(self._vertices):
            for j in range(self._vertices):
                if not self._adjMat[i][j] == 0:
                    count += 1
        return count

    def indegree(self, u):
        count = 0
        for i in range(self._vertices):
            if not self._adjMat[i][u] == 0:
                count += 1
        return count

    def outdegree(self, u):
        count = 0
        for i in range(self._vertices):
            if not self._adjMat[u][i] == 0:
                count += 1
        return count

    def display(self):
        print(self._adjMat)


    def BFS(self, source):
        """
        Perform Breadth-First Search (BFS) on a graph starting from a given source vertex.

        Parameters:
        source (int): The index of the starting vertex for the BFS traversal.

        This method prints the vertices visited during the BFS traversal in the order they are visited.

        Assumptions:
        - The graph is represented using an adjacency matrix `self._adjMat`.
        - The number of vertices in the graph is stored in `self._vertices`.
        - A `LinkedQueue` class is used to manage the queue operations during traversal.

        Example:
        Given a graph with vertices 0, 1, 2, 3 and edges between them:
        If source = 0, the method prints a BFS traversal starting from vertex 0.
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


G =Graph(7)

G.insert_edge(0,1)
G.insert_edge(0,5)
G.insert_edge(0,6)
G.insert_edge(1,0)
G.insert_edge(1,2)
G.insert_edge(1,5)
G.insert_edge(1,6)
G.insert_edge(2,3)
G.insert_edge(2,4)
G.insert_edge(2,6)
G.insert_edge(3,4)
G.insert_edge(4,2)
G.insert_edge(4,5)
G.insert_edge(5,2)
G.insert_edge(5,3)
G.insert_edge(6,3)
G.BFS(0)



"""
BFS Traversal

Explanation of the Code:

    Initialization:
        The method starts with a source vertex.
        A queue is initialized to keep track of the vertices to explore in a FIFO manner.
        A visited list tracks whether a vertex has already been visited.

    Traversal:
        The BFS algorithm explores all the adjacent vertices of the current vertex.
        For each unvisited adjacent vertex, it marks it as visited, prints it, and enqueues it.

    Queue Operations:
        The queue ensures vertices are processed in the correct order.
        A vertex is dequeued for exploration, and its neighbors are enqueued if they haven't been visited.

    Adjacency Matrix:
        The graph is represented by an adjacency matrix (self._adjMat), where 1 indicates an edge between two vertices.

This code follows the standard BFS algorithm and can handle graphs represented by adjacency matrices efficiently.
"""
