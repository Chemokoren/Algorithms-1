"""
Algorithm
-find the common point in the loop using the Floyd's Cycle detecction algorithm
-store the pointer in a temporary variable and keep a count = 0
-Traverse the LL until the same node is reached again and increase the count while moving to next node.
-Print the count as length of loop

"""

# programm to find no. of nodes in a loop in LL if present

class Node:
	def __init__(self,val):
		self.val =val
		self.next =None

# LL defining & loop length finding class
class LinkedList:
	# Function to initialize the head of the LL
	def __init__(self):
		self.head = None

	# insert new node at the end
	def AddNode(self,val):
		if self.head is None:
			self.head = Node(val)
		else:
			curr = self.head
			while(curr.next):
				curr =curr.next
			curr.next =Node(val)

	# Function to create a loop in the LL. This function creates a loop by connecting
	# the last node to the n^th node of the LL
	# (counting first node as 1)

	def CreateLoop(self, n):
		# LoopNode is the connecting node to the last node of LL
		LoopNode =self.head
		for _ in range(1, n):
			LoopNode =LoopNode.next

		# end is the last node of the LL
		end =self.head
		while(end.next):
			end =end.next


		# creating the loop
		end.next =LoopNode


	# Function to detect the loop and return the length of the loop 
	# if the returned value is zero, that means that either
	# the LL is empty or the LL does not have a loop

	def detectLoop(self):
		# if LL is empty then there is no loop, so return 0
		if self.head is None:
			return 0

		# Using Floyd's Cycle-Finding
		# Algorithm / Slow-Fast Pointer Method
		slow =self.head
		fast =self.head

		flag = 0 # to show that both slow and fast are at the start of LL

		while (slow and slow.next and fast and fast.next and fast.next.next):
			if slow ==fast and flag !=0:
				# means loop is confirmed in LL - slow and fast are both at the same node
				# which is part of the loop
				count =1
				slow =slow.next
				while(slow !=fast):
					slow =slow.next
					count += 1
				return count
			slow = slow.next
			fast  =fast.next.next
			flag = 1
		return 0 # No loop


# Setting up the code: Making a Linked List and adding the nodes
myLL = LinkedList()

myLL.AddNode(1)
myLL.AddNode(2)
myLL.AddNode(3)
myLL.AddNode(4)
myLL.AddNode(5)
  
# Creating a loop in the LL: Loop is created by connecting the 
# last node of LL to n^th node 1<= n <= len(LinkedList)
myLL.CreateLoop(2)
  
# Checking for Loop in the LL and printing the length of the loop
loopLength = myLL.detectLoop()
if myLL.head is None:
    print("Linked list is empty")
else:
    print(str(loopLength))

