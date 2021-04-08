"""
implementation to reverse a doubly linked list in groups of given size

Original list: 10 8 4 2
Modified list: 8 10 2 4

"""

# LL node
class Node:
    def __init__(self,data):
        self.data =data
        self.next =None
        self.prev =None

# Function to get a new node
def getNode(data):
    # allocate space
    new_node =Node(0)

    # put in the data
    new_node.data =data
    new_node.next =new_node.prev =None
    return new_node

# function to insert a node at the beginning of the DLL
def push(head_ref, new_node):
    # since we are adding at the beginning, prev is always None
    new_node.prev =None

    # link the old list of the new node
    new_node.next =head_ref

    # change prev of head node to new node
    if(head_ref != None):
        head_ref.prev =new_node

    # move the head to point to the new node
    head_ref =new_node
    return head_ref

# function to reverse a DLL in groups of given size

def revListInGroupOfGivenSize(head, k):

    current =head
    next = None
    newHead = None
    count = 0

    # reversing the current group of k or less than k nodes by adding them
    # at the beginning of list 'newHead'

    while(current != None and count < k):
        next =current.next
        newHead = push(newHead, current)
        current =next
        count = count + 1

    # if next group exists then make the desired adjustments in the link
    if(next !=None):
        head.next =revListInGroupOfGivenSize(next, k)
        head.next.prev =head

    # pointer to the new head of the reversed group
    return newHead


# Function to print nodes in a
# given doubly linked list
def printList(head):
    while (head != None):
        print(head.data, end=" ")
        head = head.next


# Driver program

# Start with the empty list
head = None

# Create doubly linked: 10<.8<.4<.2
head = push(head, getNode(2))
head = push(head, getNode(4))
head = push(head, getNode(8))
head = push(head, getNode(10))

k = 2

print("Original list: ")
printList(head)

# Reverse doubly linked list in groups of size 'k'
head = revListInGroupOfGivenSize(head, k)

# New expected doubly linked: 8<.10<.2<.4
print("\nModified list: ")
printList(head)

