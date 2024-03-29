"""
Reverse a linked List

Given pointer to the head node of a linked list, the task is to reverse the linked list.
We need to reverse the list by changing the links between nodes.

Input: Head of following linked list 
1->2->3->4->NULL 

Output: Linked list should be changed to, 
4->3->2->1->NULL

Input: Head of following linked list 
1->2->3->4->5->NULL 
Output: Linked list should be changed to, 
5->4->3->2->1->NULL

Input: NULL 
Output: NULL

Input: 1->NULL 
Output: 1->NULL 
 

"""

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
from generic_singly_linked_list import generic_singly_linked_list

class LinkedList(generic_singly_linked_list):

    def __init__(self) -> None:
        super().__init__()


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

 
 
print("\n Iterative approach \n")
llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(85)
 
print("Iterative: original Linked List")
llist.print_ll()
llist.reverse()
print("\nIterative: Reversed Linked List")
llist.print_ll()
 
'''
Recursive Method: 

1) Divide the list in two parts - first node and 
    rest of the linked list.
2) Call reverse for the rest of the linked list.
3) Link rest to first.
4) Fix head pointer

Time Complexity: O(n) 
Space Complexity: O(1)

'''

 
# Create and Handle list operations
class LinkedList(generic_singly_linked_list):
    def __init__(self) -> None:
        super().__init__()


    # method to reverse the list
    def reverse(self,head):
        # if head is empty or has reached the end of the list
        if head is None or head.next is None:
            return head
        # reverse the rest list
        rest =self.reverse(head.next)

        # put first element at the end
        head.next.next =head
        head.next =None

        # Fix the header pointer
        return rest

# Returns the linked list in display format
    def __str__(self):
        linkedListStr = ""
        temp = self.head
        while temp:
            linkedListStr = (linkedListStr +  str(temp.data) + " ")
            temp = temp.next
        return linkedListStr

 

linkedList = LinkedList()
linkedList.push(20)
linkedList.push(4)
linkedList.push(15)
linkedList.push(85)
 
print("Recursive: Original linked list")
print(linkedList)
 
linkedList.head = linkedList.reverse(linkedList.head)
 
print("Recursive: Reversed linked list")
print(linkedList)


"""
A Simpler and Tail Recursive Method 

"""

class Node:
 
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None

class SimplerTailRecursiveLinkedList:
 
    # Function to initialize head
    def __init__(self):
        self.head = None

    def reverseUtil(self, curr, prev):
        # if last node mark it head
        if curr.next is None:
            self.head = curr

            # update next to prev node
            curr.next = prev
            return

        # save curr.next node for recursive call
        next = curr.next

        # And update next
        curr.next =prev

        self.reverseUtil(next, curr)

    # function calls reverseUtil() with previous as None
    def reverse(self):
        if self.head is None:
            return
        self.reverseUtil(self.head, None)
    

    # Function to insert a new node at the beginning
 
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
 
    # Utility function to print the linked LinkedList
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" "),
            temp = temp.next
 
my_list = SimplerTailRecursiveLinkedList()
my_list.push(8)
my_list.push(7)
my_list.push(6)
my_list.push(5)
my_list.push(4)
my_list.push(3)
my_list.push(2)
my_list.push(1)
 
print("Given linked list")
my_list.printList()
 
my_list.reverse()
 
print("\nReverse linked list")
my_list.printList()
 

"""

Using Stack:

Store the nodes(values and address) in the stack until all the values are entered.
Once all entries are done, Update the Head pointer to the last location(i.e the last value).
Start popping the nodes(value and address) and store them in the same order until the stack is empty.
Update the next pointer of last Node in the stack by NULL.

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # program to reverse the LL using stack
    def reverseLLUsingStack(self, head):
        # Initialise the variables
        stack, temp=[], head
        while temp:
            stack.append(temp)
            temp =temp.next

        head =temp =stack.pop()

        # untill stack is not empty
        while len(stack) > 0:
            elem =stack.pop()
            temp.next =elem
            temp =elem

        elem.next =None
        return head

if __name__=='__main__':
    print(" reverse LL using stack \n")
    head =ListNode(1, ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
    obj =Solution()
    head = obj.reverseLLUsingStack(head)
    while head:
        print(head.val, end=' ')
        head = head.next


"""
Using array:

1. Create a linked list.

2. Then, make a count(head) function to count the number of nodes.

3. Initialize an array with the size of the count.

4. and start a while(p->next!=NULL) loop and store all the node’s data into the array.

5. and then print the array from the last index to the first.

Time complexity: O(N) as we visit every node once.

Auxiliary Space: O(N) as extra space is used to store all the nodes in the array.

"""


'''
<script>
// Javascript program of the above approach

// Create a class Node to enter values and address in the list
class node {
constructor() {
	this.val = null;
	this.next = null;
}
};

let head = null;
// code to count the no. of nodes
function count(head) {
let p = head;
let k = 1;
while (p != null) {
	p = p.next;
	k++;
}
return k;
}

// to reverse the linked list
function ll_reverse(head) {
let p = head;
let i = count(head), j = 1;
let arr = new Array(i);
while (i != 0 && p != null) {
	arr[j++] = p.val;
	p = p.next;
	i--;
}
j--;
while (j != 0) // loop will break as soon as j=0
	document.write(arr[j--] + " ");
return head;
}
// code to insert at end of ll
function insert_end(head, data) {
let q = head;
let p = new node();
p.val = data;
p.next = null;
while (q.next != null)
	q = q.next;
q.next = p;
p.next = null;
return head;
}

// create ll
function create_ll(head, data) {
let p = new node();
p.next = null;
p.val = data;
if (head == null) {
	head = p;
	p.next = null;
	return head;
}
else {
	head = insert_end(head, data);
	return head;
}
}

let i = 5, j = 1;
while (i != 0) {
head = create_ll(head, j++);
i--;
}
head = ll_reverse(head);

</script>


'''





