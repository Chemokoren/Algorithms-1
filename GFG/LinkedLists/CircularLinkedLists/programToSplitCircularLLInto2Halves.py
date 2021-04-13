"""
program to split circular linked list into two halves
"""

# node structure
class Node:
    # constructor to create a new node
    def __init__(self, data):
        self.data =data
        self.next =None

# class to create a new Circular Linked List
class CircularLinkedList:

    # Constructor to create an empty circular linked list
    def __init__(self):
        self.head =None

    # Function to insert a node at the beginning of a circular linked list
    def push(self, data):
        ptr1 = Node(data)
        temp =self.head

        ptr1.next =self.head

        # if linked list is not None then set the next of last node
        if self.head is not None:
            while(temp.next != self.head):
                temp =temp.next
            temp.next =ptr1

        else:
            ptr1.next =ptr1 # For the first node

        self.head =ptr1

    # Function to print nodes in a given circular linked list
    def printList(self):
        temp =self.head
        if self.head is not None:
            while(True):
                print( "%d" %(temp.data)),
                temp =temp.next
                if(temp == self.head):
                    break

    '''
    Function to split a list (starting with head) into
    two lists. head1 and head2 are the head nodes of the two resultant linked lists
    '''
    def splitList(self, head1, head2):
        slow_ptr =self.head
        fast_ptr = self.head

        if self.head is None:
            return

        # if there are odd nodes in the circular list then
        # fast_ptr->next becomes head and
        # for even nodes fast_ptr->next->next becomes the head

        while(fast_ptr.next != self.head and fast_ptr.next.next !=self.head):
            fast_ptr =fast_ptr.next.next
            slow_ptr =slow_ptr.next

        # if there are even elements in list then move fast_ptr
        if fast_ptr.next.next ==self.head:
            fast_ptr = fast_ptr.next
        # set the head pointer of first half
        head1.head =self.head

        # set the head pointer of second half
        if self.head.next !=self.head:
            head2.head =slow_ptr.next

        # Make second half circular
        fast_ptr.next = slow_ptr.next

        # Make first half circular
        slow_ptr.next =self.head

# Driver program to test above functions

# initialize lists as empty
head =CircularLinkedList()
head1 =CircularLinkedList()
head2 =CircularLinkedList()


head.push(12)
head.push(56)
head.push(2)
head.push(11)

print("Original Circular Linked List")
head.printList()

# Split the list
head.splitList(head1, head2)

print (" \n First Circular Linked List")
head1.printList()

print("\nSecond Circular Linked List")
head2.printList()

