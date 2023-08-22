class Node:
    def __init__(self,data):
        self.data =data
        self.next =None
        self.prev =None

class DoublyLinkedList:
    def __init__(self):
        self.head =None

    def push(self, node):
        new_node =Node(node)
        if self.head is not None:
            new_node.next =self.head
            new_node.prev =None
        self.head =new_node


    def doubleListPrint(self,node):
        while node is not None:
            print(node.data)
            node =node.next

    def swapKthValueFromBeginningWithEnd(self,node,kth_node):
        while node is None:
            if node ==kth_node:
                pass

            node =node.next
        pass

    def getLastNode(self,node):
        while node.next is not None:
            node =node.next
        return node.data

    def swap_linked_list(self):
        if self.head is None:
            print("the list is empty")
            return
        p =self.head
        q =p.next
        p.next=None
        p.prev =q
        while q is not None:
            q.prev =q.next
            q.next =p
            p =q
            q =q.prev
        self.head =p




dll =DoublyLinkedList()
dll.push(4)
dll.push(3)
dll.push(2)
dll.push(1)
dll.doubleListPrint(dll.head)

print("######## Last Node ###########")

print(dll.getLastNode(dll.head))

print("######## Reverse Linked List ###########")
dll.doubleListPrint(dll.swap_linked_list())
dll.doubleListPrint(dll.head)
