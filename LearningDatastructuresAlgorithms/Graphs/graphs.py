import numpy as np

class Graph:

    def __init__(self, vertices):
        self._adjMat = np.zeros((vertices, vertices))
        self._vertices = vertices

    def insert_edge(self, u, v, w=1):
        self._adjMat[u][v] = w

    def delete_edge(self, u, v):
        self._adjMat[u][v] =0

    def get_edge(self, u, v):
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
            if not self._adjMat[u][i] ==0:
                count += 1
        return count

    def display(self):
        print(self._adjMat)

G = Graph(7)
print("Graph Adjacency Matrix")
G.display()
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

print('Graph  Adjacency Matrix')
G.display()
print('Number of Vertices: ', G.vertices_count())
print('Number of Edges: ', G.edge_count())
print('Outdegree of Vertex 2:', G.outdegree(2))


