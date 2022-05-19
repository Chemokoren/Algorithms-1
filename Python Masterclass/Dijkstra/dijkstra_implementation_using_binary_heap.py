"""

"""

class WeightedGraph:

    def __init__(self) -> None:
        self.adjacencyList = {}
    
    def addVertex(self, vertex):
        if(not self.adjacencyList[vertex]): self.adjacencyList[vertex] = []
    
    def addEdge(self,vertex1,vertex2, weight):
        self.adjacencyList[vertex1].push({node:vertex2,weight:weight})
        self.adjacencyList[vertex2].push({node:vertex1,weight:weight})
    
    def Dijkstra(self, start, finish):
        nodes = PriorityQueue()
        distances = {}
        previous = {}
        path = [] # to return at end
        smallest =None

        # build up initial state
        for vertex in self.adjacencyList:
            if(vertex == start):
                distances[vertex] = 0
                nodes.enqueue(vertex, 0)
            else:
                distances[vertex] = float('inf')
                nodes.enqueue(vertex, float('inf'))
            previous[vertex] = None
        
        # as long as there is something to visit
        while(nodes.values.length):
            smallest = nodes.dequeue().val
            if(smallest == finish):
                # WE ARE DONE
                # BUILD UP PATH TO RETURN AT END
                while(previous[smallest]):
                    path.push(smallest)
                    smallest = previous[smallest]
                break
            
            if(smallest or distances[smallest] != float('inf')):
                for neighbor in self.adjacencyList[smallest]:
                    # find neighboring node
                    nextNode = self.adjacencyList[smallest][neighbor]
                    
                    # calculate new distance to neighboring node
                    candidate = distances[smallest] + nextNode.weight
                    nextNeighbor = nextNode.node

                    if(candidate < distances[nextNeighbor]):
                        # updating new smallest distance to neighbor
                        distances[nextNeighbor] = candidate
                        # updating previous - How we got to neighbor
                        previous[nextNeighbor] = smallest
                        # enqueue in priority queue with new priority
                        nodes.enqueue(nextNeighbor, candidate)
                
        return path.concat(smallest).reverse();     
    


# min binary heap
class PriorityQueue:
    def __init__(self) -> None:
        self.values = []
    
    def enqueue(sefl, val, priority):
        newNode = Node(val, priority)
        self.values.push(newNode)
        self.bubbleUp()
    
    def bubbleUp(self):
        idx = self.values.length - 1
        element = self.values[idx]
        while(idx > 0):
            parentIdx = Math.floor((idx - 1)/2)
            parent = self.values[parentIdx]
            if(element.priority >= parent.priority): break
            self.values[parentIdx] = element
            self.values[idx] = parent
            idx = parentIdx
    
    def dequeue(self):
        min = self.values[0]
        end = self.values.pop()
        if(self.values.length > 0):
            self.values[0] = end
            self.sinkDown()
        return min
    
    def sinkDown(self):
        idx = 0
        length = self.values.length
        element = self.values[0]
        while(True):
            leftChildIdx = 2 * idx + 1
            rightChildIdx = 2 * idx + 2
            leftChild,rightChild
            swap = null

            if(leftChildIdx < length):
                leftChild = self.values[leftChildIdx]
                if(leftChild.priority < element.priority):
                    swap = leftChildIdx
                
            
            if(rightChildIdx < length):
                rightChild = self.values[rightChildIdx];
                if(
                    (swap === null && rightChild.priority < element.priority) || 
                    (swap !== null && rightChild.priority < leftChild.priority)
                ):
                swap = rightChildIdx
                
            
            if(swap === None): break
            self.values[idx] = self.values[swap];
            self.values[swap] = element;
            idx = swap;
        
    


class Node:
    def __init__(self, val, priority):
        self.val = val;
        self.priority = priority
    


graph =  WeightedGraph()
graph.addVertex("A");
graph.addVertex("B");
graph.addVertex("C");
graph.addVertex("D");
graph.addVertex("E");
graph.addVertex("F");

graph.addEdge("A","B", 4);
graph.addEdge("A","C", 2);
graph.addEdge("B","E", 3);
graph.addEdge("C","D", 2);
graph.addEdge("C","F", 4);
graph.addEdge("D","E", 3);
graph.addEdge("D","F", 1);
graph.addEdge("E","F", 1);


graph.Dijkstra("A", "E");



