"""
What is a Linked List

Like arrays, Linked List is a linear data structure. Unlike arrays, linked list elements are not 
stored at a contiguous location. The elements are linked using pointers. They include a series of
connected nodes. Here, each node stores the data and the address of the next node.

Why Linked List? 

Arrays can be used to store linear data of similar types, but arrays have the following limitations:

    - The size of the arrays is fixed: So we must know the upper limit on the number of elements in 
    advance. Also, generally, the allocated memory is equal to the upper limit irrespective of the 
    usage. 
    - Insertion of a new element / Deletion of a existing element in an array of elements is expensive: 
    The room has to be created for the new elements and to create room existing elements have to be 
    shifted but in Linked list if we have the head node then we can traverse to any node through it and 
    insert new node at the required position.

Advantages of Linked Lists over arrays:

    Dynamic Array.
    Ease of Insertion/Deletion.

Drawbacks of Linked Lists: 

    - Random access is not allowed. We have to access elements sequentially starting from the first 
    node(head node). So we cannot do a binary search with linked lists efficiently with its default 
    implementation. 
    - Extra memory space for a pointer is required with each element of the list. 
    - Not cache friendly. Since array elements are contiguous locations, there is locality of 
    reference which is not there in case of linked lists.

Types of Linked Lists:

    Simple Linked List – one can move or traverse the linked list in only one direction
    Doubly Linked List – one can move or traverse the linked list in both directions 
    (Forward and Backward)
    Circular Linked List – the last node of the linked list contains the link of the first/head node 
    of the linked list in its next pointer and the first/head node contains the link of the last 
    node of the linked list in its prev pointer

Basic operations on Linked Lists:

    Deletion
    Insertion
    Search
    Display

Representation of Linked Lists: 

A linked list is represented by a pointer to the first node of the linked list. The first node is 
called the head of the linked list. If the linked list is empty, then the value of the head points 
to NULL. 

Each node in a list consists of at least two parts: 

    A Data Item (we can store integer, strings, or any type of data).
    Pointer (Or Reference) to the next node (connects one node to another) or An address of another 
    node
The LinkedList class contains a reference of Node class type. 

Traversal of a LL
- We traverse the created list and print the data of each node.

Time Complexity	    Worst Case	    Average Case
Search	                O(n)	        O(n)
Insert	                O(1)	        O(1)
Deletion	            O(1)	        O(1)

Auxiliary Space: O(N)

"""

class Node:

    # function to initialize the node object 
    def __init__(self, data):
        self.data = data 
        self.next = None

    
# create a LL with 3 nodes
class LinkedList:
    # function to initialize the linked list object
    def __init__(self) -> None:
        self.head = None

    def print_list(self):
        start = self.head
        while start is not None:
            print(start.data, end="-->")
            start =start.next
        print()

if __name__=='__main__':
    ll = LinkedList()
    ll.head =Node(1)
    second = Node(2)
    third =Node(3)

    # link first node with second
    ll.head.next=second 

    # link second node with the third node
    second.next =third
    ll.print_list()
