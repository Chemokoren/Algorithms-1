"""
program to convert a singly linked list into a circular linked list
"""
from generic_circular_linked_list import Circular_Linked_list

# LL Node
class Node:
    def __init__(self,data):
        self.data =data
        self.next =None

class convert_singly_ll_to_circular_ll(Circular_Linked_list):
    def __init__(self) -> None:
        super().__init__()

    def push_singly_list(self,data):
        node = self.head
        new_node =Node(data)
        if not node:
            self.head = new_node
            return self.head
        #newNode.next assign the address of head node.
        new_node.next =self.head

        # newNode become the headNode.
        self.head =new_node
        return self.head

    def print_singly_list(self):
            node = self.head

            while(node):
                print(node.data, end="-->")
                node =node.next
            print()

    def circular(self, node):
        # declare a node variable start and assign head node into start node
        start = node

        # check that while head.next not equal to null then head points to next node
        while(node.next is not None):
            node =node.next

        # if head.next points to null then assign start to head.next node
        node.next =start
        return start

    def print_circular_ll(self, node):
        start =node
        while(node.next is not start):
            print("{} ".format(node.data), end="--")
            node =node.next

        # Display the last node of circular linked list.
        print("{} ".format(node.data), end="")

    
    def push(self, head, data):
        if not head:
            return Node(data)

        # Allocate dynamic memory for newNode & assign the data into newNode
        newNode =Node(data)

        #newNode.next assign the address of head node.
        newNode.next =head

        # newNode become the headNode.
        head =newNode
        return head



# Driver Code
if __name__=='__main__':
    # start with empty list
    head =None
    
    ll = convert_singly_ll_to_circular_ll()

    # using push() function to convert singly linked list
    head =ll.push(head, 15)
    head =ll.push(head, 14)
    head =ll.push(head, 13)
    head =ll.push(head, 22)
    head =ll.push(head, 17)

    # call the circular_list function that converts singly LL to a circular LL
    ll.circular(head)
    print("Display List After:")
    ll.print_circular_ll(head)

    print("\n Different Approach \n")
    scll = convert_singly_ll_to_circular_ll()
    scll.push_singly_list(15)
    scll.push_singly_list(14)
    scll.push_singly_list(13)
    scll.push_singly_list(22)
    scll.push_singly_list(17)
    scll.print_singly_list()
    scll.circular(scll.head)
    scll.print_circular_ll(scll.head)
