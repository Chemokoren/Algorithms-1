"""
PairWise swap Nodes of a given linked list

Input : 1->2->3->4->5->6->NULL
Output : 2->1->4->3->6->5->NULL

Input : 1->2->3->4->5->NULL
Output : 2->1->4->3->5->NULL

Input : 1->NULL
Output : 1->NULL
"""

'''
METHOD 1 (Iterative)
Start from the head node and traverse the list. 
While traversing swap data of each node with its next node’s data.

Time complexity: O(n)
'''
from generic_singly_linked_list import generic_singly_linked_list, Node

# program to swap elements of LL pairwise
class ChildNode(Node):
    def __init__(self, data):
        super().__init__(data)
  
class LinkedList(generic_singly_linked_list):
  
    # Function to initialize head
    def __init__(self):
        self.head = None

    '''
    Function to pairwise swap elements of a linked list
    
    Time complexity: O(N) - As we traverse the linked list only once.

    Auxiliary Space: O(1)
    '''
    def pairwiseSwap(self):
        temp = self.head
         
        # There are no nodes in linked list
        if temp is None:
            return 
          
        # Traverse furthur only if there are at least two nodes left
        while(temp is not None and temp.next is not None):
              
            # If both nodes are same, no need to swap data
            if(temp.data == temp.next.data):
                  
                # Move temp by 2 to the next pair
                temp = temp.next.next
            else:
                # Swap data of node with its next node's data
                temp.data, temp.next.data = temp.next.data, temp.data
                  
                # Move temp by 2 to the next pair
                temp = temp.next.next

 
    '''
    Recursive function to pairwise swap elements of a linked list
    Time complexity: O(n)

    Auxiliary Space: O(1)

    As it is a tail recursive function, function call stack would not be build and thus
    no extra space will be used.

    The solution provided here swaps data of nodes. If the data contains many fields 
    (for example a linked list of Student Objects), the swap operation will be costly.
    
    '''
    def pairWiseSwapRecursive(self,head):
        # There must be at-least two nodes in the list
        if (head != None and head.next != None):
    
            # Swap the node's data with data of next node
            head.data, head.next.data =head.next.data,head.data
    
            # Call pairWiseSwap() for rest of the list
            self.pairWiseSwapRecursive(head.next.next)

  
  
llist = LinkedList()
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)
  
print ("Iterative: original Linked list before calling pairWiseSwap() ")
llist.print_ll()
  
llist.pairwiseSwap()
print ("Iterative: \nLinked list after calling pairWiseSwap()")
llist.print_ll()
  
# print ("Recursive: Linked list before calling pairWiseSwap() ")
# llist.print_ll()
  
# llist.pairWiseSwapRecursive(llist.head)
  
# print ("Recursive: \nLinked list after calling pairWiseSwap()")
# llist.print_ll()
