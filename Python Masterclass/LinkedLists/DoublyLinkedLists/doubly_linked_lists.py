"""
Objectives

- Construct a Doubly Linked List
- Compare and Contrast Doubly and Singly Linked Lists
- Implement basic operations on a Doubly Linked List

Almost identical to Singly Linked Lists, except every node has another pointer,
to the previous node!

more memory === more flexibility

It's almost always a tradeoff

PUSH METHOD
- adding a node to the end of the Doubly Linked List

pushing pseudocode

- create a new node with the value passed to the function
- if the head property is null, set the head and tail to be the newly created node
- if not, set the ne
xt property on the tail to be that node
- Set the previous property on the newly created node to be the tail
- Set the tail to be the newly created node
- increment the length
- Return the Doubly Linked List

POPPING
-Removing a node from the end of the Doubly Linked List

Popping Pseudocode
- If there is no head, return undefined
- Store the current tail in a variable to return later
- if the length is 1, set the head and tail to be null
- update the tail to be the previous Node
- Set the new Tails's next to null
- Decrement the length
- Return the value removed

SHIFTING
-Removing a node from the beginning of the doubly linked list

Shifting Pseudocode
- if length is 0, return undefined
- Store the current head property in a variable(old_head)
- if the length is one:
    - set the head to be null
    - set the tail to be null
- Update the head to be the next of the old head
- Set the head's prev property to null
- set the old head's next to null
- decrement the lenth
- return old head

UNSHIFTING

- adds a new value as the head

Unshifting Pseudocode
- create a new node with the value passed to the function
- if the length is 0
    - Set the head to be the new node
    - Set the tail to be the new node
- Otherwise
    - Set the prev property on the head of the list to be the new node
    - Set the next property on the new node to be the head property
    - Update the head to be the new node
- Increment the length
- Return the list

GET

- Accessing a node in a Doubly Linked List by its position

Get Pseudocode
- If the index is less than 0 or greater or equal to the length, return null
- if the index is less than or equal to half the length of the list
    - lopp through the list starting from the head and loop towards the middle
    - Return the node once it is found
- If the index is greater than half the length of the list
    - Loop through the list starting from the tail and loop towards the middle
    - Return the node once it is found

SET

- Replacing the value of a node in a Doubly Linked List

Set Pseudocode
- Create a variable which is the result of the get method at the index passed to the function
    - If the get method returns a valid node, set the value of that node to be the value passed to the function
    - Return True
- Otherwise return False

INSERT
- Adding a node in a Doubly Linked List by a certain position

Insert Pseudocode
- if the index is less than zero or greater than or equal to the length return false
- If the index is 0, unshift
- if the index is the same as the length, push
- use the get method to access the index -1
- Set the next and prev properties on the correct nodes to link everything together
- increment the length
- return true

REMOVE
- Removing a node in a Doubly Linked List by a certain position

Remove Pseudocode
- If the index is less than zero or greater than or equal to the length return undefined
- If the index is 0, shift
- If the index is the same as the length-1, pop
- Use the get method to retrieve the item to be removed
- Update the next and prev properties to remove the found node from the list
- Set next and prev to null on the found node
- Decrement the length
- Return the removed node

Big O of Doubly Linked Lists

insertion - O(1)
Removal -O(1)
Searching - O(N)
Access - O(N)

Technically searching is O(N/2) but that's still O(N)

RECAP!
- Doubly Linked Lists are almost identical to Singly Linked Lists except there is an additional pointer to 
previous nodes
- Better than Singly Linked Lists for finding nodes and can be done in half the time
- However, they do take up more memory considering the extra pointer

"""


from threading import current_thread
from jinja2 import Undefined


class Node:

    def __init__(self, val) -> None:
        self.val = val
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def push(self, val):
        n = Node(val)

        if self.size == 0:
            self.head = n
            self.tail = n
        temp_tail = self.tail
        self.tail.next = n
        self.tail.next.prev = temp_tail
        self.tail = n
        self.size += 1
        return self.size

    def popInit(self):
        if self.head == self.tail ==None:
            return Undefined
        current_tail = self.tail
        if self.size == 1:
            self.head =None
            self.tail =None
        new_tail = current_tail.prev
        new_tail.next=None
        self.size -=1
        return self.print_backwards()

    def pop(self):
        if self.head == self.tail ==None:
            return Undefined
        current_tail = self.tail
        if self.size == 1:
            self.head =None
            self.tail =None
        self.tail = current_tail.prev
        self.tail.next=None
        current_tail.prev=None
        self.size -=1
        return self.print_backwards()

    def shiftInit(self):
        if self.head ==None:return Undefined
        old_head =self.head
        if self.size == 1:
            self.head = None
            self.tail = None
        current_head = old_head.next
        current_thread.prev =None
        old_head.next=None
        self.head =current_head
        self.size -=1
        return old_head.val

    def shift(self):
        if self.head ==None:return Undefined
        old_head =self.head
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.head = old_head.next
            self.head.prev = None
            old_head.next  = None
        self.size -=1
        return old_head.val

    def unshift(self, val):
        n = Node(val)
        if(self.head == self.tail ==None):
            self.head =n
            self.tail =n
        else:
            self.head.prev =n
            n.next =self.head
            self.head =n
        self.size +=1
        return self.print()

    def get(self, idx):
        result = None
        if idx < 0 or idx > self.size:
            return None
        else:
            # count_idx = 0
            # start = self.head
            # while count_idx < self.size:
            #     if count_idx ==idx:
            #         result= start.val
            #     start = start.next
            #     count_idx +=1

            end_idx = (self.size//2)
            if idx < end_idx:
                count_idx = 0
                start = self.head
                while count_idx < end_idx:
                    if count_idx == idx:
                        result= start
                    start = start.next
                    count_idx +=1
            
            if idx >= end_idx:
                count_idx = self.size-1
                start = self.tail
                while count_idx >= end_idx:
                    if count_idx ==idx:
                        result= start
                    start = start.prev
                    count_idx -=1
        return result

    def set(self,idx,val):
        #check if node is valid
        new_node=self.get(idx)
        if(new_node != None):
            print("valid node")
            new_node.val =val
        else:
            print("invalid node")
        self.print()

    def insert(self, idx, val):
        
        # - if the index is less than zero or greater than or equal to the length return false
        if idx < 0 or idx >self.size:
            return False
         # - If the index is 0, unshift
        elif idx ==0:
            self.unshift(val)
        
        # - if the index is the same as the length, push
        elif(idx ==self.size):
            self.push(val)
        else:
            # - use the get method to access the index -1
            new_node =Node(val)

            # - Set the next and prev properties on the correct nodes to link everything together

            node_idx =self.get(idx-1)
            temp = node_idx.next
            node_idx.next =new_node
            new_node.prev =node_idx
            new_node.next=temp
            temp.prev =new_node

             # - increment the length
            self.size +=1
        return True

    def remove(self, idx):
        print("aaa:", idx, self.size)
        # - If the index is less than zero or greater than or equal to the length return undefined
        if idx < 0 or idx >= self.size:
            return Undefined
        # - If the index is 0, shift
        elif idx == 0:
            self.shift()
        # - If the index is the same as the length-1, pop
        elif(idx == self.size-1):
            self.pop()
        # - Use the get method to retrieve the item to be removed

        else:
            remove_node = self.get(idx)

            # - Update the next and prev properties to remove the found node from the list
            prev_node = remove_node.prev
            next_node =remove_node.next
            prev_node.next=next_node
            next_node.prev=prev_node

            # - Set next and prev to null on the found node

            remove_node.next=None
            remove_node.prev=None

            # - Decrement the length
            self.size -=1

            # - Return the removed node
            return remove_node.val

        
        
       
            
            

    def print(self):
        idx =0
        start = self.head
        while idx < self.size:
            print(start.val, end="-->")
            start = start.next
            idx +=1
        print()

    def print_backwards(self):
        idx =0
        start = self.tail
        while idx < self.size:
            print(start.val, end="-->")
            start = start.prev
            idx +=1
        print()



dl = DoublyLinkedList()
print("size: ", dl.size)
print("push: ", dl.push(10))
print("push: ", dl.push(20))
print("push: ", dl.push(30))
print("push: ", dl.push(40))
# print("push: ", dl.push(50))
dl.print()
# dl.print_backwards()
# dl.pop()
# dl.pop()
# dl.pop()

# test shift

# print("shift:", dl.shift())
# dl.print()
# print("shift:", dl.shift())
# dl.print()
# print("shift:", dl.shift())
# dl.print()
# print("shift:", dl.shift())
# dl.print()

# test unshift

# dl.unshift(100)
# dl.unshift(90)
# dl.unshift(80)

# test get

# print("get:", dl.get(-1))

# test set
# dl.set(10,100)

# test insert
# print(dl.insert(3, 100))

#test remove
print(dl.remove(3))
dl.print()