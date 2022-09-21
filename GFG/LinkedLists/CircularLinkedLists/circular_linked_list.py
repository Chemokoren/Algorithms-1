"""
Introuction to Circular Linked List

The circular linked list is a linked list where all nodes are connected to form a 
circle. In a circular linked list, the first node and the last node are connected to
each other which forms a circle.There is no NULL at the end.

There are two types.
1) Circular singly linked list
- In a circular singly linked list, the last node of the list contains a pointer to the
first node of the list. We traverse the circular singly linked list until we reach the
same node where we started. The circular singly linked list has no beginning or end.
No null value is present in the next part of any of the nodes.

2) Circular Doubly Linked List
- Circular doubly linked list has properties of both doubly linked list and circular
linked list in which two consecutive elements are linked or connected by the previous
and next pointer and the last node points to the first node by the next pointer and 
also the first node points to the last node by the previous pointer.

Note: We will be using the singly circular linked list to represent the working of the circular linked list.
Representation of circular linked list:

Circular linked lists are similar to single Linked Lists with the exception of 
connecting the last node to the first node.

Node representation of a circular linked list

"""
class Node:
    def __init__(self, value) -> None:
        self.value =value
        self.next = None

# example of a circular singly linked list
one =Node(3)
two =Node(5)
three =Node(9)
one.next = two
two.next =three
three.next =one

"""
Explanation: In the above program one, two, and three are the node with values 3, 5, 
and 9 respectively which are connected in a circular manner as:

    For Node One: The Next pointer stores the address of Node two.
    For Node Two: The Next stores the address of Node three
    For Node Three: The Next points to node one.

Operations on the circular linked list:

We can do some operations on the circular linked list similar to the singly linked 
list which are:

    Insertion
    Deletion

1. Insertion in the circular linked list:

A node can be added in three ways:

    Insertion at the beginning of the list
    Insertion at the end of the list
    Insertion in between the nodes

1) Insertion at the beginning of the list: To insert a node at the beginning of the 
list, follow these steps: 

    Create a node, say T. 
    Make T -> next = last -> next. 
    last -> next = T. 

Time complexity: O(1) to insert a node at the beginning no need to traverse list
    it takes constant time 
Auxiliary Space: O(1)
"""

def add_beginning(self, last_node,new_data):
    new_node =Node(new_data)
    if(last_node == None):
        last_node =new_node
    new_node.next = last_node
    last_node.next = new_node

    return last_node
    
'''
2) Insertion at the end of the list: To insert a node at the end of the list, follow these steps: 

Create a node, say T. 
Make T -> next = last -> next; 
last -> next = T. 
last = T. 

Time Complexity: O(1) to insert a node at the end of the list. No need to traverse the
list as we are utilizing the last pointer, hence it takes constant time.

Auxiliary Space: O(1)
'''
def add_end(self, last_node,new_data):
    new_node =Node(new_data)
    if(last_node == None):
        last_node =new_node
    new_node.next = last_node.next
    last_node.next = new_node

    return last_node

'''
3) Insertion in between the nodes: To insert a node in between the two nodes, follow
these steps:
- Create a node, say T
- Search for the node after which T needs to be inserted, say that node is P
- Make T->next = p->next
- p->next =T

Time Complexity: O(N)
Auxiliary Space: O(1)
'''
def add_after(last_node, new_data, item):
    if(last_node == None):
        return None
    p = last_node.next

    # searching the item
    while(p != last_node.next):
        if (p.data == item):
            new_node = Node(new_data)

            new_node.next = p.next

            # adding newly allocated node after p.
            p.next = new_node

            # checking for the last node
            if(p == last_node):
                last_node =new_node
            return last_node
        p.next = new_node
    print(f"{item} not present in the list")
    return last_node

"""
2. Deletion in a circular linked list:

1) Delete the node only if it is the only node in the circular linked list:

    Free the node’s memory
    The last value should be NULLA node always points to another node, so NULL 
    assignment is not necessary.
    Any node can be set as the starting point.
    Nodes are traversed quickly from the first to the last.

2) Deletion of the last node:

    Locate the node before the last node (let it be temp)
    Keep the address of the node next to the last node in temp
    Delete the last memory
    Put temp at the end

3) Delete any node from the circular linked list: We will be given a node and our task
 is to delete that node from the circular linked list.

Algorithm:
Case 1: List is empty. 

    If the list is empty we will simply return.

Case 2:List is not empty  

    If the list is not empty then we define two pointers curr and prev and initialize 
    the pointer curr with the head node.
    Traverse the list using curr to find the node to be deleted and before moving to curr
    to the next node, every time set prev = curr.
    If the node is found, check if it is the only node in the list. If yes, 
    set head = NULL and free(curr).
    If the list has more than one node, check if it is the first node of the list. 
    Condition to check this( curr == head). If yes, then move prev until it reaches the 
    last node. After prev reaches the last node, set head = head -> next 
    and prev -> next = head. Delete curr.
    If curr is not the first node, we check if it is the last node in the list. 
    Condition to check this is (curr -> next == head).
    If curr is the last node. Set prev -> next = head and delete the node curr by 
    free(curr).
    If the node to be deleted is neither the first node nor the last node, then set 
    prev -> next = curr -> next and delete curr.


Time Complexity: O(N), Worst case occurs when the element to be deleted is the last 
element and we need to move through the whole list.
Auxiliary Space: O(1), As constant extra space is used.
"""

# Function to insert a node at the  beginning of a Circular linked list
def push(head_ref, data):
    # Create a new node and make head  as next of it.
	ptr1 = Node(data)
	ptr1.next = head_ref

	# If linked list is not NULL then set the next of last node
	if (head_ref != None):
		#  Find the node before head and update next of it.
		temp = head_ref
		while(temp.next != head_ref):
			temp = temp.next
		temp.next = ptr1
	else:
        # For the first node
		ptr1.next = ptr1

	head_ref = ptr1

'''
Function to print nodes in a given
circular linked list
'''
def printList(self, head):
	temp = head
	if (head != None):
		while (temp != head):
			print(temp.data, end="-->")
			temp = temp.next
	print()

'''
Function to delete a given node from the list
'''
def deleteNode(head, key):

	# If linked list is empty
	if (head == None):
		return

	# If the list contains only a single node
	if(head.data == key and head.next == head):
		# free(*head)
		head = None
		return
	

	last = head

	# If head is to be deleted
	if (head.data == key):

		# Find the last node of the list
		while(last.next != head):
			last = last.next

		# Point last node to the next of head i.e. the second node of the list
		last.next = head.next
		# free(*head);
		head = last.next
		return

	# Either the node to be deleted is not found or the end of list is not reached
	while (last.next != head and last.next.data != key):
		last = last.next

	# If node to be deleted was found
	if(last.next.data == key):
		d = last.next;
		last.next = d.next
		# free(d);
	else:
		print("no such keyfound")

if __name__=="__main__":
	# Initialize lists as empty
	head = None

	# Created linked list will be : 2->5->7->8->10
	push(head, 2)
	push(head, 5)
	push(head, 7)
	push(head, 8)
	push(head, 10)

	print("List Before Deletion: ")
	printList(head)

	deleteNode(head, 7)

	print("List After Deletion: ")
	printList(head)

"""
Advantages of Circular Linked Lists: 

    Any node can be a starting point. We can traverse the whole list by starting from 
    any point. We just need to stop when the first visited node is visited again. 
    Useful for implementation of a queue. Unlike this implementation, we don’t need to 
    maintain two pointers for front and rear if we use a circular linked list. 
    We can maintain a pointer to the last inserted node and the front can always be 
    obtained as next of last.

 

    Circular lists are useful in applications to repeatedly go around the list. 
    For example, when multiple applications are running on a PC, it is common for the 
    operating system to put the running applications on a list and then cycle through 
    them, giving each of them a slice of time to execute, and then making them wait
    while the CPU is given to another application. It is convenient for the operating
    system to use a circular list so that when it reaches the end of the list it can 
    cycle around to the front of the list. 
    Circular Doubly Linked Lists are used for the implementation of advanced data 
    structures like the Fibonacci Heap.

Disadvantages of circular linked list:

    Compared to singly linked lists, circular lists are more complex.
    Reversing a circular list is more complicated than singly or doubly reversing a 
    circular list.
    It is possible for the code to go into an infinite loop if it is not handled
    carefully.
    It is harder to find the end of the list and control the loop.

Applications of circular linked lists:

    Multiplayer games use this to give each player a chance to play.
    A circular linked list can be used to organize multiple running applications on an 
    operating system. These applications are iterated over by the OS.

Why circular linked list?

    A node always points to another node, so NULL assignment is not necessary.
    Any node can be set as the starting point.
    Nodes are traversed quickly from the first to the last.

"""