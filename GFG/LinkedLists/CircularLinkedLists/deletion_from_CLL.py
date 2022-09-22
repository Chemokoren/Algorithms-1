"""
Python program to delete a given key from LL

Case 1: List is empty. 

    If the list is empty we will simply return.

Case 2:List is not empty  

    If the list is not empty then we define two pointers curr and prev and initialize 
    the pointer curr with the head node.
    Traverse the list using curr to find the node to be deleted and before moving to 
    curr to the next node, every time set prev = curr.
    If the node is found, check if it is the only node in the list. If yes, set 
    head = NULL and free(curr).
    If the list has more than one node, check if it is the first node of the list. 
    Condition to check this( curr == head). If yes, then move prev until it reaches 
    the last node. After prev reaches the last node, set 
    head = head -> next and prev -> next = head. Delete curr.
    If curr is not the first node, we check if it is the last node in the list. 
    Condition to check this is (curr -> next == head).
    If curr is the last node. Set prev -> next = head and delete the node curr by 
    free(curr).
    If the node to be deleted is neither the first node nor the last node, then set 
    prev -> next = curr -> next and delete curr.

"""

# Node of a DLL
class Node:
    def __init__(self, next =None, data =None):
        self.next =next
        self.data =data

# Function to insert a node at the beginning of a CLL
def push(head_ref, data):
    # create a new node and make head as next of it
    ptr1 =Node()
    ptr1.data = data
    ptr1.next = head_ref

    # if linked list is not None then set the next of last node
    if(head_ref !=None):
        #find the node before head and update next of it
        temp =head_ref
        while(temp.next !=head_ref):
            temp =temp.next
        temp.next =ptr1
    else:
        ptr1.next =ptr1 # for the first node

    head_ref =ptr1
    return head_ref

# Function to print nodes in a given circular linked list
def printList(head):
    temp =head
    if (head != None):
        while(True):
            print(temp.data, end=" ")
            temp =temp.next
            if(temp == head):
                break

    print()

# function to delete a given node from the list
def deleteNode(head, key):
    # if linked list is empty
    if (head == None):
        return

    # if the list contains only a single node
    if(head.data ==key and head.next == head):
        head =None

    last =head =None
    d =None
    # if head is to be deleted
    if(head.data == key):

        # FInd the last node of the list

        while(last.next !=head):
            last =last.next
        # point last node to the next of head i.e the second node of the list
        last.next =head.next
        head =last.next

    # Either the node to be deleted is not found or the end of list is not reached
    while(last.next != head and last.next.data != key):
        last =last.next

    # if node to be deleted was found
    if (last.next.data == key):
        d = last.next
        last.next = d.next
    else:
        print("no such key b")

    return head


# Initialize lists as empty
head = None

# Created linked list will be 2.5.7.8.10
head = push(head, 2)
head = push(head, 5)
head = push(head, 7)
head = push(head, 8)
head = push(head, 10)

print("List Before Deletion: ")
printList(head)

head = deleteNode(head, 7)

print("List After Deletion: ")
printList(head)