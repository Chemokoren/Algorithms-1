class Node:
    def __init__(self, data) -> None:
        self.data =data
        self.next =None

class Circular_Linked_list:

     # constructor to create an empty circular linked list
    def __init__(self) -> None:
        self.head =None

    # Function to insert a node at the beginning of a circular linked list
    def push(self, data):
        new_node =Node(data)
        curr =self.head

        new_node.next =self.head

        # If linked list is not None then set the next of last node
        if self.head is not None:
            while(curr.next != self.head):
                curr =curr.next
            curr.next =new_node

        else:
            new_node.next =new_node # for the first node
        self.head =new_node

    def push_recursive(self, data, temp=None):
        if self.head == None:
            new_node = Node(data)
            self.head = new_node
            new_node.next = self.head
            return
  
        if temp == None:
            temp = self.head
  
        if temp.next == self.head:
            new_node = Node(data)
            new_node.next = self.head
            temp.next = new_node
            return
  
        self.push_recursive(data, temp.next)

    # function to print nodes in a given circular linked list
    def print_cll(self):
        curr =self.head
        if self.head is not None:
            while(True):
                print(curr.data, end="-->"),
                curr =curr.next
                if(curr==self.head):
                    break
            print()

    '''
    Time complexity: O(1) to insert a node at the beginning no need to traverse list
    it takes constant time 
    Auxiliary Space: O(1)
    '''
    def add_beginning(self, last_node,new_data):
        new_node =Node(new_data)
        if(last_node == None):
            last_node =new_node
        new_node.next = last_node
        last_node.next = new_node

        return last_node
            
    '''
    2) Insertion at the end of the list: To insert a node at the end of the list, follow these steps: 

    Create a node, say T. 
    Make T -> next = last -> next; 
    last -> next = T. 
    last = T. 
    '''
        
