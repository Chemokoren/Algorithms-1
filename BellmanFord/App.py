from BellmanFord.Algorithm import Algorithm
from BellmanFord.Node import Node
from BellmanFord.Edge import Edge

node1 =Node("A")
node2 =Node("B")
node3 =Node("C")
node4 =Node("D")


edge1 =Edge(1, node1,node2)
edge2 =Edge(1, node2,node3)
edge3 =Edge(1, node3,node4)
edge4 =Edge(-10, node3,node2)
edge5 =Edge(300, node1,node4)

node1.adjacenciesList.append(edge1)
node1.adjacenciesList.append(edge2)
node2.adjacenciesList.append(edge3)
node3.adjacenciesList.append(edge4)
node3.adjacenciesList.append(edge2)

vertexList =[node1,node2, node3, node4]
edgeList =[edge1, edge2, edge3,edge4,edge5]

algorithm =Algorithm()
algorithm.calculateShortestPath(vertexList,edgeList, node1)
algorithm.getShortestPathTo(node4)