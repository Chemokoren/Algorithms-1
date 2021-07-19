"""
program to demonstrate the adjacency list representation of the graph

Pros: Saves space O(|V|+|E|) . In the worst case, there can be C(V, 2) number of edges in a
graph thus consuming O(V^2) space. Adding a vertex is easier.
Cons: Queries like whether there is an edge from vertex u to vertex v are not efficient 
and can be done O(V).

"""

# A class to represent the adjacency list of the node
class AdjNode:
    def __init__(self, data) -> None:
        self.vertex = data
        self.next = None

# A class to represent a graph. A graph is the list  of the adjacency lists.
# Size of the array will be the no. of the vertices "V"
class Graph:
    def __init__(self, vertices) -> None:
        self.V = vertices
        self.graph =[None] *self.V

    # Function to add an edge in an undirected graph
    def add_edge(self, src, dest):
        # adding the node to the source node
        node = AdjNode(dest)
        node.next = self.graph[src]
        self.graph[src] =node

        # Adding the source node to the destination as it is the undirected graph
        node = AdjNode(src)
        node.next = self.graph[dest]
        self.graph[dest] =node

    # Function to print the graph
    def print_graph(self):
        for i in range(self.V):
            print("Adjacency list of vertex {} \n head".format(i), end=" ")
            temp = self.graph[i]
            while temp:
                print("->{}". format(temp.vertex), end=" ")
                temp =temp.next

            print("\n")

if __name__=='__main__':
    V = 5
    graph =Graph(V)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)

    graph.print_graph()


print(" \n A simple representation of graph using Adjacency Matrix: \n")

"""

A simple representation of graph using Adjacency Matrix


"""

class Graph:
    
    def __init__(self, numvertex) -> None:
        self.adjMatrix =[[-1]*numvertex for x in range(numvertex)]
        self.numvertex = numvertex
        self.vertices ={}
        self.verticeslist =[0] * numvertex

    def set_vertex(self, vtx, id):
        if 0 <= vtx <= self.numvertex:
            self.vertices[id] = vtx
            self.verticeslist[vtx] =id

    def set_edge(self, frm , to, cost=0):
        frm =self.vertices[frm]
        to = self.vertices[to]
        self.adjMatrix[frm][to] =cost
        # for directed graph do not add this
        self.adjMatrix[to][frm] =cost


    def get_vertex(self):
        return self.verticeslist


    def get_edges(self):
        edges =[]
        for i in range(self.numvertex):
            for j in range(self.numvertex):
                if(self.adjMatrix[i][j] !=-1):
                    edges.append((self.verticeslist[i], self.verticeslist[j], self.adjMatrix[i][j]))
        return edges

    def get_matrix(self):
        return self.adjMatrix

G = Graph(6)
G.set_vertex(0, 'a')
G.set_vertex(1, 'b')
G.set_vertex(2, 'c')
G.set_vertex(3, 'd')
G.set_vertex(4, 'e')
G.set_vertex(5, 'f')
G.set_edge('a','e',10)
G.set_edge('a','c',20)
G.set_edge('c','b',30)
G.set_edge('b','e',40)
G.set_edge('e','d',50)
G.set_edge('f','e',60)

print("Vertices of Graph")
print(G.get_vertex())
print("Edges of Graph")
print(G.get_edges())
print("Adjacency Matrix of Graph")
print(G.get_matrix())