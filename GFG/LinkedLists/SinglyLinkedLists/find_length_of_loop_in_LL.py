"""
Find length of loop in linked list
Write a function detectAndCountLoop() that checks whether a given Linked List contains
loop and if loop is present then returns count of nodes in loop. For example, the loop
is present in below linked list and length of loop is 4. if the loop is not present,
then the function should return 0.

1-->2-->3
	^	|
	|	V
	5<--4

Approach
--------
It is known that Floyd's Cycle detection algorithm terminates when fast and slow pointers
meet at a common point. It is also known that this common point is one of the loop nodes.
Store the address of this common point in a pointer variable say(ptr).
Then initialize a counter with 1 and start from the common point and keeps on visiting
the next node and increasing the counter till the common pointer is reached again.

At that point, the value of the counter will be equal to the length of the loop.

Algorithm
-find the common point in the loop using the Floyd's Cycle detection algorithm
-store the pointer in a temporary variable and keep a count = 0
-Traverse the LL until the same node is reached again and increase the count while moving
to next node.
-Print the count as length of loop

    Time complexity: O(n). 
    Only one traversal of the linked list is needed.
    Auxiliary Space: O(1). 
    As no extra space is required.

"""
from generic_singly_linked_list import Node, generic_singly_linked_list

class ChildNode(Node):
	def __init__(self, data):
		super().__init__(data)


# LL defining & loop length finding class
class LinkedList(generic_singly_linked_list):
	
	# Function to initialize the head of the LL
	def __init__(self):
		super().__init__()

	# insert new node at the end
	def AddNode(self,val):
		if self.head is None:
			self.head = ChildNode(val)
		else:
			curr = self.head
			while(curr.next):
				curr =curr.next
			curr.next =ChildNode(val)

	# Function to create a loop in the LL. This function creates a loop by connecting
	# the last node to the n^th node of the LL (counting first node as 1)
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

		# Using Floyd's Cycle-Finding: Slow-Fast Pointer Method
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

