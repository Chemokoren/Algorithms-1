"""
Objectives 
- Define what a Singly Linked List is
- Compare and contrast Linked Lists with Arrays
- Implement insertion, removal and traversal methods on Singly Linked Lists

What is a Linked List?

- A data structure that contains a head, tail and length property.
- Linked Lists consist of nodes, and each node has a value and a pointer to another node or null

Comparisons with Arrays

Lists
- Do not have indexes!
- Connected via nodes with a next pointer
- Random access is not allowed

Arrays
- Indexed in order!
- Insertion and deletion can be expensive
- Can quickly be accessed at a specific index

Pushing
-Adding a new node to the end of the Linked List!

Pushing Pseudocode
- This function should accept a value
- Create a new node using the value passed to the function
- If there is no head property on the list, set the head and tail to be the newly created node
- Otherwise set the next property on the tail to be the new node and set the tail property on the list to be
the newly created node
- increment the length by one

Popping 
- Removing a node from the end of the Linked List!

Popping pseudocode
- if there are no nodes in the list, return undefined
- Loop through the list until you reach the tail
- Set the next property of the 2nd to last node to be null
- Set the tail to be the 2nd to last node
- Decrement the length of the list by 1
- Return the value of the node to be removed

Shifting

-Removing a new node from the beginning of the Linked List!

Shifting pseudocode
- if there are no nodes, return undefined
- Store the current head property in a variable
- Set the head property to be the current head's next property
- Decrement the length by 1
- Return the value of the node removed

Unshifting

- Adding a new node to the beginning of the Linked List!

Unshifting pseudocode
- This function should accept a value
- Create a new node using the value passed to the function
- If there is no head property on the list, set the head and tail to be the newly created node
- Otherwise set the newly created node's next property to be the current head property on the list
- Set the head property on the list to be that newly created node
- Increment the length of the list by 1
- Return the linked list

Get

-Retrieving a node by it's position in the Linked List!

Get pseudocode
- This function should accept an index
- If the index is less than zero or greater than or equal to the length of the list, return null
- Loop through the list until you reach the index and return the node at that specific index

Set 

- Changing the value of a node based on it's position in the Linked List

Set Pseudocode

- This function should accept a value and an index
- Use your get function to find the specific node.
- If the node is not found, return false
- If the node is found, set the value of that node to be the value passed to the function and return true

Insert 

- Adding a node to the Linked List at a specific position

Insert Pseudocode

- If the index is less than zero or greater than the length, return false
- If the index is the same as the length, push a new node to the end of the list
- If the index is 0, unshift a new node to the start of the list
- Otherwise, using the get method, access the node at the index -1
- Set the next property on that node to be the new node
- Set the next property on the new node to be the previous next
- Increment the length
- Return true

Remove 

- Removing a node from the Linked List at a specific position

Remove Pseudocode

- If the index is less than zero or greater than the length, return undefined
- If the index is the same as the length-1, pop
- If the index is 0, shift
- otherwise, using the get method, access the node at the index -1
- Set the next property on that node to be the next of the next node
- Decrement the length 
- Return the value of the node removed

REVERSE

- Reversing the Linked List in place

Reverse pseudocode

-swap the head and tail
-Create a variable called next
-Create avariable called prev
-Create a variable called node and initialize to the head property
-Loop through the list
-Set the next to be the next property on whatever node is
-Set the next property on the node to be whatever prev is
-Set prev to be the value of the node variable
-Set the node variable to be the value of the next variable


"""
from jinja2 import Undefined


class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def traverse(self):
        current = self.head
        while(current):
            print(current.val, end="-->")
            current = current.next
        print()

    def push(self,val):
        n = Node(val)
        if self.head ==self.tail ==None:
            self.head =n
            self.tail =n
        else:
            self.tail.next =n
            self.tail =n
        self.size += 1
    
    def pop(self):
        # - if there are no nodes in the list, return undefined
        if self.size ==0:
            return None
        elif self.size ==1:
            remove_node = self.head
            self.head = None
            self.tail = None
            return remove_node.val if remove_node else None
        else:    
            idx = 0
            start = self.head

            # - Loop through the list until you reach the tail
            while idx < self.size -2:
                start = start.next
                idx +=1
            second_last_node =start
            remove_node = second_last_node.next

            # - Set the next property of the 2nd to last node to be null
            second_last_node.next =None
            # - Set the tail to be the 2nd to last node
            self.tail = second_last_node
            # - Decrement the length of the list by 1
            self.size -=1
            # - Return the value of the node to be removed
            return remove_node.val
    
    def shift(self):
        if self.size == 0:
            return Undefined
        temp = self.head
        new_head = self.head.next
        self.head =new_head
        self.size -=1
        return temp.val

    def unshift(self, val):
        n = Node(val)
        if self.size == 0:
            self.head =n
            self.tail =n
        else:
            n.next = self.head
            self.head =n
        self.size +=1
        return self.traverse()

    def get(self, idx):
        if idx < 0 or idx >=self.size:
            return None

        start = self.head
        count_idx =0
        result = None

        while count_idx < self.size:
            if count_idx == idx:
                result = start
            start = start.next
            count_idx +=1
        return result
                
    def set(self, idx, val):

        get_val = self.get(idx)
        if get_val ==None:
            return False
        get_val.val=val
        return True

    def insert(self, idx, val):
        if idx < 0 or idx > self.size :
            return False
        elif idx == self.size:
            self.push(val)
        elif idx == 0:
            self.unshift(val)
        else:
            before_node = self.get(idx-1)
            current_node =Node(val)
            after_node =before_node.next
            before_node.next =current_node
            current_node.next=after_node
            self.size +=1
            return True

    def remove(self, idx):
        if idx < 0 or idx >=self.size:
            return None
        elif idx == self.size-1:
            removed_node = self.get(idx).val
            self.pop()
            return removed_node
        elif idx == 0:
            removed_node =self.get(idx).val
            self.shift()
            return removed_node
        else:
            before_node =self.get(idx-1)
            removed_node =before_node.next
            before_node.next =before_node.next.next
            self.size -=1
            return removed_node.val
        
    def reverse(self):
        #13 -->27-->32-->71
        #13<--27<--32<--71
        self.tail, self.head =self.head, self.tail
        return self.traverse

    def print(self):
        idx =0
        start = self.head
        while idx < self.size:
            print(start.val,end="-->")
            start = start.next
            idx +=1
        print()



# first = Node("Hi")
# first.next =Node("there")
# first.next.next =Node("how")
# first.next.next.next =Node("are")
# first.next.next.next.next =Node("you")

# print("1",first.val)
# print("2",first.next.val)
# print("3",first.next.next.val)
# print("4",first.next.next.next.val)
# print("5",first.next.next.next.next.val)

s = SinglyLinkedList()
s.push("Hi")
s.push("there")
s.push("how")
s.push("are")
s.push("you")
s.traverse()

# test pop
# print("removed node:",s.pop())
# s.traverse()
# print("removed node:",s.pop())
# s.traverse()
# print("removed node:",s.pop())
# s.traverse()
# print("removed node:",s.pop())
# s.traverse()
# print("removed node:",s.pop())
# s.traverse()
# print("removed node:",s.pop())
# s.traverse()
# print("removed node:",s.pop())
# s.traverse

# test shift
# print("remove head: ", s.shift())
# s.traverse()
# print("remove head: ", s.shift())
# s.traverse()
# print("remove head: ", s.shift())
# s.traverse()
# print("remove head: ", s.shift())
# s.traverse()
# print("remove head: ", s.shift())
# s.traverse()
# print("remove head: ", s.shift())
# s.traverse()
# print("remove head: ", s.shift())
# s.traverse()

# test unshift
# s.unshift(10)
# s.unshift(30)
# s.unshift(40)
# s.unshift(50)

# test get
# print("get:",s.get(-1))
# print("get:",s.get(0))
# print("get:",s.get(1))
# print("get:",s.get(2))
# print("get:",s.get(3).val if s.get(3).val else None)
# print("get:",s.get(4).val if s.get(4) else None)
# print("get:",s.get(5).val if s.get(5) else None)
# print("get:",s.get(6).val if s.get(6) else None)


# test set
# print("set val:", s.set(2, 13))
# s.traverse()

# test insert
# print("insert: ", s.insert(4, "anii"))
# s.traverse()

# test remove node
# print("removed node: ", s.remove(0))
# s.traverse()

# test reverse
s.reverse()
s.traverse()