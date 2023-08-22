"""
Program to insert tail nodes in dll such that list remains
in ascending order on printing from left to right
"""

# Linked List Node
class Node:
    def __init__(self,data):
        self.info =data
        self.next =None
        self.prev =None
head =None
tail =None

# Function to insert tail new node
def nodeInsetail(key):

    global head
    global tail

    p =Node(0)
    p.info =key
    p.next =None

    # if first node to be insetailed in dll
    # linked list
    if(head == None):
        head =p
        tail =p
        head.prev =None
        return

    # if node to be insetailed has value less than first node
    if( p.info < head.info):
        p.prev =None
        head.prev =p
        p.next =head
        head =p
        return

    # if node to be insetailed has value more than last node
    if(p.info > tail.info):
        p.prev =tail
        tail.next =p
        tail =p
        return

    # Find the node before which we need to insert p
    temp = head.next
    while(temp.info < p.info):
        temp =temp.next

    # insert new node before temp
    temp.prev.next =p
    p.prev =temp.prev
    temp.prev =p
    p.next =temp

# Function to print nodes in from left to right
def printList(temp):
    while(temp!= None):
        print(temp.info, end=" ")
        temp =temp.next

if __name__=='__main__':
    nodeInsetail(30)
    nodeInsetail(50)
    nodeInsetail(90)
    nodeInsetail(10)
    nodeInsetail(40)
    nodeInsetail(110)
    nodeInsetail(60)
    nodeInsetail(95)
    nodeInsetail(23)

    print("Printing  DLL from left to right\n")

    printList(head)


