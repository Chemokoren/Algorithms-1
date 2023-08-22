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

                current.next =temp.next
                temp.next.prev=current

                current.prev.next =new_current
                current.prev=new_current

    #           link new_current_node to previous
    #             temp.prev =current

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



print(" ############################ The official approach #############################")
'''
given a sorted doubly linked list containing n nodes. 
The problem is to remove duplicate nodes from the given list
'''

'''
Logic:

removeDuplicates(head_ref, x):
    if head_ref ==None:
        return
    current =head_ref
    while current->next != None:
        if current->data == current->next->data:
            deleteNode(head_ref, current->next)
        else:
            current = current->next
'''

# python implementation to remove duplicates from a sorted doubly linked list
class Node:
    def __init__(self, new_data):
        self.data =new_data
        self.next =None
        self.prev =None

'''
Function to delete a node in a Dll
head_ref : -pointer to head node pointer
_del : - pointer to node to be _deleted.
'''

def _deleteNode(head_ref, _del):

    # base case
    if (head_ref == None or _del == None):
        return
    # if node to be deleted is head node
    if(head_ref == _del):
        head_ref =_del.next

    # change next only if the node to be deleted is not the last node
    if(_del.next != None):
        _del.next.prev =_del.prev

    # change prev only if the node to be deleted is not the first node
    if(_del.prev !=None):
        _del.prev.next =_del.next

    return head_ref

'''
Function to remove duplicates from a sorted dll
'''
def removeDuplicates(head_ref):
    # check if head_ref is None or list is empty
    if(head_ref == None ):
        return
    current =head_ref

    while(current.next != None):
        next_current =current.next
        if(current.data == next_current.data):
            _deleteNode(head_ref, next_current)
        else:
            current =next_current
    return head_ref

'''
Function to insert a node at the beginning of the DLL
'''

def push(head_ref, new_data):

    # allocate node
    new_node =Node(0)

    # put in the data
    new_node.data =new_data

    # since we are adding at the beginning, prev is always None
    new_node.prev =None

    # link the old list off the new node
    new_node.next =head_ref

    # change prev of head node to new node
    if(head_ref !=None):
        head_ref.prev =new_node

    #move the head to point to the new node
    head_ref =new_node
    return head_ref

# Function to print nodes in a given doubly linked list
def printList(head):

    # if list is empty
    if (head == None):
        print("Doubly Linked list empty")

    while (head != None) :
        print(head.data, end = " ")
        head = head.next

# Driver program to test above functions

# Start with the empty list
head = None

# Create the doubly linked list:
# 4<->4<->4<->4<->6<->8<->8<->10<->12<->12
head = push(head, 12)
head = push(head, 12)
head = push(head, 10)
head = push(head, 8)
head = push(head, 8)
head = push(head, 6)
head = push(head, 4)
head = push(head, 4)
head = push(head, 4)
head = push(head, 4)

print( "original dll:\n")
printList(head)

# remove duplicate nodes
head = removeDuplicates(head)

print("\ndll after removing duplicates:")
printList(head)



