"""

Convert a Binary Tree to a Circular Doubly Linked List

Given a Binary Tree, convert it to a circular doubly linked list(in-place).
- The left and right pointers in nodes are to be used as previous and next pointers 
respectively in converted circular linked list
- The order of nodes in the list must be the same as inorder for the given binary tree
- The first node of inorder traversal must be the head node of the circular list.

Binary Tree to CDLL

The idea can be described using the below steps.
1. Write a general-purpose function that concatenates two given circular doubly lists
2. Now traverse the given tree
    1. Recursively convert left subtree to a Circular DLL. Let the converted list be 
    leftList
    2. Recursively convert right subtree to a circular DLL. Let the converted list be
     rightList
    3. Make a circular linked list of root of the tree, make left and right of root to 
    point to itself.
    4. Concatenate leftList with the list of single root node.
    5. Concatenate the list produced in the step above (d) with rightList

    Not ethat the above code traverses the tree in Postorder fashion. we can traverse in an 
    inorder fashion also. We can first concatenate left subtree and root, then recur for the
    right subtree and concatenate the result with left-root concatenation.

    How to Concatenate two circular DLLs?
    - Get the last node of the left list. Retrieving the last node is an O(1) operation
    since the prev pointer of the head points to the last node of the list.
    - Connect it with the first node of the right list
    - Get the last node of the second list
    - Connect it with the head of the list

TIme Complexity: O(N) 

As every node is visited at most once.

Auxiliary space: O(log N)

The extra space is used in recursion call stack which can grow upto a maximum size of logN 
as it is a binary tree.

"""
class newNode:

    def __init__(self, data):
        self.data = data
        self.left = self.right = None

# A function that appends rightList at the end of leftList
def concatenate(leftList, rightList):
    # if either of the list is empty then return the other list
    if(leftList == None):
        return rightList
    if(rightList == None):
        return leftList

    # Store the last Node of left List
    leftLast = leftList.left

    # store the last Node of right List
    rightLast = rightList.left

    # connect the last node of Left List with the first Node of the right List
    leftLast.right = rightList
    rightList.left = leftLast

    # left of first node points to the last node in the list
    leftList.left = rightLast

    # Right of last node refers to the first node of the list
    rightLast.right = leftList

    return leftList

# Function converts a tree to a circular linked list and then returns the head of LL
def bTreeToCList(root):
    if(root == None):
        return None

    # recursively convert left and right subtrees
    left = bTreeToCList(root.left)
    right = bTreeToCList(root.right)

    # Make a circular linked list of single node(or root). To do so, make the right and 
    # left pointers of this  node to point to itself
    root.left = root.right =root

    '''
    Step 1
    - Concatenate the left list with the list with single node, i.e., current node
    Step 2
    - Concatenate the returned list with the right list
    '''
    return concatenate(concatenate(left, root), right)

# display circular link list
def displayCList(head):
    print("Circular Linked List is: ")
    itr = head
    first =1
    while(head != itr or first):
        print(itr.data, end=" ")
        itr = itr.right
        first = 0
    print()

if __name__ == '__main__':
    root = newNode(10)
    root.left = newNode(12)
    root.right = newNode(15)
    root.left.left = newNode(25)
    root.left.right = newNode(30)
    root.right.left = newNode(36)
 
    head = bTreeToCList(root)
    displayCList(head)

'''
            10
           /  \
         12    15
        /  \   /
       25   30 36        

'''
# 25 12 30 10 36 15 - inorder traversal

print("\n Another approach \n")
"""
Another approach

- Uses the idea of converting a given Binary Tree to Doubly Link List and then converting
this Doubly Linked List to a Circular Linked List

TIme Complexity: O(N)

As every node is visited at most once.

Auxiliary space: O(log N)

The extra space is used in recursive function call stack which can grow upto a maximum 
size of logN.


"""
#  A binary tree node has - data , left and right pointers 
class Node:
    
    def __init__(self, data) -> None:
        self.data =data
        self.left = None
        self.right = None



'''

A utility function that converts given binary tree to
a doubly linked list
root --> the root of the binary tree
head --> head of the created doubly linked list

'''
def BTree2DoublyLinkedList(root, head):
    
    # Base case
    if (root == None):
        return root

	# Initialize previously visited node as None. This is
	# static so that the same value is accessible in all recursive calls
    prev = None

	# Recursively convert left subtree
    BTree2DoublyLinkedList(root.left, head)
    
    # Now convert this node
    if (prev == None):
        head = root
    else:
        root.left = prev
        prev.right = root
        
    prev = root

	# Finally convert right subtree
    BTree2DoublyLinkedList(root.right, head)
    return prev


'''
A simple recursive function to convert a given Binary tree to
Circular Doubly Linked List using a utility function
root --> Root of Binary Tree
tail --> Pointer to tail node of created circular doubly linked list

'''
def BTree2CircularDoublyLinkedList(root):
	head = None
	tail = BTree2DoublyLinkedList(root, head)
	
    # make the changes to convert a DLL to CDLL
	tail.right = head
	head.left  = tail
	# return the head of the created CDLL
	return head


'''
Helper function that allocates a new node with the
given data and None to left and right pointers.
'''
def newNode(data):
	new_node = Node(data)
	new_node.left = new_node.right = None
	return new_node

''' Function to print nodes in a given circular doubly linked list '''
def printList(head):
    
    if(head==None):
        return
    ptr = head
    
    while(ptr != head):
        print(ptr.data)
        ptr = ptr.right
    print()


root        = newNode(10)
root.left   = newNode(12)
root.right	= newNode(15)
root.left.left = newNode(25)
root.left.right = newNode(30)
root.right.left = newNode(36)

# convert to DLL
head = BTree2CircularDoublyLinkedList(root)

#Print the converted list
printList(head)

# 25 12 30 10 36 15 