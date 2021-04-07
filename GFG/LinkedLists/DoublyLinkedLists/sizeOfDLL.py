# program to find size of DLL

# Node
class Node:
    def __init__(self):
        self.data =None
        self.next =None
        self.prev =None

# Function adds DLL to front of DLL
def push(head_ref,new_data):
    new_node =Node()
    new_node.data =new_data
    new_node.next = head_ref
    new_node.prev =None
    if head_ref !=None:
        head_ref.prev =new_node
    head_ref =new_node
    return head_ref

# size of linked list
def findSize(node):
    res =0
    while(node != None):
        res = res + 1
        node = node.next
    return res

if __name__=='__main__':
    head = None
    head = push(head, 4)
    head = push(head, 3)
    head = push(head, 2)
    head = push(head, 1)
    print(findSize(head))