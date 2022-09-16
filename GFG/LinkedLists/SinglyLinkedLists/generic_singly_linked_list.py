class Node:
	def __init__(self, data):
		self.data =data
		self.next =None

class generic_singly_linked_list:
	def __init__(self) -> None:
		self.head = None

	def push(self, new_data):
		new_node = Node(new_data)
		if self.head == None:
			self.head = new_node
		else:
			new_node.next =self.head
			self.head =new_node

	def print_ll(self):
		curr = self.head
		while(curr):
			print(curr.data, end="-->")
			curr =curr.next
		print()