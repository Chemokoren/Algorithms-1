"""
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
'''

# program to swap elements of LL pairwise
# Time complexity: O(n)
class Node:
  
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None
  
class LinkedList:
  
    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to pairwise swap elements of a linked list
    def pairwiseSwap(self):
        temp = self.head
         
        # There are no nodes in linked list
        if temp is None:
            return 
          
        # Traverse furthur only if there are at least two
        # left
        while(temp is not None and temp.next is not None):
              
            # If both nodes are same,
            # no need to swap data
            if(temp.data == temp.next.data):
                  
                # Move temp by 2 to the next pair
                temp = temp.next.next
            else:
                  
                # Swap data of node with its next node's data
                temp.data, temp.next.data = temp.next.data, temp.data
                  
                # Move temp by 2 to the next pair
                temp = temp.next.next


    # Recursive function to pairwise swap elements of a linked list 
    def pairWiseSwapRecursive(self,head):
        # There must be at-least two nodes in the list
        if (head != None and head.next != None):
    
            # Swap the node's data with data of next node
            head.data, head.next.data =head.next.data,head.data
    
            # Call pairWiseSwap() for rest of the list
            self.pairWiseSwapRecursive(head.next.next)


    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
  
    # Utility function to prit the linked LinkedList
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data,end=" ")
            temp = temp.next
  
  
# Driver program
llist = LinkedList()
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)
  
# print ("Linked list before calling pairWiseSwap() ")
# llist.printList()
  
# llist.pairwiseSwap()
  
# print ("\nLinked list after calling pairWiseSwap()")
# llist.printList()
  
print ("Recursive: Linked list before calling pairWiseSwap() ")
llist.printList()
  
llist.pairWiseSwapRecursive(llist.head)
  
print ("Recursive: \nLinked list after calling pairWiseSwap()")
llist.printList()
