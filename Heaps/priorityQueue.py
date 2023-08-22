# implementation program for Priority Queue using a Queue
class priorityQueue(object):
	def __init__(self):
		self.queue = []

	def __str__(self):
		return ' '.join([str(i) for i in self.queue])

	# function to check if the queue is empty
	def isQueueEmpty(self):
		return len(self.queue) == 0

	# function to appendElement an element in the queue
	def appendElement(self, data):
		self.queue.append(data)

	# function to pop an element based on Priority
	def deleteElement(self):
		try:
			max = 0
			for i in range(len(self.queue)):
				if self.queue[i] > self.queue[max]:
					max = i
			item = self.queue[max]
			del self.queue[max]
			return item
		except IndexError:
			print()
			exit()

if __name__ == '__main__':
    _queue = priorityQueue()
    _queue.appendElement(12)
    _queue.appendElement(1)
    _queue.appendElement(14)
    _queue.appendElement(7)
    print(_queue)
    print("delete elements from the queue \n")
    while not _queue.isQueueEmpty():
        print("delete element: ",_queue.deleteElement())



print("######################## last example ##############################")

# Code to implement the Max Heap
import sys


class MaxHeap:
	def __init__(self, maxsize):

		self.maxsize = maxsize
		self.size = 0
		self.Heap = [0] * (self.maxsize + 1)
		self.Heap[0] = sys.maxsize
		self.FRONT = 1

	'''
	Function to return the position of parent for the current node
	'''
	def parentPosition(self, pos):
		return pos // 2

	'''
	Function that returns the position of the left child for current node
	'''
	def returnLeftChild(self, pos):

		return 2 * pos

	'''
	Function that returns the position of the right child for the current node
	'''
	def returnRightChild(self, pos):
		return (2 * pos) + 1

	'''
	Function that returns true if the passed node is a leaf node
	'''
	def returnIsLeaf(self, pos):
		if pos >= (self.size // 2) and pos <= self.size:
			return True
		return False

	'''
	Function that swaps two nodes of the heap
	'''
	def swapNodes(self, fpos, spos):
		self.Heap[fpos], self.Heap[spos] = (self.Heap[spos],
											self.Heap[fpos])

	'''
	Function to heapify the current node 
	'''
	def maxHeapify(self, pos):

		# If the node is a non-leaf node and smaller than any of its child
		if not self.returnIsLeaf(pos):
			if (self.Heap[pos] < self.Heap[self.returnLeftChild(pos)] or
					self.Heap[pos] < self.Heap[self.returnRightChild(pos)]):

				# Swap with the left child and heapify the left child
				if (self.Heap[self.returnLeftChild(pos)] >
						self.Heap[self.returnRightChild(pos)]):
					self.swapNodes(pos, self.returnLeftChild(pos))
					self.maxHeapify(self.returnLeftChild(pos))

				# Swap with the right child and heapify the right child
				else:
					self.swapNodes(pos, self.returnRightChild(pos))
					self.maxHeapify(self.returnRightChild(pos))

	'''
	Function that inserts a node into the heap
	'''
	def insertElement(self, element):

		if self.size >= self.maxsize:
			return
		self.size += 1
		self.Heap[self.size] = element

		current = self.size

		while (self.Heap[current] >
			   self.Heap[self.parentPosition(current)]):
			self.swapNodes(current, self.parentPosition(current))
			current = self.parentPosition(current)

	'''
	Function that print's heap contents
	'''
	def printHeap(self):
		for i in range(1, (self.size // 2) + 1):
			print(" PARENT : " + str(self.Heap[i]) +
				  " LEFT CHILD : " + str(self.Heap[2 * i]) +
				  " RIGHT CHILD : " + str(self.Heap[2 * i + 1]))

	'''
	Function to remove and return the maximum element from the heap
	'''
	def extractMaximum(self):

		popped = self.Heap[self.FRONT]
		self.Heap[self.FRONT] = self.Heap[self.size]
		self.size -= 1
		self.maxHeapify(self.FRONT)

		return popped


# code to test the program MaxHeap
if __name__ == "__main__":
	maxHeap = MaxHeap(15)
	maxHeap.insertElement(22)
	maxHeap.insertElement(3)
	maxHeap.insertElement(5)
	maxHeap.insertElement(17)
	maxHeap.insertElement(19)
	maxHeap.insertElement(10)
	maxHeap.insertElement(6)
	maxHeap.insertElement(84)
	maxHeap.insertElement(9)

	maxHeap.printHeap()

	print("\nThe Maximum value in the heap is: " + str(maxHeap.extractMaximum()))