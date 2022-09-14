"""
A node can be added in three ways 

    - At the front of the linked list  
    - After a given node. 
    - At the end of the linked list.

Add a node at the front
-----------------------

Approach: The new node is always added before the head of the given Linked List. And newly added node
becomes the new head of the Linked List. 

Time Complexity: O(1), We have a pointer to the head and we can directly attach a node and change
the pointer.
Auxiliary Space: O(1)


Add a node after a given node
----------------------------- 

We are given a pointer to a node, and the new node is inserted after the given node.

Follow the steps to add a node after a given node:

    - Firstly, check if the given previous node is NULL or not.
    - Then, allocate a new node and
    - Assign the data to the new node
    - And then make the next of new node as the next of previous node. 
    - Finally, move the next of the previous node as a new node.

Time complexity: O(N), where N is the size of the linked list
Auxiliary Space: O(1) since using constant space to modify pointers


Add a node at the end:
    - The new node is always added after the last node of the given Linked List.
    For example if the given Linked List is 5->10->15->20->25 and we add an item 30 at the end, then 
    the Linked List becomes 5->10->15->20->25->30. 
    Since a Linked List is typically represented by the head of it, we have to traverse the list till 
    the end and then change the next to last node to a new node.

    Time complexity: O(N), where N is the number of nodes in the linked list. Since there is a loop 
    from head to end, the function does O(n) work. 
        This method can also be optimized to work in O(1) by keeping an extra pointer to the tail of 
        the linked list/
    Auxiliary Space: O(1)

Delete from a Linked List:-

You can delete an element in a list from:

    Beginning
    End
    Middle

1) Delete from Beginning:

Point head to the next node i.e. second node
    temp = head
    head = head->next
    
Make sure to free unused memory
    free(temp); or delete temp;

2) Delete from End:

Point head to the previous element i.e. last second element
    Change next pointer to null
    struct node *end = head;
    struct node *prev = NULL;
    while(end->next)
    {
        prev = end;
        end = end->next;
    }
    prev->next = NULL;
    
Make sure to free unused memory
    free(end); or delete end;

3) Delete from Middle:

Keeps track of pointer before node to delete and pointer to node to delete
    temp = head;
    prev = head;
    for(int i = 0; i < position; i++)
    {
        if(i == 0 && position == 1)
            head = head->next;
            free(temp)
        else
        {
            if (i == position - 1 && temp)
            {
                prev->next = temp->next;
                free(temp);
            }
            else
            {
                prev = temp;
                if(prev == NULL) // position was greater than number of nodes in the list
                    break;
                temp = temp->next; 
            }
        }
    }
    

Iterative Method to delete an element from the linked list:

To delete a node from the linked list, we need to do the following steps:

    Find the previous node of the node to be deleted. 
    Change the next of the previous node. 
    Free memory for the node to be deleted.



"""

class Node:

    def __init__(self,data) -> None:
        self.data =data
        self.next =None


class LinkedList:

    def __init__(self) -> None:
        self.head =None

    def print_list(self):
        start = self.head
        while start is not None:
            print(start.data, end="-->")
            start =start.next
        print()

    def push(self, new_data):
    
        # create a new Node & Put in the data
        new_node = Node(new_data)
            
        # make next of the new Node as head
        new_node.next = self.head
            
        # Move the head to point to new Node
        self.head = new_node

    def insert_after_prev_node(self, prev_node, new_data):
        if prev_node == None:
            return
        new_node =Node(new_data)
        new_node.next =prev_node.next
        prev_node.next =new_node 
        
    def insert_at_end(self, new_data):
        new_node =Node(new_data)

        if self.head == None:
            self.head =new_node
        else:
            start = self.head
            while(start.next):
                start =start.next
            start.next =new_node

    def insert_after_pos(self, pos, new_data):
        start = self.head
        count = 0
        while count < pos:
            start = start.next
            count +=1
        temp = start.next
        start.next =Node(new_data)
        start.next.next =temp

    def delete_from_beginning(self):
        if self.head == None:
            return "No item to delete"
        else:
            temp = self.head
            self.head = self.head.next
            
    def delete_from_end(self):
        if self.head == None:
            return "No item to delete"
        start =self.head
        while(start.next.next):
            start =start.next
        start.next =None

    def delete_from_middle(self, pos):
        start =self.head

        count = 0
        while count < pos-1:
            start = start.next
            count += 1

        start.next= start.next.next
        # print("aaa", start.data)


if __name__=='__main__':
    ll = LinkedList()
    ll.push(1)
    ll.push(2)
    ll.push(3)
    ll.push(4)
    ll.push(5)
    ll.print_list()
    # ll.insert_after_pos(2,7)
    ll.insert_after_prev_node(ll.head.next.next,58)
    ll.print_list()
    ll.insert_at_end(49)
    ll.print_list()
    ll.delete_from_beginning()
    ll.print_list()
    ll.delete_from_end()
    ll.print_list()
    ll.delete_from_middle(2)
    ll.print_list()

