"""
OBJECTIVES

- understand the importance of Dijkstra's 
- Implement a Weighted Graph
- Walk through the steps of Dijkstra's 
- Implement Dijkstra's using a naive priority queue
- Implement Dijkstra's using a binary heap priority queue

Prerequisites:
-Graphs
-Priority Queues

What is it?
-----------
- Finds the shortest path between two vertices on a graph
- It answers the question, "What's the fastest way to get from point A to point B?"

Who was Dijkstra
- Edsger Dijkstra was a Dutch programmer, physicist, essayist, and all around smarty-pants
- He helped to advance the field of computer science from an "art" to an academic discipline.
- Many of his discoveries and algorithms are still commonly used to this day.

QUOTE
'''
What is the shortest way to travel from Rotterdam to Groningen, in general: from given city to given city.
It is the algorithm for the shortst path, which I designed in about 20 minutes. One morning I was shopping 
in Amsterdam with my young fiancee and tired, we sat down on the cafe' terrace to drink a cup of coffee
 and i was just thinking about whether I could do this, and I then designed the algorithm for the shortest
 path. As I said, it was a twenty-minute invention. Eventually that algorithm became, to my great amazement
 , one of the cornerstones of my fame.

 -Edsger Dijkstra

'''

Why is it useful?
----------------
- Biology - used to model the spread of viruses among humans
- Airline tickets - finding cheapest route to your destination
- Network routing - finds open shortest path for data
- GPS - finding fastest route

"""

# class WeightedGraph:

#     def __init__(self):
#         self.adjacencyList ={}

#     def addVertex(self,vertex):
#         if(not self.adjacencyList[vertex]):
#             pass
#         else:
#             self.adjacencyList[vertex] =[]

#     def addEdge(self,vertex1, vertex2, weight):
#         self.adjacencyList[vertex1].push({node:vertex2, weight:weight})
#         self.adjacencyList[vertex2].push({node:vertex1, weight:weight})

# graph = WeightedGraph()
# graph.addVertex("A")
# graph.addVertex("B")
# graph.addVertex("C")

# graph.addEdge("A","B", 9)
# graph.addEdge("A", "C", 5)
# graph.addEdge("B", "C", 7)
# print("output:", graph.adjacencyList)

"""

THE APPROACH
- Every time we look to visit a new node, we pick the node with the smallest known distance to visit first.
- Once we've moved to the node we're going to visit, we look at each of it's neighbors.
- For each neighboring node, we calculate the distance by summing  the total edges that lead to the node 
we're checking from the starting node.
- If the new total distance to a node is less than the previous total, we store the new shorter distance for
that node.

Initialize distances for different vertices from A

- The distance from a vertex to itself is 0

Vertex      Shortest Dist from A
A           0
B           Infinity 4
C           Infinity 2
D           Infinity 4
E           Infinity 7 6
F           Infinity 6  5

Pick node with smallest distance (A)

visited
[A, C, B, D]

previous
{
    A:None
    B:A 
    C:A
    D:C
    E:B F
    F:C D
}
"""

# A simple PQ

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

q = PriorityQueue()
q.enqueue("B", 3)
q.enqueue("C", 5)
q.enqueue("D", 2)
q.enqueue("Q", 20)
print(q.values)

"""
Dijkstra's Pseudocode
- This function should accept a starting and ending vertex
- Create an object(we'll call it distances) and set each key to be every vertex in the adjacency list with
a value of infinity, except for the starting vertex which should have a value of 0
- After setting a value in the distances object, add each vertex with a priority of Infinity to the priority
queue, except the starting vertex, which should have a priority of 0 because that's where we begin.
-Create another object called previous and set each key to be every vertex in the adjacency list with a 
value of null
-Start looping as long as there is anything in the priority queue
    1) dequeue a vertex from the priority queue
    2) If that vertex is the same as the ending vertex -we are done!
    3) Otherwise loop through each value in the adjacency list at that vertex
        - Calculate the distance to that vertex from the starting vertex
        - If the sistance is less than what is currently stored in our distances object
            a) update the distances object with new smaller distance
            b) update the previous object to contain that vertex
            c) Enqueue the vertex with the total distance from start node
            

"""