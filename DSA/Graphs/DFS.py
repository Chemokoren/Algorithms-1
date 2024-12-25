import numpy as np
from LinkedQueue import LinkedQueue

class Graph:
    def __init__(self, vertices) -> None:
        self._adjMat = np.zeros((vertices, vertices))
        self._vertices = vertices
        self._visited =[0] * vertices

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

    def DFS(self, source):
        """
        Perform Depth-First Search (DFS) on a graph starting from a given source vertex.

        Parameters:
        source (int): The index of the starting vertex for the DFS traversal.

        This method prints the vertices visited during the DFS traversal in the order they are visited.

        Assumptions:
        - The graph is represented using an adjacency matrix `self._adjMat`.
        - The number of vertices in the graph is stored in `self._vertices`.
        - The `self._visited` list is used to track whether a vertex has been visited (1 for visited,
        0 for not visited).

        Example:
        Given a graph with vertices 0, 1, 2, 3 and edges between them:
        If source = 0, the method prints a DFS traversal starting from vertex 0.
        """
        # Check if the current vertex has not been visited
        if self._visited[source] == 0:
            # Mark the current vertex as visited and print it
            print(source, end=' - ')
            self._visited[source] = 1

            # Recursively visit all unvisited adjacent vertices
            for j in range(self._vertices):
                # If there is an edge and the vertex hasn't been visited
                if self._adjMat[source][j] == 1 and self._visited[j] == 0:
                    self.DFS(j)


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
G.DFS(0)

"""
Explanation of the Code:

    Initialization:
        The method starts with a given source vertex.
        The self._visited list tracks which vertices have already been visited.

    Recursive Traversal:
        The algorithm uses recursion to explore as far as possible along each branch before backtracking.
        For each vertex, if it hasn't been visited, it is marked as visited and printed.
        Adjacent vertices are then explored recursively.

    Adjacency Matrix:
        The graph is represented by self._adjMat, where 1 indicates an edge between two vertices and 0 indicates no edge.

    Base Case:
        The recursion stops for a vertex if it has already been visited, ensuring no infinite loops occur.

    Example Walkthrough:
    
    For a graph with 4 vertices (0 to 3) and the following adjacency matrix:
    
    [[0, 1, 0, 0],
     [1, 0, 1, 1],
     [0, 1, 0, 1],
     [0, 1, 1, 0]]
    
    If source = 0, the traversal order will be 0 - 1 - 2 - 3, as it explores each branch to its end before backtracking.

"""

