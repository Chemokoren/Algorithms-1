"""
Write a function that counts the number of times a given int occurs in a Linked List

Given a singly linked list and a key, count the number of occurrences of the given key 
in the linked list. For example, if the given linked list is 1->2->1->2->1->3->1 and 
the given key is 1, then the output should be 4.

program to count the number of time a given int occurs in LL


"""
from generic_singly_linked_list import generic_singly_linked_list
class Node:
	def __init__(self, data):
		self.data =data
		self.next =None

"""

Method 1- Without Recursion 

Algorithm:  

Step 1: Start
Step 2: Create A Function Of A Linked List, Pass A Number 
        As Arguments And Provide The Count Of The Number To The Function.
Step 3: Initialize Count Equal To 0.
Step 4: Traverse In Linked List Until Equal Number Found.
Step 5: If Found A Number Equal To Update Count By 1.
Step 6: After Reaching The End Of The Linked List Return Count.
Step 7: Call The Function.
Step 8: Prints The Number Of Int Occurrences.
Step 9: Stop.

Time Complexity: O(n) 
Auxiliary Space: O(1)
"""

class LinkedList_one(generic_singly_linked_list):

	def __init__(self) -> None:
		super().__init__()
		
	# counts the no. of occurrences of a node(search_for) in a linked list(head)
	def count(self, search_for):
		current = self.head
		count = 0
		while(current is not None):
			if current.data == search_for:
				count +=1

			current = current.next
		return count

llist = LinkedList_one()
llist.push(1)
llist.push(3)
llist.push(1)
llist.push(2)
llist.push(1)
 

print ("count of 1 is % d" %(llist.count(1)))



'''
Algorithm: Recursion
count(head, key);
if head is NULL
return frequency
if(head->data==key)
increase frequency by 1
count(head->next, key)

Time complexity: O(n) where n is size of linked list

Auxiliary Space: O(n) for call stack since using recursion 
'''
class LinkedList_two(generic_singly_linked_list):
	def __init__(self):
		super().__init__()
		self.count =0


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



# driver code to test the program
if __name__ == '__main__':
	print("function counts number of times int occurs in a LinkedList")
	ll =LinkedList_two()
	ll.push(10)
	ll.push(20)
	ll.push(30)
	ll.push(10)
	ll.push(50)
	# ll.printLL()
	print("Recursion")
	print(ll.countRecurs(ll.head,10))
	print("Recursion 1")
	print(ll.countRecurs1(ll.head, 10))



print("\n my tests \n")

class linked_list_my_tests(generic_singly_linked_list):
	def __init__(self) -> None:
		super().__init__()

	def count_number_of_int(self,key):
		curr = self.head
		count =0
		while(curr):
			if curr.data ==key:
				count +=1
			curr =curr.next
		return count
		

ll = linked_list_my_tests()
ll.push(1)
ll.push(3)
ll.push(1)
ll.push(2)
ll.push(1)
ll.push(2)
ll.push(1)
ll.print_ll()
print("count of 1 is:", ll.count_number_of_int(1))
print("count of 2 is:", ll.count_number_of_int(2))
