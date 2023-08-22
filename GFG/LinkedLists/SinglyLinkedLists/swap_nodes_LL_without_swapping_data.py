"""

Swap nodes in a linked list without swapping data

Given a linked list and two keys in it, swap nodes for two given keys. Nodes should be
swapped by changing links. Swapping data of nodes may be expensive in many situations
when data contains many fields. It may be assumed that all keys in the linked list are 
distinct.

Examples: 

    Input: 10->15->12->13->20->14,  x = 12, y = 20
    Output: 10->15->20->13->12->14

    Input: 10->15->12->13->20->14,  x = 10, y = 20
    Output: 20->15->12->13->10->14

    Input: 10->15->12->13->20->14,  x = 12, y = 13
    Output: 10->15->13->12->20->14

The problem has the following cases to be handled:

    x and y may or may not be adjacent.
    Either x or y may be a head node.
    Either x or y may be the last node.
    x and / or y may not be present in the linked list.


"""
from generic_singly_linked_list import generic_singly_linked_list,Node


class LinkedList(generic_singly_linked_list):
	
	def __init__(self) -> None:
		super().__init__()
		

    # Function to swap Nodes x and y in LL by changing links
	def swapNodes(self,x,y):
		
		# nothing to do if x and y are same
		if x == y:
			return
        
		# search for x (keep track of prevX and CurrX)
		prevX =None
		currX =self.head
		while currX != None and currX.data != x:
			prevX =currX
			currX =currX.next
	
		# search for y (keep track of prevY and currY)
		prevY =None
		currY =self.head
		while currY !=None and currY.data !=y:
			prevY =currY
			currY = currY.next
			
		# If either x or y is not present, nothing to do
		if currX == None or currY == None:
			return

        # If x is not head of LL
		if prevX !=None:
			prevX.next = currY
		else:
			# makey y the new head
			self.head =currY
        
        # if y is not head of LL
		if prevY != None:
			prevY.next =currX
		else:
			# make x the new head
			self.head =currX
        # swap next pointers
		temp =currX.next
		currX.next =currY.next
		currY.next =temp

 
llist = LinkedList()
 
# The constructed linked list is: # 1->2->3->4->5->6->7
llist.push(7)
llist.push(6)
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)
print ("Linked list before calling swapNodes() ")
llist.print_ll()
llist.swapNodes(4, 3)
print ("\nLinked list after calling swapNodes() ")
llist.print_ll()

"""
optimizations: optimize the above program to search x and y in single traversal
Two loops keep the program simple
"""

# class ChildNode(Node):

# 	def __init__(self, data):
# 		super().__init__(data)
	

# 	# constructor
# 	def __init__(self, val=None, next1=None):
# 		self.data = val
# 		self.next = next1

# 	# print list from this to last till None
# 	def printList(self):

# 		node = self

# 		while (node != None):
# 			print(node.data, end=" ")
# 			node = node.next
# 		print(" ")

# #Function to add a node at the beginning of List
# def push(head_ref, new_data):

# 	# allocate node
# 	(head_ref) = Node(new_data, head_ref)
# 	return head_ref

'''
Time complexity: O(N)
Auxiliary Space: O(1)
'''
class linked_list_two(generic_singly_linked_list):

	def __init__(self) -> None:
		super().__init__()

	def swapNodes(self, head_ref, x, y):
		head = head_ref

		# Nothing to do if x and y are same
		if (x == y):
			return None

		a = None
		b = None

		# search for x and y in the linked list
		# and store their pointer in a and b
		while (head_ref.next != None):

			if ((head_ref.next).data == x):
				a = head_ref

			elif ((head_ref.next).data == y):
				b = head_ref

			head_ref = ((head_ref).next)

		# if we have found both a and b
		# in the linked list swap current
		# pointer and next pointer of these
		if (a != None and b != None):
			temp = a.next
			a.next = b.next
			b.next = temp
			temp = a.next.next
			a.next.next = b.next.next
			b.next.next = temp

		return head

ll = linked_list_two()


# The constructed linked list is: 1.2.3.4.5.6.7
ll.push(7)
ll.push(6)
ll.push(5)
ll.push(4)
ll.push(3)
ll.push(2)
ll.push(1)

print("Linked list before calling swapNodes() ")
ll.print_ll()

ll.swapNodes(ll.head, 6, 1)

print("Linked list after calling swapNodes() ")
ll.print_ll()

 

    
