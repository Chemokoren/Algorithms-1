"""
Input: 17->15->8->12->10->5->4->1->7->6->NULL
Output: 8->12->10->4->6->17->15->5->1->7->NULL

Input: 8->12->10->NULL
Output: 8->12->10->NULL

Input: 1->3->5->7->NULL
Output: 1->3->5->7->NULL

Method 1 :
Algorithm: 
-Get pointer to the last node. 
-Move all the odd nodes to the end. 
……..a) Consider all odd nodes before the first even node and move them to end. 
……..b) Change the head pointer to point to the first even node. 
……..b) Consider all odd nodes after the first even node and move them to the end. 

Time Complexity: O(n), As we are only traversing linearly through the list.
Auxiliary Space: O(1)
"""
# program to segregate even and odd nodes in LL

head = None 

class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

def segregateEvenOdd():
    global head
    end =head
    prev = None
    curr= head

    # get pointer of last Node
    while(end.next !=None):
        end =end.next
    new_end= end

    # consider all odd nodes before getting first even node
    while(curr.data % 2 !=0 and curr != end):
        new_end.next=curr
        curr = curr.next
        new_end.next.next =None
        new_end =new_end.next

    # do the following steps only if there is an even node
    if(curr.data % 2 == 0):
        head = curr
        
        # now curr points to first even node
        while(curr != end):
            if(curr.data % 2 == 0):
                prev = curr
                curr = curr.next
            else:
                # break the link between prev and curr
                prev.next = curr.next

                # make next of curr as None
                curr.next = None

                # move curr to end
                new_end.next = curr

                # make curr as new end of list
                new_end = curr

                # update curr pointer
                curr = prev.next

    # we have to set prev before executing rest of this code
    else:
        prev =curr

    if(new_end !=end and end.data % 2 != 0):
        prev.next =end.next
        end.next =None
        new_end.next = end


# Given a reference (pointer to pointer) to the head
# of a list and an int, push a new node on the front
# of the list.
def push(new_data):
    global head
 
    # 1 & 2: Allocate the Node &
    #         Put in the data
    new_node = Node(new_data)
 
    # 3. Make next of new Node as head
    new_node.next = head
 
    # 4. Move the head to point to new Node
    head = new_node
 
# Utility function to print a linked list
def printList():
    global head
    temp = head
    while(temp != None):
         
        print(temp.data, end = " ")
        temp = temp.next
         
    print(" ")
 
 
push(11)
push(10)
push(8)
push(6)
push(4)
push(2)
push(0)
print("Origional Linked List")
printList()
 
segregateEvenOdd()
 
print("Modified Linked List")
printList()

# Input: 17->15->8->12->10->5->4->1->7->6->NULL
print("###############  second test  ###############")

push(6)
push(7)
push(1)
push(4)
push(5)
push(10)
push(12)
push(8)
push(15)
push(17)


print("Origional Linked List")
printList()
 
segregateEvenOdd()
 
print("Modified Linked List")
printList()


print("\n Method 2 \n")

"""
Method 2 

The idea is to split the linked list into two: one containing all even nodes and other 
containing all  odd nodes. And finally, attach the odd node linked list after the even 
node linked list. 
To split the Linked List, traverse the original Linked List and move all odd nodes to a 
separate  Linked List of all odd nodes. 
At the end of loop, the original list will have all the even nodes and the odd node list
will have all the odd nodes.
To keep the ordering of all nodes same, we must insert all the odd nodes at the end of 
the odd node list. And to do that in constant time, we must keep track of last pointer 
in the odd node list.
 
Time Complexity: O(n), As we are only traversing linearly through the list.
Auxiliary Space: O(1)

"""
from generic_singly_linked_list import generic_singly_linked_list
class segregate_even_and_odd(generic_singly_linked_list):

    def __init__(self) -> None:
        super().__init__()

    # Function to segregate even and odd nodes.
    def segregateEvenOdd(self, head):
        
        # Starting node of list having even values.
        evenStart = None
        
        # Ending node of even values list.
        evenEnd = None
        
        # Starting node of odd values list.
        oddStart = None
        
        # Ending node of odd values list.
        oddEnd = None
        
        # Node to traverse the list.
        currNode = head
        
        while(currNode != None):
            val = currNode.data
            
            # If current value is even, add it to even values list.
            if(val % 2 == 0):
                if(evenStart == None):
                    evenStart = currNode
                    evenEnd = evenStart
                else:
                    evenEnd.next = currNode
                    evenEnd = evenEnd.next
            
            # If current value is odd, add it to odd values list.
            else:
                if(oddStart == None):
                    oddStart = currNode
                    oddEnd = oddStart
                else:
                    oddEnd.next = currNode
                    oddEnd = oddEnd.next
                    
            # Move head pointer one step in forward direction
            currNode = currNode . next
        
        #If either odd list or even list is empty,no change is required as all elements
        # are either even or odd.
        if(oddStart == None or evenStart == None):
            return
        
        # Add odd list after even list.    
        evenEnd.next = oddStart
        oddEnd.next = None
        
        # Modify head pointer to starting of even list.
        head = evenStart


ll = segregate_even_and_odd()
ll.push(11)
ll.push(10)
ll.push(9)
ll.push(6)
ll.push(4)
ll.push(1)
ll.push(0)
 
print("Original Linked list")
ll.print_ll()
 
ll.segregateEvenOdd(ll.head)
 
print("Modified Linked list")
ll.print_ll()