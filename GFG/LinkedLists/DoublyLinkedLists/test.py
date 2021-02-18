"""
function to reverse a doubly-linked list
swap next and prev pointers for all the nodes
change prev of the head node
change head pointer
"""
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    """
    method to reverse a Doubly-Linked List using Stacks
    """
    def reverseUsingStacks(self):

        stack =[]
        temp = self.head
        # add all the elements in the stack in a sequence to the stack
        while temp is not None:
            stack.append(temp.data)
            temp = temp.next

        # popped all the elements and the added in the linked list, in a reversed order.
        temp = self.head
        while temp is not None:
            temp.data = stack.pop()
            temp = temp.next



    """
    method to push a new item before the head
    """
    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next =self.head

        if self.head is not None:
            self.head.prev =new_node

        self.head = new_node

    """
    method to traverse the doubly-linked list and print every node in the list
    """
    def printList(self, node):
        while(node is not None):
            print(node.data)
            node =node. next


# driver program for the doubly-linked list
dll = DoublyLinkedList()
dll.push(2)
dll.push(4)
dll.push(8)
dll.push(10)

print("original doubly-linked list")
dll.printList(dll.head)

# reverse a doubly-linked list
dll.reverseUsingStacks()

print(" reversed doubly-linked list")
dll.printList(dll.head)





