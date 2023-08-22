"""
Priority Queue

- A data structure where each element has a priority.
- Elements with higher priorities are served before elements with lower priorities.
- A heap is an abstract concept that can be implemented using various ways including an array, or
using a priority queue

Naive Version
- use a list to store all elements
[priority: 3, priority: 1, priority: 2, priority:5, priority:4]
-iterate over the entire thing to find the highest priority element

Our Priority Queue
- write a Min Binary Heap - lower number means higher priority
- Each Node has a val and a priority. Use the priority to build the heap
- Enqueue method accepts a value and a priority, makes a new node, and puts it in the
right spot base off of its priority
-Dequeue method remoes root element, returns it, and rearranges heap using priority


"""

class MinHeapBinary:

    def __init__(self) -> None:
        self.values = []

    def enqueue(self, val, priority):
        new_node =Node(val, priority)
        self.values.append(new_node)
        self.bubbleUP()
    
    def __str__(self) -> str:
        for i in self.values:
            print(i.val,":", i.priority)


    def bubbleUP(self):
        index = len(self.values)-1
        parentIndex  = (index-1) // 2

        while self.values[parentIndex].priority > self.values[index].priority:
            self.values[parentIndex],self.values[index] =self.values[index],self.values[parentIndex]
            index =parentIndex

    def dequeue(self):
        if len(self.values) > 1:
            parent = self.values[0]
            end = self.values.pop()
            self.values[0] = end
            self.bubbleDown()
            return parent.val
        return self.values.pop()

    def bubbleDown(self):
        print("sifiki apa")
        parentIdx = 0
        leftChildIdx = (parentIdx * 2) + 1
        rightChildIdx = (parentIdx * 2) + 2

        length = len(self.values)

        while rightChildIdx < length:

            leftChild  = self.values[leftChildIdx]
            rightChild = self.values[rightChildIdx]
            element =self.values[parentIdx]

            
            greaterChild=None
            greaterChildPriority =min(leftChild.priority, rightChild.priority)
            if greaterChildPriority==leftChild.priority:
                greaterChild =leftChild
            else:
                greaterChild = rightChild
            

            
            greaterChildIdx =self.values.index(greaterChild)
            print("compare:", greaterChild.val, self.values[greaterChildIdx].val)
            

            if greaterChildPriority < element.priority:
                self.values[greaterChildIdx],element= element,self.values[greaterChildIdx]
                # greaterChild,element= element,greaterChild
                parentIdx = greaterChildIdx

class Node():

    def __init__(self,val, priority) -> None:
        self.val =val
        self.priority=priority

sol = MinHeapBinary()
sol.enqueue("exploded head",1)
sol.enqueue("common flu",2)
sol.enqueue("running nose",5)
sol.enqueue("drunk",4)
sol.enqueue("accident",3)
sol.__str__()
print("done: ",sol.dequeue())
# sol.__str__()