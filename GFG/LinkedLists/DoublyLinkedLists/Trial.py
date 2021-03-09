# program to delete a node in a doubly linked list

# insert items in a dll
# find item in dll
# delete item

# code to initialize a node
class Node:
    def __init__(self, data):
        self.data =data
        self.next =None
        self.prev =None

class DoublyLinkedList:
    def __init__(self):
        self.head =None

    def push(self,node):
        new_node =Node(node)
        # check if dll is empty
        if self.head !=None:
            self.head.prev =new_node
            new_node.next =self.head
        self.head =new_node

    def printDll(self):
        current =self.head
        while current !=None:
            print(current.data)
            current =current.next

    def printDll1(self,head):
        while head !=None:
            print(head.data)
            head =head.next

    def deleteItemInaDoublyLinkedList(self, node):
        current =self.head
        # check if head does not exist and return
        if self.head ==None:
            return
        # check if head is equal to node to be deleted
        if self.head == node:
            self.head =self.head.next
            self.head.prev=None
            return

        # if you hit end of the list
        if current.next == None:
            current.prev =None
            return

        # if head is not the last item, keep traversing till you find the item or reach
        # the end of the list

        while current.next !=None:
            if(current == node):
                node.prev.next =node.next
                node.next.prev=node.prev
            current =current.next





# Driver code

dll =DoublyLinkedList()

dll.push(10)
dll.push(3)
dll.push(1)
dll.push(7)
dll.push(5)

dll.printDll()

print("############## item does not exist ##############")
dll.deleteItemInaDoublyLinkedList(20)
dll.printDll()
print("############## item is the head ##############")
dll.deleteItemInaDoublyLinkedList(dll.head)
dll.printDll()
print("############## item is the tail ##############")
dll.deleteItemInaDoublyLinkedList(10)
dll.printDll()

