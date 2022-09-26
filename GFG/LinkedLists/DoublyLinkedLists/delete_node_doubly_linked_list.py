"""
deleting a node in a doubly-linked list

Algorithm:

    Let the node to be deleted be del.
    If node to be deleted is head node, then change the head pointer to next current head.

if headnode == del then
      headnode =  del.nextNode

    Set prev of next to del, if next to del exists.

if del.nextNode != none 
      del.nextNode.previousNode = del.previousNode 

    Set next of previous to del, if previous to del exists.

if del.previousNode != none 
      del.previousNode.nextNode = del.next

"""
# Garbage collection
import gc
from generic_doubly_linked_list import generic_doubly_linked_list


class DoublyLinkedList(generic_doubly_linked_list):

    def __init__(self):
        super().__init__()

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

        # free ,e, occupied by dele

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
        if(head_ref == None or n <= 0):
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
deleteLL.deleteNode(deleteLL.head)
# deleteLL.deleteNode(deleteLL.head.next)

# deleteLL.newDeleteNode(deleteLL.head, 8)
# deleteLL.deleteNodeAtGivenPos(deleteLL.head, 0)

print("print modified Doubly-Linked List: \n")
deleteLL.printList(deleteLL.head)

