
class node:
	def __init__(self,data):
		self.data = data
		self.next = None

class LinkedList:
	# function should return index to the any valid peak element
	# createNode and and make linked list

	def __init__(self):
		self.head = None

	def push(self, new_data):
		new_node = node(new_data)
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