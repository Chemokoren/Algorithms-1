"""
A biotonic doubly linked list is a doubly linked list which is first increasing
and then decreasing. However, a strictly increasing or strictly decreasing list
is also a biotonic dll

"""

class Node:
    def __init__(self, next =None, prev =None, data =None):
        self.next =next
        self.prev =prev
        self.data =data
# Function to reverse a dll
def reverse(head_ref):
    temp =None
    current = head_ref

    # swap next and prev for all nodes of doubly linked list
    while( current !=None):
        temp =current.prev
        current.prev =current.next
        current.next =temp
        current = current.prev
    # before changing head, check for cases, like empty list and list with only one node
    if(temp !=None):
        head_ref =temp.prev
        return head_ref

'''
Function to merge two sorted dll
'''
def merge(first, second):
    # if first linked list is empty
    if(first ==None):
        return second
    # if second linked list is empty
    if(second ==None):
        return first
    #pick the samller value
    if(first.data < second.data):
        first.next =merge(first.next, second)
        first.next.prev =first
        first.prev =None
        return first
    else:
        second.next =merge(first, second.next)
        second.next.prev =second
        second.prev =None
        return second
'''
Function to sort a biotonic doubly linked list
'''
def sort( head ):
    if(head ==None or head.next ==None):
        return head
    current =head.next

    while(current !=None):
        # if true, then 'current' is the first node
        # which is smaller than its previous node
        if(current.data < current.prev.data):
            break

        #move to the next node
        current =current.next

    # if true, then list is already sorted
    if (current == None):
        return head

    # split into two lists, one starting with 'head'
    # and other starting with 'current'
    current.prev.next =None
    current.prev =None

    #reverse the list starting with 'current'
    current =reverse(current)

    #merge the two lists and return the
    # final merged doubly linked list
    return merge(head, current)

'''
Function to insert a node at the beginning 
of the Doubly Linked List 
'''
def push( head_ref, new_data):

    # allocate node
    new_node =Node()

    # put in the data
    new_node.data = new_data

    # since we are adding at the beginning,
    # prev is always None
    new_node.prev = None

    # link the old list off the new node
    new_node.next = (head_ref)

    # change prev of head node to new node
    if ((head_ref) != None):
        (head_ref).prev = new_node

    # move the head to point to the new node
    (head_ref) = new_node
    return head_ref


# Function to print nodes in a given doubly
# linked list
def printList( head):

    # if list is empty
    if (head == None):
        print("Doubly Linked list empty")

    while (head != None):

        print(head.data, end= " ")
        head = head.next

# Driver Code

head = None

# Create the doubly linked list:
# 2<.5<.7<.12<.10<.6<.4<.1
head = push(head, 1)
head = push(head, 4)
head = push(head, 6)
head = push(head, 10)
head = push(head, 12)
head = push(head, 7)
head = push(head, 5)
head = push(head, 2)

print("original dll:n")
printList(head)

# sort the biotonic DLL
head = sort(head)

print("\ndll after sorting:")
printList(head)



