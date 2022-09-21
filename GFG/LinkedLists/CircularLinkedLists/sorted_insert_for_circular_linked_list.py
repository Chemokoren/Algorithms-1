"""
program to insert a new value in a sorted Circular Linked List(CLL)

Algorithm:
Allocate memory for the newly inserted node and put data in the newly allocated node. Let the pointer to the new node
be new_node. After memory allocation, following are the three cases that need to be handled

Linked List is empty:
    a)  since new_node is the only node in CLL, make a self loop.
          new_node.next = new_node;
    b) change the head pointer to point to new node.
          head_ref = new_node;
2) New node is to be inserted just before the head node:
  (a) Find out the last node using a loop.
         while(current.next != head_ref)
            current = current.next
  (b) Change the next of last node.
         current.next = new_node
  (c) Change next of new node to point to head.
         new_node.next = head_ref;
  (d) change the head pointer to point to new node.
         head_ref = new_node;
3) New node is to be  inserted somewhere after the head:
   (a) Locate the node after which new node is to be inserted.
         while ( current.next != head_ref and current.next.data < new_node.data)
         {   current = current.next   }
   (b) Make next of new_node as next of the located pointer
         new_node.next = current.next;
   (c) Change the next of the located pointer
         current.next = new_node;
"""
from generic_circular_linked_list import Circular_Linked_list
# Node class
class Node:

	# Constructor to initialize the node object
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList(Circular_Linked_list):

    def __init__(self) -> None:
        super().__init__()

            
    """ function to insert a new_node in a list in sorted way.
	Note that this function expects a pointer to head node
	as this can modify the head of the input linked list """
    
    def sortedInsert(self, new_node):
        
        current = self.head

		# Case 1
        if current is None:
            new_node.next = new_node
            self.head = new_node
		
		# Case 2
        elif (current.data >= new_node.data):
			
			# If value is smaller than head's value, change next of last node
            while current.next != self.head :
                current = current.next
            current.next = new_node
            new_node.next = self.head
            self.head = new_node			
            
        # Case 3
        else:
            # Locate the node before the point of insertion
            while (current.next != self.head and current.next.data < new_node.data):
                current = current.next
            new_node.next = current.next
            current.next = new_node



llist = LinkedList()
arr = [12, 56, 2, 11, 1, 90]

# Create linked list from the array arr[]: 1->2->11->12->56->90
for i in range(len(arr)):
	temp = Node(arr[i])
	llist.sortedInsert(temp)



llist.print_cll()