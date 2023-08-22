"""
function checks whether a given LL contains a loop and if loop is present
then removes the loop and returns true.
If the list does not contain a loop then it returns false.

"""

class Node:
	def __init__(self,data):
		self.data =data
		self.next = None

class LinkedList:

	def __init__(self):
		self.head =None

	def detectAndRemoveLoop(self):
		slow_p =fast_p =self.head
		while(slow_p and fast_p and fast_p.next):
			slow_p =slow_p.next
			fast_p =fast_p.next.next

			# if slow_p and fast_p meet at some point then there is a loop
			if slow_p == fast_p:
				self.removeLoop(slow_p)

				# return 1 to indicate that loop if found
				return 1

		# return 0 to indicate that there is no loop
		return 0


	# Function to remove loop
	# loop node-> pointer to one of the loop nodes
	# head --> pointer to the start node of the LL
	def removeLoop2(self, loop_node):
		ptr1 =loop_node
		ptr2 =loop_node

		# count the number of nodes in loop
		k =1
		while(ptr1.next !=ptr2):
			ptr1 =ptr1.next
			k +=1
		# Fix one pointer to head
		ptr1 =self.head

		# And the other pointer to k nodes after head
		ptr2 =self.head
		for i in range(k):
			ptr2 =ptr2.next

		# move both pointers at the same place
		# they will meet at loop starting node
		while(ptr2 != ptr1):
			ptr1 = ptr1.next
			ptr2 = ptr2.next

		# Get pointer to the last node
		while(ptr2.next != ptr1):
			ptr2 =ptr2.next

		# so the next node of the loop ending node to fix the loop
		ptr2.next =None

	def removeLoop(self, loop_node):
		# set a pointer to the beginning of the LL and move it one by one to find
		# the first node which is part of the LL
		ptr1 =self.head
		while(1):
			# Now start a pointer from loop_node and check if it ever reaches ptr2
			ptr2 =loop_node
			while(ptr2.next != loop_node and ptr2.next !=ptr1):
				ptr2 =ptr2.next

			# If ptr2 reached ptr1 then there is a loop.#
			# so break the loop
			if ptr2.next == ptr1:
				break

			ptr1 =ptr1.next

		# After the end of loop ptr2 is the lsat node of
		# the loop . so make next of ptr2 as NULL
		ptr2.next =None

	# Function to remove loop
	# loop_node --> pointer to one of the loop nodes
	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

		# Utility function to prit the linked LinkedList
	def printList(self):
		temp = self.head
		while(temp):
			print(temp.data),
			temp = temp.next

# Driver code
llist = LinkedList()
llist.push(10)
llist.push(4)
llist.push(15)
llist.push(20)
llist.push(50)

# Create a loop for testing
llist.head.next.next.next.next.next = llist.head.next.next

llist.detectAndRemoveLoop()

print ("Linked List after removing loop")
llist.printList()
 

"""
Method 2: dependent on Floyd's Cycle detection algorithm.
- detect Loop using Floyd's Cycle detection algorithm and get the pointer to a loop node
- count the number of nodes in loop. Let the count be k.
- Fix one pointer to the head and another to a kth node from the head.
- Move both pointers at the same pace, they will meet at loop starting node.
- Get a pointer to the last node of the loop and make next of it as NULL
"""


