"""
program to find last man standing

There are n people standing in a circle waiting to be executed. The counting out begins
at some point in the circle and proceeds around the circle in a fixed direction. In 
each step, a certain number of people are skipped and the next person is executed. The
elimination proceeds around the circle(which is becoming smaller and smaller as the
executed people are removed), until only the last person remains, who is given freedom.
Given the total number of person n and a number of k which indicates that k-1 persons
are skipped and the kth person is killed in the circle. The task is to choose the place
in the inititial circle so that you are the last one remaining and so you survive.
(0 - based indexing)

Examples : 

Input : Length of circle : n = 4
        Count to choose next : k = 2
Output : 0

Input : n = 5
        k = 3
Output : 3

Time complexity: O(k * n), as we are using nested loops to traverse k*n time. 
Auxiliary Space: O(n), as we are using extra space for the linked list.
"""
# Python3 program to find last man standing

# /* structure for a node in circular
# linked list */
class Node:
	def __init__(self, x):
		self.data = x
		self.next = None

# function to find the only person left after one in every m-th node is killed
# in a circle of n nodes 
def get_josephus_position(m, n):
	
	# Create a circular linked list of size N
	head = Node(0)
	prev = head
	for i in range(1, n + 1):
		prev.next = Node(i)
		prev = prev.next
	prev.next = head # Connect last node to first

	# while only one node is left in the linked list
	ptr1 = head
	ptr2 = head
	while (ptr1.next != ptr1):
		# find m-th node
		count = 1
		while (count != m):
			ptr2 = ptr1
			ptr1 = ptr1.next
			count += 1

		# remove the m-th node 
		ptr2.next = ptr1.next

		# free(ptr1)
		ptr1 = ptr2.next

	return ptr1.data


print("Expected:, Actual: ", get_josephus_position(2, 14))
print("Expected:, Actual: ", get_josephus_position(3, 5))
print("Expected:, Actual: ", get_josephus_position(2, 4))
