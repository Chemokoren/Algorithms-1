# program to demonstrate common binary heap operation

# import the heap functions from python library
from heapq import heappush, heappop, heapify

# heappop - pop and return the smallest element from heap
#heappush -push the value item onto the heap, maintaining heap invariant
# heapify - transform list into heap, in place, in linear time

# A class for Min Heap
class MinHeap:

    def __init__(self) -> None:
        self.heap =[]

    def parent(self, i):
        return (i-1) /2

    # Inserts a ew key 'k'
    def insertKey(self, k):
        heappush(self.heap, k)

    #Decrease value of key at index 'i' to new_val
    # it is assumed that new_val is smaller than heap[i]
    
    def decreaseKey(self, i, new_val):
        self.heap[i]  = new_val 
        while(i != 0 and self.heap[self.parent(i)] > self.heap[i]):
            # Swap heap[i] with heap[parent(i)]
            self.heap[i] , self.heap[self.parent(i)] = (
            self.heap[self.parent(i)], self.heap[i])

        
    # Method to remove minimum element from min heap
    def extractMin(self):
        return heappop(self.heap)

    # This function deletes key at index i. It first reduces value to minus infinite 
    # and then calls extractMin()
    def deleteKey(self, i):
        self.decreaseKey(i, float("-inf"))
        self.extractMin()

    # Get the minimum element from the heap
    def getMin(self):
        return self.heap[0]


# Driver program to text above fnction
heapObj =MinHeap()
heapObj.insertKey(3)
heapObj.insertKey(2)
heapObj.insertKey(1)
heapObj.insertKey(15)
heapObj.insertKey(5)
heapObj.insertKey(4)
heapObj.insertKey(45)

print(heapObj.extractMin())
print(heapObj.getMin())
heapObj.decreaseKey(2, 1)
print(heapObj.getMin())

'''
Output:
2 4 1

'''