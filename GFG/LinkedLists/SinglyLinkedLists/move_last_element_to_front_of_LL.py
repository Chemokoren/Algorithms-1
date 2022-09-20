"""
program to move last element to front of a given LL

e.g. 
Input: 1->2->3->4->5
Output: 5->1->2->3->4

Input: 3->8->1->5->7->12
Output: 12->3->8->1->5->7  

Time Complexity: O(N), As we need to traverse the list once.
Auxiliary Space: O(1), As constant extra space is used.

"""
from generic_singly_linked_list import generic_singly_linked_list
class LinkedList(generic_singly_linked_list):
	
	def __init__(self) -> None:
		super().__init__()
		  
	# loop through ll to get the last val
	def findLastVal(self):
		temp=self.head
		prev =None
		while(temp.next is not None):
			prev =temp
			temp=temp.next
		last_val =temp.data
		prev.next=None
		self.insert_start(last_val)

	# Function to bring the last node to the front
	def move_last_node_to_front(self):
		tmp = self.head
		sec_last = None # To maintain the track of the second last node

		# To check whether we have not received the empty list or list with a single node
		if not tmp or not tmp.next:
			return

		# Iterate till the end to get the last and second last node
		while tmp and tmp.next :
			sec_last = tmp
			tmp = tmp.next

		# point the next of the second last node to None
		sec_last.next = None

		# Make the last node as the first Node
		tmp.next = self.head
		self.head = tmp

 
if __name__ == '__main__':
	llist = LinkedList()
	llist.insert_start(5)
	llist.insert_start(4)
	llist.insert_start(3)
	llist.insert_start(2)
	llist.insert_start(1)
	
	print("Linked List before moving last to front ")
	llist.print_ll()
	llist.move_last_node_to_front()
	print ("Linked List after moving last to front ")
	llist.print_ll()
	
	# print ("Linked List before moving last to front ")
	# llist.print_ll()
	# llist.findLastVal()
	# print ("Linked List after moving last to front ")
	# llist.print_ll()
	