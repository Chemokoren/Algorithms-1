"""
Objectives
-Define what a queue is
-Understand use cases for a queue
-Implement operations on a queue datastructure

FIFO datastructure - First In First Out

Use cases
- Background tasks
- Uploading resources
- Printing / Task processing
- Waiting to join an online game -there is some sort of queue to monitor who has been
waiting the longest.

Implementation
-with an array
-our own

Enqueue Pseudocode
- This function accepts some value
- Create a new node using that value passed to the function
- If there are no nodes in the queue, set this node to be the first and last property
of the queue
- Otherwise, set the next property on the current last to be that node, and then set
the last property of the queue to be that node
-increment the size of the queue by 1

Dequeue Pseudocode
- If there is no first property, just return null
- Store the first property in a variable
- See if the first is the same as the last(check if there is only 1 node). If so, set the first and last to be 
null
- if there is more than 1 node, set the first property to be the next property of first
- Decrement the size by 1
- Return the value of the node dequed

Big O of Queues

- Insertion - O(1)
- Removal - O(1)
- Searching - O(N)
- Access - O(N)

RECAP
- Queuues are a FIFO data structure, all elements are first in first out.
- Queues are useful for processing tasks and are foundational for more complex data structures
- Insertion and Removal can be done in O(1)


"""

class Queue:

    def __init__(self) -> None:
        self.first = None
        self.last = None
        self.size = 0

    def enqueueInitial(self,value):
        n = Node(value)
        if(self.size ==0):
            self.first = n
            self.last =n
        current_node = self.first
        idx = 0
        while idx < self.size -1:
            current_node = current_node.next
            idx +=1
        current_node.next =n
        self.last=n
        self.size +=1
        return self.size

    def enqueue(self,value):
        n = Node(value)
        if(self.size ==0):
            self.first = n
            self.last =n
        else:
            self.last.next =n
            self.last=n
        self.size +=1
        return self.size

    def dequeue(self):
        if(self.size == 0):
            return None
        current = self.first
        if(self.first == self.last):
            self.first =None
            self.last = None
        self.first =current.next
        self.size -=1

        return current.value

    def print(self):
        idx = 0
        start_node =self.first
        while idx < self.size:
            print(start_node.value,end="-->")
            start_node = start_node.next
            idx +=1

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

q = Queue()
print("Enqueue: ", q.enqueue(10))
print("Enqueue: ", q.enqueue(36))
print("Enqueue: ", q.enqueue(78))
print("Enqueue: ", q.enqueue(40))
# print(q.print())
print("Dequeue: ",q.dequeue())
# print(q.print())
print("Dequeue: ",q.dequeue())
print("Dequeue: ",q.dequeue())
print("Dequeue: ",q.dequeue())
print("Dequeue: ",q.dequeue())
# print(q.print())

