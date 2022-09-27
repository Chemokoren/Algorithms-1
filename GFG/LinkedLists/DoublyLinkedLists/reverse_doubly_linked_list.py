"""
function to reverse a doubly-linked list
swap next and prev pointers for all the nodes
change prev of the head node
change head pointer

"""
from generic_doubly_linked_list import generic_doubly_linked_list



class DoublyLinkedList(generic_doubly_linked_list):

    def __init__(self):
        super().__init__()

    # method to reverse a doubly-linked list
    # Time Complexity: O(N), where N denotes the number of nodes in the doubly linked list.
    # Auxiliary Space: O(1)
    def reverse(self):
        temp = None
        current = self.head

        # swap all the next and prev of all the nodes in a doubly linked list
        while current is not None:
            temp = current.prev
            current.prev =current.next
            current.next =temp
            current = current.prev

        # check for cases like an empty list and the list with only one node before 
        # changing the head
        if temp is not None:
            self.head =temp.prev

    # method to reverse a Doubly-Linked List using Stacks
    # Time Complexity: O(N) | Auxiliary Space: O(N)
    def reverseUsingStacks(self):

        stack =[]
        temp = self.head
        # add all the elements in the stack in a sequence to the stack
        while temp is not None:
            stack.append(temp.data)
            temp = temp.next

        new_node = self.head
        # popped all the elements and the added in the linked list, in a reversed order.
        while new_node is not None:
            new_node.data = stack.pop()
            new_node = new_node.next
        


dll = DoublyLinkedList()
dll.push(2)
dll.push(4)
dll.push(8)
dll.push(10)

print("original linked list")
dll.printList(dll.head)

# reverse a doubly-linked list
# dll.reverse()
dll.reverseUsingStacks()

print(" reversed linked list")
dll.printList(dll.head)





