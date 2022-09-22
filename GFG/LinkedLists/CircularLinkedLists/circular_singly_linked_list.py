
"""

Circular Singly Linked List Insertion

"""
class Node:
    def __init__(self,data):
        self.data =data
        self.next =None

class CircularLinkedList:
    def __init__(self):
        self.last =None

    # This function is only for empty list
    def addToEmpty(self, data):
        if(self.last !=None):
            return self.last
        # creating the newnode temp
        temp =Node(data)
        self.last =temp

        # creating the link
        self.last.next =self.last
        return self.last

    '''
    Create a node, say T
    Make T -> next = last -> next
    last -> next = T
    '''
    # Time complexity: O(1)  |Auxiliary Space: O(1)
    def addBegin(self, data):
        if(self.last == None):
            return self.addToEmpty(data)

        temp =Node(data)
        temp.next =self.last.next
        self.last.next =temp

        return self.last

    '''
    Create a node, say T
    Make T -> next = last -> next
    last -> next = T
    last = T
    '''
    # Time complexity: O(1)  |Auxiliary Space: O(1)
    def addEnd(self, data):
        if(self.last == None):
            return self.addToEmpty(data)

        temp =Node(data)
        temp.next =self.last.next
        self.last.next =temp
        self.last =temp

        return self.last


    '''
    Create a node, say T. 
    Search for the node after which T needs to be inserted, say that node is P. 
    Make T -> next = P -> next; 
    P -> next = T.
    '''
    # Time Complexity: O(N) | Auxiliary Space: O(1)
    def addAfter(self, data, item):
        if(self.last == None):
            return None

        temp =Node(data)
        p =self.last.next

        while p:
            if(p.data ==item):
                temp.next =p.next
                p.next =temp

                if(p == self.last):
                    self.last =temp
                    return self.last
                else:
                    return self.last

            p =p.next
            if (p == self.last.next):
                print(item, "not present in the list")
                break

            
    def traverse(self):
        if(self.last == None):
            print("List is empty")
            return
        temp =self.last.next
        while temp:
            print(temp.data, end =" ")
            temp =temp.next
            if temp == self.last.next:
                break
# driver code to test program
if __name__=='__main__':
    llist =CircularLinkedList()

    llist.addToEmpty(6)
    llist.addBegin(4)
    llist.addBegin(2)
    llist.addEnd(8)
    llist.addEnd(12)
    llist.addAfter(10,8)

    llist.traverse()