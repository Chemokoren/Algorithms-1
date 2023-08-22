# program to find the n'th node from end
class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None
     
class LinkedList:
	
	def __init__(self):
		self.head = None
		
	# createNode and and make linked list
	
	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node
		
	def printLL(self):
		temp =self.head
		while(temp):
			print(temp.data, end=",")
			temp =temp.next
			
	# Function to get the nth node from the last of a LL
	'''
	Time complexity: O(M) where M is the size of the linked list
	Auxiliary Space: O(1)
	'''
	def printNthFromLast(self, n):
		temp =self.head
		length = 0
		while temp is not None:
			temp =temp.next
			length += 1
		
		# print count
		if n > length:
			print('Location is greater than the length of LinkedList')
			return
			
		temp =self.head
		for i in range(0, length -n):
			temp =temp.next
		print(temp.data)
	   
	def nth_node(self, pos):
		if self.head == None:
			print("No nodes to traverse")
			return
			
		curr =self.head
		count = 0
		while(curr):
			curr =curr.next
			count +=1
		if count >= pos:
			new_pos = count - pos
		else:
			return "position is greater than the Linked List"
		i = 0
		start = self.head
		while i < new_pos:
			start =start.next
			i +=1
		return start.data

	"""
	Time Complexity: O(M) where M is the length of the linked list. 
	Auxiliary Space: O(M) for call stack
	"""
	def print_nth_from_last_recursive(self,head, N):
		i = 0
		if(head == None):
			return 
		self.print_nth_from_last_recursive(head.next, N)
		i +=1
		if(i == N):
			print("bbb", head.data)
			return head.data

	def recursive_nth(self,N):
		return self.print_nth_from_last_recursive(self.head, N)

	"""
	Nth node from the end of a Linked List using two pointers:

    As Nth node from the end equals to (Length – N + 1)th node from the start, so the idea is 
	to Maintain two pointers starting from the head of the Linked-List and move one pointer
	to the Nth node from the start and then move both the pointers together until the pointer
	at the Nth position reaches the last node. Now the pointer which was moved later points
	at the Nth node from the end of the Linked-List

	Follow the given steps to solve the problem:

    Maintain two pointers main_ptr and ref_ptr
    Move ref_ptr to the Nth node from the start
    Now move both main_ptr and ref_ptr, until the ref_ptr reaches the last node
    Now print the data of the main_ptr, as it is at the Nth node from the end
	Time Complexity: O(M) where M is the length of the linked list.
	Auxiliary Space: O(1)
	"""
	def printNthFromLast(self, N):
		main_ptr = self.head
		ref_ptr = self.head

		count = 0
		if(self.head is not None):
			while(count < N):
				if(ref_ptr is None):
					print("% d is greater than the no. of nodes in list" % (N))
					return 
				ref_ptr = ref_ptr.next
				count += 1

		if (ref_ptr is None):
			self.head = self.head.next
			if (self.head is not None):
				print("Node no. % d from last is % d "     % (N, main_ptr.data))
		else:
			while(ref_ptr is not None):
				main_ptr = main_ptr.next
				ref_ptr = ref_ptr.next
			print("Node no. % d from last is % d "  % (N, main_ptr.data))
         
llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(35)
print("check the current list:")
print(llist.printLL())
llist.printNthFromLast(4)  
print("Expected:, Actual:", llist.nth_node(4))
print("\n aaa \n")
llist.printNthFromLast(3)