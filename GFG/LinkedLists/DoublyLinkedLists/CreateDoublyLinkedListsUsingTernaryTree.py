# # Python program to create a doubly linked
# # list out of a given ternary tree
#
# class newNode:
#     def __init__(self, data):
#         self.data =data
#         self.left =None
#         self.right =None
#         self.middle =None
#
# class createDoublyLinkedList:
#     def __init__(self):
#         # Tail of the linked list.
#         self.tail =None
#
#     #Function to push the node to the tail.
#     def push(self, node):
#         # To put the node at the end of
#         # the already existing tail.
#         self.tail.right =node
#
#         # To point to the previous node.
#         node.left =self.tail
#
#         # Middle pointer should point to
#         # nothing so null. initiate right
#         # pointer to null.
#         node.middle =node.right =None
#
#         # update the tail position.
#         self.tail =node
#
#     # Create a doubly linked list out of given
#     # a ternary tree by traversing the tree in
#     # preorder fashion.
#     def ternaryTree(self, node, head):
#         if node ==None:
#             return
#
#         left =node.left
#         middle =node.middle
#         right =node.right
#
#         if self.tail != node:
#             # Already root is in the tail so dont push
#             # the node when it was root. In the first
#             # case both node and tail have root in them.
#             self.push(node)
#
#         # First the left child is to be taken.
#         # Then middle and then right child.
#         self.ternaryTree(left, head)
#         self.ternaryTree(middle, head)
#         self.ternaryTree(right, head)
#
#     def startTree(self, root):
#         # Initiate the head and tail with root.
#         head =root
#         self.tail =root
#         self.ternaryTree(root, head)
#
#         # since the head, root are passed
#         # with reference to the changes in
#         # root will be reflected in head.
#         return head
#
#     # Utility function for printing double linked list.
#     def printList(self, head):
#         print(head.data, end = " ")
#         head =head.right
#
# # Driver code to test the program
# if __name__ =='__main__':
#     # Constructing ternary tree as shown
#     # in the above figure
#     root =newNode(30)
#     root.left =newNode(5)
#     root.middle =newNode(11)
#     root.right =newNode(63)
#     root.left.left =newNode(1)
#     root.left.middle =newNode(4)
#     root.left.right =newNode(8)
#     root.middle.left =newNode(6)
#     root.middle.middle =newNode(7)
#     root.middle.right =newNode(15)
#     root.right.left =newNode(31)
#     root.right.middle =newNode(55)
#     root.right.right =newNode(65)
#
#     # The function which initiates the list
#     # process returns the head.
#     # head = None
#     dll =createDoublyLinkedList()
#     head =dll.startTree(root)
#
#     dll.printList(head)
#
#


# Python3 program to create a doubly linked
# list out of given a ternary tree.

# Custom node class.
class newNode:

	def __init__(self, data):

		self.data = data
		self.left = None
		self.right = None
		self.middle = None

class GFG:

	def __init__(self):

		# Tail of the linked list.
		self.tail = None

	# Function to push the node to the tail.
	def push(self, node):

		# To put the node at the end of
		# the already existing tail.
		self.tail.right = node

		# To point to the previous node.
		node.left = self.tail

		# Middle pointer should point to
		# nothing so null. initiate right
		# pointer to null.
		node.middle = node.right = None

		# Update the tail position.
		self.tail = node

	# Create a doubly linked list out of given
	# a ternary tree By traversing the tree in
	# preoder fashion.
	def ternaryTree(self, node, head):

		if node == None:
			return

		left = node.left
		middle = node.middle
		right = node.right

		if self.tail != node:

			# Already root is in the tail so dont push
			# the node when it was root.In the first
			# case both node and tail have root in them.
			self.push(node)

		# First the left child is to be taken.
		# Then middle and then right child.
		self.ternaryTree(left, head)
		self.ternaryTree(middle, head)
		self.ternaryTree(right, head)

	def startTree(self, root):

		# Initiate the head and tail with root.
		head = root
		self.tail = root
		self.ternaryTree(root, head)

		# Since the head,root are passed
		# with reference the changes in
		# root will be reflected in head.
		return head

	# Utility function for printing double linked list.
	def printList(self, head):

		print("Created Double Linked list is:")

		while head:
			print(head.data, end = " ")
			head = head.right

# Driver code
if __name__ == '__main__':

	# Construting ternary tree as shown
	# in above figure
	root = newNode(30)
	root.left = newNode(5)
	root.middle = newNode(11)
	root.right = newNode(63)
	root.left.left = newNode(1)
	root.left.middle = newNode(4)
	root.left.right = newNode(8)
	root.middle.left = newNode(6)
	root.middle.middle = newNode(7)
	root.middle.right = newNode(15)
	root.right.left = newNode(31)
	root.right.middle = newNode(55)
	root.right.right = newNode(65)

	# The function which initiates the list
	# process returns the head.
	# head = None
	gfg = GFG()
	head = gfg.startTree(root)

	gfg.printList(head)
