"""
Write a Min Binary Heap - Lower number means higher priority

"""


class PriorityQueue:
    def __init__(self) -> None:
        self.values =[]

    def __str__(self) -> str:
        for i in self.values:
            print(i.val, i.priority)


    '''
    Enqueue method accepts a value and priority, makes a new node,
    and puts it in the right spot based off of its priority
    '''
    def enqueue(self, val, priority):
        n = Node(val, priority)
        self.values.append(n)
        self.bubbleUP()

    def bubbleUP(self):
        elementIdx = len(self.values)-1

        while elementIdx > 0:
            parentIdx = (elementIdx -1)// 2

            element = self.values[elementIdx]
            parent = self.values[parentIdx]

            if(element.priority > parent.priority):
                break

            if(element.priority < parent.priority):
                self.values[elementIdx], self.values[parentIdx] = self.values[parentIdx], self.values[elementIdx]
                elementIdx = parentIdx
            


    '''
    Dequeue method removes root element, returns it, and 
    rearranges heap using priority.

    '''
    def dequeue(self):
        max = self.values[0]
        end = self.values.pop()
        self.values[0] =end
        self.trickleDown()
        return max.val
    
    def trickleDown(self):
        parentIdx = 0
        leftChildIdx  = (2 * parentIdx) + 1
        rightChildIdx = (2 * parentIdx) + 2

        length = len(self.values)
        swapIdx = None


        parent =self.values[parentIdx]

        while(True):
            if(leftChildIdx < length):
                leftChild = self.values[leftChildIdx]
                if(self.values[leftChildIdx].priority < parent.priority):
                    swapIdx = leftChildIdx

            if(rightChildIdx < length):
                rightChild =self.values[rightChildIdx]
                if(
                    (rightChild.priority < leftChild.priority and swapIdx != None) or
                    (rightChild.priority < parent.priority and swapIdx == None)
                ):
                    swapIdx = rightChildIdx

            if(swapIdx == None):
                break
            self.values[parentIdx], self.values[swapIdx] = self.values[swapIdx] , self.values[parentIdx]
            parentIdx = swapIdx

    
        


'''
Each Node has a val and a priority. Use the priority to build
the heap
'''
class Node:
    def __init__(self, val, priority) -> None:
        self.val = val
        self.priority = priority


er = PriorityQueue()
er.enqueue("Common cold", 5)
er.enqueue("gunshot wound", 1)
er.enqueue("high fever", 4)
er.enqueue("broken arm", 2)
er.enqueue("glass in foot", 3)
print("Starting: \n")
print(er.__str__())
print("removed: ", er.dequeue())
print(er.__str__())
