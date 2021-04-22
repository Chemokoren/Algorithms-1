"""
program to demonstrate deletion in SLL
"""

class Node:
	# constructor to initialize the node object
	def __init__(self, data):
		self.data =data
		self.next =None

class LinkedList:
	# initialize head
	def __init__(self):
		self.head = None

	# Function to insert a new node at the beginning
	def push(self, new_data):
		new_node =Node(new_data)
		new_node.next =self.head
		self.head =new_node

	#Given a reference to the head of a SLL and a key,
	# delete the first occurrence of key in SLL
	def deleteNode(self, key):

		temp =self.head

		# if head node itself holds the key to be deleted
		if(temp is not None):
			if(temp.data == key):
				self.head =temp.next
				temp =None
				return

		# search for the key to be deleted, & keep track of the 
		# prev node since we need to change 'prev.next'

		while(temp is not None):
			if temp.data ==key:
				break
			prev =temp
			temp = temp.next

		# if key was not present in LL
		if (temp == None):
			return

		# unlink the node from LL
		prev.next =temp.next

		temp =None

	# function to print the LL
	def printList(self):
		temp = self.head
		while(temp):
			print(" %d" % (temp.data)),
			temp =temp.next

# Driver program
llist = LinkedList()
llist.push(7)
llist.push(1)
llist.push(3)
llist.push(2)
 
print ("Created Linked List: ")
llist.printList()
llist.deleteNode(1)
print ("\nLinked List after Deletion of 1:")
llist.printList()

