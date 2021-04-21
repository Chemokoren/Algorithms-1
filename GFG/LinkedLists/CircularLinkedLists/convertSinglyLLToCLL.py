"""
program to convert a singly linked list into a circular linked list
"""
import sys

# LL Node
class Node:
    def __init__(self,data):
        self.data =data
        self.next =None

def push(head, data):
    if not head:
        return Node(data)

    # Allocate dynamic memory for newNode & assign the data into newNode
    newNode =Node(data)

    #newNode.next assign the address of head node.
    newNode.next =head

    # newNode become the headNode.
    head =newNode
    return head

# Function that convert singly linked list into a circular linked list
def circular(head):
    # declare a node variable start and assign head node into start node
    start = head

    # check that while head.next not equal to null then head points to next node
    while(head.next is not None):
        head =head.next

    # if head.next points to null then assign start to head.next node
    head.next =start
    return start

# function that display the elements of a circular linked list
def displayList(node):
    start =node
    while(node.next is not start):
        print("{} ".format(node.data), end="")
        node =node.next

    # Display the last node of circular linked list.
    print("{} ".format(node.data), end="")

# Driver Code
if __name__=='__main__':
    # start with empty list
    head =None

    # using push() function to convert singly linked list
    head =push(head, 15)
    head =push(head, 14)
    head =push(head, 13)
    head =push(head, 22)
    head =push(head, 17)

    # call the circular_list function that converts singly LL to a circular LL

    circular(head)
    print("Display List After:")
    displayList(head)

