# deleting a node in a doubly-linked list

# Garbage collection
import gc

class Node:
    # Constructor for the new node
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    # empty constructor for doubly-linked list
    def __init__(self):
        self.head = None

    """
    function to delete a node in a doubly-linked list
    head_ref = head node pointer
    dele = pointer to node to be deleted
    """
    def deleteNode(self, dele):
        # base case when head is empty or node to delete is empty
        if self.head is None or dele is None:
            return

        # if node to be deleted is equal to the current head node
        if self.head == dele:
            self.head =dele.next

        # if the node that is to be deleted is NOT the last, then change the next only
        if dele.next is not None:
            dele.next.prev = dele.prev

        # if the node that is to be delete is NOT the first, then change prev only
        if dele.prev is not None:
            dele.prev.next =dele.next

        # free ,e,pru occupied by dele

        gc.collect()


    def newDeleteNode(self, head_ref,del_):
        # base case
        if (head_ref ==None or del_ ==None):
            return
        # if node to be deleted is head node
        if(head_ref ==del_):
            head_ref =del_.next

        # change next only if node to be deleted is NOT the last node
        if (del_.next !=None ):
            del_.next.prev =del_.prev

        # change prev only if node to be deleted is NOT the first node
        if(del_.prev !=None):
            del_.prev.next =del_.next

        return head_ref


    # Function to delete the node at the given position
    # in the doubly linked list
    def deleteNodeAtGivenPos(self, head_ref, n):
        # if list is None or invalid position is given
        if(head_ref ==None or n <= 0):
            return
        current =head_ref
        i = 1

        # if 'n' is greater than the number of nodes
        # in the doubly linked list
        if(current ==None):
            return
        # delete the node pointed to by 'current'
        self.newDeleteNode(head_ref, current)

        return head_ref

        # code to insert a new node in front of the list given an integer and a reference to the head of a list
    def push(self, new_data):
        # allocate a node and put data in the node
        new_node = Node(new_data)

        # make previous None (already None), and next of new node as head
        new_node.next = self.head

        # change prev of the head node to the new_node
        if self.head is not None:
            self.head.prev =new_node

        # alter the prev of the former head node to new_node
        if self.head is not None:
            self.head.prev = new_node

        # make the new node the current head
        self.head = new_node

    # given the start node print the nodes as long as we don't get to null
    def printList(self, node):
        while(node is not None):
            print(node.data),
            node = node.next

# program to test deleting a node in a doubly linked list
deleteLL = DoublyLinkedList()

#create a doubly linked list with the following items 10<->8<->4<->2
deleteLL.push(2)
deleteLL.push(4)
deleteLL.push(8)
deleteLL.push(10)

print("original Doubly Linked List: \n")
deleteLL.printList(deleteLL.head)

# delete nodes from doubly linked list
# deleteLL.deleteNode(deleteLL.head)
# deleteLL.deleteNode(deleteLL.head.next)

deleteLL.newDeleteNode(deleteLL.head, 8)

print("print modified Doubly-Linked List: \n")
deleteLL.printList(deleteLL.head)

