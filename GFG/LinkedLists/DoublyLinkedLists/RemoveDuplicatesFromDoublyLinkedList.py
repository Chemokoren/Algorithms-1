# program to remove duplicates from a doubly linked list
# 1 - Node class
# 2 - push items in a doubly linked list
# 3 - traverse linked list & check if current is same as current->next, if so
#     delete current -> next
# 4 -function to delete a node

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
        if(self.head !=None):
            temp =self.head
            self.head =new_node
            self.head.prev =new_node
            self.head.next =temp
        self.head =new_node

    def sortDll(self):

        if self.head == None:
            return
        current =self.head

        while current.next != None:
            new_current= current.next
            if new_current.data < current.data:
                temp =new_current.next

                current.prev=new_current
                current.next =temp
    #           link new_current_node to previous
                temp.prev =current

    def removeDuplicates(self):
        while self.head != None:
            current =self.head
            new_current =self.head.next
            while current !=new_current:
                current =new_current
                new_current=current.next
            self.deleteNode(new_current)

    def deleteNode(self):
        pass


    def printDll(self):
        while self.head !=None:
            print(self.head.data)
            self.head =self.head.next



dll =DoublyLinkedList()
dll.push(6)
dll.push(8)
dll.push(1)
dll.push(9)
dll.push(4)
dll.push(5)
dll.printDll()
dll.sortDll()
print("##################################")
dll.printDll()
