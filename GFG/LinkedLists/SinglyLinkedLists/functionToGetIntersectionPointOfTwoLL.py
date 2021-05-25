"""
Using Hashing
1) Create an empty hash set. 
2) Traverse the first linked list and insert all nodes’ addresses in the hash set. 
3) Traverse the second list. For every node check if it is present in the hash set. If we find a node in the hash set, return the node.
"""

#  program to get intersection point of two linked list

class Node:
    def __init__(self,d):
        self.data = d
        self.next = None

class LinkedListIntersect:
    
    #    function to print the list
    def Print(self,n):
        cur = Node(n)
        while(cur != None):
            print(cur.data, end= " ")
            cur = cur.next
        print()
    
    # function to find the intersection of two node
    def MegeNode(self,n1, n2):
        hs = []# # define hashset
        while (n1 != None):
            hs.append(n1)
            n1 = n1.next
        while (n2 != None):
            if (n2 in hs):
                return n2
            n2 = n2.next
        return None

if __name__=='__main__':
    ll = LinkedListIntersect()
    # list 1
    n1 = Node(1)
    n1.next =  Node(2)
    n1.next.next =  Node(3)
    n1.next.next.next =  Node(4)
    n1.next.next.next.next =  Node(5)
    n1.next.next.next.next.next =  Node(6)
    n1.next.next.next.next.next.next = Node(7)
    
    # list 2
    n2 =  Node(10)
    n2.next =  Node(9)
    n2.next.next =  Node(8)
    n2.next.next.next = n1.next.next.next
    ll.Print(n1)
    ll.Print(n2)
    print(ll.MegeNode(n1, n2).data)
