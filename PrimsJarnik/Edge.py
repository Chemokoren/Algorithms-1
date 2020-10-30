class Edge(object):
    def __init__(self,weight, startVertex, targetVertex):
        self.weight =weight
        self.startVertex =startVertex
        self.targetVertex =targetVertex

    def __cmp__(self, otherEdge):
        return self.cmp(self.weight,otherEdge.weight)

    def __lt__(self, other):
        return self.weight < other.weight
    