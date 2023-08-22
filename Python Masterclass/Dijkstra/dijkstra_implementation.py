# A simple PQ

from importlib.resources import path


class PriorityQueue:
    def __init__(self):
        self.values =[]

    def enqueue(self,val, priority):
        self.values.append({val, priority})
        self.sort()

    def dequeue(self):
        return self.values.pop(0)

    # O(N * log(N)) because we are sorting every time
    def sort(self):
        n = len(self.values)
        for i in range(n):
            print(self.values[i])
    #         if self.values[i].priority < self.values[i+1].priority:
    #             self.values[i],self.values[i+1] =self.values[i+1], self.values[i]


class WeightedGraph:

    def __init__(self):
        self.adjacencyList ={}

    def addVertex(self,vertex):
        if(not self.adjacencyList[vertex]):
            pass
        else:
            self.adjacencyList[vertex] =[]

    def addEdge(self,vertex1, vertex2, weight):
        self.adjacencyList[vertex1].push({node:vertex2, weight:weight})
        self.adjacencyList[vertex2].push({node:vertex1, weight:weight})

    def Dijkstra(self, start, finish):
        nodes = PriorityQueue()
        distances ={}
        previous  ={}
        path =[] # return at the end
        smallest =None

        # build up initial state
        for vertex in self.adjacencyList:
            if (vertex == start):
                distances[vertex] =0
                nodes.enqueue(vertex,0)
            else:
                distances[vertex] =float('inf')
                nodes.enqueue(vertex,float('inf'))
            previous[vertex] =None
        print("check distances", distances)

        # as long as there is something to visit
        while(len(nodes.values)):
            smallest = nodes.dequeue().val
            if(smallest == finish):
                while(previous[smallest]):
                    path.push(smallest)
                    smallest = previous[smallest]
                # we are done
                # build up path to return at end
            if(smallest or distances[smallest] != float('inf')):
                for neighbor in self.adjacencyList[smallest]:
                    # find neighboring node
                    nextNode = self.adjacencyList[smallest][neighbor]

                    # calculate new distance to neighboring node
                    candidate = distances[smallest] + nextNode.weight
                    nextNeighbor =nextNode.node
                    if(candidate < distances[nextNeighbor]):
                        # updating new smallest distance to neighbor
                        distances[nextNeighbor] = candidate

                        # updating previous - How we got to neighbor
                        previous[nextNeighbor] = smallest

                        # enqueue in priority queue with new priority
                        nodes.enqueue(nextNeighbor, candidate)

        return path



graph = WeightedGraph()
graph.addVertex("A")
graph.addVertex("B")
graph.addVertex("C")
graph.addVertex("D")
graph.addVertex("E")
graph.addVertex("F")

graph.addEdge("A","B", 4)
graph.addEdge("A","C", 2)
graph.addEdge("B","E", 3)
graph.addEdge("C","D", 2)
graph.addEdge("C","F", 4)
graph.addEdge("D","E", 3)
graph.addEdge("D","F", 1)
graph.addEdge("E","F", 1)

print(graph.Dijkstra("A", "E"))


# ["A", "C", "D", "F", "E"]