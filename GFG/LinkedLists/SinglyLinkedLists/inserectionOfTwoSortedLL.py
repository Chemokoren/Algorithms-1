'''
Link list node

Time Complexity: O(m+n) where m and n are number of nodes in first and second linked lists respectively. 
Only one traversal of the lists are needed.

Auxiliary Space: O(min(m, n)). 
The output list can store at most min(m,n) nodes .
'''
class Node:
    def __init__(self):
        self.data = 0
        self.next = None
'''
This solution uses the temporary
dummy to build up the result list
'''
def sortedIntersect(a,b):
    dummy = Node()
    tail = dummy;
    dummy.next =None

    '''
    once one or the other list runs out -- we're done
    '''
    while (a !=None and b!=None):
        if(a.data == b.data):
            tail.next =push((tail.next), a.data)
            tail = tail.next
            a = a.next
            b = b.next

        # advance the samller list
        elif(a.data < b.data):
            a = a.next
        else:
            b =b.next
    return dummy.next

''' UTILITY FUNCTIONS '''
''' Function to insert a node at
the beginning of the linked list '''
def push(head_ref, new_data):

    new_node = Node()
  
    new_node.data = new_data
  
    ''' link the old list off the new node '''
    new_node.next = head_ref
  
    ''' move the head to point to the new node '''
    head_ref = new_node 
    return head_ref
 
''' Function to print nodes in
   a given linked list '''
def printList(node):
    while (node != None):
        print(node.data, end=' ')
        node = node.next
      
''' Driver code'''
if __name__=='__main__':
     
    ''' Start with the empty lists '''
    a = None
    b = None
    intersect = None
  
    ''' Let us create the first sorted
     linked list to test the functions
     Created linked list will be
     1.2.3.4.5.6 '''
    a = push(a, 6);
    a = push(a, 5);
    a = push(a, 4);
    a = push(a, 3);
    a = push(a, 2);
    a = push(a, 1);
  
    ''' Let us create the second sorted linked list
   Created linked list will be 2.4.6.8 '''
    b = push(b, 8);
    b = push(b, 6);
    b = push(b, 4);
    b = push(b, 2);
  
    ''' Find the intersection two linked lists '''
    intersect = sortedIntersect(a, b);
  
    print("Linked list containing common items of a & b ");
    printList(intersect);

