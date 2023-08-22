"""
program to detect loop in LL

algorithm:

Traverse the list one by one and keep putting the node addresses in a Hash Table.
At any point if NULL is reached then return false and if next of current node points
to any of the previously stored nodes in Hash then return true
"""
from generic_singly_linked_list import generic_singly_linked_list,Node

class LinkedList(generic_singly_linked_list):

	# Function to initialize head
	def __init__(self):
		super().__init__()

	def detect_loop(self):
		temp = self.head
		hash_table =[]
		while(temp):
			if(temp.data in hash_table):
				return True
			hash_table.append(temp.data)
			temp = temp.next
		return False

	# Approach 1: Time Complexity: O(n), space complexity: O(n)
	def detect_loop_one(self):
		s = set()
		temp = self.head
		while (temp):
			if (temp in s):
				return True
			s.add(temp) # insert new node in hash
			temp = temp.next
		return False


	'''
	Floyd’s Cycle-Finding Algorithm 

	Approach: This is the fastest method and has been described below:  

    Traverse linked list using two pointers.
    Move one pointer(slow_p) by one and another pointer(fast_p) by two.
    If these pointers meet at the same node then there is a loop. If pointers do not 
	meet then linked list doesn’t have a loop.

	Time complexity: O(n)
    Only one traversal of the loop is needed.
    Auxiliary Space:O(1). 
    There is no space required.

	'''

	def detect_loop_two(self):
		slower_p =self.head
		faster_p =self.head
		while(slower_p and faster_p and faster_p.next):
			slower_p = slower_p.next
			faster_p = faster_p.next.next
			if slower_p == faster_p:
				return True
		return False

llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(10)

# Create a loop for testing
llist.head.next.next.next.next = llist.head

print("Expected: True, Actual:", llist.detect_loop())
print("Expected: True, Actual:", llist.detect_loop_one())
print("Expected: True, Actual:", llist.detect_loop_two())

	
'''
	This solution works by modifying the basic LL datastructure (no hashmap)

	- Have a visited flag with each node
	-Traverse the LL and keep marking visited nodes.
	-If you see a visited node again then there is a loop. This solutions works in O(n)
	 but requires additional information with each node
	 -A variation of this solution that doesn’t require modification to basic data 
	 structure can be implemented using a hash, just store the addresses of visited 
	 nodes in a hash and if you see an address that already exists in hash then there 
	 is a loop.

'''
class node_modified:
	def __init__(self):
		self.data =0
		self.flag =0
		self.next =None

class linked_list_three(generic_singly_linked_list):
	def __init__(self) -> None:
		super().__init__()

	def push(self,head_ref, new_data):
		# allocate node
		new_node =node_modified()

		# put in the data
		new_node.data =new_data
		new_node.flag = 0

		# link the old list off the new node
		new_node.next =(head_ref)

		# move the head to point to the new node
		(head_ref) = new_node
		return head_ref

	# returns true if there is a loop in linked list else returns false
	def detect_loop(self,h):

		while(h != None):
			# if this node is already traversed, it means there is a cycle
			# because you were encountering the node for the second time
			if(h.flag == 1):
				return True

			# if we are seeing the node for the first time, mark its flag as 1
			h.flag = 1
			h = h.next
		return False

head = None

ll = linked_list_three()
ll.push(head, 20)
ll.push(head, 4)
ll.push(head, 15)
ll.push(head, 10)

''' Create a loop for testing '''
# ll.head.next.next.next.next = head
  
# if(ll.detect_loop(head)):
# 	print("Flag Loop found")
# else:
# 	print("FlagNo Loop")










# Time Complexity: O(n) | Space complexity: O(1)
class Approach2Node:

	def __init__(self):
		self.data = 0
		self.next = None
		self.flag = 0
def push(head_ref, new_data):
	''' allocate node '''
	new_node = Approach2Node()

	''' put in the data '''
	new_node.data =new_data
	new_node.flag = 0

	''' link the old list off the new node '''
	new_node.next =head_ref

	''' move the head to point to the new node '''
	head_ref =new_node
	return head_ref

# Returns true if there is a loop in linked list else returns false
def Approach2detectLoop(h):

	while(h !=None):

		if(h.flag == 1):
			return True

		h.flag =1
		h=h.next
	return False



''' Driver program to test approach2 function'''
if __name__=='__main__':

	''' Start with the empty list '''
	head = None;

	head = push(head, 20)
	head = push(head, 4)
	head = push(head, 15)
	head = push(  head, 10)

	''' Create a loop for testing '''
	head.next.next.next.next = head;

	if (Approach2detectLoop(head)):
		print("Loop found")
	else:
		print("No Loop")
 


"""
Approach 4

Algorithm
In this method, a temporary node is created. The next pointer of each node that is 
traversed is made to point to this temporary node. This way we are using the next pointer of a node
as a flag to indicate whether the node has been traversed or not.
Every node is checked to see if the next is pointing to a temporary node or not.
In this case of the first node of the loop, the second time we traverse it this condition will be true, 
hence we find that loop exists. If we come across a node that points to null 
then loop doesn't exist.
"""

# program to return first node of loop
'''
A binary tree node has data, pointer to
left child and a pointer to right child
Helper function that allocates a new node
with the given data and None left and right pointers
'''


class newNode:
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None


# A utility function to pra linked list


def printList(head):
	while (head != None):
		print(head.key, end=" ")
		head = head.next

	print()

# Function to detect first node of loop
# in a linked list that may contain loop


def detectLoop4(head):
	temp =""
	while(head != None):

		# This condition is for the case when there is no loop
		if(head.next == None):
			return False

		# check if next is already pointing to temp
		if(head.next == temp):
			return True

		# store the pointer to the next node in order to get to it in the next step
		nex = head.next

		head.next =temp

		return False


# Driver Code
head = newNode(1)
head.next = newNode(2)
head.next.next = newNode(3)
head.next.next.next = newNode(4)
head.next.next.next.next = newNode(5)

# Create a loop for testing(5 is pointing to 3)
head.next.next.next.next.next = head.next.next

found = detectLoop4(head)
if (found):
	print("Loop Found here:")
else:
	print("No Loop here:")



"""
Solution 5: Store length

In this method, two pointers are created, first (always points to head) and last.
Each time the last pointer moves we calculate no of nodes in between first and last and 
check whether the current no of nodes > previous no of nodes, if yes we proceed by 
moving last pointer else it means we’ve reached the end of the loop, so we return output 
accordingly.

Time complexity: O(n2)
Auxiliary Space: O(1)

"""

# Python program to return first node of loop
class newNode:
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None
		

# A utility function to print a linked list
def printList(head):

	while (head != None) :
		print(head.key, end=" ")
		head = head.next;
	
	print()


# returns distance between first and last node every time
# last node moves forwards
def distance(first, last):

	# counts no of nodes between first and last
	counter = 0

	curr = first

	while (curr != last):
		counter = counter + 1
		curr = curr.next
	

	return counter + 1


# Function to detect first node of loop
# in a linked list that may contain loop
def detectLoop(head):

	# Create a temporary node
	temp = ""

	# first always points to head
	first = head;
	# last pointer initially points to head
	last = head;

	# current_length stores no of nodes between current
	# position of first and last
	current_length = 0

	#current_length stores no of nodes between previous
	# position of first and last*/
	prev_length = -1

	while (current_length > prev_length and last != None) :
		# set prev_length to current length then update the
		# current length
		prev_length = current_length
		# distance is calculated
		current_length = distance(first, last)
		# last node points the next node
		last = last.next;
	
	
	if (last == None) :
		return False
	
	else :
		return True


# Driver program to test above function

head = newNode(1);
head.next = newNode(2);
head.next.next = newNode(3);
head.next.next.next = newNode(4);
head.next.next.next.next = newNode(5);

# Create a loop for testing(5 is pointing to 3)
head.next.next.next.next.next = head.next.next;

found = detectLoop(head)
if (found) :
	print("Loop Found")
else :
	print("No Loop Found")


"""
    This is the simplest approach of the given problem, the only thing we have to do is 
	to assign a new value to each data of node in the linked list which is not in the 
	range given.
    Example suppose (1 <= Data on Node <= 10^3) then after visiting node assign the data
	as -1 as it is out of the given range.

	Time Complexity: O(N)
	Auxiliary Space: O(1)
"""

# Python program to return first node of loop
class Node:
	def __init__(self,d):
		self.data = d
		self.next = None

head = None
def push(new_data):
	global head
	new_node = Node(new_data)
	new_node.next = head
	head=new_node

def detectLoop(h):
	global head
	
	if (head == None):
		return False
	else:
		
		while (head != None):
			if (head.data == -1):
				return True
			else:
				head.data = -1
				head = head.next
		
		return False

push(1)
push(2)
push(3)
push(4)
push(5)

head.next.next.next.next.next = head.next.next

if (detectLoop(head)):
	print("1")
else:
	print("0")


