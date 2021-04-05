import math
class minHeap:
    def __init__(self):
        self.heap = []
        self.elements = 0

    def insert(self,val):
        if (self.elements >= len(self.heap)):
            self.elements = self.elements + 1
            self.heap.append(val)
            self.__percolateUp(len(self.heap) - 1)
        else:
            self.heap[self.elements] = val
            self.elements = self.elements + 1
            self.__percolateUp(self.elements - 1)


    def getMin(self):
        if (len(self.heap) != 0):
            return self.heap[0]
        return null


    def removeMin(self):
        min = self.heap[0]
        if (self.elements > 1):
            self.heap[0] = self.heap[self.elements - 1]
            self.elements = self.elements - 1
            self.__minHeapify(0)
            return min
        elif (self.elements == 1):
            self.elements = self.elements - 1
            return min
        else:
            return null


    def __percolateUp(self,index):
        parent = math.floor((index - 1) / 2)
        if (index <= 0):
            return
        elif (self.heap[parent] > self.heap[index]):
            tmp = self.heap[parent]
            self.heap[parent] = self.heap[index]
            self.heap[index] = tmp
            self.__percolateUp(parent)



    def __minHeapify(self,index):
        left = (index * 2) + 1
        right = (index * 2) + 2
        smallest = index
        if ((self.elements > left) and (self.heap[smallest] > self.heap[left])):
            smallest = left

        if ((self.elements > right) and (self.heap[smallest] > self.heap[right])):
            smallest = right
        if (smallest != index):
            tmp = self.heap[smallest]
            self.heap[smallest] = self.heap[index]
            self.heap[index] = tmp
            self.__minHeapify(smallest)



    def buildHeap(self,arr):
        self.heap = arr
        self.elements = len(self.heap)
        for i in range(0,len(self.heap) - 1):
            self.__minHeapify(i)


if __name__=='__main__':
    heap = minHeap()
    heap.insert(12)
    heap.insert(10)
    heap.insert(-10)
    heap.insert(100)

    print(heap.getMin()) # you should get - 10
    #
    # newheap = minHeap()
    # arr = [12, 6, 8, 3, 16, 4, 27]
    #
    # newheap.buildHeap(arr) # builds self new heap with elements from the array
    # print(newheap.getMin()) # self logs 3
    # #
    # newheap.removeMin()
    # #
    # print(newheap.getMin())

    print('The minHeap is ')
    _newHeap = minHeap()
    _newHeap.insert(15)
    _newHeap.insert(5)
    _newHeap.insert(3)
    _newHeap.insert(17)
    _newHeap.insert(10)
    _newHeap.insert(84)
    _newHeap.insert(19)
    _newHeap.insert(6)
    _newHeap.insert(22)
    _newHeap.insert(9)

    print(_newHeap.getMin())
    # print("The Min val is " + str(minHeap.remove()))



print("##################### approach 2 ###############################")

# implementation program for Min Heap

import sys


class MinHeap:

    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0] * (self.maxsize + 1)
        self.Heap[0] = -1 * sys.maxsize
        self.FRONT = 1

    # Function to return the position of
    # parent for the node currently
    # at pos
    def parent(self, pos):
        return pos // 2

    # Function to return the position of
    # the left child for the node currently
    # at pos
    def leftChild(self, pos):
        return 2 * pos

    # Function to return the position of
    # the right child for the node currently
    # at pos
    def rightChild(self, pos):
        return (2 * pos) + 1

    # Function that returns true if the passed
    # node is a leaf node
    def isLeaf(self, pos):
        if pos >= (self.size // 2) and pos <= self.size:
            return True
        return False

    # Function to swap two nodes of the heap
    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]

    # Function to heapify the node at pos
    def minHeapify(self, pos):

        # If the node is a non-leaf node and greater
        # than any of its child
        if not self.isLeaf(pos):
            if (self.Heap[pos] > self.Heap[self.leftChild(pos)] or
                    self.Heap[pos] > self.Heap[self.rightChild(pos)]):

                # Swap with the left child and heapify
                # the left child
                if self.Heap[self.leftChild(pos)] < self.Heap[self.rightChild(pos)]:
                    self.swap(pos, self.leftChild(pos))
                    self.minHeapify(self.leftChild(pos))

                # Swap with the right child and heapify
                # the right child
                else:
                    self.swap(pos, self.rightChild(pos))
                    self.minHeapify(self.rightChild(pos))

    # Function to insert a node into the heap
    def insert(self, element):
        if self.size >= self.maxsize:
            return
        self.size += 1
        self.Heap[self.size] = element

        current = self.size

        while self.Heap[current] < self.Heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

    # Function to print the contents of the heap
    def Print(self):
        for i in range(1, (self.size // 2) + 1):
            print(" PARENT : " + str(self.Heap[i]) + " LEFT CHILD : " +
                  str(self.Heap[2 * i]) + " RIGHT CHILD : " +
                  str(self.Heap[2 * i + 1]))

    # Function to build the min heap using
    # the minHeapify function
    def minHeap(self):

        for pos in range(self.size // 2, 0, -1):
            self.minHeapify(pos)

    # Function to remove and return the minimum
    # element from the heap
    def remove(self):

        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size -= 1
        self.minHeapify(self.FRONT)
        return popped


# Driver Code
if __name__ == "__main__":
    print('The minHeap is ')
    minHeap = MinHeap(15)
    minHeap.insert(5)
    minHeap.insert(3)
    minHeap.insert(17)
    minHeap.insert(10)
    minHeap.insert(84)
    minHeap.insert(19)
    minHeap.insert(6)
    minHeap.insert(22)
    minHeap.insert(9)
    minHeap.minHeap()

    minHeap.Print()
    print("The Min val is " + str(minHeap.remove()))
