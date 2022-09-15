"""
Iterative solution
------------------
- Time complexity: O(n) 

Where n is the size of the linked list, and we have to traverse the list only once.

- Auxiliary Space: O(1) As constant extra space is used.

Recursive solution
------------------

int getCount(head)

1) If head is Null, return 0
2) Else return 1+ getCount(head->next)

- Time Complexity: O(n)

As we are traversing the linked list only once.

- Auxiliary Space: O(n)

Extra space is used in recursion call stack.

"""

# Program to find length of a LL recursively.

class Node:
	def __init__(self, data):
		self.data =data # assign data
		self.next =None # initialize next as null


# Linked List class contains a Node object
class LinkedList:

	def __init__(self):
		self.head =None


	# Inserts a new node at the beginnning of a linked list
	def push(self, new_data):
		new_node =Node(new_data)
		new_node.next =self.head
		self.head =new_node

	# count number of nodes in LL iteratively
	def countIterative(self):
		count =0
		temp = self.head
		while(temp):
			count =count + 1
			temp =temp.next
		return count

	# function counts number of nodes in LL recursively given 'node' as starting node.
	def getCountRec(self, node):
		if(not node): # Base case
			return 0
		else:
			return 1 + self.getCountRec(node.next)


	# A wrapper over getCountRec()
	def getCount(self):
		return self.getCountRec(self.head)

# Code execution starts here
if __name__=='__main__':
	llist =LinkedList()
	llist.push(1)
	llist.push(3)
	llist.push(1)
	llist.push(2)
	llist.push(1)
	print('Count of nodes is: ', llist.getCount())
	print("Iterative Expected:5, Actual:",llist.countIterative())


"""
The above recursive approach can be modified to make it a tail recursive function and thus
our auxiliary space will become O(1):

Time Complexity: O(n) i.e. we are traversing the list only once.

Auxiliary Space: O(1) i.e. since we are using tail recursive function, no extra space is
used in function call stack .
"""

# using tail recursion to find length of a linked list
class Node:
	def __init__(self, data):
		self.data =data 
		self.next = None

# Linked List class contains a Node object
class LinkedList:

	def __init__(self) -> None:
		self.head = None

	def push(self, new_data):
		new_node = Node(new_data)

		# make next of new node as head
		new_node.next = self.head

		# move the head ponter to the new node
		self.head = new_node

	def getCountRec(self, node, count=0):
		if(not node): # base case
			return count
		else:
			return self.getCountRec(node.next, count +1)

	# a wrapper over getCountRec()
	def getCount(self):
		return self.getCountRec(self.head)

if __name__=='__main__':
    llist = LinkedList()
    llist.push(1)
    llist.push(3)
    llist.push(1)
    llist.push(2)
    llist.push(1)
    print ('Count of nodes is :',llist.getCount())

