"""
Given a Circular linked list exchange the first and the last node.
The task should be done with only one extra node, you can not declare more than one extra node
and also you are not allowed to declare any other temporary variable.
Note: Extra node means need of a node to traverse a list.
"""
# program to exhange first and last node in CLL
import math
class Node:
    def __init__(self, data):
        self.data =data
        self.next =None

def addToEmpty(head, data):
    # This function is only for empty list
    if(head !=None):
        return head
    # Creating a node dynamically.
    temp =Node(data)

    # Assigning the data.
    temp = Node(data)

    # Assigning the data.
    temp.data =data
    head =temp

    # Creating the link
    head.next =head
    return head
def addBegin(head, data):
    if(head ==None):
        return addToEmpty(head, data)
    temp =Node(data)
    temp.data =data
    temp.next =head.next
    head.next =temp

    return head

# function for traversing the list
def traverse(head):
    # if list is empty, return
    if(head == None):
        print("List is empty.")
        return
    # Pointing to first Node of the list.
    p =head
    print(p.data, end=" ")
    p =p.next

    # Traversing the list.
    while(p !=head ):
        print(p.data, end=" ")
        p = p.next

def exchangeNodes(head):
    # case 1: LL either empty or has a single node
    if head == None or head.next ==head:
        return head
    # case 2: LL has 2 nodes
    elif head.next.next ==head:
        head =head.next
        return head
    # case 3: LL has multiple nodes
    else:
        prev =None
        curr =head
        temp =head
        # finding last and second last nodes in LL
        while curr.next != head:
            prev =curr
            curr =curr.next
        #  point the last node to second node of the list
        curr.next =temp.next
        # point the second last node to first node
        prev.next =temp
        # point the end of node to start (make LL circular)
        temp.next =curr
        # mark the starting of LL
        head =curr
        return head

# Driver Code
if __name__=='__main__':
    head =None
    head =addToEmpty(head, 6)
    for x in range(5, 0, -1):
        head =addBegin(head, x)
    print("List Before: ", end="")
    traverse(head)
    print()

    print("List After: ", end="")
    head =exchangeNodes(head)
    traverse(head)
