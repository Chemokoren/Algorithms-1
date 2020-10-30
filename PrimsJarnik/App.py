from PrimsJarnik.Algorithm import Algorithm
from PrimsJarnik.Vertex import Vertex
from PrimsJarnik.Edge import Edge

node1 =Vertex("1")
node2 =Vertex("2")
node3 =Vertex("3")
node4 =Vertex("4")

edge1 =Edge(1,node1, node2)
edge2 =Edge(1,node1, node3)
edge3 =Edge(0.01,node1, node4)
edge4 =Edge(1,node3, node4)

node1.adjacenciesList.append(edge1)
node1.adjacenciesList.append(edge2)
node1.adjacenciesList.append(edge3)
node3.adjacenciesList.append(edge4)

unvisitedList =[]
unvisitedList.append(node1)
unvisitedList.append(node2)
unvisitedList.append(node3)
unvisitedList.append(node4)

algorithm =Algorithm(unvisitedList)
algorithm.constructSpanningTree(node1)