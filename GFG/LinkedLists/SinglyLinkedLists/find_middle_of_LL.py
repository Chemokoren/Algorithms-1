
"""
Find the middle of a given linked list

Given a signly linked list, find the middle of the linked list. For example, if the given 
linked list is 1->2->3->4->5 then the output should be 3. If there are even nodes, then 
there would be two middle nodes, we need to print the second middle element. For example,
if the given linked list is 1->2->3->4->5->6 then the output should be 4.

Method 1
- Traverse the whole linked list and count the no. of nodes. Now traverse the list again till 
count/2 and return the noe at count/2

Time Complexity: O(n) where n is no of nodes in linked list

Auxiliary Space: O(1)
"""
class Node:
	def __init__(self,data):
		self.data = data
		self.next = None


class NodeOperation:

	# function to add a new node
	def pushNode(self, head_ref, data_val):

		# Allocate node and put in the data
		new_node = Node(data_val)

		# link the old list off the new node
		new_node.next =head_ref

		# move the head to point to the new node
		head_ref = new_node
		return head_ref

	# A utility fuction to print a given linked list
	def printNode(self, head):
		while(head != None):
			print('%d->' % head.data, end="")
			head = head.next
		print("NULL")

	''' Utility Function to find length of linked list '''
	def getLen(self, head):
		temp = head
		len = 0

		while(temp != None):
			len +=1
			temp = temp.next
		return len

	def printMiddle(self, head):
		if head != None:
			# find length
			len = self.getLen(head)
			temp = head

			# traverse till we reach half of length
			midIdx  = len //2

			while midIdx != 0:
				temp = temp.next
				midIdx -=1

			print("mid val is:", temp.data)


head = None
temp = NodeOperation()
for i in range(5, 0, -1):
    head = temp.pushNode(head, i)
    temp.printNode(head)
    temp.printMiddle(head)


"""
Traverse linked list using two-pointers. Move one pointer by one and the other pointers by 
two. When the fast pointer reaches the end, the slow pointer will reach the middle of the 
linked list

Time Complexity: O(N), As we are traversing the list only once.
Auxiliary Space: O(1), As constant extra space is used.

"""

class middle_of_ll_pointers:

	def __init__(self) -> None:
		self.head =None

	def push_at_head(self,new_data):
		new_node =Node(new_data)
		if self.head == None:
			self.head =new_node
		else:
			new_node.next =self.head
			self.head =new_node


	def calc_mid(self):
		slow_point = self.head
		fast_point = self.head

		while fast_point.next != None:
			fast_point =fast_point.next.next
			slow_point =slow_point.next
		return slow_point.data


ll = middle_of_ll_pointers()
ll.push_at_head(5)
ll.push_at_head(4)
ll.push_at_head(3)
ll.push_at_head(2)
ll.push_at_head(1)
print("median val using pointers: ", ll.calc_mid())


"""
Method 3

Initialize the mid element as head and initialize a counter as 0. Traverse the list from the
head, while traverseing increment the counter and change mid to mid->next whenever the counter
is odd. So the mid will move only half of the total length of the list.

Time Complexity: O(N), As we are traversing the list once.
Auxiliary Space: O(1), As constant extra space is used.
"""
class LinkedList_three:

	def __init__(self) -> None:
		self.head = None

	# Function to insert a new node at the beginning
	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node
  
    # Print the linked list
	def printList(self):
		node = self.head
		while node:
			print(str(node.data) + "->", end = "")
			node = node.next
		print("NULL")

	# function to get the middle of the linked list
	def printMiddle(self):
		count = 0
		mid = self.head
		heads = self.head

		while heads != None:
			# update mid, when 'count' is odd number
			if count&1:
				mid = mid.next 
			count +=1
			heads = heads.next

		# if empty list is provided
		if mid != None:
			print("The middle element is ", mid.data)

print(" \n three \n")
llist = LinkedList_three()
for i in range(5, 0, -1):
        llist.push(i)
        llist.printList()
        llist.printMiddle()
  




# Method 2
class LinkedList:
	# function should return index to the any valid peak element
	# createNode and and make linked list

	def __init__(self):
		self.head = None

	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	def printLL(self):
		temp =self.head
		while(temp):
			print(temp.data, end=",")
			temp =temp.next
		print("")

		# Print the linked list
	def printList(self):
		node = self.head
		while node:
			print(str(node.data) + "->", end="")
			node = node.next
		print("NULL")

	def findMid(self,head):
		first =self.head
		second =self.head
		while second and second.next:
			first =first.next
			second=second.next.next
		return first.data

	# Function to get the middle of the linked list
	def printMiddle(self):
		count = 0
		mid =self.head
		heads =self.head
		while(heads != None):
			# update mid, when 'count' is odd number
			if count&1:
				mid =mid.next
			count +=1
			heads =heads.next

		# If empty list is provided
		if mid !=None:
			print("The middle element is", mid.data)




# Driver Code       
llist = LinkedList()
for i in range(0,13,1):
	llist.push(i)
# llist.push(20)
# llist.push(4)
# llist.push(15)
# llist.push(35)
print("check the current list:")
print(llist.printList())
print(llist.findMid(llist.head))
print("########################################")
print(llist.printMiddle())

print("\n my tests \n")
class my_node:

	def __init__(self,data) -> None:
		self.data = data
		self.next = None

class my_tests:

	def __init__(self) -> None:
		self.head =None

	def push_at_head(self,new_data):
		new_node =my_node(new_data)
		if self.head == None:
			self.head =new_node
		else:
			new_node.next =self.head
			self.head =new_node

	def calc_median(self):
		curr =self.head
		count = 0
		while(curr):
			curr= curr.next
			count +=1
		
		if count % 2 != 0:
			pos = 1+(count//2)
			return (self.get_val_pos(pos))
		else:
			first_val =count//2
			second_val =1 + first_val
			first_pos = (self.get_val_pos(first_val))
			second_pos = (self.get_val_pos(second_val))
			
			return (first_pos +second_pos)/2

	def get_val_pos(self,pos):
		curr = self.head
		count = 0
		while(count < pos-1):
			curr =curr.next
			count +=1
		return curr.data

	def print_ll(self):

		curr = self.head
		while(curr):
			print(curr.data,end="-->")
			curr =curr.next
		print()

		
ll = my_tests()
ll.push_at_head(5)
ll.push_at_head(4)
ll.push_at_head(3)
ll.push_at_head(2)
ll.push_at_head(1)
ll.print_ll()
print("median val: ", ll.calc_median())
