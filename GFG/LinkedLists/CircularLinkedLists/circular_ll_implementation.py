"""
program for insertion and deletion in circular queue

Front:Get the front item from queue.
Rear: Get the last item from queue.
enqueue(value): This function is used to insert an element into the circular queue. 
In a circular queue, the new element is always inserted at Rear position.

Steps:

Create a new node dynamically and insert value into it.
Check if front==NULL, if it is true then front = rear = (newly created node)
If it is false then rear=(newly created node) and rear node always contains the address
of the front node.
dequeue(): This function is used to delete an element from the circular queue. 
In a queue, the element is always deleted from front position.

Steps:
1)Check whether queue is empty or not means front == NULL.
2)If it is empty then display Queue is empty.If queue is not empty then step 3
3)Check if (front==rear) if it is true then set front = rear = NULL else move the front 
forward in queue, update address of front in rear node and return the element.

Time Complexity: Time complexity of enQueue(), deQueue() operation is O(1) as there is 
no loop in any of the operation. 

In case of linked list implementation, a queue can be easily implemented without 
being circular. However, in the case of array implementation, we need a circular queue 
to save space. 

"""

# Node Structure
class Node:
    def __init__(self):
        self.data =None
        self.link =None

class Queue:
    def __init__(self):
        front   =None
        rear    =None

# Function to create Circular Queue
def enqueue(q, value):
    temp =Node()
    temp.data =value

    if(q.front == None):
        q.front = temp
    else:
        q.rear.link =temp

    q.rear =temp
    q.rear.link =q.front

# Function to delete element from circular queue
def dequeue(q):
    if(q.front == None):
        print("Queue is empty")
        return -999999999999

    # if this is the last node to be deleted
    value =None # Value to be dequeued
    if(q.front == q.rear):
        value = q.front.data
        q.front = None
        q.rear = None
    else: # There are more than one nodes
        temp =q.front
        value =temp.data
        q.front =q.front.link
        q.rear.link =q.front
    return value

# Function displaying the elements of circular queue
def display_queue(q):
    temp = q.front
    print("Elements in Circular Queue are:", end =" ")
    while(temp.link != q.front):
        print(temp.data, end=" ")
        temp =temp.link
    print(temp.data)

if __name__=='__main__':
    # Create a queue and initialize front and rear
    q =Queue()
    q.front = q.rear = None

    # Inserting elements in Circular Queue
    enqueue(q, 14)
    enqueue(q, 22)
    enqueue(q, 6)

    # Display elements present in Circular Queue
    display_queue(q)

    # Deleting elements from Circular Queue
    print("Deleted value =", dequeue(q))
    print("Deleted value =", dequeue(q))

    # Remaining elements in Circular Queue
    display_queue(q)

    enqueue(q, 9)
    enqueue(q, 20)
    display_queue(q)



