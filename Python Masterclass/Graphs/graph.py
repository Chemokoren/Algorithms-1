'''
addVertex
-accepts a name of a vertex
- it should add a key to the adjacency list with the name of the vertex and set its 
value to be an empty array

'''
class Graph:

    def __init__(self) -> None:
        self.adjacency_list ={}

    def addVertex(self,vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] =[]

    def addEdge(self,vertex1,vertex2):
        if vertex1 in self.adjacency_list: 
            self.adjacency_list[vertex1].append(vertex2)
        if vertex2 in self.adjacency_list: 
            self.adjacency_list[vertex2].append(vertex1)
    
    def removeEdge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list: 
            self.adjacency_list[vertex1].remove(vertex2)
        if vertex2 in self.adjacency_list: 
            self.adjacency_list[vertex2].remove(vertex1)

    def removeVertex(self, vertex):

        while len(self.adjacency_list[vertex]):
            for i in self.adjacency_list[vertex]:
                self.removeEdge(vertex,i)

        self.adjacency_list.pop(vertex)

    
sol =Graph()
sol.addVertex("Tokyo")
sol.addVertex("Nairobi")
sol.addVertex("Eldy")
sol.addVertex("Kisumu")
print(sol.adjacency_list)
sol.addEdge("Nairobi","Eldy")
sol.addEdge("Nairobi","Kisumu")
print(sol.adjacency_list)
sol.removeEdge("Nairobi","Kisumu")
sol.removeEdge("Nairobi","Eldy")
print(sol.adjacency_list)
sol.addEdge("Nairobi","Eldy")
sol.addEdge("Nairobi","Kisumu")
sol.removeVertex("Nairobi")
print("after removing edge: ", sol.adjacency_list)