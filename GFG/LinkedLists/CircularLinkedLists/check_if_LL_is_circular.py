"""
A linked list is called circular if it is not NULL - terminated and all nodes
are connected in the form of a cycle.
An empty linked list is considered as circular
Note: This problem is different from cycle detection problem - here all nodes have
to be part of cycle

Store the head of the linked list and traverse it. If we reach NULL, linked list is not circular.
But if we reach the head again, then the linked list is circular
"""

from generic_circular_linked_list import Circular_Linked_list

# program to check if a linked list is circular

# Node class
class Node:
    # Function to initialize the node object
    def __init__(self,data):
        self.data =data # assign data
        self.next =None # Initialize next as null

# Linked List class contains a Node object
class LinkedList(Circular_Linked_list):

    def __init__(self) -> None:
        super().__init__()

    def Circular(self,head):
        if head == None:
            return True

        # Next of head
        node = head.next
        i = 0

        # This loop would stop in  both cases (1) If Circular (2) Not Circular
        while((node is not None) and (node is not head)):
            i = i + 1
            node =node.next
        return (node ==head)

# Driver Program
if __name__ =='__main__':
    llist = LinkedList()
    llist.head =Node(1)
    second =Node(2)
    third =Node(3)
    fourth =Node(4)

    llist.head.next =second
    second.next = third
    third.next =fourth

    if(llist.Circular(llist.head)):
        print('Yes')
    else:
        print('No')

    fourth.next =llist.head
    if(llist.Circular(llist.head)):
        print('Yes')
    else:
        print('No')


