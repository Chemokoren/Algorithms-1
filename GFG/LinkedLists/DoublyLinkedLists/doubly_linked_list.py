"""

Doubly Lined List : Introduction and Insertion

A Doubly Linked List (DLL) contains an extra pointer, typically called the previous pointer, 
together with the next pointer and data which are there in the singly linked list.

Node of a doubly linked list

class Node:
	def __init__(self, next=None, prev=None, data=None):
		
		# reference to next node in DLL
		self.next = next
		
		# reference to previous node in DLL
		self.prev = prev
		self.data = data


Advantages of DLL over the singly linked list:

    A DLL can be traversed in both forward and backward directions. 
    The delete operation in DLL is more efficient if a pointer to the node to be deleted is
    given. 
    We can quickly insert a new node before a given node. 
    In a singly linked list, to delete a node, a pointer to the previous node is needed.
    To get this previous node, sometimes the list is traversed. In DLL, we can get the 
    previous node using the previous pointer. 

Disadvantages of DLL over the singly linked list:

    Every node of DLL Requires extra space for a previous pointer. It is possible to 
    implement DLL with a single pointer though (See this and this). 
    All operations require an extra pointer previous to be maintained. For example, in 
    insertion, we need to modify previous pointers together with the next pointers. 
    For example in the following functions for insertions at different positions, we need 1
    or 2 extra steps to set the previous pointer.

Insertion in DLL:

A node can be added in four ways:

    At the front of the DLL 
    After a given node. 
    At the end of the DLL 
    Before a given node.


1) Add a node at the front:

The new node is always added before the head of the given Linked List. And newly added node 
becomes the new head of DLL. For example, if the given Linked List is 1->0->1->5 and we add
an item 5 at the front, then the Linked List becomes 5->1->0->1->5. Let us call the function 
that adds at the front of the list push(). The push() must receive a pointer to the head 
pointer because the push must change the head pointer to point to the new node


"""

# Node of a doubly linked list
class Node:
	def __init__(self, next=None, prev=None, data=None):
		
		# reference to next node in DLL
		self.next = next
		
		# reference to previous node in DLL
		self.prev = prev
		self.data = data


# Adding a node at the front of the list
def push(self, new_data):

	# 1 & 2: Allocate the Node & Put in the data
	new_node = Node(data=new_data)

	# 3. Make next of new node as head and previous as NULL
	new_node.next = self.head
	new_node.prev = None

	# 4. change prev of head node to new node
	if self.head is not None:
		self.head.prev = new_node

	# 5. move the head to point to the new node
	self.head = new_node

'''
2) Add a node after a given node:

We are given a pointer to a node as prev_node, and the new node is inserted after the given
node.
'''
# Given a node as prev_node, insert
# a new node after the given node


def insertAfter(self, prev_node, new_data):

	# 1. check if the given prev_node is NULL
	if prev_node is None:
		print("This node doesn't exist in DLL")
		return

	# 2. allocate node & 3. put in the data
	new_node = Node(data=new_data)

	# 4. Make next of new node as next of prev_node
	new_node.next = prev_node.next

	# 5. Make the next of prev_node as new_node
	prev_node.next = new_node

	# 6. Make prev_node as previous of new_node
	new_node.prev = prev_node

	# 7. Change previous of new_node's next node */
	if new_node.next is not None:
		new_node.next.prev = new_node

'''
3) Add a node at the end:

The new node is always added after the last node of the given Linked List. For example, 
if the given DLL is 5->1->0->1->5->2 and we add item 30 at the end, then the DLL becomes
 5->1->0->1->5->2->30. Since a Linked List is typically represented by its head of it, 
 we have to traverse the list till the end and then change the next of last node to the 
 new node.

'''
# Add a node at the end of the DLL
def append(self, new_data):

	# 1. allocate node 2. put in the data
	new_node = Node(data=new_data)
	last = self.head

	# 3. This new node is going to be the
	# last node, so make next of it as NULL
	new_node.next = None

	# 4. If the Linked List is empty, then
	# make the new node as head
	if self.head is None:
		new_node.prev = None
		self.head = new_node
		return

	# 5. Else traverse till the last node
	while (last.next is not None):
		last = last.next

	# 6. Change the next of last node
	last.next = new_node
	# 7. Make last node as previous of new node */
	new_node.prev = last




'''
4) Add a node before a given node: 

Follow the below steps to solve the problem:

Let the pointer to this given node be next_node and the data of the new node be added as 
new_data. 

    Check if the next_node is NULL or not. If it’s NULL, return from the function because 
    any new node can not be added before a NULL
    Allocate memory for the new node, let it be called new_node
    Set new_node->data = new_data
    Set the previous pointer of this new_node as the previous node of the next_node, 
    new_node->prev = next_node->prev
    Set the previous pointer of the next_node as the new_node, next_node->prev = new_node
    Set the next pointer of this new_node as the next_node, new_node->next = next_node;
    If the previous node of the new_node is not NULL, then set the next pointer of this 
    previous node as new_node, new_node->prev->next = new_node
    Else, if the prev of new_node is NULL, it will be the new head node. So, make 
    (*head_ref) = new_node.


'''
# A complete working Python3
# program to demonstrate all
# insertion methods

# A linked list node


class Node:

	# Constructor to create a new node
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

# Class to create a Doubly Linked List


class DoublyLinkedList:

	# Constructor for empty Doubly Linked List
	def __init__(self):
		self.head = None

	# Given a reference to the head of a list and an
	# integer, inserts a new node on the front of list
	def push(self, new_data):

		# 1. Allocates node
		# 2. Put the data in it
		new_node = Node(new_data)

		# 3. Make next of new node as head and
		# previous as None (already None)
		new_node.next = self.head

		# 4. change prev of head node to new_node
		if self.head is not None:
			self.head.prev = new_node

		# 5. move the head to point to the new node
		self.head = new_node

	# Given a node as prev_node, insert a new node after
	# the given node
	def insertAfter(self, prev_node, new_data):

		# 1. Check if the given prev_node is None
		if prev_node is None:
			print("the given previous node cannot be NULL")
			return

		# 2. allocate new node
		# 3. put in the data
		new_node = Node(new_data)

		# 4. Make net of new node as next of prev node
		new_node.next = prev_node.next

		# 5. Make prev_node as previous of new_node
		prev_node.next = new_node

		# 6. Make prev_node ass previous of new_node
		new_node.prev = prev_node

		# 7. Change previous of new_nodes's next node
		if new_node.next:
			new_node.next.prev = new_node

	# Given a reference to the head of DLL and integer,
	# appends a new node at the end
	def append(self, new_data):

		# 1. Allocates node
		# 2. Put in the data
		new_node = Node(new_data)

		# 3. This new node is going to be the last node,
		# so make next of it as None
		# (It already is initialized as None)

		# 4. If the Linked List is empty, then make the
		# new node as head
		if self.head is None:
			self.head = new_node
			return

		# 5. Else traverse till the last node
		last = self.head
		while last.next:
			last = last.next

		# 6. Change the next of last node
		last.next = new_node

		# 7. Make last node as previous of new node
		new_node.prev = last

		return

	# This function prints contents of linked list
	# starting from the given node
	def printList(self, node):

		print("\nTraversal in forward direction")
		while node:
			print(" {}".format(node.data))
			last = node
			node = node.next

		print("\nTraversal in reverse direction")
		while last:
			print(" {}".format(last.data))
			last = last.prev

# Driver code


# Start with empty list
if __name__ == "__main__":
    llist = DoublyLinkedList()

    # Insert 6. So the list becomes 6->None
    llist.append(6)

    # Insert 7 at the beginning.
    # So linked list becomes 7->6->None
    llist.push(7)

    # Insert 1 at the beginning.
    # So linked list becomes 1->7->6->None
    llist.push(1)

    # Insert 4 at the end.
    # So linked list becomes 1->7->6->4->None
    llist.append(4)

    # Insert 8, after 7.
    # So linked list becomes 1->7->8->6->4->None
    llist.insertAfter(llist.head.next, 8)

    print("Created DLL is: ")
    llist.printList(llist.head)
