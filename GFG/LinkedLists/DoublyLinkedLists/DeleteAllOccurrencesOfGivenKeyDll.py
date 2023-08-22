"""
Given a doubly linked list and a key x. The problem is to delete all occurrences
of the given key x from the doubly liinked list

delAllOccurOfGivenKey(head_ref, x)
      if head_ref == NULL
          return
      Initialize current = head_ref
      Declare next
      while current != NULL
           if current->data == x
               next = current->next
               deleteNode(head_ref, current)
               current = next
           else
               current = current->next
"""


# Implementation to delete all occurrences of a given key in a doubly linked list
import math

# a node of the doubly  linked list
class Node:
    def __init__(self,data):
        self.data =data
        self.next =None
        self.prev =None

'''
Function to delete a node in a Doubly Linked List
head_ref --> pointer to head node pointer
del --> pointer to node to be deleted
'''
def deleteNode(head, delete):
#     base case
    if (head ==None or delete == None):
        return None

    # If node to be deleted is head node
    if(head ==delete):
        head =delete.next

#     change next only if node to be deleted
    # is NOT the last node
    if (delete.next !=None ):
        delete.next.prev =delete.prev

    # Change prev only if node to be deleted
    # is NOT the first node
    if (delete.prev !=None):
        delete.prev.next =delete.next

    # finally, free the memory occupied by del
    # free(del)
    delete =None
    return head

# Function to delete all occurrences of the given key 'x'
def deleteAllOccurOfX(head, x):
    # if list is empty
    if (head ==None):
        return

    current =head

    # traverse the list up to the end
    while(current != None):
        #  if node found with the value 'x'
        if(current.data == x):
            # Save current's next node in the pointer 'next'
            next =current.next

            # delete the node pointed by 'current'
            head =deleteNode(head, current)

            # update current
            current =next
        else:
            current =current.next
    return head

# Function to insert a node at the beginning of the Doubly Linked List
def push(head,new_data):
    # allocate node
    new_node = Node(new_data)

    # put in the data
    new_node.data = new_data

    # since we are adding at the beginning,
    #prev is always None
    new_node.prev = None

    # link the old list off the new node
    new_node.next = head

    # change prev of head node to new node
    if (head != None):
        head.prev = new_node

    # move the head to point to the new node
    head = new_node
    return head


# Function to print nodes in a given doubly linked list
def printList(head):
    # iflist is empty
    if(head ==None):
        print("Doubly Linked list empty")

    while(head !=None):
        print(head.data, end=" ")
        head =head.next

# Driver functions
if __name__=='__main__':
    # start with the empty list
    head =None

    # Create the doubly linked list:
    head =push(head, 2)
    head =push(head, 5)
    head =push(head, 2)
    head =push(head, 4)
    head =push(head, 8)
    head =push(head, 10)
    head =push(head, 2)
    head =push(head, 2)

    print("Orginal Doubly linked list:")
    printList(head)

    x =2
    # delete all occurrences of 'x'
    head =deleteAllOccurOfX(head, x)

    print("\nDoubly linked list after deletion of ", x,":")
    printList(head)

