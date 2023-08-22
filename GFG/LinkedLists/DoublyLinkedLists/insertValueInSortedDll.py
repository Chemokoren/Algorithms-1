# solution 1
# structure of node of doubly linked list
# class Node:
#     def __init__(self,x):
#         self.data =x
#         self.next =None
#         self.prev =None
#
#
# class DoublyLinkedList:
#     def __init__(self):
#         self.head =None
#
#     def push(self,data):
#         _node =Node(data)
#         if self.head is not None:
#             _node.next =self.head
#         self.head =_node
#
#
#
#     def sortDll(self):
#         if(self.head ==None):
#             return
#         current =self.head
#
#         while current.next is not None:
#             index =current.next
#
#             while(index != None):
#                 if current.data > index.data:
#                     temp =index.data
#                     index.data = current.data
#                     current.data =temp
#                 index =index.next
#             current =current.next
#
#     def insertItemInSortedDll(self, node):
#         _node=Node(node)
#         if(self.head == None):
#             self.head =_node
#         current =self.head
#         while current.next is not None:
#             index =current.next
#             while(index !=None):
#                 if current.data >= _node.data: #
#                     # temp = current.next
#                     # _node =current.next.prev
#                     # current.next =_node
#                     # _node.next=temp
#                     # _node.prev =current
#                     _node.next = current
#                 else:
#                     current.next = _node
#                     _node.prev =current
#
#                 index =index.next
#
#             current =current.next
#
#     def printDll(self, node):
#         _node =Node(node)
#         while node is not None:
#             print(node.data)
#             node =node.next

# Driver code
# dll =DoublyLinkedList()
# dll.push(9)
# dll.push(1)
# dll.push(4)
# dll.push(6)
# dll.push(15)
#
# dll.printDll(dll.head)
# print("############### after sorting ####################")
# dll.sortDll()
# dll.printDll(dll.head)
# dll.insertItemInSortedDll(13)
# print("############### insert new value ####################")
# dll.printDll(dll.head)


# solution 2
# implementation to insert
# value in sorted way in a sorted
# doubly linked list

# Python3 implementation to insert
# value in sorted way in a sorted
# doubly linked list

# Node of a doubly linked list
class Node:

    # Constructor to initialize
    # the node object
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:

    # Function to initialize head
    def __init__(self):

        self.head = None

    # Function to create and return a
    # new node of a doubly linked list
    def getNode(self, data):

        return Node(data)

    # Function to insert a new node in
    # sorted way in a sorted doubly linked list
    def sortedInsert(self, data):

        new_node = self.getNode(data)

        # If the list is empty
        if self.head is None:
            self.head = new_node

        # If the node is to be inserted at
        # the beginning of the doubly linked list
        elif self.head.data >= new_node.data:
            new_node.next = self.head
            new_node.next.prev = new_node
            self.head = new_node
        else:
            current = self.head

            # Locate the node after which
            # the new node is to be inserted
            while ((current.next is not None) and
                   (current.next.data < new_node.data)):
                current = current.next

            # Make the appropriate links
            new_node.next = current.next

            # If the new node is not inserted
            # at the end of the list
            if current.next is not None:
                new_node.next.prev = new_node

            current.next = new_node
            new_node.prev = current

    # Function to print the doubly linked list
    def printList(self):

        node = self.head
        while node:
            print(str(node.data), end=" ")
            node = node.next


# Driver code
if __name__ == '__main__':
    # Insert the following nodes
    # in sorted way
    llist = DoublyLinkedList()

    llist.sortedInsert(8)
    llist.sortedInsert(5)
    llist.sortedInsert(3)
    llist.sortedInsert(10)
    llist.sortedInsert(12)

print("Created Doubly Linked List\n")
llist.printList()

llist.sortedInsert(9)

print("\nDoubly Linked List After Sorting\n")
llist.printList()

################## logic for this code ##################
# sortedInsert(head_ref, newNode)
#       if (head_ref == NULL)
#       head_ref = newNode
#
#       else if head_ref->data >= newNode->data
#           newNode->next = head_ref
#       newNode->next->prev = newNode
#       head_ref = newNode
#
#       else
#       Initialize current = head_ref
#       while (current->next != NULL and
#                current->next->data < newNode->data)
#         current = current->next
#
#       newNode->next = current->next
#       if current->next != NULL
#         newNode->next->prev = newNode
#
#           current->next = newNode
#       newNode->prev = current
