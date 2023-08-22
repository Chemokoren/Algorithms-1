"""
The main point here is not to access the next of the current pointer if the current 
pointer is deleted

Garbage collection happens automatically in python thus deleting a linked list is easy
- change head to null

Time Complexity: O(n) 
Auxiliary Space: O(1)
"""

# program for deleting all the nodes of SLL

class Node:
	# Function to initialize the node object
	def __init__(self,data):
		self.data =data # assign data
		self.next =None # Initialize next as null

# Constructor to initialize the node object
class LinkedList:

	# Function to initialize head
	def __init__(self):
		self.head =None

	def deleteList(self):

		# initalize the current node
		current =self.head
		while(current):
			prev =current.next # move next node

			# delete the current node
			del current.data

			# set current equals  prev node
			current = prev

		# Garbage collection happens in python, thus only
		# self.head = None #would also delete the LL

	# push function to add in from of llist
	def push(self, new_data):
		# Allocate the Node & put in the data
		new_node =Node(new_data)

		# Make next of new Node as head
		new_node.next =self.head


		# Move the head to point to new Node
		self.head =new_node

	def printList(self):
		if self.head == None:
			print("No item to print!")
			return
		temp =self.head
		while(temp.next):
			print(temp.data,end=",")
			temp =temp.next


# Use push() to construct: 1->12->1->4->1

if __name__ == '__main__':
	llist =LinkedList()
	llist.push(1)
	llist.push(4)
	llist.push(1)
	llist.push(12)
	llist.push(1)

	print("Deleting Linked List\n")
	llist.printList()
	llist.deleteList()
	print("Linked List deleted\n")
	llist.printList()



