import heapq


class Algorithm(object):
    def __init__(self, unvisitedList):
        self.unvisitedList =unvisitedList
        self.spanningTree =[]
        self.edgeHeap =[]
        self.fullcost =0

    def constructSpanningTree(self,vertex):
        self.unvisitedList.remove(vertex)

        while self.unvisitedList:
            for edge in vertex.adjacenciesList:
                if edge.targetVertex in self.unvisitedList:
                    heapq.heappush(self.edgeHeap,edge)

                minEdge =heapq.heappop(self.edgeHeap)

                self.spanningTree.append(minEdge)
                print("Edge added to spanning tree: %s -%s" % (minEdge.startVertex.name, minEdge.targetVertex.name))
                self.fullcost +=minEdge.weight

                vertex =minEdge.targetVertex
                self.unvisitedList.remove(vertex)

    def getSpanningTree(self):
        return self.spanningTree

    

