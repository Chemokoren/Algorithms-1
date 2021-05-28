"""Input: Head of following linked list 
1->2->3->4->NULL 
Output: Linked list should be changed to, 
4->3->2->1->NULL"""

'''
method 1: iterative
Initialize three pointers prev as NULL, curr as head and next as NULL.
Iterate through the linked list. In loop, do following. 
// Before changing next of current, 
// store next node 
next = curr->next
// Now change next of current 
// This is where actual reversing happens 
curr->next = prev 
// Move prev and curr one step forward 
prev = curr 
curr = next

Time Complexity: O(n) 
Space Complexity: O(1)
'''

 
class Node:
 
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head =None

    # Function to reverse LL
    def reverse(self):
        prev = None
        current =self.head
        while(current is not None):
            next = current.next
            current.next =prev
            prev =current
            current =next
        self.head = prev

# Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
 
    # Utility function to print the linked LinkedList
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data),
            temp = temp.next
 
 
# Driver code
llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(85)
 
print("Given Linked List")
llist.printList()
llist.reverse()
print("\nReversed Linked List")
llist.printList()
 
'''
Recursive Method: 

1) Divide the list in two parts - first node and 
    rest of the linked list.
2) Call reverse for the rest of the linked list.
3) Link rest to first.
4) Fix head pointer
'''
