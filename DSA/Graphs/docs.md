# Graphs Definition & Properties
- Graph is a collection of object called as Vertices and together with relationship between them called as Edges
- Each Edge in the Graph joins two vertices
- Vertices = {A, B, C, D}
- Edges = {A->B, A->D, B->C,B->D,C->D}

# Applications of Maps
- Road Maps
- Flight Maps

# Types of Edges
- Directed
  - Directed: Edge has orientation (A->B and B->A are not same)
- Undirected
  - Edge has no orientation (A-B or B-A are same)
- Weighted
  - Weights or cost are assigned to each edge
    - Weighted Undirected Graph
    - Weighted Directed Graph
- End Vertices or End Points
  - if edge is directed, first end point is origin and the other is the destination
- Outgoing Edges: directed edges whose origin is that vertex
- Incoming Edges: directed edges whose destination is that vertex
- Degree of Vertex: number of incident edges of the Vertex e.g. degree of vertex b is 3
  - In Degree of Vertex : number of incoming edges of the Vertex e.g. 1 (A->B)
  - Out Degree of Vertex: number of outgoing edges of the vertex e.g. 2(B->D, B->C)
- Path: is a sequence of Edges starting at one Vertex and ending at another Vertex
  - A -B -D -C or A->B->C->D
- Cycle is a path that start and end at the same Vertex (A->B->D->A)
# Graph ADT
- Create(n): create graph with n vertices and n edges
- Add(u, v): insert an edge from u to v
- Delete(u, v): remove an edge from u to v
- Edges(): returns number if edges exists
- Vertices(): returns number of vertices
- Exist(u, v): return true if edge between u and v exists
- Degree(u): returns degree of the vertex u
- InDegree(u): returns in-degree of the vertex u
- OutDegree(u): returns out-degree of the vertex u