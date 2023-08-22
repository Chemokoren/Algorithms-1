'''
Intersection of two sorted linked lists

Given two lists sorted in increasing order, createe and return a new list representing
the intersection of two lists. The new list should be made with its own memory - the 
original lists should be changed.

Input: 
First linked list: 1->2->3->4->6
Second linked list be 2->4->6->8, 
Output: 2->4->6.
The elements 2, 4, 6 are common in 
both the list so they appear in the 
intersection list. 

Input: 
First linked list: 1->2->3->4->5
Second linked list be 2->3->4, 
Output: 2->3->4
The elements 2, 3, 4 are common in 
both the list so they appear in the 
intersection list.

Link list node

Time Complexity: O(m+n) where m and n are number of nodes in first and second linked lists respectively. 
Only one traversal of the lists are needed.

Auxiliary Space: O(min(m, n)). 
The output list can store at most min(m,n) nodes .
'''
class Node:
    def __init__(self):
        self.data = 0
        self.next = None
'''
This solution uses the temporary dummy to build up the result list

Approach: 
The idea is to use a temporary dummy node at the start of the result list. The pointer 
tail always points to the last node in the result list, so new nodes can be added easily.
The dummy node initially gives the tail a memory space to point to. This dummy node is 
efficient, since it is only temporary, and it is allocated in the stack. The loop 
proceeds, removing one node from either ‘a’ or ‘b’ and adding it to the tail. When the 
given lists are traversed the result is in dummy. next, as the values are allocated from
next node of the dummy. If both the elements are equal then remove both and insert the
element to the tail. Else remove the smaller element among both the lists. s

    Time Complexity: O(m+n) where m and n are number of nodes in first and second 
    linked lists respectively. 
    Only one traversal of the lists are needed.
    Auxiliary Space: O(min(m, n)). 
    The output list can store at most min(m,n) nodes .

'''
def sortedIntersect(a,b):
    dummy = Node()
    tail = dummy;
    dummy.next =None

    '''
    once one or the other list runs out -- we're done
    '''
    while (a !=None and b!=None):
        if(a.data == b.data):
            tail.next =push((tail.next), a.data)
            tail = tail.next
            a = a.next
            b = b.next

        # advance the samller list
        elif(a.data < b.data):
            a = a.next
        else:
            b =b.next
    return dummy.next

''' UTILITY FUNCTIONS '''
''' Function to insert a node at
the beginning of the linked list '''
def push(head_ref, new_data):

    new_node = Node()
  
    new_node.data = new_data
  
    ''' link the old list off the new node '''
    new_node.next = head_ref
  
    ''' move the head to point to the new node '''
    head_ref = new_node 
    return head_ref
 
''' Function to print nodes in
   a given linked list '''
def printList(node):
    while (node != None):
        print(node.data, end=' ')
        node = node.next
      
''' Driver code'''
if __name__=='__main__':
     
    ''' Start with the empty lists '''
    a = None
    b = None
    intersect = None
  
    ''' Let us create the first sorted
     linked list to test the functions
     Created linked list will be
     1.2.3.4.5.6 '''
    a = push(a, 6)
    a = push(a, 5)
    a = push(a, 4)
    a = push(a, 3)
    a = push(a, 2)
    a = push(a, 1)
  
    ''' Let us create the second sorted linked list
   Created linked list will be 2.4.6.8 '''
    b = push(b, 8)
    b = push(b, 6)
    b = push(b, 4)
    b = push(b, 2)
  
    ''' Find the intersection two linked lists '''
    intersect = sortedIntersect(a, b)
  
    print("Linked list containing common items of a & b ")
    printList(intersect)

"""

Using Local References

Approach: 

This solution is structurally very similar to the above, but it avoids using a
dummy node Instead, it maintains a struct node** pointer, lastPtrRef, that always points
to the last pointer of the result list. This solves the same case that the dummy node 
did — dealing with the result list when it is empty. If the list is built at its tail, 
either the dummy node or the struct node** “reference” strategy can be used. 

    Time Complexity: O(m+n) where m and n are number of nodes in first and second linked
    lists respectively. 
    Only one traversal of the lists are needed.
    Auxiliary Space: O(max(m, n)). 
    The output list can store at most m+n nodes.
"""
# Python3 program to implement above approach

# Link list node
class Node:
	def __init__(self, d):
		self.data = d
		self.next = None


def sortedIntersect(a, b):

	result = Node(0)
	curr = result

	# Advance comparing the first
	# nodes in both lists.
	# When one or the other list runs
	# out, we're done.
	while (a != None and b != None):
			if (a.data == b.data):
				# found a node for the intersection
				curr.next = Node(a.data)
				curr = curr.next

				a = a.next
				b = b.next
			elif (a.data < b.data):
				a = a.next # advance the smaller list
			else:
				b = b.next
	result = result.next
	return result


# UTILITY FUNCTIONS
# Function to insert a node at the beginning of the linked list
def push(head_ref, new_data):

	# Allocate node
	new_node = Node(new_data)

	# Link the old list off the new node
	new_node.next = head_ref

	# Move the head to point to the new node
	head_ref = new_node
	return head_ref

	# Function to print nodes in a given linked list


def printList(node):
	while (node != None):
		print(node.data, end=" ")
		node = node.next


# Driver code

# Start with the empty lists
a = None
b = None
intersect = None

# Let us create the first sorted linked list to test the functions Created
# linked list will be 1.2.3.4.5.6

a = push(a, 6)
a = push(a, 5)
a = push(a, 4)
a = push(a, 3)
a = push(a, 2)
a = push(a, 1)

# Let us create the second sorted linked list Created linked list will be
# 2.4.6.8

b = push(b, 8)
b = push(b, 6)
b = push(b, 4)
b = push(b, 2)

# Find the intersection two linked lists
intersect = sortedIntersect(a, b)

print("Linked list containing " + "common items of a & b")
printList(intersect)


"""

Recursive Solution

Approach: 
The recursive approach is very similar to the above two approaches. Build a recursive 
function that takes two nodes and returns a linked list node. Compare the first element 
of both the lists. 

    If they are similar then call the recursive function with the next node of both the 
    lists. Create a node with the data of the current node and put the returned node 
    from the recursive function to the next pointer of the node created. Return the node 
    created.
    If the values are not equal then remove the smaller node of both the lists and call
    the recursive function.

    Time Complexity: O(m+n) where m and n are number of nodes in first and second linked 
    lists respectively. 
    Only one traversal of the lists are needed.
    Auxiliary Space: O(max(m, n)). 
    The output list can store at most m+n nodes.

"""
# Link list node
class Node:
	def __init__(self):
		self.data = 0
		self.next = None
		

def sortedIntersect(a, b):

	# base case
	if (a == None or b == None):
		return None

	# If both lists are non-empty
	# Advance the smaller list and call recursively
	if (a.data < b.data):
		return sortedIntersect(a.next, b);

	if (a.data > b.data):
		return sortedIntersect(a, b.next);

	# Below lines are executed only
	# when a.data == b.data
	temp = Node();
	temp.data = a.data;

	# Advance both lists and call recursively
	temp.next = sortedIntersect(a.next, b.next);
	return temp;	

	# UTILITY FUNCTIONS
	# Function to insert a node at the beginning of the linked list

def push(head_ref, new_data):

	# Allocate node
	new_node = Node()

	# Put in the data
	new_node.data = new_data;

	# Link the old list off the new node
	new_node.next = head_ref;

	# Move the head to point to the new node
	head_ref = new_node;
	return head_ref;	

	# Function to print nodes in a given linked list
		
def printList(node):
	while (node != None):
		print(node.data, end=" ")
		node = node.next;		


# Driver code

# Start with the empty lists
a = None
b = None
intersect = None

# Let us create the first sorted linked list to test the functions Created
# linked list will be 1.2.3.4.5.6
		
a = push(a, 6)
a = push(a, 5)
a = push(a, 4)
a = push(a, 3)
a = push(a, 2)
a = push(a, 1)

# Let us create the second sorted linked list Created linked list will be
# 2.4.6.8
		
b = push(b, 8)
b = push(b, 6)
b = push(b, 4)
b = push(b, 2)

# Find the intersection two linked lists
intersect = sortedIntersect(a, b)

print("\n Linked list containing " + "common items of a & b");
printList(intersect)


"""
Use Hashing

    Time Complexity: O(n)
    Space complexity: O(n) since auxiliary space is being used
    
"""
# Python3 program to implement above approach

# Link list node
class Node:
	def __init__(self):
		self.data = 0
		self.next = None


def printList(node):
	while (node != None):
		print(node.data, end=" ")
		node = node.next;


def append(head_ref, new_data):

	new_node = Node()

	new_node.data = new_data;

	new_node.next = head_ref;

	head_ref = new_node;
	return head_ref;


def intersection(tmp1,tmp2,k):
	res = [0]*k

	set1 = set()
	while (tmp1 != None):
		set1.add(tmp1.data)
		tmp1 = tmp1.next

	cnt = 0
	while (tmp2 != None):
		if tmp2.data in set1:
			res[cnt] = tmp2.data;
			cnt += 1
	
		tmp2 = tmp2.next
	
	return res

def printList(node):
	while (node != None):
		print(node.data, end=" ")
		node = node.next;		


# Driver code

# Start with the empty lists
ll = None
ll1 = None
		
ll = append(ll , 7)
ll = append(ll , 6)
ll = append(ll , 5)
ll = append(ll , 4)
ll = append(ll , 3)
ll = append(ll , 2)
ll = append(ll , 1)
ll = append(ll , 0)
		
ll1 = append(ll1 , 7)
ll1 = append(ll1 , 6)
ll1 = append(ll1 , 5)
ll1 = append(ll1 , 4)
ll1 = append(ll1 , 3)
ll1 = append(ll1 , 12)
ll1 = append(ll1 , 0)
ll1 = append(ll1 , 9)


arr = intersection(ll , ll1 , 6)

for i in range(6):
    print(arr[i])



print("\n my tests \n")
from generic_singly_linked_list import generic_singly_linked_list
class my_tests(generic_singly_linked_list):
    def __init__(self) -> None:
        super().__init__()

    def check_ll_intersection(self,head_one, head_two):
        dic =dict()
        res=[]
        curr_one =head_one

        while(curr_one):
            dic[curr_one.data]=True
            curr_one =curr_one.next

        
        curr_two =head_two
        
        while(curr_two):
            if curr_two.data in dic:
                res.append(curr_two.data)
            curr_two=curr_two.next
            

        return res

first_ll =my_tests()
first_ll.insert_start(6)
first_ll.insert_start(4)
first_ll.insert_start(3)
first_ll.insert_start(2)
first_ll.insert_start(1)


sec_ll =my_tests()
sec_ll.insert_start(8)
sec_ll.insert_start(6)
sec_ll.insert_start(4)
sec_ll.insert_start(2)


print("Expected:, Actual: ", first_ll.check_ll_intersection(first_ll.head, sec_ll.head))

