"""
Recursive solution

int getCount(head)

1) If head is Null, return 0
2) Else return 1+ getCount(head->next)

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
	print('Iterative count ', llist.countIterative())
