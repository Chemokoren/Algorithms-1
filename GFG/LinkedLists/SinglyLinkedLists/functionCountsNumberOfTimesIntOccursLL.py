"""
program to count the number of time a given int occurs in LL

Algorithm: Recursion
count(head, key);
if head is NULL
return frequency
if(head->data==key)
increase frequency by 1
count(head->next, key)

"""

class Node:
	def __init__(self, data):
		self.data =data
		self.next =None

class LinkedList:
	def __init__(self):
		self.head =None
		self.count =0

	def count_int(self,int_val):
		count =0
		temp =self.head
		while temp:
			if(temp.data == int_val):
				count =count +1
			temp =temp.next
		return count

	def countRecurs(self,head, key):

		if not(head):
			return self.count

		if(head.data==key):
			self.count =self.count + 1

		return self.countRecurs(head.next, key)

	def countRecurs1(self, temp, key):
		if temp is None:
			return 0
		if temp.data == key:
			return 1 + self.countRecurs1(temp.next, key)
		return self.countRecurs1(temp.next, key)

	def printLL(self):
		temp =self.head
		while temp:
			print(temp.data)
			temp=temp.next

	def push(self,data):
		new_node =Node(data)
		new_node.next =self.head
		self.head=new_node

# driver code to test the program
if __name__ == '__main__':
	print("function counts number of times int occurs in a LinkedList")
	ll =LinkedList()
	ll.push(10)
	ll.push(20)
	ll.push(30)
	ll.push(10)
	ll.push(50)
	# ll.printLL()
	print(ll.count_int(10))
	print("Recursion")
	print(ll.countRecurs(ll.head,10))
	print("Recursion 1")
	print(ll.countRecurs1(ll.head, 10))
