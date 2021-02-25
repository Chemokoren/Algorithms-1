# structure of node of doubly linked list
class Node:
    def __init__(self,x):
        self.data =x
        self.next =None
        self.prev =None


class DoublyLinkedList:
    def __init__(self):
        self.head =None

    def push(self,data):
        _node =Node(data)
        if self.head is not None:
            _node.next =self.head
        self.head =_node



    def sortDll(self):
        if(self.head ==None):
            return
        current =self.head

        while current.next is not None:
            index =current.next

            while(index != None):
                if current.data > index.data:
                    temp =index.data
                    index.data = current.data
                    current.data =temp
                index =index.next
            current =current.next

    def insertItemInSortedDll(self, node):
        _node=Node(node)
        if(self.head == None):
            self.head =_node
        current =self.head
        while current.next is not None:
            index =current.next
            while(index !=None):
                if current.data > _node.data and _node.data < index.data:
                    # temp = current.next
                    # _node =current.next.prev
                    # current.next =_node
                    # _node.next=temp
                    # _node.prev =current

                    _node.next = current.next
                    _node.next.prev = _node
                    current = _node
                index =index.next

            current =current.next

    def printDll(self, node):
        _node =Node(node)
        while node is not None:
            print(node.data)
            node =node.next

# Driver code
# Driver code
dll =DoublyLinkedList()
dll.push(9)
dll.push(1)
dll.push(4)
dll.push(6)
dll.push(15)

dll.printDll(dll.head)
print("############### after sorting ####################")
dll.sortDll()
dll.printDll(dll.head)
dll.insertItemInSortedDll(13)
print("############### insert new value ####################")
dll.printDll(dll.head)
