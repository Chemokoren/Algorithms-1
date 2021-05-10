"""
program to detect loop in LL

algorithm:

Traverse the list one by one and keep putting the node addresses in a Hash Table.
At any point if NULL is reached then return false and if next of current node points
to any of the previously stored nodes in Hash then return true
"""


class Node:

	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:

	# Function to initialize head
	def __init__(self):
		self.head = None

	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	# Utility function to print the linked LinkedList
	def printList(self):
		temp = self.head
		while(temp):
			print(temp.data, end=" ")
			temp = temp.next

	def detectLoop(self):
		temp = self.head
		hash_table =[]
		while(temp):
			if(temp.data in hash_table):
				return True
			hash_table.append(temp.data)
			temp = temp.next
		return False

	# Approach 1: Time Complexity: O(n), space complexity: O(n)
	def detectLoop1(self):
		s = set()
		temp = self.head
		while (temp):
			if (temp in s):
				return True
			s.add(temp) # insert new node in hash
			temp = temp.next
		return False

		'''
        This solution works by modifying the LL datastructure
    
        Approach:
        - Have a visited flag with each node
        -Traverse the LL and keep marking visited nodes.
        -If you see a visited node again then there is a loop. This solutions works in O(n) but
        additional information with each node
    
        '''

		def detectLoop3(self):
			slower_p =self.head
			faster_p =self.head
			while(slower_p and faster_p and faster_p.next):
				slower_p = slower_p.next
				faster_p = faster_p.next.next
				if slower_p == faster_p:
					return



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




"""
Approach 3: Floyd's Cycle-Finding Algorithm

Pseudocode:
-Traverse LL using two pointers
-Move one pointer(slower_p) by one and another pointer(faster_p) by two
-If these pointers meet at the same node then there is a loop. If pointers do not meet then the
LL does not have a loop

"""



# Driver program for testing approach 1
llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(10)

# Create a loop for testing
llist.head.next.next.next.next = llist.head

if(llist.detectLoop()):
	print("Loop found")
else:
	print("No Loop ")


print("This is approach3:")
print(llist.detectLoop())



# if(apr.detectLoop1()):
#     print("Loop found")
# else:
#     print("No Loop ")



print("This is approach2:")

''' Driver program to test approach2 function'''
if __name__=='__main__':

	''' Start with the empty list '''
	head = None;

	head = push(head, 20);
	head = push(head, 4);
	head = push(head, 15);
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






