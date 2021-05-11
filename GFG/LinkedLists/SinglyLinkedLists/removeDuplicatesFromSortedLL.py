"""
program to remove duplicate nodes from a sorted LL
"""
class Node:
    def __init__(self, data):
        self.data =data
        self.next =None

class LinkedList:
    def __init__(self):
        self.head =None
    # insert node at the beginning
    def push(self,new_data):
        new_node =Node(new_data)
        new_node.next =self.head
        self.head=new_node

    # Given a reference to the head of a list and a key, delete the first
    # occurence of key in LL
    def deleteNode(self, key):
        temp =self.head

        # If head node itself holds the key to be deleted
        if(temp is not None):
            if(temp.data == key):
                self.head =temp.next
                temp =None
                return

        # search for the key to be deleted, keep track of the previous node
        # as we need to change 'prev.next'
        while(temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        # if key was not present in LL
        if(temp == None):
            return

        # unlink the node from LL
        prev.next = temp.next
        temp =None
    def printList(self):
        temp =self.head
        while(temp):
            print(temp.data, end=" ")
            temp =temp.next

    # This function removes duplicates from a sorted list
    def removeDuplicates(self):
        temp =self.head
        if temp is None:
            return
        while temp.next is not None:
            if temp.data == temp.next.data:
                new = temp.next.next
                temp.next =None
                temp.next =new
            else:
                temp =temp.next
        return self.head

llist = LinkedList()

llist.push(20)
llist.push(13)
llist.push(13)
llist.push(11)
llist.push(11)
llist.push(11)
print("Created Linked List: ")
llist.printList()
print()
print("Linked List after removing",
      "duplicate elements:")
llist.removeDuplicates()
llist.printList()

"""

"""

import math

class Node:
    def __init__(self,data):
        self.data =data
        self.next =None

'''
Recursive approach to remove duplicates in LL -not complete
'''
def removeDuplicatesRecursive(head):

    # do nothing if the list is empty
    if(head == None):
        return
    # Traverse the list till last node
    if(head.next != None):

        # compare head node with next node
        if(head.data == head.next.data):
            # The sequence of steps is important
            # to_free pointer stores the next of head
            # pointer which is to be deleted
            to_free = head.next
            head.next =head.next.next

            # free(to_free)
            removeDuplicatesRecursive(head)
        else:
            removeDuplicatesRecursive(head.next)
    return head

"""
Another Approach: Create a pointer that will point towards the first occurrence of 
every element and another pointer temp which will iterate to every element and when 
the value of the previous pointer is not equal to the temp pointer, we will set the 
pointer of the previous pointer to the first occurrence of another node.
"""
# The function removes duplicates from the given LL
def removeDuplicates(head):
    # do nothing if the list consist of one element or empty
    if (head == None and head.next == None):
        return
    # construct a pointer pointing towards the head
    current = head

    # Initialize a while loop till the second last node of the LL
    while (current.next):
        # If the data of the current and next node is equal, we will skip the node
        # between them
        if current.data == current.next.data:
            current.next = current.next.next

        # If the data of current and next node is different move the pointer to the next node
        else:
            current = current.next
    return


    # UTILITY FUNCTIONS
# Function to insert a node at the
# beginging of the linked list
def push(head_ref, new_data):
    # allocate node
    new_node = Node(new_data)

    # put in the data
    new_node.data = new_data

    # link the old list off the new node
    new_node.next = head_ref

    # move the head to point to the new node
    head_ref = new_node
    return head_ref


# Function to print nodes in a given linked list
def printList(node):
    while (node != None):
        print(node.data, end=" ")
        node = node.next


# Driver code
if __name__ == '__main__':
    # Start with the empty list
    head = None

    # Let us create a sorted linked list
    # to test the functions
    # Created linked list will be 11.11.11.13.13.20
    head = push(head, 11)
    head = push(head, 20)
    head = push(head, 14)
    head = push(head, 15)
    head = push(head, 13)
    head = push(head, 13)
    head = push(head, 11)
    head = push(head, 11)
    head = push(head, 11)

    print("\nLinked list before duplicate removal ",
          end="")
    printList(head)

    # Remove duplicates from linked list
    removeDuplicatesRecursive(head)

    print("\nLinked list after duplicate removal ",
          end="")
    printList(head)


'''
 Another Approach: Using Maps

The idea is to push all the values in a map and printing its keys.
'''
"""
// Java program for the above approach
import java.io.*;
import java.util.*;

class Node
{
	int data;
	Node next;
	Node()
	{
		data = 0;
		next = null;
	}
}
class GFG
{
	
	/* Function to insert a node at
the beginging of the linked
* list */
	static Node push(Node head_ref, int new_data)
	{
	
		/* allocate node */
		Node new_node = new Node();
	
		/* put in the data */
		new_node.data = new_data;
		
		/* link the old list off
		the new node */
		new_node.next = (head_ref);
		
		/* move the head to point
		to the new node */
		head_ref = new_node;
		return head_ref;
	}
	
	/* Function to print nodes
	in a given linked list */
	static void printList(Node node)
	{
		while (node != null)
		{
			System.out.print(node.data + " ");
			node = node.next;
		}
	}
	
	// Function to remove duplicates
	static void removeDuplicates(Node head)
	{
		HashMap<Integer, Boolean> track = new HashMap<>();
		Node temp = head;
		
		while(temp != null)
		{
			if(!track.containsKey(temp.data))
			{
				System.out.print(temp.data + " ");
			}
			track.put(temp.data , true);
			temp = temp.next;
		}
	}
	
	// Driver Code
	public static void main (String[] args)
	{
		Node head = null;
	
		/* Created linked list will be
		11->11->11->13->13->20 */
		head = push(head, 20);
		head = push(head, 13);
		head = push(head, 13);
		head = push(head, 11);
		head = push(head, 11);
		head = push(head, 11);
		System.out.print("Linked list before duplicate removal ");
		printList(head);
		System.out.print("\nLinked list after duplicate removal ");
		removeDuplicates(head);
	}
}

// This code is contributed by avanitrachhadiya2155

"""

