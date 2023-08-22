# Program to clone a linked list
# with random pointers

class Node:
    def __init__(self,data):
        self.data=data
        self.next =None
        self.random =None

# Ductionary
class MyDictionary(dict):

    # __init__ function
    def __init__(self):
        super().__init__()
        self =dict()

    # Function to add key:value
    def add(self, key, value):
        # Adding Values to dictionary
        self[key] = value

# Linked list class
class LinkedList:
    # Linked list constructor
    def __init__(self,node):
        self.head =node

    # Method to print the list.
    def __repr__(self):
        temp =self.head
        while temp is not None:
            random =temp.random
            random_data =(random.data if random is not None else -1)
            data = temp.data
            print(
                f"Data-{data}, Random data: {random_data}")
            temp =temp.next
        return "\n"
    # push method to put data always at the head
    # in the linked list
    def push(self,data):
        node =Node(data)
        node.next =self.head
        self.head = node

    # Actual clone method which returns head
    # reference of cloned linked list.
    def clone(self):
        # initialize two references, one
        # with original list's head.

        original =self.head
        clone = None

        # Initialize two references, one
        # with original lis's hea
        mp = MyDictionary()

        # Traverse the original list and
        # make a copy of that
        # in the clone linked list
        while original is not None:
            clone = Node(original.data)
            mp.add(original,clone)
            original =original.next

        # Adjusting the original
        # list reference again
        original =self.head

        # Traversal of original lst again
        # to adjust the next and random
        # references of clone list using hash map.
        while original is not None:
            clone =mp.get(original)
            clone.next=mp.get(original.next)
            clone.random =mp.get(original.random)
            original =original.next

        # Return the head reference of the clone list.
        return LinkedList(self.head)

# Driver code for the progrm

# Pushing data in the linked list.

l =LinkedList(Node(5))
l.push(4)
l.push(3)
l.push(2)
l.push(1)

# Setting up random references.
l.head.random =l.head.next.next
l.head.next.random = l.head.next.next.next
l.head.next.next.random = l.head.next.next.next.next
l.head.next.next.next.random =(l.head.next.next.next.next.next)
l.head.next.next.next.next.random =l.head.next

# Making a clone of the
# original linked list.
clone =l.clone()

# print the original and cloned
# linked lists

print("Original linked list")
print(l)
print("Cloned linked list")
print(clone)

"""

Clone a Linked List with next and Random Pointer

An example of linked list with a random PointerGiven a linked list of size N where each 
node has two links: one pointer points to the next node and the second pointer points to
any node in the list. The task is to create a clone of this linked list in O(N) time.

Note: The pointer pointing to the next node is 'next' pointer and the one pointing to an
arbitrary node is called 'arbit' pointer as it can point to any arbitrary node in the 
linked list.

An example of the linked list is show in the below image:

1 --> 2 --> 3 --> 4 --> 5

arbitrary pointers

1-->3
3-->5
5-->2
4-->3
2-->1

Approach 1: Using extra space

- First create a single linked list with only the 'next' pointer and use a mapping to map
the new nodes to their corresponding nodes in the given linked list. Now, use this mapping
to point the arbitrary node from any node in the newly created list

Follow the steps mentioned below to implement the above idea:
- Create a duplicate (say Y) for each node (say X) and map them with corresponding old 
nodes(say mp, so mp[X] = Y).
- Create the single linked list of the duplicate nodes where each nodes only has the 'next'
pointer.
- Now iterate over the old linked list and do the following:
    a) find the duplicate node mapped with the current one. (i.e., if the current node is
    X then duplicate is mp[x])
    b) make the arbit pointer of the duplicate node pointing to the duplicate of the 
    current->arbit node (i.e., mp[x]->arbit will point to mp[X->arbit]).
- The linked list created in this way is the required linked list


Time Complexity: O(N) 
Auxiliary Space: O(N) 

"""
print("\nApproach 1: Using extra space \n")
class Node:
    
    def __init__(self, x) -> None:
        self.val = x
        self.next = None
        self.arbit = None


# Function to clone the linked list
def cloneLinkedList(head):
    
    # Map to store the mapping of old nodes with new ones
    mp = {}
    temp = None
    nhead = None
    
    # Duplicate of the first node
    
    temp  = head
    nhead = Node(temp.val)
    mp[temp] = nhead

	# Loop to create duplicates of nodes with only next pointer
    
    while (temp.next != None):
        nhead.next = Node(temp.next.val)
        temp = temp.next
        nhead = nhead.next
        mp[temp] = nhead
        
    temp = head
    
    # Loop to clone the arbit pointers
    
    while (temp != None):
        mp[temp].arbit = mp[temp.arbit]
        temp = temp.next
        
    # Return the head of the clone
    return mp[head]


# Function to print the linked list
def printList(head):
    # cout << head->val << "("<< head->arbit->val << ")";
	print(head.val<< head.arbit.val)
	head = head.next
	while (head != None):
        # cout << " -> " << head->val << "(" << head->arbit->val << ")";
		print(" -> ", head.val << head.arbit.val)
		head = head.next
	print()
    

if __name__== "__main__":
    # Creating a linked list with random pointer
	head = Node(1)
	head.next =Node(2)
	head.next.next = Node(3)
	head.next.next.next =Node(4)
	head.next.next.next.next = Node(5)
	head.arbit = head.next.next
	head.next.arbit = head
	head.next.next.arbit = head.next.next.next.next
	head.next.next.next.arbit = head.next.next
	head.next.next.next.next.arbit= head.next

	# Print the original list
	print("The original linked list:\n")
	printList(head)

	# Function call
	sol = cloneLinkedList(head)

	print("The cloned linked list:\n")
	printList(sol)


"""
Approach 2: Using Constant Extra Space

- The idea to solve using extra space is:
Create duplicate of a node and insert it in between that node and the node just next to it.
Now for a node X its duplicate will be X->next and the arbitrary pointer of the duplicate
will point to X->arbit->next[as that is the duplicate of X->arbit]

Follow the steps mentioned below to implement the idea:
- Create the copy of node 1 and insert it between node 1 and node 2 in the original linked 
list, create the copy of node 2 and insert it between 2nd and 3rd node and so on. Add the
copy of N after the Nth node.
- Now copy the arbitrary link in this fashion:
original->next->arbitrary = original->arbitrary->next 
- Now restore the original and copy linked lists in this fashion in a single loop

original->next = original->next->next;
copy->next = copy->next->next;

Make sure that the last element of original->next is NULL

Time Complexity: O(N) 
Auxiliary Space: O(1)
"""


"""
Clone a linked list with next and random pointer in O(1) space

Given a linked list having two pointers in each node. the first one points to the next node
of the list, however, the other pointer is random and can point to any node of the list.
Write a progrm that clones the given list in O(1) space, i.e., without an extra space.

Examples:
Input: Head of the below-linked list

1 --> 2 --> 3--> 4--> 5

Output:
A new linked list indentical to the original list

In this post, we'll be implementing an algorithm that'd require no additional space 

- create the copy of node 1 and insert it between node 1 & node 2 in the original Linked
List, create a copy of 2 and insert it between 2 & 3. continue in this fashion, add the
copy of N after the Nth node.
- Now copy the random link in this fashion.

original->next->random= original->random->next;  /*TRAVERSE TWO NODES*/

- This works because original->next is nothing but a copy of the original and 
original->random->next is nothing but a copy of the random.
- Now restore the original and copy linked lists in this fashion in a single loop.

original->next = original->next->next;
     copy->next = copy->next->next;

- Ensure that original->next is NULL and return cloned list

Time Complexity: O(n) As we are moving through the list thrice, i.e. 3n ,  but in asymptotic
notations we drop the constant terms
Auxiliary Space: O(1) As no extra space is used. The n nodes which are inserted in between 
the nodes was already required to clone the list, so we can say that we did not use any 
extra space.

"""

'''Python program to clone a linked list with next and arbitrary pointers'''
'''Done in O(n) time with O(1) extra space'''
class Node:
	'''Structure of linked list node'''

	def __init__(self, data):
		self.data = data
		self.next = None
		self.random = None

def clone(original_root):
	'''Clone a doubly linked list with random pointer'''
	'''with O(1) extra space'''

	'''Insert additional node after every node of original list'''
	curr = original_root
	while curr != None:
		new = Node(curr.data)
		new.next = curr.next
		curr.next = new
		curr = curr.next.next

	'''Adjust the random pointers of the newly added nodes'''
	curr = original_root
	while curr != None:
		curr.next.random = curr.random.next
		curr = curr.next.next

	'''Detach original and duplicate list from each other'''
	curr = original_root
	dup_root = original_root.next
	while curr.next != None:
		tmp = curr.next
		curr.next = curr.next.next
		curr = tmp

	return dup_root

def print_dlist(root):
	'''Function to print the doubly linked list'''

	curr = root
	while curr != None:
		print('Data =', curr.data, ', Random =', curr.random.data)
		curr = curr.next

####### Driver code #######
'''Create a doubly linked list'''
original_list = Node(1)
original_list.next = Node(2)
original_list.next.next = Node(3)
original_list.next.next.next = Node(4)
original_list.next.next.next.next = Node(5)

'''Set the random pointers'''

# 1's random points to 3
original_list.random = original_list.next.next

# 2's random points to 1
original_list.next.random = original_list

# 3's random points to 5
original_list.next.next.random = original_list.next.next.next.next

# 4's random points to 5
original_list.next.next.next.random = original_list.next.next.next.next

# 5's random points to 2
original_list.next.next.next.next.random = original_list.next

'''Print the original linked list'''
print('Original list:')
print_dlist(original_list)

'''Create a duplicate linked list'''
cloned_list = clone(original_list)

'''Print the duplicate linked list'''
print('\nCloned list:')
print_dlist(cloned_list)

