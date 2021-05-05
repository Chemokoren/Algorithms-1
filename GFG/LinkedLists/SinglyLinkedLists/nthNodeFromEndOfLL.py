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

# Driver Code       
llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(35)
print("check the current list:")
print(llist.printLL())
llist.printNthFromLast(4)  